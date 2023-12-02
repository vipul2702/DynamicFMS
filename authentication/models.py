from django.db import models
from datetime import date

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    coursename=models.CharField(max_length=100)
    courseduration=models.CharField(max_length=100)
    coursedescription=models.TextField()
    
    def __str__(self):
        return self.coursename

class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateField(default=date(2023, 10, 31))
    feetype = models.CharField(max_length=100)
    feedescription = models.TextField()

    def __str__(self):
        return f"Rs.{self.amount}"
        # return f"{self.course.coursename} - ${self.amount} ({self.payment_date})"


class EnrolledStudent(models.Model):
    enumber = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.IntegerField()
    adhaarnumber = models.IntegerField()
    fname = models.CharField(max_length=100, default=None)
    mname = models.CharField(max_length=100, default=None)
    address = models.TextField()
    highmarks = models.FloatField()
    intermarks = models.FloatField()
    graduationmarks = models.FloatField()
    profileimage = models.ImageField(upload_to='Profiles', blank=True)
    adhaarpdf = models.FileField(upload_to='PDF', blank=True)
    highschoolpdf = models.FileField(upload_to='PDF', blank=True)
    interpdf = models.FileField(upload_to='PDF', blank=True)
    graduationpdf = models.FileField(upload_to='PDF', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return f"{self.fullname} - {self.course.coursename} - ${self.fee.amount}"

    # def __str__(self):
    #     return str(self.enumber)
      
class Profile(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos')
    age = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=20)