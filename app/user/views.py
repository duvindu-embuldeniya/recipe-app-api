

from rest_framework import viewsets
from core.models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from . permissions import UpdateOwnUser
from rest_framework.permissions import IsAuthenticated




from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings







class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # even we logged-in,need to pass Token Header
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnUser]






class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
