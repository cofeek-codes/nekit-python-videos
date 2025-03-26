from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TeacherForm

# Create your views here.

def index(request):

    return render(request, 'backend/user/начало.html')


def home_def(request):

    return render(request, 'backend/user/home_def.html')


def rating(request):

    return render(request, 'backend/user/рейтинг.html')


def statistics(request):

    return render(request, 'backend/user/статистика.html')


def admin_main(request):

    return render(request, 'backend/admin/сайт.html')

def eng_teacher_list(request):

    return render(request, 'backend/admin/angl-teacher.html')

def edit_groups(request):

    return render(request, 'backend/admin/edit-groups.html')

def pe_teacher_list(request):

    return render(request, 'backend/admin/fizra-teacher.html')

def math_teacher_list(request):

    return render(request, 'backend/admin/matan-teacher.html')


def rus_teacher_list(request):

    return render(request, 'backend/admin/russian-teacher.html')


def new_period(request):

    return render(request, 'backend/admin/new-period.html')


def teacher_edit(request):

    return render(request, 'backend/admin/teacher-redact.html')


def admin_edit(request):

    return render(request, 'backend/admin/админы-школы.html')


def statistics_def(request):

    return render(request, 'backend/admin/общая-таблица.html')


def dpo_table(request):

    return render(request, 'backend/admin/редактирование-дпо.html')


def criteria_table(request):

    return render(request, 'backend/admin/редактировать-критерии.html')
