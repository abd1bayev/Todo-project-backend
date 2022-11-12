from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Bu yerda models dagi modellar
from .models import (
    UserProfile,
)
# Bu yerda permissions dagi malumotlar
from .permissions import (
    UpdateOwnProfile,
)
# Bu yerda serializers dagi malumotlar
from .serializers import (
    UserProfileSerializer,
)

class UserProfileViewSet(viewsets.ModelViewSet):
    """Profil yaratish va yangilash bilan shug'ullanadi"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')
class LoginViewSet(viewsets.ViewSet):
    """ Elektron pochta va parolni tekshiradi va autentifikatsiya belgisini qaytaradi."""
    serializer_class = AuthTokenSerializer
    def create(self, request):
        """Tokenni tasdiqlash va yaratish uchun ObtainAuthToken APIView-dan foydalaning."""
        return ObtainAuthToken().as_view()(request=request._request)
