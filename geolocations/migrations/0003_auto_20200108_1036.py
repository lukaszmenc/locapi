# Generated by Django 3.0.2 on 2020-01-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocations', '0002_auto_20200108_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocation',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geolocation',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='geolocation',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='url',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
