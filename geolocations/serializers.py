from rest_framework import serializers
from geolocations.models import Geolocation


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ["id", "ip", "url", "latitude", "longitude"]
