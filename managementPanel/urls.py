from django.contrib import admin
from django.urls import path, include

from managementPanel import views

urlpatterns = [
    # path('login/', include('userAuth.urls')),
    # path('admin/', admin.site.urls)
    path('directorDashboard', views.dashboard, name='directordashboard'),
    path('addclub', views.addclub, name='addclub'),
    path('logout', views.logout_user, name='logout')
]
