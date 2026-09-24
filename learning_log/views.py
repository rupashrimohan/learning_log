from django.shortcuts import render
from .models import Topic
from django.http import Http404

# Create your views here.


def index(request):
    """The Home page for Learning Log."""
    return render(request, "learning_log/index.html")


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_log/topics.html", context)


def topic(request, topic_id):
    """Show the specific topic details"""
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist.")
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_log/topic.html", context)
