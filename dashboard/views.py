from django.shortcuts import render

def dashboard(request):
    return render(request, 'StudentDashboard/paymentReceipt.html')
# Create your views here.
