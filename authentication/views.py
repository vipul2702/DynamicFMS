# from base64 import urlsafe_b64decode
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
# from authentication.serializers import EnrolledStudentSerializer
# from rest_framework.views import APIView
# from rest_framework import status
from authentication.models import StudentAdmission
from .forms import StudentAdmissionForm
from .forms import ProfileForm
from .forms import FeePaymentForm
from .forms import FeePayment
import razorpay
from django.views.decorators.csrf import csrf_exempt


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
    # admission_form = 'authentication/admissionform.html'
    form = StudentAdmission.objects.all()
    for i in form:
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
    return render(request, "authentication/admissionform.html", {'form':fm, 'email':email, 'fname':fname})
    # return render(request, "authentication/admissionform.html", {'form':fm})

# class EnrolledStudentView(APIView):
#     def post(self, request, format=None):
#         serializer = EnrolledStudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Admission Form Upload Successfully', 'status': 'success',
#                              'candidate': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     def get(self, request, format=None):
#         candidates = EnrolledStudent.objects.all()
#         serializer = EnrolledStudentSerializer(candidates, many=True)
#         return Response({'status':'success', 'candidates':serializer.data}, status=status.Http_200_OK)


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        
        # username = request.POST.get('username')
        # username = request.POST.get('username')
        # fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        # email = request.POST.get('email')
        # pass1 = request.POST.get('pass1')
        # pass2 = request.POST.get('pass2')

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email'] 
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

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

        messages.success(request, "Your Account has been successfully created. Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email

        subject = "Welcome to Our - Fee Management System Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to FMS \n Thank you for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You\n Vipul Sharma"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ FMS - Login!!"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')

    return render(request, "authentication/signup.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
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
            
            return render(request, "authentication/dashboard.html", {'fname': fname, 'lname':lname})
        else:
            # verifyLogin = myuser.is_active
            # if not verifyLogin: 
            #     # user = User.objects.get(myuser=username)
            #     return render(request, "authentication/student_wait_approval.html")
            messages.success(request, "Invalid User !!")
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
    if request.method == "POST":
        name = request.POST.get("name")
        # amount = request.POST.get("amount")
        amount = int(request.POST.get("amount"))*100
        # create razorpay client
        client = razorpay.Client(auth = ("rzp_test_tD2iMN2MtNXkvn", "ZPomIdSDuPB5xg0e2GhKMUSk"))
        # create order
        # response_payment = client.order.create(dict(amount=amount,currency='INR'))
        response_payment = client.order.create({'amount':amount,'currency':'INR', 'payment_capture':'1'})
        print(response_payment)
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            feepay = FeePayment(name=name,amount=amount,order_id=order_id)
            feepay.save()
            response_payment['name'] = name
            
            form = FeePaymentForm(request.POST or None)
            return render(request, "authentication/payment.html", {"form":form, "payment":response_payment})

    form = FeePaymentForm()
    return render(request, "authentication/payment.html", {"form":form})

@csrf_exempt
def payment_status(request):
    response = request.POST
    # print(response)
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
        }
    # client instance
    client = razorpay.Client(auth = ("rzp_test_tD2iMN2MtNXkvn", "ZPomIdSDuPB5xg0e2GhKMUSk"))
    
    try: 
        status = client.utility.verify_payment_signature(params_dict)
        feepay = FeePayment.objects.get(order_id=response['razorpay_order_id'])
        feepay.razorpay_payment_id = response['razorpay_payment_id']
        feepay.paid = True
        feepay.save()
        return render(request, 'authentication/payment_status.html', {'status':True})
    except:
        return render(request, 'authentication/payment_status.html', {'status':False})
    
    # return render(request, 'authentication/payment_status.html')

def profile(request):
    email = request.user.email
    data = StudentAdmission.objects.all()
    # print(data)
    for i in data:
        if(i.email == request.user.email):
            return render(request, "authentication/profile.html",{'data':data})
    return render(request, "authentication/profile.html")

def feereceipt(request):
    return render(request, "authentication/feereceipt.html")

def helo(request):
    return render(request, "authentication/helo.html")

def setting(request):
    return render(request, "authentication/passwordchange.html")


def student_wait(request):
    return render(request, 'authentication/student_wait_approval.html')

def about(request):
    return render(request, 'authentication/about.html')

def contact(request):
    return render(request, 'authentication/contact.html')

# views.py
from django.http import HttpResponseForbidden

def csrf_failure(request, reason=""):
    return HttpResponseForbidden('CSRF verification failed. Reason: {}'.format(reason))
