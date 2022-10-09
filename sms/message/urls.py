from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.signIn , name = 'signIn'),
    path('message',views.message, name = 'message'),
    path('gmessage',views.gmessage, name = 'gmessage'),
    path('fromexcel',views.fromExcel , name = 'fromExcel'),
    path('contact',views.contact , name = 'contact'),
    path('gcontact',views.gcontact , name = 'gcontact'),
    path('login',views.signIn , name = 'login'),
    path('reports',views.reports , name = 'reports'),



]

