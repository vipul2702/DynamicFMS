from django import forms
class StudentAdmission(forms.Form):
    enumber = forms.IntegerField()
    full_name = forms.CharField()
    gender = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    phone = forms.IntegerField()
    adhaar_number = forms.IntegerField()
    address = forms.CharField()
    high_school_marks = forms.IntegerField()
    inter_marks = forms.IntegerField()
    graduation_marks = forms.IntegerField()
    profile_image = forms.ImageField()
    adhaarpdf = forms.FileField()
    highschoolpdf = forms.FileField()
    interpdf = forms.FileField()
    graduationpdf = forms.FileField()