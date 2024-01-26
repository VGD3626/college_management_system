from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def studentPanel(request):
    # s = Student('vrund','vrund')
    return render(request, "login.html", {'title': 'home', 'sidebar': 'sidebars/facultySidebar.html'})