from django.contrib import admin
from .models import (
    UserProfile,
)

# admin.site.register(UserProfile) # modelni adminda ko'rinishi
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """User admin, Accaunt"""
    list_display = ("id", "email", "name","is_staff", "is_active")
    list_display_links = ("name",)