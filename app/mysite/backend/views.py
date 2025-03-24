from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'green page',
        'colors': ['pink', 'green', 'red']
    }

    return render(request, 'backend/index.html', data)
