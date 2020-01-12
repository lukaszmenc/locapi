from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("geolocations.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/accounts/", include("accounts.urls")),
]


def response400(request, exception):
    status = 400
    data = {
        "status": status,
        "message": "Bad request.",
    }
    return JsonResponse(data=data, status=status)


def response404(request, exception):
    status = 404
    data = {
        "status": status,
        "message": "Failed to establish connection. Unable to connect requested service or database.",
    }
    return JsonResponse(data=data, status=status)


def response500(request):
    status = 500
    data = {
        "status": status,
        "message": "Failed to establish connection. Unable to connect requested service or database.",
    }
    return JsonResponse(data=data, status=status)


handler400 = response400
handler404 = response404
handler500 = response500
