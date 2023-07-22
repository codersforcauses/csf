from django.urls import reverse
from django.core import mail
from rest_framework.test import APITestCase
from .models import User, Team


class UserTest(APITestCase):
    def setUp(self):
        self.username = "user0"
        self.email = f"{self.username}@csf.com"
        self.password = "dfjhvb593cdch"
        self.new_password = "fkj1191cndcdc"
        self.newer_password = "dc3002jnvbicbcw"
        self.fake_token = "!@#$%^&*"
        self.new_username = "user1"
        self.new_avatar = 'avatar6.jpg'
        self.bad_new_email = "fhushfw@sfd"

        self.team = Team.objects.create(
            name="mockTeam",
            join_code="j01NtH3m0cKT34M",
            bio="mockTeamFor UnitTest"
        )

        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )

    def test_change_password(self):
        # test response is 200
        url = reverse("user:change-password", kwargs={"id": self.user.id})
        response = self.client.patch(url, {"old_password": self.password, "password": self.new_password})
        self.assertEqual(response.status_code, 200)

        # test user has new password
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.check_password(self.new_password), True)

    def test_change_details(self):
        url = reverse("user:change-details", kwargs={"id": self.user.id})
        response = self.client.patch(url,
                                     {"username": self.new_username,
                                      "email": self.email,
                                      "avatar": self.new_avatar})
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, self.new_username)
        self.assertEqual(self.user.avatar, self.new_avatar)
        response = self.client.patch(url,
                                     {"username": self.username,
                                      "email": self.bad_new_email})
        self.assertEqual(response.status_code, 400)

        # check that the was an error about an invalid email
        self.assertTrue("email" in response.data)

    def test_reset_password(self):
        url = reverse("user:request-reset-password")
        response = self.client.post(url, {"email": self.email})

        # test an email with the subject 'Reset Password' was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Reset Password")

        # find the token sent in the email in a not particularly robust way
        token_from_mail_start = mail.outbox[0].body.find("\n\n")
        token_from_mail_end = mail.outbox[0].body.find(
            "\n\n", token_from_mail_start + 1
        )
        token_from_mail = mail.outbox[0].body[
            token_from_mail_start + 2:token_from_mail_end
        ]

        # check the emailed token is considered valid, giving a 200 status code
        url = reverse("user:verify-token")
        response = self.client.post(url, {"reset_token": token_from_mail})
        self.assertEqual(response.status_code, 200)

        # check an invalid token gives a 400 status code
        response = self.client.post(url, {"reset_token": self.fake_token})
        self.assertEqual(response.status_code, 400)

        url = reverse("user:reset-password")
        response = self.client.post(
            url, {"reset_token": token_from_mail,
                  "password": self.newer_password}
        )

        # test user has new password
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.check_password(self.newer_password), True)

    def test_get_user(self):
        url = reverse("user:get-user", kwargs={"username": self.username})
        response = self.client.get(url)
        user_to_match = User.objects.get(username=self.username)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], user_to_match.username)
        self.assertEqual(response.data["email"], user_to_match.email)
        self.assertEqual(response.data["password"], user_to_match.password)

    def test_join_team_valid(self):
        mock_user = User.objects.get(id=self.user.id)
        mock_team = Team.objects.get(team_id=self.team.team_id)
        url = reverse("user:join-team",
                      kwargs={"id": mock_user.id})
        response = self.client.patch(
            url,
            {
                "join_code": mock_team.join_code,
                "team_admin": False,
            },
            format="json",
        )
        mock_user_reget = User.objects.get(id=self.user.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_user_reget.team_id, mock_team)

    def test_join_team_not_found(self):
        mock_user = User.objects.get(id=self.user.id)
        url = reverse("user:join-team",
                      kwargs={"id": mock_user.id})
        response = self.client.patch(
            url,
            {
                "join_code": "f4k3J0iNC0d3",
                "team_admin": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 404)
