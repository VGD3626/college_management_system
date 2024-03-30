from django.shortcuts import render, redirect
from .models import Faculty, AttendanceRecord, Exam, Subject, Program
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

def syllabus(request):
    return render(request, 'viewSyllabus.html', {'title': 'syllabus', 'sidebar': 'sidebars/facultySidebar.html'})


def studentlist(request):
    stus = Student.objects.all()
    return render(request, 'studentlist.html',
                  {'title': 'studentlist', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus})


def addmarks(request):
    global examtype
    global student_examin
    global sub_examin
    stus=Student.objects.all()

    if request.method == "POST":
        sid=request.POST.get('student_id')
        stus1=Student.objects.get(username=sid)
        student_examin=stus1
        eid=request.POST.get('exam_id')
        exam=Exam.objects.get(examid=eid)
        examtype=exam
        print(stus1.username)

        # print(request.POST)
        if 'marks' in request.POST:
            print("success")
        else:
            program_name=stus1.program_name
            program=Program.objects.get(program_name=program_name)
            sub=Subject.objects.filter(programe=program)
            sub_examin=sub
            for x in sub:
                print(x.subjectname)
            eid=int(request.POST.get('exam_id'))
            exam=Exam.objects.get(examid=eid)
            print(eid)
            print(exam.start_date)
            return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus,'exam':exam,"sub":sub})
    return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus})

def addmarks2(request):
    stus=Student.objects.all()
    if request.method == "POST":
        marks=request.POST.get("marks")
        # for i,j in zip(marks,sub_examin):

            # print(i)
            # print(j)
            # mark=Mark(obtainmarks=i,student=student_examin,exam=examtype,subject=j)
            # print(mark)
            # mark.save()
    return redirect('addmarks')
    # return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus})