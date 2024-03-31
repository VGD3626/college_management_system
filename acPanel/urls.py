from django.contrib import admin
from django.urls import path
from acPanel import views

urlpatterns = [
    # path('login/', include('userAuth.urls')),
    path('accounts', views.displayAcDashboard, name='displayAcDashboard'),
    path('verifyFees', views.verifyFees, name='verifyFees'),
    path('admin/', admin.site.urls),
    path('logout', views.logout_user, name='logout')

]
