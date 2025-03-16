from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class UserViewSet(CreateAPIView):
    serializer_class = UserSerializer
