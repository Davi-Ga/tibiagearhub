from django.urls import path, include, reverse
from django.shortcuts import redirect

urlpatterns = [
    path("docs/", include("core.swagger.urls")),
]
