from django.test import APITestCase
from django.urls import reverse
from .models import User

# Create your tests here.
class UserTest(APITestCase):
  
    def test_change_password(self):
       
        self.user = User.objects.create_user(
            username="username", email="user@user.com", password="pass_word100"
        )
        self.client.login(username=self.user.username, password=self.user.password)

        url = reverse("change-password")
        response = self.client.patch(url, {"password": "new_pwd"})
        self.assertEqual(response.status_code, 200)