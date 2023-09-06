from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
# from . import views
from authentication import views
from authentication.forms import MyPasswordChangeForm, MyPasswordResetFrom, MySetPasswordForm
from django.contrib.auth import views as auth_views
# from .views import create_profile

urlpatterns = [
    path('logout/', RedirectView.as_view(url = '/admin/logout/')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('create-profile/', create_profile, name='create_profile'),
    # path('StudentAdmission/', views.StudentAdmissionView.as_view(), name="StudentAdmission"),
    # path('list/', views.StudentAdmissionView.as_view(), name="list"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('admissionform', views.showformdata, name="admissionform"),
    path('payment', views.payment, name="payment"),
    path('profile', views.profile, name="profile"),
    path('registration', views.create_profile, name="showformdata"),   
    path('student_wait', views.student_wait, name=""),
    path('setting', views.setting, name="setting"),
    path('feereceipt', views.feereceipt, name="feereceipt"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('passwordchange', auth_views.PasswordChangeView.as_view(template_name='authentication/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone',auth_views.PasswordChangeView.as_view(template_name='authentication/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html', form_class=MyPasswordResetFrom), name="password_reset"),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name="password_reset_done"),
    path('password-reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html',form_class=MySetPasswordForm), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name="password_reset_complete"),
    
]

# admin.site.index_title="Fee Management System"
# admin.site.site_header = "Fee Management System Admin"
# admin.site.site_title = "Site Title The FMS"
