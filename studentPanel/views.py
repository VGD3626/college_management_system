from time import strftime
from django.shortcuts import render
from facultyPanel.models import *
from .models import Student

def display_studentdashboard(request):
    user = Student.objects.get(username=request.user.username)
    program = user.program
    courses = Subject.objects.filter(program__program_name=program.program_name)

    context = {'title': 'home', 'sidebar': 'sidebars/studentSidebar.html','user':user, 'courses':courses}
    return render(request,'studentDashboard.html', context)


def display_attendance(request):
    user = Student.objects.get(username=request.user.username)
    attendance_records = AttendanceRecord.objects.filter(student__username=user.username)

    for record in attendance_records:
        record.upload_date = strftime('%B-%Y')

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    context = {'title': 'home', 'sidebar': 'sidebars/studentSidebar.html', 'user': user, 'attendance_records':attendance_records, 'months':months}
    return render(request,'viewAttendance.html',context)

def display_result(request):
    return render(request,'viewResults.html', {'title': 'results', 'sidebar': 'sidebars/studentSidebar.html'})

def display_syllabus(request):
    return render(request,'viewSyllabus.html', {'title': 'syllabus', 'sidebar': 'sidebars/studentSidebar.html'})

def display_gen_fee_receipt(request):
    return render(request,'generateFeeReciept.html', {'title': 'generate fee receipt', 'sidebar': 'sidebars/studentSidebar.html'})

def display_gen_hallticket(request):
    return render(request,'generatehallTicket.html', {'title': 'download hall-ticket', 'sidebar': 'sidebars/studentSidebar.html'})

def display_notifications(request):
    return render(request,'viewNotifications.html', {'title': 'view notifications', 'sidebar': 'sidebars/studentSidebar.html'})