from django.urls import path
from . views import MyLoginview , DashboardView , MyLogoutView

urlpatterns = [
    path("",MyLoginview.as_view(),name='login'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('logout/',MyLogoutView.as_view(),name='logout'),

]