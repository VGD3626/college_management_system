from django.contrib.auth import logout
from django.shortcuts import render, redirect
from acPanel.models import Accountant, Payment
from facultyPanel.models import Announcement
from studentPanel.models import Student


def displayAcDashboard(request):
    uname = request.user.username
    user = Accountant.objects.get(username=uname)
    print(user.first_name)
    return render(request, 'acDashboard.html',
                  {'title': 'accountantDashboard', 'sidebar': 'sidebars/accountantSidebar.html', 'user': user})

def verifyFees(request):
    user = Accountant.objects.get(username=request.user.username)
    transactions = Payment.objects.all()
    if request.method == 'POST':
        t = Payment.objects.get(transID=request.POST['transID'])
        if(t.verification_status == False):
            t.verification_status = True
        t.save(force_update=True)
    return render(request, 'verifyFeeStatus.html',
                  {'title': 'fees verification', 'sidebar': 'sidebars/accountantSidebar.html', 'transactions': transactions})

def logout_user(request):
    logout(request)
    return redirect('login')