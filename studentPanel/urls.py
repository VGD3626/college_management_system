from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('studentDashboard', views.display_studentdashboard, name='display_studentdashboard'),
    path('attendance', views.display_attendance, name='display_attendance'),
    path('result', views.display_result, name='display_result'),
    path('syllabus', views.display_syllabus, name='display_syllabus'),
    path('fees', views.display_gen_fee_receipt, name='display_gen_fee_receipt'),
    path('hall-ticket', views.display_gen_hallticket, name='display_gen_hallticket' ),
    path('notifications', views.display_notifications, name='display_notifications'),
    path('download', views.download_hallticket, name='download_hallticket'),
    path('feeReceipt', views.display_gen_fee_receipt, name='display_gen_fee_receipt'),
    path('downloadFeeReceipt', views.download_fee_receipt, name='download_fee_receipt'),
    path('logout', views.logout_user, name='logout')
\
]
