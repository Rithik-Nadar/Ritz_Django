from django.shortcuts import render, redirect
from store.models.enquiry import Enquiry
from django.views import View
# Create your views here.


def enquiry(request):
    if request.method == 'POST':
        custname = request.POST.get('custname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        en = Enquiry(custname=custname, email=email,
                     contact=contact, message=message)
        en.save()
        return redirect('/')
    else:
        return render(request, 'contactus.html')
