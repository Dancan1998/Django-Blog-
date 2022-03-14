from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'Dancan Chibole',
     'age': 33,
     'content': 'developer',
     'title': 'Hello World',
     'date_posted':'August 20',
     },
    {'author': 'Evans Smith',
     'age': 22,
     'content': 'teacher',
     'title': '100 days',
     'date_posted':'Nov 18',
     }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context=context)
