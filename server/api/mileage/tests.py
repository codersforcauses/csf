from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer

from freezegun import freeze_time
import datetime


class MileageTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.mileage = Mileage.objects.create(user=self.user, kilometres=100.0)

    def test_get_mileage(self):
        url = reverse('mileage:get-mileage-by-user', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = MileageSerializer([self.mileage], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_post_mileage(self):
        url = reverse('mileage:post-mileage')

        data = {'user': self.user.id, 'kilometres': 200.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        twos_days_ago = datetime.date.today() - datetime.timedelta(days=2)
        data = {'user': self.user.id, 'kilometres': 200.0, 'date': twos_days_ago}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Mileage.objects.count(), 3)

    def test_post_mileage_invalid_data(self):
        url = reverse('mileage:post-mileage')

        data = {'user': self.user.id}  # Missing 'kilometres' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        twos_days_time = datetime.date.today() + datetime.timedelta(days=2)
        data = {'user': self.user.id, 'kilometres': 20, 'date': twos_days_time}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(Mileage.objects.count(), 1)

    # test challenge periods

    def test_start_challenge(self):
        url = reverse('mileage:post-mileage')
        data = {'user': self.user.id, 'kilometres': 200.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # refresh user
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.challenge_start_date, datetime.date.today())

    def test_get_challenge_mileages(self):
        url = reverse('mileage:post-mileage')

        # start challenge period
        data = {'user': self.user.id, 'kilometres': 200.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # post mileage before the challenge period
        twos_days_ago = datetime.date.today() - datetime.timedelta(days=2)
        data = {'user': self.user.id, 'kilometres': 200.0, 'date': twos_days_ago}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test only get mileages within challenge period if challenge param in query
        url = reverse('mileage:get-mileage-by-user', args=[self.user.id])
        response = self.client.get(url, {'challenge': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

    def test_rollover_challenge(self):
        url = reverse('mileage:post-mileage')

        # start challenge period
        data = {'user': self.user.id, 'kilometres': 200.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # simulate the future and rollover to next challenge period
        self._test_rollover_challenge()

    @freeze_time(datetime.date.today() + datetime.timedelta(days=15))
    def _test_rollover_challenge(self):

        # get mileages after challenge period has ended
        url = reverse('mileage:get-mileage-by-user', args=[self.user.id])
        response = self.client.get(url, {'challenge': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        url = reverse('mileage:post-mileage')
        data = {'user': self.user.id, 'kilometres': 5.5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test only gets mileage in new challenge period
        url = reverse('mileage:get-mileage-by-user', args=[self.user.id])
        response = self.client.get(url, {'challenge': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)

        # refresh user
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.challenge_start_date, datetime.date.today())
