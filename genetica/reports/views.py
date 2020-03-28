from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from genetica.base.base_viewset import BaseViewset
from genetica.decorators import to_json_response
from genetica.reports.models import Report
from genetica.reports.serializers import ReportSerializer
from genetica.reports.services import ReportService


class ReportViewset(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    BaseViewset):

    permission_classes = [IsAuthenticated]
    serializer_class = ReportSerializer

    def get_queryset(self):
        queryset = ReportService.list_all_reports_by_user(user=self.request.user)

        return queryset

    @to_json_response
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if 'state' in request.query_params:
            queryset = queryset.filter(state=request.query_params.get('state'))

        queryset = self.serializer_class.setup_eager_loading(queryset)
        data = self.get_paginated_data(queryset)

        return data, 200

    @action(detail=False, methods=['GET'])
    @to_json_response
    def ready(self, request, *args, **kwargs):
        """
        This endpoint is only for requirement
        """
        kwargs['state'] = Report.STATE_READY
        queryset = ReportService.list_all_reports_by_user_and_state(request.user, state=Report.STATE_READY)
        queryset = self.serializer_class.setup_eager_loading(queryset)
        data = self.get_paginated_data(queryset)

        return data, 200
