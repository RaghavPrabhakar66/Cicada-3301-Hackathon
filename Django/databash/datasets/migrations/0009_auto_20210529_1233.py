# Generated by Django 3.2.3 on 2021-05-29 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0008_contribution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='integer',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='text',
        ),
    ]