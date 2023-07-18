from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.team.models import Team


class teamnoAuthTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="mockTeam1",
            join_code="mockTeamCode1",
        )

    def test_create_team(self):
        data = {'name': "ben", 'join_code': None, 'bio': None}
        response = self.client.post(reverse('team:create-team'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_team(self):
        teamBeforeUpdate = Team.objects.get(team_id=self.team.team_id)
        response = self.client.put(
            reverse(
                "team:update-team",
                kwargs={"team_id": teamBeforeUpdate.team_id}
            ),
            {"name": "team1Updated", "join_code": "team1Updated", "bio": "team1Updated"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_team(self):
        teamCountBeforeDelete = Team.objects.all().count()
        response = self.client.delete(
            reverse(
                "team:delete-team",
                kwargs={"team_id": self.team.team_id}
            ),
            format='json'
        )
        teamCountAfterDelete = Team.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(teamCountBeforeDelete, teamCountAfterDelete)
