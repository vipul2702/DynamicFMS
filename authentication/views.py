from base64 import urlsafe_b64decode
from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from Registration import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib.auth.decorators import login_required
# from rest_framework.response import Response
from authentication.models import StudentAdmission
# from authentication.serializers import StudentAdmissionSerializer
# from rest_framework.views import APIView
# from rest_framework import status
from .forms import StudentAdmissionForm
from .forms import ProfileForm

def create_profile(request):
    if request.method == 'POST':
        
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('profile_created')  # Redirect to a success page
    else:
        form = ProfileForm()
    return render(request, 'authentication/usersdata.html', {'form': form})

@login_required(login_url='/signin')
def showformdata(request):
    email = request.user.email
    fname = request.user.first_name +" "+ request.user.last_name
    admission_form = 'authentication/admissionform.html'
    data = StudentAdmission.objects.all()
    for i in data:
        if(i.email == request.user.email):
            admission_form = 'authentication/student_wait_approval.html'
            break
    if request.method == 'POST':
        
        
        fm = StudentAdmissionForm(request.POST, request.FILES)
        if fm.is_valid() :
            fm.save()
            return render(request,"authentication/student_wait_approval.html")
    else:
        fm = StudentAdmissionForm()
    return render(request, admission_form, {'form':fm, 'email':email, 'fname':fname})

# class StudentAdmissionView(APIView):
#     def post(self, request, format=None):
#         serializer = StudentAdmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Admission Form Upload Successfully', 'status': 'success',
#                              'candidate': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     def get(self, request, format=None):
#         candidates = StudentAdmission.objects.all()
#         serializer = StudentAdmissionSerializer(candidates, many=True)
#         return Response({'status':'success', 'candidates':serializer.data}, status=status.Http_200_OK)


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        
        # username = request.POST.get('username')
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # username = request.POST['username']
        # # fname = request.POST['fname']
        # lname = request.POST['lname']
        # email = request.POST['email'] 
        # pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
                messages.warning(request, "Username already exist! please try some other username")
                return redirect('home')

        if User.objects.filter(email=email):
            messages.warning(request, "Email already registered")  
            return redirect('home')

        if len(username)>20:
            messages.warning(request, "Username must be under 20 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.warning(request, "Password didn't match")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, "Username must be Alpha-Numeric!")    
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        # Welcome Email

        # subject = "Welcome to Our - Dynamic Fee Management System Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to DynamicFMS!! \n Thank you for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You\n Vipul Sharma"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # # Email Address Confirmation Email

        # curren_site = get_current_site(request)
        # email_subject = "Confirm your email @ DynamicFMS - Login!!"
        # message2 = render_to_string('email_confirmation.html',{
        #     'name': myuser.first_name,
        #     # 'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('signin')

    return render(request, "authentication/signup.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_b64decode)
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            return render(request, "authentication/index.html", {'fname': fname, 'lname':lname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

# @login_required(login_url='/signin')
def dashboard(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            global email 
            email = user.email
            # print(email)
            # print("i love you jaan")
            
            return render(request, "authentication/dashboard.html", {'fname': fname, 'lname':lname})
        else:
            # verifyLogin = myuser.is_active
            # if not verifyLogin: 
            #     # user = User.objects.get(myuser=username)
            #     return render(request, "authentication/student_wait_approval.html")
            messages.success(request, "Your account not verified yet! Wait for some time")
            return redirect('home')

    return render(request, "authentication/dashboard.html")

def forgetpassword(request):
    return render(request, 'forgetpassword.html')


def admissionform(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            global email 
            email = user.email
            print(email)
            print("i love you jaan")
            return render(request, "authentication/admissionform.html", {'fname': fname, 'lname':lname})
        else:
            messages.error(request, "Invalid User!")
            return redirect('home')
    return render(request, "authentication/admissionform.html")

def payment(request):
    return render(request, "authentication/payment.html")

def profile(request):
    return render(request, "authentication/profile.html")

def feereceipt(request):
    return render(request, "authentication/feereceipt.html")

def helo(request):
    return render(request, "authentication/helo.html")

def setting(request):
    return render(request, "authentication/setting.html")


def student_wait(request):
    return render(request, 'authentication/student_wait_approval.html')

def about(request):
    return render(request, 'authentication/about.html')

def contact(request):
    return render(request, 'authentication/contact.html')