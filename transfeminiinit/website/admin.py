from django.contrib import admin
from .models import Post
from parler.admin import TranslatableAdmin

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    search_fields = ('translations__title', 'translations__body')
    list_display = ('title', 'slug', 'author', 'publish',  'status')
    list_filter = ('translations__status', 'translations__created', 'translations__publish', 'translations__author')
    #raw_id_fields = ('translations__author',)
    date_hierarchy = 'translations__publish'
    ordering = ('translations__status', 'translations__publish')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
