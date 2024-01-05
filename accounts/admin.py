from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from accounts.models import Contact,Place


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email","phone_number","first_name","last_name","address", "is_staff", "is_active",)
    list_filter = ("email","phone_number","first_name","last_name","address","is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password","phone_number","first_name","last_name","address",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions","phone_number",
                "first_name","last_name","address"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact)
admin.site.register(Place)