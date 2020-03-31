from django.urls import reverse
from rest_framework.test import APITestCase

from genetica.auth.models import User
from genetica.reports.models import Report
from genetica.reports.serializers import ReportSerializer
from genetica.services.models import Service
from genetica.user_profiles.models import UserProfile


class ReportTest(APITestCase):
    def setUp(self) -> None:
        self.client = self.client_class()
        user = User.objects.create(**{
            'username': 'user',
            'email': 'user@user.com',
            'password': '1'
        })
        self.profile = UserProfile.objects.create(
            name="Profile 1",
            description="Profile 1",
            account=user,
        )
        service = Service.objects.create(
            name="Service 1",
            description="service 1",
            price=1.0
        )
        Report.objects.create(
            name="report 1",
            description="report 1",
            meta={},
            service=service,
            user_profile=self.profile,
            state="ready"
        )
        Report.objects.create(
            name="report 1",
            description="report 1",
            meta={},
            service=service,
            user_profile=self.profile,
            state="prepare"
        )

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

    def test_list_ready_reports(self):
        url = reverse('report-ready')

        self.client.credentials(HTTP_AUTHORIZATION=self.user_token)
        response = self.client.get(url)

        reports = Report.objects.filter(user_profile=self.profile, state='ready')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ReportSerializer(instance=reports, many=True).data, response.data['results'])
