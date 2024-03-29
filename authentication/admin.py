from django.contrib import admin
from authentication.models import StudentAdmission
from authentication.models import Course
# from authentication.models import Fee
from authentication.models import Profile
from authentication.models import FeePayment


# Register StudentAdimission model using decorators
@admin.register(StudentAdmission)
class StudentAdmissionAdmin(admin.ModelAdmin):
    list_display = ['enumber', 'fullname', 'course', 'gender', 'email', 'dob', 'phone', 'adhaarnumber', 'address', 'highmarks',
                    'intermarks', 'graduationmarks', 'profileimage', 'adhaarpdf', 'highschoolpdf', 'interpdf', 'graduationpdf']

# Register StudentAdimission model using admin.site.register
# admin.site.register(StudentAdmission, StudentAdmissionAdmin)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [ 'coursename', 'courseduration', 'coursedescription', 'totalfee', ]

# @admin.register(Fee)
# class FeeAdmin(admin.ModelAdmin):
#     list_display = [ 'feetype', 'totalfee', 'feedescription', ]

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'amount', 'email', 'order_id', 'razor_payment_id', 'paid']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo', 'age', 'mobile_number', ]
    