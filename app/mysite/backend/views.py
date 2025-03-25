from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AForm

# Create your views here.

def index(request):

    return render(request, 'backend/user/начало.html')


def rating(request):

    return render(request, 'backend/user/рейтинг.html')


def statistics(request):

    return render(request, 'backend/user/статистика.html')


def admin_main(request):

    return render(request, 'backend/admin/сайт.html')

