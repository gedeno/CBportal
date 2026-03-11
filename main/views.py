from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView 

# Create your views here.
class MyLoginview(LoginView):
    template_name = "main/login.html"
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "main/dashboard.html"
    login_url = "/login/"
class MyLogoutView(LogoutView):
    next_page = '/login/'