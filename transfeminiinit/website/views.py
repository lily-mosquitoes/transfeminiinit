from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Post, Tag
from django.views import generic

def home(request):
    context = {
        'home_title': _('home_title'),
        'home_message': _('home_message'),
    }

    return render(request, 'home.html', context=context)

# def post_list(request):
#     posts = Post.objects.filter(translations__status='published').order_by('translations__publish')
#
#     return render(request, 'post_list.html', { 'posts': posts })
#
# def post_detail(request):
#     post = get_object_or_404(Post, slug=post, status='published')

class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        print(context)
        return context

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
