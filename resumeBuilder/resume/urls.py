from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from resume import views

urlpatterns = [ 
    path('testing/', views.testing, name="testing"), 
    path('details/', views.forms, name="forms"),  
] 