from django.urls import path
from .views import PostListView, PostDetailView, AboutTemplateView, ContactCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_posts'),
    path('contact/', ContactCreateView.as_view(), name='blog_contact'),
    path('about/', AboutTemplateView.as_view(), name='blog_about'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='blog_post')
]
