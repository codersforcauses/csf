from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

class UserTest(APITestCase):
    
    def setUp(self):
        self.username = "user0"
        self.email = f"{self.username}@csf.com"
        self.password = "dfjhvb593cdch"
        self.new_password = "fkj1191cndcdc"
        self.newer_password = "dc3002jnvbicbcw"
       
        self.user = User.objects.create_user(
            username=self.username, 
            email=self.email,
            password=self.password
        )
    
    def test_change_password(self):
        # test response is 200
        url = reverse("user:change-password", kwargs={"id": self.user.id})
        response = self.client.patch(url, {"password": self.new_password})
        self.assertEqual(response.status_code, 200)

        # test user has new password
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.password, self.new_password)

    def test_request_reset_password(self):
        url = reverse("user:request-reset-password")
        response = self.client.post(url, {"email": self.email})

        # this must change when email implemented
        self.assertTrue("reset_token" in response.data)
        self.reset_token = response.data["reset_token"]

    def test_reset_password(self):
        url = reverse("user:reset-password")
        response = self.client.post(url, {"reset_token": self.reset_token, "password": self.newer_password})

        # test user has new password
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.password, self.newer_password)
        

