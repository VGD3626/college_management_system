from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Faculty, AttendanceRecord, Exam
from studentPanel.models import Student
from django.utils import timezone


def dashboard(request):
    uname = request.user.username
    user = Faculty.objects.get(username=uname)
    print(user.first_name)
    return render(request, 'facultyDashboard.html',
                  {'title': 'facultyDashboard', 'sidebar': 'sidebars/facultySidebar.html', 'user': user})


def updateattendance(request):
    stus = Student.objects.all()
    today = timezone.now()
    if request.method == "POST":
        sid = request.POST.get('student_id')
        # month=request.POST.get('month')
        total_hour = request.POST.get('tday')
        working_hour = request.POST.get('pday')
        print(working_hour)
        student = Student.objects.get(username=sid)
        record = AttendanceRecord(student=student, total_hours=total_hour, present_hours=working_hour,
                                  upload_date=today)
        record.save()
    return render(request, 'updateAttendance.html',
                  {'title': 'updateattendance', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus,
                   'today': today})


def addmarks(request):
    stus = Student.objects.all()

    if request.method == "POST":
        print("check")
        if 'marks' in request.POST:
            print("check")

        else:
            eid = request.POST.get('exam_id')
            exam = Exam.objects.get(examid=eid)
            print(eid)
            print(exam.start_date)
            return render(request, 'addMarks.html',
                          {'title': 'addmarks', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus, 'exam': exam})
    return render(request, 'addMarks.html',
                  {'title': 'addmarks', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus})


def syllabus(request):
    return render(request, 'viewSyllabus.html', {'title': 'syllabus', 'sidebar': 'sidebars/facultySidebar.html'})


def studentlist(request):
    stus = Student.objects.all()
    return render(request, 'studentlist.html',
                  {'title': 'studentlist', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus})