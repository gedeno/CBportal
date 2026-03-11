from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.
class RegisterView(FormView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    success_url = "/login/"
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
class MyLoginView(LoginView):
    template_name = "main/login.html"
    def get_success_url(self):
        return "home"
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'main/home.html'
class MyLogoutView(LogoutView):
    next_page = "/login/"