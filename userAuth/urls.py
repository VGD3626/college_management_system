from django.contrib import admin
from django.urls import path, include
import CMS
from . import views

urlpatterns = [
    path('', views.user_authantication, name='login'),
    path('', include('studentPanel.urls'), name='studentPanel'),
    path('', include('facultyPanel.urls'), name='facultyPanel'),
    path('', include('acPanel.urls'), name='acPanel'),
    path('', include('managementPanel.urls'), name='managementPanel')
]
