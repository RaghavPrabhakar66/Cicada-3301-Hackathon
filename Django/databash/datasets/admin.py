from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class DatasetAdmin(admin.ModelAdmin):

    list_display = ('id', 'owner', 'description', 'stars')
    list_filter = ('owner', 'id', 'owner', 'description', 'stars')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Dataset, DatasetAdmin)
