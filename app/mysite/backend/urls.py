from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rating', views.rating, name='rating'),
    path('statistics', views.statistics, name='statistics'),
    path('admin_main', views.admin_main, name='admin_main'),
    ]
