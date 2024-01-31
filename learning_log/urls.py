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

    # Entry
    path('entries/create', view=views.create_entry, name='entry.create'),

    path('ping', view=views.ping, name='ping'),
]
