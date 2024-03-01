from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Faculty

def dashboard(request):
    # uname=request.user.username
    # user=Faculty.objects.get(username=uname)
    # print(user.first_name)
    return render(request, 'facultyHomepage.html', {'title':'facultyDashboard', 'sidebar':'sidebars/facultySidebar.html'})

def updateattendance(request):
     return render(request, 'updateAttendance.html', {'title':'updateattendance', 'sidebar':'sidebars/facultySidebar.html'})

def addmarks(request):
    return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html'})

def syllabus(request):
    return render(request, 'viewSyllabus.html', {'title':'syllabus', 'sidebar':'sidebars/facultySidebar.html'})

def studentlist(request):
    return render(request, 'studentlist.html', {'title':'studentlist', 'sidebar':'sidebars/facultySidebar.html'})



