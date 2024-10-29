# Generated by Django 3.2.24 on 2024-10-18 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=100)),
                ('facility', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('number_days', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Package_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('PACKAGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.package')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='PLACE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.place'),
        ),
        migrations.CreateModel(
            name='Hotel_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('number_rooms', models.CharField(max_length=100)),
                ('HOTEL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='PLACE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.place'),
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
