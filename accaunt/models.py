from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Djangoga bizning foydalanuvchi modelimiz bilan ishlashga yordam beradi"""

    def create_user(self, email, name, password=None):
        """Yangi foydalanuvchi profili obyektlarini yaratadi"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Berilgan tafsilotlar bilan yangi superfoydalanuvchi yaratadi va saqlaydi"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Tizimimizda "foydalanuvchi profili" ni ifodalaydi."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Foydalanuvchilarning to'liq ismini olish uchun foydalaniladi."""
        return self.name

    def get_short_name(self):
        """Foydalanuvchilarning qisqa nomini olish uchun foydalaniladi."""
        return self.name

    def __str__(self):
        return self.email
