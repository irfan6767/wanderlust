# Generated by Django 3.2.24 on 2024-10-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_hotel_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='package_booking',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
