from django.contrib import admin
from .models import Topic, Entry

# Register your models here.

admin.site.register([
    Topic,
    Entry,
])
