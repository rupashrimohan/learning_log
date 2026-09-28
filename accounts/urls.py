"""Defines URL patterns for accounts."""

from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register, name="register"),
]  # Include default urls.
