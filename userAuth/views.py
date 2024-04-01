from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

def user_authantication(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if username[0] == 'S':
                login(request, user)
                return redirect('display_studentdashboard')
            elif username[0:2] == 'AC':
                login(request, user)
                return redirect('displayAcDashboard')
            elif(username[0] == 'F'):
                login(request, user)
                return redirect('facultydashboard')
            elif(username[0] == 'M'):
                login(request, user)
                return redirect('directordashboard')
    return render(request, 'login.html')
