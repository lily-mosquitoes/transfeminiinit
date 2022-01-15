from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    body = models.TextField()

    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
