from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Contact

from django.contrib import messages
# Create your views here.
def contact_tubers(request):

    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        detailed_message = request.POST['detailed_message']

     
                  
        contact = Contact(
        fullname=fullname, phone_number=phone_number, 
        email=email,  company_name=company_name,
        subject=subject, detailed_message=detailed_message)

        contact.save()

        messages.success(request, 'Thanks for your query , will reach out soon')
        return redirect('contact')

    return redirect('contact')