from django.db import models
from django.contrib.auth.models import User
from django.http import Http404

# Create your models here.


class Topic (models.Model):
    text = models.CharField(max_length=254)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def check_topic_owner(self, user):
        if self.owner != user:
            raise Http404


class Entry (models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
