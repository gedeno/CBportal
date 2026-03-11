from django.urls import path
from .views import MyLoginView,RegisterView,HomeView ,MyLogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(),name = "register"),
    path('login/',MyLoginView.as_view(),name="login"),
    path('',HomeView.as_view(),name="home"),
    path('logout/',LogoutView.as_view(next_page = "login"), name = "logout"),

]