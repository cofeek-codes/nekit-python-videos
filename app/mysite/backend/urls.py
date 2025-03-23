from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
    # path('role', views.choice_role, name='role')
]
