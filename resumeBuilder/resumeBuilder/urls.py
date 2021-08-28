from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views as user_views
from resume import views as resume_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('',resume_views.home, name='home'),
    path('resume/', include('resume.urls')),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
