from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username", "email", "last_name",
        "first_name", "role", "team",
        "is_staff"
    ]
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (
            None, {
                "classes": ("wide", ),
                "fields": ("username", "first_name", "last_name", "email", "role", "team", "password1", "password2")
                }
        ),
    )
    fieldsets = (
        (
            None, {"fields": ("first_name", "last_name", "role", "team")}
        ),
    )




admin.site.register(CustomUser, CustomUserAdmin)