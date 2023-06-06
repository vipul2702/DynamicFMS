from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', RedirectView.as_view(url = '/admin/logout/')),
    # path('', views.home, name="home"),
    # path('signup', views.signup, name="signup"),
    # path('admissionform', views.admissionform, name="admissionform"),
    # path('payment', views.payment, name="payment"),
    # path('profile', views.profile, name="profile"),
    # path('helo', views.helo, name="helo"),
    # path('setting', views.setting, name="setting"),
    # path('feereceipt', views.feereceipt, name="feereceipt"),
    # path('signin', views.signin, name="signin"),
    # path('signout', views.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
    # path('dashboard', views.dashboard, name="dashboard"),
    # path('forgetpassword', views.forgetpassword, name="forgetpassword"),
]