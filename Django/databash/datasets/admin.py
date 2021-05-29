from django.contrib import admin
from . import models

class DatasetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'owner',
        'data',
        'columns',
        'description',
        'stars',
    )
    list_filter = (
        'owner',
        'id',
        'name',
        'owner',
        'data',
        'columns',
        'description',
        'stars',
    )
    search_fields = ('name',)


class AttributeAdmin(admin.ModelAdmin):

    list_display = ('id', 'dataset', 'name', 'datatype')
    list_filter = ('dataset', 'id', 'dataset', 'name', 'datatype')
    search_fields = ('name',)


class ContributionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sender',
        'dataset',
        'isSpam',
        'textinput',
        'intinput',
    )
    list_filter = (
        'sender',
        'dataset',
        'isSpam',
        'id',
        'sender',
        'dataset',
        'isSpam',
        'textinput',
        'intinput',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Dataset, DatasetAdmin)
_register(models.Attribute, AttributeAdmin)
_register(models.Contribution, ContributionAdmin)
