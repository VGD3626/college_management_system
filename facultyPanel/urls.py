from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('facultyDashboard', views.dashboard,name='facultydashboard'),
    path('updateattendance', views.updateattendance,name='updateattendance'),
    path('addmarks', views.addmarks,name='addmarks'),
    path('syllabus', views.syllabus,name='syllabus'),
    path('studentlist', views.studentlist,name='studentlist'),

]
