from django.urls import path
from .views import MyLoginView,RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',RegisterView.as_view(),name = "register"),
    path('login/',MyLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout")
    ,

]