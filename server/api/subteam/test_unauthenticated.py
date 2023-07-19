from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.users.models import User
from api.team.models import Team
from .models import SubTeam


class subTeamTestsnoAuth(APITestCase):
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

    def test_create_subteam(self):
        data = {'name': "ben", 'team_id': None}
        response = self.client.post(reverse('subteam:create-subteam'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        data = {'name': "ben", 'team_id': self.team.team_id}
        response = self.client.post(reverse('subteam:create-subteam'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_subteam(self):
        response = self.client.get(reverse('subteam:get-subteams', args=[self.subteam1.subteam_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_subteam(self):
        subBeforeUpdate = SubTeam.objects.get(subteam_id=self.subteam1.subteam_id)
        response = self.client.put(
            reverse(
                "subteam:update-subteam",
                kwargs={"subteam_id": subBeforeUpdate.subteam_id}
            ),
            {"name": "subTeam1Updated", "team_id": self.team.team_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_subteam(self):
        subBeforeDelete = SubTeam.objects.get(subteam_id=self.subteam1.subteam_id)
        response = self.client.delete(
            reverse(
                "subteam:delete-subteam",
                kwargs={"subteam_id": subBeforeDelete.subteam_id}
            ),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
