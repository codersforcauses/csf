from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.users.models import User
from api.team.models import Team


class teamTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="mockTeam1",
            join_code="mockTeamCode1",
        )
        self.team2 = Team.objects.create(
            name="mockTeam2",
            join_code="mockTeamCode2",
        )
        self.user = User.objects.create_user(username='testuser', password='testuser123', team_id=self.team, team_admin=True, is_active=True)
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

    def test_create_team(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        data = {'name': "ben", 'join_code': None, 'bio': None}
        response = self.client.post(reverse('team:create-team'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_team(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        teamBeforeUpdate = Team.objects.get(team_id=self.team.team_id)
        response = self.client.put(
            reverse(
                "team:update-team",
                kwargs={"team_id": teamBeforeUpdate.team_id}
            ),
            {"name": "team1Updated", "join_code": "team1Updated", "bio": "team1Updated"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(
            reverse(
                "team:update-team",
                kwargs={"team_id": self.team2.team_id}
            ),
            {"name": "team2Updated", "join_code": "team2Updated", "bio": "team2Updated"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_team(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        teamCountBeforeDelete = Team.objects.all().count()
        response = self.client.delete(
            reverse(
                "team:delete-team",
                kwargs={"team_id": self.team.team_id}
            ),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        teamCountAfterDelete = Team.objects.all().count()
        self.assertEqual(teamCountBeforeDelete - 1, teamCountAfterDelete)
