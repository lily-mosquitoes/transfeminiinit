from django.contrib import admin
from .models import Post, Tag
from parler.admin import TranslatableAdmin

@admin.register(Tag)
class TagAdmin(TranslatableAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    search_fields = ('translations__title', 'translations__body')
    list_display = ('title', 'slug', 'author', 'publish',  'status')
    list_filter = ('translations__status', 'translations__created', 'translations__publish', 'translations__author')
    #raw_id_fields = ('translations__author',) ## can't make this work
    date_hierarchy = 'translations__publish'
    ordering = ('translations__status', '-translations__publish')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
