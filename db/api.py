from db.models import User
from rest_framework import viewsets, permissions
from db.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
