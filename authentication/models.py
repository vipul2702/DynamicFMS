from django.db import models

# Create your models here.
class StudentAdmission(models.Model):
    enumber = models.IntegerField()
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.IntegerField()
    adhaarnumber = models.IntegerField()
    address = models.TextField()
    highmarks = models.IntegerField()
    intermarks = models.IntegerField()
    graduationmarks = models.IntegerField()
    profileimage = models.ImageField(upload_to='Upload/Profiles', blank=True)
    adhaarpdf = models.FileField(upload_to='Upload/PDF', blank=True)
    highschoolpdf = models.FileField(upload_to='Upload/PDF', blank=True)
    interpdf = models.FileField(upload_to='Upload/PDF', blank=True)
    graduationpdf = models.FileField(upload_to='Upload/PDF', blank=True)

    def __str__(self):
        return str(self.enumber)