from django.db import models


class Geolocation(models.Model):
    ip = models.GenericIPAddressField()
    url = models.CharField(max_length=2048, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
