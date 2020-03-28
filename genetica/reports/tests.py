from django.urls import reverse
from rest_framework.test import APITestCase

from genetica.auth.models import User
from genetica.auth.serializers import UserSerializer
from genetica.reports.models import TraitTemplate
from genetica.user_profiles.models import UserProfile


class ReportTest(APITestCase):
    def setUp(self) -> None:
        self.client = self.client_class()
        user = User.objects.create(**{
            'username': 'user',
            'email': 'user@user.com',
            'password': '1'
        })
        UserProfile.objects.create(
            name="Profile 1",
            description="Profile 1",
            account=user,
        )
        TraitTemplate.objects.create()

        self.obtain_tokens()

    def obtain_tokens(self):
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
