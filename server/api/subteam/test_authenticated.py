from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.users.models import User
from api.team.models import Team
from .models import SubTeam


class subTeamTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="mockTeam1",
            join_code="mockTeamCode1",
        )
        self.subteam1 = SubTeam.objects.create(
            name="subTeam1",
            team_id=self.team,
        )
        self.subteam2 = SubTeam.objects.create(
            name="subTeam2",
            team_id=self.team,
        )
        self.user = User.objects.create_user(username='testuser', password='testuser123', team_id=self.team, team_admin=True)
        self.user.save()

    def get_token(self):
        get_token_url = reverse('auth:jwt_token')
        get_token_body = {
            'username': 'testuser',
            'password': 'testuser123'
        }
        get_token_response = self.client.post(get_token_url, get_token_body, format='json')
        token = get_token_response.data['access']
        return token

    def test_create_subteam(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        data = {'name': "ben", 'team_id': None}
        response = self.client.post(reverse('subteam:create-subteam'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'name': "ben", 'team_id': self.team.team_id}
        response = self.client.post(reverse('subteam:create-subteam'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_subteam(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.get(reverse('subteam:get-subteams', args=[self.subteam1.subteam_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_subteam(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        subBeforeUpdate = SubTeam.objects.get(subteam_id=self.subteam1.subteam_id)
        response = self.client.put(
            reverse(
                "subteam:update-subteam",
                kwargs={"subteam_id": subBeforeUpdate.subteam_id}
            ),
            {
                "name": "updatesubTest",
                "team_id": self.team.team_id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subteam(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        subCountBeforeDelete = SubTeam.objects.all().count()
        subToDelete = SubTeam.objects.get(subteam_id=self.subteam1.subteam_id)
        response = self.client.delete(
            reverse(
                "subteam:delete-subteam",
                kwargs={"subteam_id": subToDelete.subteam_id}
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subCountAfterDelete = SubTeam.objects.all().count()
        self.assertEqual(subCountBeforeDelete - 1, subCountAfterDelete)
