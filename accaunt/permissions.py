from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Foydalanuvchilarga o'z profilini tahrirlashiga ruxsat bering."""
    def has_object_permission(self, request, view, obj):
        """Foydalanuvchilarning o'z profilini tahrir qilmoqchi ekanligini tekshiring"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
class PostOwnStatus(permissions.BasePermission):
    """Foydalanuvchilarga o'z holatini yangilashiga ruxsat bering."""
    def has_object_permission(self, request, view, obj):
        """Foydalanuvchilar o'z holatini yangilamoqchi ekanligini tekshiring"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id