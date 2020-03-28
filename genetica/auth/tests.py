from django.urls import reverse
from rest_framework.test import APITestCase

from genetica.auth.models import User
from genetica.auth.serializers import UserSerializer


class UserTests(APITestCase):
    def setUp(self) -> None:
        self.client = self.client_class()
        self.admin = User.objects.create(**{
            'username': 'admin',
            'email': 'admin@admin.com',
            'password': 'admin',
            'is_superuser': True,
            'is_staff': True,
        })
        self.user = User.objects.create(**{
            'username': 'user',
            'email': 'user@user.com',
            'password': '1'
        })
        self.obtain_tokens()

    def obtain_tokens(self):
        self.admin_token = self.request_token({
            'username': 'admin',
            'password': 'admin'
        })
        self.user_token = self.request_token({
            'username': 'user',
            'password': '1'
        })

    def request_token(self, data):
        auth_url = reverse('obtain-token-pair')
        auth_response = self.client.post(auth_url, data=data)
        return 'Bearer ' + auth_response.data['access']

    def test_list_user(self):
        url = reverse('user-list')

        self.client.credentials(HTTP_AUTHORIZATION=self.admin_token)
        response = self.client.get(url)

        users = User.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserSerializer(instance=users, many=True).data, response.data['results'])
