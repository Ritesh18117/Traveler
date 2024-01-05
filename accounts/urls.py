from django.contrib import admin  
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path("",views.index,name="index"),
    path("about", views.about, name='about'),
    path("services", views.services, name='Services'),
    path("contact", views.contact, name='contact'),
    path("register", views.registerUser, name='register'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("addPlace", views.addPlace, name='addPlace'),
    path("demo", views.demo, name='demo'),
    path("edit/<str:id>",views.edit, name="edit"),
    path("viewPlace/<str:id>",views.viewPlace,name="viewPlace")
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
