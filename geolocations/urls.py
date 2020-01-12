from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from geolocations import views

urlpatterns = [
    path("geolocations/", views.geolocation_list),
    path("geolocations/<int:pk>", views.geolocation_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
