from django.shortcuts import render, redirect
from .models import Topic
from django.http import JsonResponse
from .forms import TopicForm, EntryForm


# Home
def index(request):
    """The home page for Learning Log."""

    return render(request, 'learning_log/index.html')


# Topic
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_log/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }

    return render(request, 'learning_log/topic.html', context)


def create_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(to='learning_log:topic.index')

    context = {
        'form': form
    }

    return render(request, 'learning_log/create_topic.html', context)


# Entry
def create_entry(request):
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)

        if (form.is_valid()):
            form.save()
            return redirect(to='learning_log:index')

    return render(request, 'learning_log/create_entry.html', {'form': form})


# Ping
def ping(request):
    return JsonResponse({'ping': 'pong'})
