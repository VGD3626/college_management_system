from django.contrib import admin
from django.urls import path, include
import userAuth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userAuth.urls'), name='userAuth'),
]





