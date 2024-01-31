"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_log'

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Topic
    path('topics', views.topics, name='topic.index'),
    path('topics/<int:topic_id>', views.topic, name='topic.show'),
    path('topics/create', view=views.create_topic, name='topic.create'),
    path(
        'topics/<int:topic_id>/entries/create',
        view=views.create_entry,
        name='topic.entry.create'
    ),

    path('entries/<int:entry_id>/edit', view=views.edit_entry, name='entry.edit'),

    path('ping', view=views.ping, name='ping'),
]
