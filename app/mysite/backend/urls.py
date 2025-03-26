from django.urls import path

from . import views

urlpatterns = [
    # user
    path('', views.index, name='index'),
    path('update_criterias', views.update_criterias, name='update_criterias'),
    path('home_def', views.home_def, name='home_def'),
    path('rating', views.rating, name='rating'),
    path('statistics', views.statistics, name='statistics'),
    # admin
    path('admin_main', views.admin_main, name='admin_main'),
    path('eng_teacher_list', views.eng_teacher_list, name='eng_teacher_list'),
    path('edit_groups', views.edit_groups, name='edit_groups'),
    path('math_teacher_list', views.math_teacher_list, name='math_teacher_list'),
    path('rus_teacher_list', views.rus_teacher_list, name='rus_teacher_list'),
    path('new_period', views.new_period, name='new_period'),
    path('teacher_edit', views.teacher_edit, name='teacher_edit'),
    path('admin_edit', views.admin_edit, name='admin_edit'),
    path('statistics_def', views.statistics_def, name='statistics_def'),
    path('dpo_table', views.dpo_table, name='dpo_table'),
    path('criteria_table', views.criteria_table, name='criteria_table'),
    path('criteria_table_add', views.criteria_table_add, name='criteria_table_add'),
    path('criteria_table_remove/<int:id>/', views.criteria_table_remove, name='criteria_table_remove'),
    ]
