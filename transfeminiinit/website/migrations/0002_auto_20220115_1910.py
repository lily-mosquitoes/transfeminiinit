# Generated by Django 3.2 on 2022-01-15 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=250, verbose_name='post_title')),
                ('body', models.TextField(verbose_name='post_body')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish', verbose_name='post_slug')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='post_publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='post_created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='post_updated')),
                ('status', models.CharField(choices=[('draft', 'post_status_draft'), ('published', 'post_status_published')], default='draft', max_length=10, verbose_name='post_status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='post_author')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='website.post')),
            ],
            options={
                'verbose_name': 'post Translation',
                'db_table': 'website_post_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
