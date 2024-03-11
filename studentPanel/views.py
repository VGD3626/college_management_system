import io
from time import strftime

from django.contrib.auth import logout
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

from facultyPanel.models import *
from .models import Student
import reportlab


def display_studentdashboard(request):
    user = Student.objects.get(username=request.user.username)
    program = user.program
    courses = Subject.objects.filter(program__program_name=program.program_name)
    print(user.first_name)
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
    user = Student.objects.get(username=request.user.username)
    with open(f'static/{user.program_name}syllabus.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=syllabus.pdf'
        return response

def display_gen_fee_receipt(request):
    return render(request,'generateFeeReceipt.html', {'title': 'generate fee receipt', 'sidebar': 'sidebars/studentSidebar.html'})

def display_gen_hallticket(request):
    user = Student.objects.get(username=request.user.username)
    hall_ticket = Hallticket.objects.filter(student__username=user.username)

    context = {'title': 'download hall-ticket', 'sidebar': 'sidebars/studentSidebar.html', 'hall_ticket': hall_ticket, 'user':user}
    return render(request,'generatehallTicket.html', context)


def download_hallticket(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica", 12)

    user = Student.objects.get(username=request.GET['studentID'])
    exam_id = int(request.GET['examId'])
    exam = Exam.objects.get(id=exam_id)

    # Drawing elements on the PDF
    p.drawString(50, 750, "Hall Ticket")
    p.drawString(50, 730, f"Username: {user.username}")
    p.drawString(50, 710, f"Exam Type: {exam.exam_type}")
    p.drawString(50, 690, f"Program Name: {exam.program_name}")
    p.drawString(50, 670, f"Roll Number: {user.roll_no}")
    p.drawString(50, 650, f"Name: {user.first_name} {user.middle_name} {user.last_name}")

    # Drawing additional elements like exam date, venue, etc.
    # Add more information as per your requirement

    # Drawing a rectangle to simulate a border
    p.rect(40, 640, 500, 140)

    # Saving and returning the PDF as a FileResponse
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"HT{user.username}{exam.exam_type}.pdf")


def display_notifications(request):
    user = Student.objects.get(username=request.user.username)
    announcements = Announcement.objects.filter(receiver=user.id)
    context = {'title': 'view notifications', 'sidebar': 'sidebars/studentSidebar.html','announcements':announcements}
    return render(request,'viewNotifications.html', context)