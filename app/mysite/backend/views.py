from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'main page',
        'h1': 'Заголовок 1',
        'colors': ['pink', 'green', 'red']
    }

    return render(request, 'backend/index.html', data)


def about(request):
    data = {
        'title': 'about page',
        'h1': 'About h',
        'colors': ['pink', 'green', 'red']
    }

    return render(request, 'backend/about.html', data)


def profile(request):
    data = {
        'user': 'some user'
    }

    return render(request, 'backend/profile.html', data)
