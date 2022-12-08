from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest, JsonResponse

from .models import Post


def blog_list(request: HttpRequest):
    posts_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts_list})


def post_detail(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse(f'<b>{post.title}</b>')


def error404(request, exception):
    return render(request, 'blog/error_404.html')