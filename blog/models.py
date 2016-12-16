from django.db import models
from django.utils import timezone
#coding: utf-8
SHORT_LEN_TXT = 100

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def get_short_text(self):
        if len(self.text) > SHORT_LEN_TXT:
            return self.text[:SHORT_LEN_TXT] + '...'
        else:
            return self.text

