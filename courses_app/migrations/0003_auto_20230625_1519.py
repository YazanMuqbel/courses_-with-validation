# Generated by Django 2.2.4 on 2023-06-25 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_auto_20230625_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]
