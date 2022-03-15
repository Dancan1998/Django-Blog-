from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm


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


def register(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)
