from django.http import HttpResponse
from django.shortcuts import redirect, render

import json

from .models import Criteria, Period, Teacher

from .forms import TeacherForm

# Create your views here.

def index(request):
    data = {
        'criterias': Criteria.objects.all()
    }

    return render(request, 'backend/user/начало.html', data)

def update_criterias(request):
     if request.method == 'POST':

        data = json.loads(request.body)
        
        # Обновляем все критерии
        for i, item in enumerate(data['titles']):
            criteria = Criteria.objects.filter(id=i+1).first()
            if criteria:
                criteria.title = item['title']
                criteria.save()

        for i, count in enumerate(data['counts']):
            criteria = Criteria.objects.filter(id=i+1).first()
            if criteria:
                criteria.count = count['count']
                criteria.save()

        return redirect('index')
                
def home_def(request):

    return render(request, 'backend/user/home_def.html')


def rating(request):
    data = {
    'teachers': Teacher.objects.all()    
    }
    
    return render(request, 'backend/user/рейтинг.html', data)


def statistics(request):
    data = {
        'periods': Period.objects.all()
        }

    return render(request, 'backend/user/статистика.html', data)


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
