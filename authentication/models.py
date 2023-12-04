from django.db import models
# from django.contrib.auth.models import AbstractUser
# from datetime import date

# Create your models here.

# class CustomUser(AbstractUser):
#     is_registered = models.BooleanField(default=False)
#     is_paid = models.BooleanField(default=False)

class StudentAdmission(models.Model):
    enumber = models.IntegerField()
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.IntegerField()
    adhaarnumber = models.IntegerField()
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    address = models.TextField()
    highmarks = models.FloatField()
    intermarks = models.FloatField()
    graduationmarks = models.FloatField()
    profileimage = models.ImageField(upload_to='Profiles', blank=True)
    adhaarpdf = models.FileField(upload_to='PDF', blank=True)
    highschoolpdf = models.FileField(upload_to='PDF', blank=True)
    interpdf = models.FileField(upload_to='PDF', blank=True)
    graduationpdf = models.FileField(upload_to='PDF', blank=True)


    # def __str__(self):
    #     return str(self.enumber)
    
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=100)
    courseduration=models.CharField(max_length=100)
    coursedescription=models.TextField()
    totalfee=models.IntegerField(default=0)
    
    def __str__(self):
        return self.coursename

# class Fee(models.Model):
    # feetype=models.CharField(max_length=100)
    # totalfee=models.IntegerField()
    # feedescription=models.TextField()
      
class Profile(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos')
    age = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=20)

class FeePayment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default=None)
    order_id = models.CharField(max_length=100, blank=True)
    razor_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    