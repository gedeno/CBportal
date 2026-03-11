from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView


# Create your views here.
class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserChangeForm
    success_url = "/login/"
    def form_invalid(self, form):
        form.save()
        return super().form_invalid(form)
class MyLoginView(LoginView):
    template_name = "login.html"