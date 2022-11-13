from django.contrib import admin
from .models import Todo

# Register your models here.


# admin.site.register(Todo)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Todo admin"""
    list_display = ("id","text", "image", "description", "price", "timestamp","completed", "updated", "user")
    list_display_links = ("text",)

