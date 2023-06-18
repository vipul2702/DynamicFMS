from django import forms
from .models import StudentAdmission
from .models import Profile
class StudentAdmissionForm(forms.ModelForm):
    class Meta:
        model = StudentAdmission
        fields =  ['enumber', 'fullname', 'course', 'gender', 'email', 'dob', 'phone', 'adhaarnumber', 'address', 'highmarks',
                    'intermarks', 'graduationmarks', 'profileimage', 'adhaarpdf', 'highschoolpdf', 'interpdf', 'graduationpdf']
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'age', 'mobile_number']  
    
    
    
    # enumber = forms.IntegerField()
    # full_name = forms.CharField()
    # gender = forms.CharField()
    # email = forms.EmailField()
    # dob = forms.DateField()
    # phone = forms.IntegerField()
    # adhaar_number = forms.IntegerField()
    # address = forms.CharField()
    # high_school_marks = forms.IntegerField()
    # inter_marks = forms.IntegerField()
    # graduation_marks = forms.IntegerField()
    # profile_image = forms.ImageField()
    # adhaarpdf = forms.FileField()
    # highschoolpdf = forms.FileField()
    # interpdf = forms.FileField()
    # graduationpdf = forms.FileField()
