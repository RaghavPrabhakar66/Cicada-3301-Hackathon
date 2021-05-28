from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'password',
        'last_login',
        'is_superuser',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'bio',
        'github',
        'xp',
        'rank',
    )

    raw_id_fields = ('groups', 'user_permissions')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.User, UserAdmin)
