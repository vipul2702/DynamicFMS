from django.contrib import admin
from authentication.models import StudentAdmission


# Register StudentAdimission model using decorators
@admin.register(StudentAdmission)
class StudentAdmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'enumber', 'fullname', 'gender', 'email', 'dob', 'phone', 'adhaarnumber', 'address', 'highmarks',
                    'intermarks', 'graduationmarks', 'profileimage', 'adhaarpdf', 'highschoolpdf', 'interpdf', 'graduationpdf']

# Register StudentAdimission model using admin.site.register
# admin.site.register(StudentAdmission, StudentAdmissionAdmin)