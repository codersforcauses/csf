from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

TEST_USERNAME = "afojwieapj;icawe"
TEST_PASSWORD = "ah;iusevajskaf"
TEST_EMAIL = "test@email.com"


class JWTTestCase(TestCase):

    def setUp(self):
        self.user: User = User.objects.create_user(username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD)

    def _token(self, *, active=True, passwd=None):
        self.user.is_active = active
        self.user.save()

        return self.client.post(reverse("jwt_token"), {"username": TEST_USERNAME, "password": passwd or TEST_PASSWORD}, format="json")

    def test_jwt_token_with_inactive_user(self):
        resp = self._token(active=False)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_jwt_token(self):
        resp = self._token()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for k, v in resp.data.items():
            self.assertTrue(k in ["refresh", "access"])
            self.assertTrue(v.split(".", maxsplit=1)[0] == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")

    def test_jwt_token_with_invalid_pass(self):
        resp = self._token(passwd="invalidpassword")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_jwt_refresh(self):
        token = self._token().data["refresh"]
        resp = self.client.post(reverse("jwt_refresh"), {"refresh": token}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_jwt_verify(self):
        token = self._token().data["access"]
        resp = self.client.post(reverse("jwt_verify"), {"token": token}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_jwt_verify_with_invalid_token(self):
        token = self._token().data["access"]
        token = token[:50] + chr(ord(token[50])+1) + token[51:]  # increment 50th character to make invalid
        resp = self.client.post(reverse("jwt_verify"), {"token": token}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
