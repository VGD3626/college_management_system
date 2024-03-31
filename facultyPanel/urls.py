from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('facultyDashboard', views.dashboard,name='facultydashboard'),
    path('updateattendance', views.updateattendance,name='updateattendance'),
    path('addmarks', views.addmarks,name='addmarks'),
    path('viewSyllabus', views.syllabus,name='syllabus'),
    path('studentlist', views.studentlist,name='studentlist'),
    path('addmarks2', views.addmarks2,name='addmarks2'),
    path('makeAnnouncement', views.makeAnnouncement,name='makeAnnouncement'),
    path('logout', views.logout_user, name='logout')
]
