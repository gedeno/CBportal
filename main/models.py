from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    usernames = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name
class assessment(models.Model):
    quiz1= models.IntegerField(default=0)
    quiz2 =models.IntegerField(default=0)
    assignment1 = models.IntegerField(default=0)
    assignment2 = models.IntegerField(default=0)
    mid_exam = models.IntegerField(default=0)
    final_exam = models.IntegerField(default=0)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    usernames = models.ForeignKey(User,on_delete=models.CASCADE)
