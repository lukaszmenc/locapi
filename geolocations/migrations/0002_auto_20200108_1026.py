# Generated by Django 3.0.2 on 2020-01-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolocations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geolocation',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='geolocation',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='geolocation',
            name='longitude',
        ),
    ]