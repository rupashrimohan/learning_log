from django.shortcuts import get_object_or_404, render, redirect
from .models import Topic, Entry
from django.http import Http404
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# --- Internal Helper Functions ---
def _check_topic_owner(request, topic):
    """Verify that the topic belongs to the current user."""
    if topic.owner != request.user:
        raise Http404("You didn't create the topic you requested.")


# Public views
def index(request):
    """The Home page for Learning Log."""
    return render(request, "learning_log/index.html")


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_log/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show the specific topic details"""

    topic = get_object_or_404(Topic, id=topic_id)

    # Make sure the topic belongs to the current user.
    _check_topic_owner(request, topic)

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_log/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted;create a blank form.
        form = TopicForm()

    else:
        # POST data submitted;process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_log:topics")

    # Display a blank invalid form.
    context = {"form": form}
    return render(request, "learning_log/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a specific topic"""
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    _check_topic_owner(request, topic)

    if request.method != "POST":
        # No data submitted
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_log:topic", topic_id=topic_id)

    # Display a blank form
    context = {"topic": topic, "form": form}
    return render(request, "learning_log/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit the entries"""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    # Make sure the topic belongs to the current user.
    _check_topic_owner(request, topic)

    if request.method != "POST":
        # Initial Request, fill the form with the current entry
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_log:topic", topic_id=topic.id)
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_log/edit_entry.html", context)
