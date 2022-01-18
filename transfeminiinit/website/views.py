from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Post, Tag
from django.views import generic
from parler.views import TranslatableSlugMixin

def home(request):
    context = {
        'home_title': _('home_title'),
        'home_message': _('home_message'),
    }

    return render(request, 'home.html', context=context)

class PostListView(generic.ListView):
    model = Post
    template_name = 'website/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        context['post_list'] = list()
        for p in context['object_list'].filter(translations__status='published').order_by('-translations__publish'):
            if p not in context['post_list']:
                context['post_list'].append(p)

        return context

class PostDetailView(TranslatableSlugMixin, generic.DetailView):
    model = Post
    template_name = 'website/post_detail.html'
    context_object_name = 'post'
