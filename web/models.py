from django.db import models
import datetime
# Create your models here.
class login_info(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type=models.CharField(max_length=50)

class admin_info(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70)
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    pic=models.FileField(upload_to="images/")
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    date=datetime.datetime.now().date()

class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    qualification=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    resume=models.FileField(upload_to="resume/")
    date=datetime.datetime.now().date()
class company(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
  
    address=models.CharField(max_length=150)
    date=datetime.datetime.now().date()
class feedback(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=40)
    message=models.CharField(max_length=170)
