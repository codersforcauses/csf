from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer

class MileageTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.mileage = Mileage.objects.create(user=self.user, kilometres=100.0)

    def test_get_mileage(self):
        url = reverse('mileage:get-mileage', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = MileageSerializer([self.mileage], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_post_mileage(self):
        url = reverse('mileage:post-mileage')
        data = {'user': self.user.id, 'kilometres': 200.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mileage.objects.count(), 2)

    def test_post_mileage_invalid_data(self):
        url = reverse('mileage:post-mileage')
        data = {'user': self.user.id}  # Missing 'kilometres' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Mileage.objects.count(), 1)