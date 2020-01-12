import requests
import os

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from geolocations.models import Geolocation
from geolocations.serializers import GeolocationSerializer
from dotenv import load_dotenv


load_dotenv()

API_access_key = os.getenv("API_ACCESS_KEY")


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def geolocation_list(request):
    if request.method == "GET":
        geolocations = Geolocation.objects.all()
        serializer = GeolocationSerializer(geolocations, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        ip = request.data.get("ip") or request.data.get("url")
        try:
            url = "http://api.ipstack.com/" + ip + "?access_key=" + API_access_key
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ip_stack_response = requests.get(url)
        result = ip_stack_response.json()
        request.data["ip"] = result["ip"]
        request.data["latitude"] = result["latitude"]
        request.data["longitude"] = result["longitude"]

        serializer = GeolocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((IsAuthenticated,))
def geolocation_detail(request, pk):
    try:
        geolocation = Geolocation.objects.get(pk=pk)
    except Geolocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GeolocationSerializer(geolocation)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GeolocationSerializer(geolocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
