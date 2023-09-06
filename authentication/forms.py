from django import forms
from .models import StudentAdmission
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation

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

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=("New Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))

class MyPasswordResetFrom(PasswordResetForm):
    email = forms.EmailField(label=("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))
    