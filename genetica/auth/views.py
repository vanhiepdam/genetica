from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from genetica.auth.serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer
from genetica.auth.services import UserService
from genetica.decorators import to_json_response
from genetica.permissions import IsAccountOwnerOrAdmin


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserService.list_all_users()
    lookup_field = 'username'

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'destroy']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAccountOwnerOrAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    @to_json_response
    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)

            return self.serializer_class(instance=user).data, 200
        raise ValidationError("Can not create user")

    @to_json_response
    def update(self, request, pk=None, *args, **kwargs):
        user = self.get_object()
        serializer = UpdateUserSerializer(data=request.data, instance=user)

        if serializer.is_valid():
            user = serializer.save()

            return self.serializer_class(instance=user).data, 200
        raise ValidationError("Can not update user")
