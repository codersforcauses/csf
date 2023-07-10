from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

import uuid

class UserTest(APITestCase):
  
    def test_change_password(self):
        username = str(uuid.uuid4())[:20]
        password = "old_password48537945"
        new_password = "new_password0347357"
       
        user = User.objects.create_user(
            username=username, 
            email=f"{username}@csf.com",
            password=password
        )

        # test response is 200
        url = reverse("user:change-password")
        response = self.client.patch(url, {"username": username, "password": new_password})
        self.assertEqual(response.status_code, 200)

        # test user has new password
        user = User.objects.get(id=user.id)
        self.assertEqual(user.password, new_password)

    def test_request_reset_password(self):
        pass

