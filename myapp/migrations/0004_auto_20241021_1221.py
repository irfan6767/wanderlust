# Generated by Django 3.2.24 on 2024-10-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_package_booking_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='status',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='type',
        ),
    ]
