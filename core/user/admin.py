from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import MyUserChangeForm, MyUserCreationForm
# Register your models here.

@admin.register(MyUser)
class CustomAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    change_user_id_template = None

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (("Personal info"), {"fields": ("role", "first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ("phone_number", "role", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "role")
    search_fields = ("phone_number", "first_name", "last_name", "email")
    ordering = ("phone_number",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
