from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context=context)
