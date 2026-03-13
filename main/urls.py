from django.urls import path
from .views import MyLoginView,RegisterView,HomeView, CourseDetail, Update, Teacher,Teachercourse,Teachercoursedetail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(),name = "register"),
    path('login/',MyLoginView.as_view(),name="login"),
    path('',HomeView.as_view(),name="home"),
    path('logout/',LogoutView.as_view(next_page = "login"), name = "logout"),
    path('detail/<int:pk>/', CourseDetail.as_view(), name='detail'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('teach/', Teacher.as_view(), name='teach'),
    path('teachcourse/<int:pk>/',Teachercourse.as_view(),name='teachcourse'),
    path('coursedetail/<int:pk>/',Teachercoursedetail.as_view(), name='coursedetail'),
    path('stud/<int:pk>/', HomeView.as_view(), name='stud' )
]