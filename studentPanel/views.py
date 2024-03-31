import io
from time import strftime

from django.contrib.auth import logout
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from acPanel.models import Payment
from facultyPanel.models import *
from .models import Student
import reportlab


def display_studentdashboard(request):
    user = Student.objects.get(username=request.user.username)
    program = user.program
    courses = Subject.objects.filter(program__program_name=program.program_name)
    print(user.first_name)
    context = {'title': 'home', 'sidebar': 'sidebars/studentSidebar.html', 'user': user, 'courses': courses}
    return render(request, 'studentDashboard.html', context)


def display_attendance(request):
    user = Student.objects.get(username=request.user.username)
    attendance_records = AttendanceRecord.objects.filter(student__username=user.username)

    for record in attendance_records:
        record.upload_date = strftime('%B-%Y')

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}
    context = {'title': 'home', 'sidebar': 'sidebars/studentSidebar.html', 'user': user,
               'attendance_records': attendance_records, 'months': months}
    return render(request, 'viewAttendance.html', context)


def display_result(request):
    user = Student.objects.get(username=request.user)
    exams = Exam.objects.filter(program_name=user.program_name)
    marks = Mark.objects.filter(student=user)
    context = {'title': 'results', 'sidebar': 'sidebars/studentSidebar.html', 'exams': exams, 'marks': marks, 'user': user}
    return render(request, 'viewResults.html', context)


def display_syllabus(request):
    user = Student.objects.get(username=request.user.username)
    with open(f'static/{user.program_name}syllabus.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=syllabus.pdf'
        return response


def display_gen_fee_receipt(request):
    user = Student.objects.get(username=request.user.username)
    transactions = Payment.objects.filter(student=user)
    context = {'title': 'generate fee receipt', 'sidebar': 'sidebars/studentSidebar.html', 'transactions': transactions,'user' : user}
    return render(request, 'generateFeeReceipt.html', context)


def download_fee_receipt(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica", 12)

    u = User.objects.get(username=request.POST['studentID'])
    user = Student.objects.get(username=u.username)
    payment = Payment.objects.get(transID=request.POST['transID'])

    # Drawing elements on the PDF
    p.drawString(50, 750, "--FEE RECEIPT--")
    p.drawString(50, 730, f"Username: {user.username}")
    p.drawString(50, 710, f"Transaction Id: {payment.transID}")
    p.drawString(50, 690, f"Program Name: {payment.amount}")
    p.drawString(50, 670, f"Roll Number: {user.roll_no}")
    p.drawString(50, 650, f"Name: {user.first_name} {user.middle_name} {user.last_name}")
    p.drawString(50, 610, f"Amount: {payment.amount} INR")
    p.drawString(50, 590, f"Transaction type: {payment.payment_type}")
    p.drawString(50, 570, f"Bank: {payment.bank}")

    p.rect(40, 560, 500, 200)

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"FR.pdf")


def display_gen_hallticket(request):
    user = Student.objects.get(username=request.user.username)
    hall_ticket = Hallticket.objects.filter(student__username=user.username)

    context = {'title': 'download hall-ticket', 'sidebar': 'sidebars/studentSidebar.html', 'hall_ticket': hall_ticket,
               'user': user}
    return render(request, 'generatehallTicket.html', context)


def download_hallticket(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica", 12)

    user = Student.objects.get(username=request.GET['studentID'])
    exam_id = int(request.GET['examId'])
    exam = Exam.objects.get(id=exam_id)

    p.drawString(50, 750, "Hall Ticket")
    p.drawString(50, 730, f"Username: {user.username}")
    p.drawString(50, 710, f"Exam Type: {exam.exam_type}")
    p.drawString(50, 690, f"Program Name: {exam.program_name}")
    p.drawString(50, 670, f"Roll Number: {user.roll_no}")
    p.drawString(50, 650, f"Name: {user.first_name} {user.middle_name} {user.last_name}")

    p.rect(40, 640, 500, 140)

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"HT{user.username}{exam.exam_type}.pdf")


def display_notifications(request):
    user = request.user
    announcements = Announcement.objects.filter(receiver=user.id)
    if(user.username[0] == 'S'):
        s='sidebars/studentSidebar.html'
    elif(user.username[0:2] == 'AC'):
        s='sidebars/accountantSidebar.html'
    elif(user.username[0] == 'F'):
        s='sidebars/facultySidebar.html'
    else:
        s='sidebars/dirSidebar.html'
    context = {'title': 'view notifications', 'sidebar': s, 'announcements': announcements}
    return render(request, 'viewNotifications.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')