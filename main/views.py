from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import generic
from .models import Courses,assessment
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
    success_url = "/"
class HomeView(LoginRequiredMixin,generic.DetailView):
    template_name = 'main/home.html'
    def get(self,request,*args,**kwargs):
        subjects = ['mathematics','physics','chemistry','english','python','logic']
        for subject in subjects:
            course = Courses.objects.create(
                course_name = subject,
                usernames =self.request.user)
            assessment.objects.create(
                course = course,
                usernames = self.request.user
            )
            return super().get(request,*args,**kwargs)
        
class MyLogoutView(LogoutView):
    template_name = "main/logout.html"
    


    
