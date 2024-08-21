from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
"""
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'userName', 'firstName', 'lastName', 'is_admin', 'is_staff', 'is_service_provider')
    list_filter = ('is_admin', 'is_staff', 'is_service_provider')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('userName', 'firstName', 'lastName', 'phoneNumber', 'address')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_service_provider', 'is_active')}),
        ('Important dates', {'fields': ('lastLogin', 'createdAt', 'updatedAt')}),
    )
    search_fields = ('email', 'userName')
    ordering = ('email',)
    filter_horizontal = ()
"""
admin.site.register(User)