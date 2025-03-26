from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

import json
import time


from .models import Criteria, Period, Subject, Teacher

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

def edit_groups(request):

    return render(request, 'backend/admin/edit-groups.html')

def new_period(request):

    return render(request, 'backend/admin/new-period.html')


def subject_edit(request):
    data = {
    'subjects': Subject.objects.all()    
    }
    return render(request, 'backend/admin/subject-redact.html', data)

def subject_table_remove(request, id):
    subject_to_delete = Subject.objects.get(id=id)
    if subject_to_delete:
        subject_to_delete.delete()
    
    return redirect('subject_edit')

def subject_table_add(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_subject = Subject(title=data['title'])
        new_subject.save()
        time.sleep(1)
        
    return redirect('subject_edit')


def teacher_edit(request, id):
    data = {
    'teachers': Teacher.objects.filter(subject_id=id),
    'subject': Subject.objects.filter(id=id).first()
    }
    return render(request, 'backend/admin/teacher-redact.html', data)



def admin_edit(request):

    return render(request, 'backend/admin/админы-школы.html')


def statistics_def(request):

    return render(request, 'backend/admin/общая-таблица.html')


def dpo_table(request):

    return render(request, 'backend/admin/редактирование-дпо.html')


def criteria_table(request):
    data = {
    'criterias': Criteria.objects.all()    
    }
    return render(request, 'backend/admin/редактировать-критерии.html', data)

def criteria_table_add(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_criteria = Criteria(title=data['title'])
        new_criteria.save()
    return redirect('criteria_table')
        

def criteria_table_remove(request, id):
    criteria_to_delete = Criteria.objects.get(id=id)
    if criteria_to_delete:
        criteria_to_delete.delete()
    
    return redirect('criteria_table')

def teacher_table_remove(request, id):
    teacher_to_delete = Teacher.objects.get(id=id)
    subject_id = teacher_to_delete.subject_id
    if teacher_to_delete:
        teacher_to_delete.delete()
    
    return redirect('teacher_edit', subject_id)

def teacher_table_add(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        new_teacher = Teacher(name=data['name'], subject_id=id)
        new_teacher.save()
        time.sleep(1)
        
    return redirect('teacher_edit', id)
