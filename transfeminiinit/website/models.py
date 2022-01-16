from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Tag(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=10, verbose_name=_('tag_name')),
    )

    def __str__(self):
        return self.name

class Post(TranslatableModel):
    STATUS_CHOICES = (
        ('draft', _('post_status_draft')),
        ('published', _('post_status_published')),
    )

    translations = TranslatedFields(
        title = models.CharField(max_length=70, verbose_name=_('post_title')),
        description = models.CharField(max_length=170, blank=True, verbose_name=_('post_description')),
        body = RichTextUploadingField(verbose_name=_('post_body')),
        tags = models.ManyToManyField('Tag', verbose_name=_('post_tags')),

        author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts', verbose_name=_('post_author')),
        slug = models.SlugField(max_length=70, unique_for_date='publish', verbose_name=_('post_slug')),

        publish = models.DateTimeField(default=timezone.now, verbose_name=_('post_publish')),
        created = models.DateTimeField(auto_now_add=True, verbose_name=_('post_created')),
        updated = models.DateTimeField(auto_now=True, verbose_name=_('post_updated')),

        status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name=_('post_status')),
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def published_string(self):
        return dict(self.STATUS_CHOICES)['published']
