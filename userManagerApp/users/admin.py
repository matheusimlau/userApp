from django.contrib import admin
from users import models
from django.apps import apps

app = apps.get_app_config("users")


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


admin.site.register(models.User, UserAdmin)
