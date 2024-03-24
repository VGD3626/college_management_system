from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userAuth.urls'), name='userAuth'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





