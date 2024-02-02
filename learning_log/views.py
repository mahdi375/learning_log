from django.shortcuts import render, redirect
from .models import Topic, Entry
from django.http import JsonResponse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# Home
def index(request):
    """The home page for Learning Log."""

    return render(request, 'learning_log/index.html', {'user': request.user})


# Topic
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_log/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    topic.check_topic_owner(request.user)

    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }

    return render(request, 'learning_log/topic.html', context)


@login_required
def create_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if (form.is_valid()):
            topic = form.save(commit=False)
            topic.owner = request.user
            topic.save()
            return redirect(to='learning_log:topic.index')

    context = {
        'form': form
    }

    return render(request, 'learning_log/create_topic.html', context)


# Entry
@login_required
def create_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    topic.check_topic_owner(request.user)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if (form.is_valid()):
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()

            return redirect(to='learning_log:topic.show', topic_id=topic.id)

    return render(request, 'learning_log/create_entry.html', {'form': form, 'topic': topic})


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    form = EntryForm(instance=entry)

    if request.method == 'POST':
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='learning_log:topic.show', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry)

    return render(request, 'learning_log/edit_entry.html', {'form': form, 'entry': entry})

# Ping


def ping(request):
    return JsonResponse({'ping': 'pong'})
