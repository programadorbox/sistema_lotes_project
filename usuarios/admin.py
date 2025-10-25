from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "rol", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "rol")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
