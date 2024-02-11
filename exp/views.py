from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def x(request):
    return render(request, 'updateAttendance.html',{'title':'Add Marks','sidebar':'sidebars/facultySidebar.html'})