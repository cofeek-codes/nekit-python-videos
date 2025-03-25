from django.urls import path

from . import views

urlpatterns = [
    # user
    path('', views.index, name='index'),
    path('home_def', views.home_def, name='home_def'),
    path('rating', views.rating, name='rating'),
    path('statistics', views.statistics, name='statistics'),
    # admin
    path('admin_main', views.admin_main, name='admin_main'),
    path('eng_teacher_list', views.eng_teacher_list, name='eng_teacher_list'),
    ]
