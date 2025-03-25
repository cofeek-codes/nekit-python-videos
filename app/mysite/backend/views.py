from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AForm

# Create your views here.

def index(request):

    return render(request, 'backend/user/начало.html')
