from django.shortcuts import render,redirect
from .models import *
import requests
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        html_version = 'emailtemp.html'
        context = {
            'title':"Knock! Knock! Great Opportunity",
            'name' : name
             
        }
        html_message = render_to_string(html_version,context)
        subject = "Thank You for contacting!!"
        to_email = email
        text = "Hey! " + name +" " + " Thank You for Contacting. " +  " Will get back to you soon!! :) "
        message = EmailMessage(subject, text,'shivlanipalak@gmail.com', [to_email])
        message.send()
        obj = contact.objects.create(name=name,email=email,subject=subject,message=message)
    return render(request,'index.html')

def clone(request):
    return render(request,'projects/clone.html')

def crypto(request):
    return render(request,'projects/Crypto.html')

def karwaan(request):
    return render(request,'projects/karwaan.html')

def tracker(request):
    return render(request,'projects/tracker.html')

def weather(request):
    return render(request,'projects/weather.html')

def farmer(request):
    return render(request,'projects/farmer.html')