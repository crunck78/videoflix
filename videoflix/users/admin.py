from dataclasses import fields
from django.contrib import admin

from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Individual Dates',
            {
                'fields': (
                    'custom',
                    'phone',
                    'address',
                )
            }
        )
    )
# Register your models here.
# admin.site.register(CustomUser)