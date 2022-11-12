from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# Bu yerda views dagi malumotlar
from .views import (
    UserProfileViewSet,
    LoginViewSet,
    )

# Tayyor bo'lgan django rest api
router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename="profile")
router.register('login', LoginViewSet, basename="login")

urlpatterns = [
    path('', include(router.urls)),
]