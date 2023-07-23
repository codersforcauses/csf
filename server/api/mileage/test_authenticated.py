from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer

from freezegun import freeze_time
import datetime

USERNAME = 'testuser'
PASSWORD = 'testuser123'


class MileageTests(APITestCase):
    def _get_token(self):
        get_token_url = reverse('auth:jwt_token')
        get_token_body = {
            'username': USERNAME,
            'password': PASSWORD
        }
        get_token_response = self.client.post(get_token_url, get_token_body, format='json')
        token = get_token_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def setUp(self):
        self.user = User.objects.create_user(username=USERNAME, password=PASSWORD)
        self.user.save()
        self.mileage = Mileage.objects.create(user=self.user, kilometres=100.0)
        self._get_token()

    def test_get_mileage(self):
        response = self.client.get(reverse('mileage:get-mileage'), {'user': self.user.id})
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

    def test_total_km(self):
        response = self.client.post(
            reverse('mileage:post-mileage'),
            {'user': self.user.id, 'kilometres': 200.0}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(reverse('mileage:get-mileage'), {'user': self.user.id, 'sum': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 100 + 200)

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
        response = self.client.get(reverse('mileage:get-mileage'), {'challenge': True, 'user': self.user.id})
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
        self._get_token()  # an ugly fix

        # get mileages after challenge period has ended
        response = self.client.get(reverse('mileage:get-mileage'), {'challenge': True, 'user': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        url = reverse('mileage:post-mileage')
        data = {'user': self.user.id, 'kilometres': 5.5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test only gets mileage in new challenge period
        response = self.client.get(reverse('mileage:get-mileage'), {'challenge': True, 'user': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)

        # refresh user
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.challenge_start_date, datetime.date.today())
