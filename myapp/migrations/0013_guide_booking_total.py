# Generated by Django 3.2.24 on 2024-10-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_guide_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide_booking',
            name='total',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
