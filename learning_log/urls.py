"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = "learning_log"
urlpatterns = [
    path("", views.index, name="index"),  # Home Page
    path("topics/", views.topics, name="topics"),  # Topics page
    path(
        "topics/<int:topic_id>/", views.topic, name="topic"
    ),  # Detail page for single topic
]
