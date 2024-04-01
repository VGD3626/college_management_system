from django.contrib.auth import logout
from django.shortcuts import render, redirect

from django.shortcuts import render

from facultyPanel.models import Faculty
from managementPanel.models import Hod, Club
from studentPanel.models import Student

def dashboard(request):
    uname = request.user.username
    user = Hod.objects.get(username=uname)
    print(user.first_name)
    return render(request, 'directorDashboard.html',
                  {'title': 'DirectorDashboard', 'sidebar': 'sidebars/dirSidebar.html', 'user': user})


def addclub(request):
    hod = Hod.objects.all()
    stus = Student.objects.all()
    faculty = Faculty.objects.all()
    if request.method == "POST":
        id = request.POST.get('clubid')
        facultyname = request.POST.get('faculty')
        clubname = request.POST.get('clubname')
        hodname = request.POST.get('hod')
        studentname = request.POST.getlist('student')
        date = request.POST.get('estdate')
        clubtype = request.POST.get('type')
        hod1 = Hod.objects.get(first_name=hodname)
        faculty1 = Faculty.objects.get(first_name=facultyname)
        print(hod1)
        print(date)
        print(clubtype)
        print(faculty1)
        # for i in studentname:
        #     stus1=Student.objects.get(first_name=i)
        #     print(stus1)
        #     club=Club(clubid=id,clubname=clubname,hod=hod1,student=stus1,faculty=faculty1,estdate=date,type=clubtype)
        #     # club.save()
        club = Club.objects.create(clubid=id, clubname=clubname, faculty=faculty1, estdate=date, type=clubtype)

        # Assign Hod to the club
        club.hod.add(hod1)

        # Assign Students to the club
        for studentname in studentname:
            student = Student.objects.get(first_name=studentname)
            club.student.add(student)
            print(club)
    return render(request, 'addClubs.html',
                  {'title': 'addclub', 'sidebar': 'sidebars/dirSidebar.html', 'hods': hod, 'students': stus,
                   'faculty': faculty})


def logout_user(request):
    logout(request)
    print("logged out")
    return redirect('login')