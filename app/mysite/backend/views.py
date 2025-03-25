from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AForm

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

def create(request):
    error = ''
    if request.method == 'POST':
        form = AForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'false data'
            
    form = AForm()
    data = {
        'form': form,
        'error': error
    }
        
    return render(request, 'backend/create.html', data)
    
        
