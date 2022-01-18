from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name="post_list"),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
]
