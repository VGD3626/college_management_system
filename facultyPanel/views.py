from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Faculty, AttendanceRecord, Exam, Subject, Program, Announcement, Mark
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
    user = Faculty.objects.get(username=request.user.username)
    with open(f'static/{user.department}syllabus.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=syllabus.pdf'
        return response


def studentlist(request):
    stus = Student.objects.all()
    return render(request, 'studentlist.html',
                  {'title': 'studentlist', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus})


def addmarks(request):
    global examtype
    global student_examin
    global sub_examin
    stus = Student.objects.all()

    if request.method == "POST":
        sid = request.POST.get('student_id')
        stus1 = Student.objects.get(username=sid)
        student_examin = stus1
        eid = request.POST.get('exam_id')
        exam = Exam.objects.get(examid=eid)
        examtype = exam
        print(stus1.username)

        # print(request.POST)
        if 'marks' in request.POST:
            print("success")
        else:
            program_name = stus1.program_name
            program = Program.objects.get(program_name=program_name)
            sub = Subject.objects.filter(programe=program)
            sub_examin = sub
            for x in sub:
                print(x.subjectname)
            eid = int(request.POST.get('exam_id'))
            exam = Exam.objects.get(examid=eid)
            print(eid)
            print(exam.start_date)
            return render(request, 'addMarks.html',
                          {'title': 'addmarks', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus, 'exam': exam,
                           "sub": sub})
    return render(request, 'addMarks.html',
                  {'title': 'addmarks', 'sidebar': 'sidebars/facultySidebar.html', 'stus': stus})



def makeAnnouncement(request):
    return render(request, 'makeAnnouncment.html', {'title': 'make announcement', 'sidebar': 'sidebars/facultySidebar.html'})

def submitAnnouncement(request):
    user = request.user
    announcement = Announcement(content=request.POST.get("content"), sender=user, time=now(),
                                title=request.POST.get("title"))
    announcement.save()
    for s in Student.objects.all():
        announcement.receiver.add(User.objects.get(username=s.username))
    return render(request, 'makeAnnouncment.html', {'title': 'make announcement', 'sidebar': 'sidebars/facultySidebar'
                                                                                             '.html'})

def logout_user(request):
    logout(request)
    return redirect('login')


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
        exam=Exam.objects.get(id=eid)
        examtype=exam
        print(stus1.username)

        # print(request.POST)
        if 'marks' in request.POST:
            print("success")
        else:
            # sid=request.POST.get('student_id')
            # stus1=Student.objects.get(username=sid)
            program_name=stus1.program_name
            program=Program.objects.get(program_name=program_name)
            sub=Subject.objects.filter(program=program)
            sub_examin=sub
            for x in sub:
                print(x.subjectname)
            # eid=request.POST.get('exam_id')
            # exam=Exam.objects.get(examid=eid)
            print(eid)
            print(exam.start_date)
            return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus,'exam':exam,"sub":sub})
    return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus})

def addmarks2(request):
    stus=Student.objects.all()
    if request.method == "POST":
        marks=request.POST.getlist("marks")
        print(examtype)
        print(student_examin)
        for i,j in zip(marks,sub_examin):
            if i and j and examtype and student_examin:
                print("yes")
            print(i)
            print(j.subjectname)
            markobject=Mark(obtained_marks=i,student=student_examin,exam=examtype,subject=j)
            markobject.save()
            print(markobject)
    return redirect('addmarks')
    # return render(request, 'addMarks.html', {'title':'addmarks', 'sidebar':'sidebars/facultySidebar.html','stus':stus})