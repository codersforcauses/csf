from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

class UserTest(APITestCase):
  
    def test_change_password(self):
        username = "user0"
        password = "dfjhvb593cdch"
        new_password = "fkj1191cndcdc"
       
        user = User.objects.create_user(
            username=username, 
            email=f"{username}@csf.com",
            password=password
        )

        # test response is 200
        url = reverse("user:change-password", kwargs={"id": user.id})
        response = self.client.patch(url, {"password": new_password})
        self.assertEqual(response.status_code, 200)

        # test user has new password
        user = User.objects.get(id=user.id)
        self.assertEqual(user.password, new_password)

    def test_request_reset_password(self):
        pass

