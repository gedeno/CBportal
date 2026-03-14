from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Courses,assessment
from django.contrib.auth.models import User
from .forms import AssForm
# Create your views here.
class Teacher(generic.ListView):
    model = User
    template_name = 'main/teacher.html'
    queryset = User.objects.all()
    context_object_name = 'stud'
class Teachercourse(generic.ListView):
    template_name = "main/teachearcourse.html"
    context_object_name = 'courses'
    def get_queryset(self):
        return Courses.objects.filter(usernames=self.request.user)
class Teachercoursedetail(DetailView):
    model = Courses
    template_name = 'main/coursedetail.html'
    queryset = Courses.objects.all()
    def get_course(self):
        return get_object_or_404(Courses, pk=self.kwargs['pk']) 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assesment'] = assessment.objects.get(course=self.get_course())
        return context
class RegisterView(FormView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    success_url = "/login/"
    def form_valid(self,form):
        user = form.save()
        subjects = ['mathematics','physics','chemistry','english','python','logic']
        success_url = 'login'
        for subject in subjects:
            course = Courses.objects.create(
                course_name = subject,
                usernames =user)
            assessment.objects.create(
                course = course,
                usernames = user )
        return super().form_valid(form)
class MyLoginView(LoginView):
    template_name = "main/login.html"
    success_url = "/"
class HomeView(LoginRequiredMixin, generic.ListView):
    template_name = 'main/home.html'
    context_object_name = 'courses'
    def get_queryset(self):
        return Courses.objects.filter(usernames=self.request.user)
class CourseDetail(DetailView):
    model = Courses
    template_name = 'main/detail.html'
    queryset = Courses.objects.all()
    def get_course(self):
        return get_object_or_404(Courses, pk=self.kwargs['pk'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assesment'] = assessment.objects.get(course=self.get_course())
        return context
class Update(generic.UpdateView):
    model = assessment
    template_name = "main/update.html"
    queryset = assessment.objects.all()
    form_class = AssForm
    success_url = '/teach'
class MyLogoutView(LogoutView):
    template_name = "main/logout.html"




    
