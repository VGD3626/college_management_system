from django.shortcuts import render
from CMS.models import Person
from django.contrib.auth.models import User


def x(request):
    # u = User.objects.create_user(username='n', password='<PASSWORD>')
    # p = Person(userId='433',user=u)
    # p.save()
    # print(p)
    return render(request, 'updateAttendance.html',{'title':'Add Marks','sidebar':'sidebars/facultySidebar.html'})