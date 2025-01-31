from django.contrib import admin

from .models import Habilitation, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "groups_list")


@admin.register(Habilitation)
class HabilitationAdmin(admin.ModelAdmin):
    pass
