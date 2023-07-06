from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from .models import SubTeam
from api.team.models import Team


class SubteamTests(APITestCase):
    def setUp(self):
        createTeam = Team.objects.create(
            name="mockTeam1",
            join_code="mockTeamCode1",
        )
        SubTeam.objects.create(
            name="subTeam1",
            team_id=createTeam,
        )
        SubTeam.objects.create(
            name="subTeam2",
            team_id=createTeam,
        )

    def test_create_subteam(self):
        createTeam = Team.objects.create(
            name="mockTeam2",
            join_code="mockTeamCode2",
        )
        create_subteam_name = "createsubTeam1"
        create_subteam_team_id = createTeam
        response = self.client.post(
            reverse("subteam:create-subteam"),
            {
                "name": create_subteam_name,
                "team_id": create_subteam_team_id.team_id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_subteam = SubTeam.objects.get(name=create_subteam_name)
        self.assertEqual(created_subteam.name, create_subteam_name)
        self.assertEqual(created_subteam.team_id, create_subteam_team_id)

    def test_get_subteams(self):
        existingTeam = Team.objects.get()
        subteams = SubTeam.objects.filter(team_id=existingTeam.team_id)
        response = self.client.get(
            reverse("subteam:get-subteams", kwargs={"team_id": existingTeam.team_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subteams_name = [i.name for i in subteams]
        response_subteams_name = [i['name'] for i in response.data]
        self.assertEqual(subteams_name, response_subteams_name)

    def test_update_subteam(self):
        subteamBeforeUpdate = SubTeam.objects.get(name="subTeam1")
        response = self.client.put(
            reverse(
                "subteam:update-subteam",
                kwargs={"subteam_id": subteamBeforeUpdate.subteam_id}
                ),
            {
                "name": "updatesubTeam1",
                "team_id": subteamBeforeUpdate.team_id.team_id
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "updatesubTeam1")
        self.assertEqual(response.data["team_id"], subteamBeforeUpdate.team_id.team_id)

    def test_delete_subteam(self):
        subteamCountBeforeDelete = SubTeam.objects.all().count()
        subteamToDelete = SubTeam.objects.get(name="subTeam1")
        response = self.client.delete(
            reverse(
                "subteam:delete-subteam",
                kwargs={"subteam_id": subteamToDelete.subteam_id}
                ),
        )
        subteamCountAfterDelete = SubTeam.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(subteamCountBeforeDelete - 1, subteamCountAfterDelete)
