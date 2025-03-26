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
    path('edit_groups', views.edit_groups, name='edit_groups'),
    path('new_period', views.new_period, name='new_period'),
    path('subject_edit', views.subject_edit, name='subject_edit'),
    path('subject_table_remove/<int:id>/', views.subject_table_remove, name='subject_table_remove'),
    path('subject_table_add', views.subject_table_add, name='subject_table_add'),
    path('teacher_edit/<int:id>/', views.teacher_edit, name='teacher_edit'),
    path('admin_edit', views.admin_edit, name='admin_edit'),
    path('statistics_def', views.statistics_def, name='statistics_def'),
    path('dpo_table', views.dpo_table, name='dpo_table'),
    path('criteria_table', views.criteria_table, name='criteria_table'),
    path('criteria_table_add', views.criteria_table_add, name='criteria_table_add'),
    path('criteria_table_remove/<int:id>', views.criteria_table_remove, name='criteria_table_remove'),
    path('teacher_table_remove/<int:id>', views.teacher_table_remove, name='teacher_table_remove'),
    path('teacher_table_add/<int:id>', views.teacher_table_add, name='teacher_table_add'),
    ]
