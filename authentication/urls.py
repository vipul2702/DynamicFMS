from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
# from . import views
from authentication import views
# from .views import create_profile

urlpatterns = [
    path('logout/', RedirectView.as_view(url = '/admin/logout/')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('create-profile/', create_profile, name='create_profile'),
    path('StudentAdmission/', views.StudentAdmissionView.as_view(), name="StudentAdmission"),
    path('list/', views.StudentAdmissionView.as_view(), name="list"),
    path('signup', views.signup, name="signup"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('admissionform', views.admissionform, name="admissionform"),
    path('payment', views.payment, name="payment"),
    path('profile', views.profile, name="profile"),
    # path('registration', views.create_profile, name="showformdata"),
    path('registration', views.showformdata, name="showformdata"),
    path('student_wait', views.student_wait, name=""),
    path('setting', views.setting, name="setting"),
    path('feereceipt', views.feereceipt, name="feereceipt"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('forgetpassword', views.forgetpassword, name="forgetpassword"),
]

# admin.site.index_title="Fee Management System"
# admin.site.site_header = "Fee Management System Admin"
# admin.site.site_title = "Site Title The FMS"
