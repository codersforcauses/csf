from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from .models import Team


class TeamTests(APITestCase):
    def setUp(self):
        Team.objects.create(
            name="mockTeam",
            join_code="mockTeam",
        )

    def test_create_team(self):
        create_team_name = "testCreateTeam"
        create_team_join_code = "T35T"
        response = self.client.post(
            reverse("team:create-team"),
            {
                "name": create_team_name,
                "join_code": create_team_join_code,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_team = Team.objects.get(name=create_team_name)
        self.assertEqual(created_team.name, create_team_name)
        self.assertEqual(created_team.join_code, create_team_join_code)

    def test_get_team(self):
        existing_team = Team.objects.get()
        response = self.client.get(
            reverse("team:get-team", kwargs={"team_id": existing_team.team_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(existing_team.name, response.data["name"])
        self.assertEqual(existing_team.join_code, response.data["join_code"])

    def test_get_teams(self):
        all_team = Team.objects.all()
        response = self.client.get(reverse("team:get-teams"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_count = 0
        for x in response.data:
            data_count = data_count + 1
        self.assertEqual(all_team.count(), data_count)

    def test_update_team(self):
        team_before_update = Team.objects.get()
        response = self.client.patch(
            reverse("team:update-team",
                    kwargs={"team_id": team_before_update.team_id}),
            {
                "name": "updateTeamNameTest",
                "join_code": "TEST",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "updateTeamNameTest")
        self.assertEqual(response.data["join_code"], "TEST")

    def test_delete_team(self):
        team_count_before_delete = Team.objects.all().count()
        team_to_delete = Team.objects.get(name="mockTeam")
        response = self.client.delete(
            reverse("team:delete-team",
                    kwargs={"team_id": team_to_delete.team_id}),
        )
        team_count_after_delete = Team.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(team_count_before_delete - 1, team_count_after_delete)
