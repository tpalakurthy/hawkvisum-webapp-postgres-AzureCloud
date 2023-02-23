from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError, EmailMessage

from .forms import ContactForm, CareersForm
from .models import career_content_dynamic, blog_content_dynamic, team_dynamic

from django.http import StreamingHttpResponse
import mimetypes

import os

# Home Page #
def homepage(request):
    return render(request, 'homepage.html');

# About Page #
def aboutpage(request):
    teams = team_dynamic.objects.all()
    return render(request, 'about_us.html', {'teams':teams});

# Services Page #
def servicespage(request):
    return render(request, 'services.html');

# Product Page #
def productspage(request):
    return render(request, 'products.html');

# Contact Page #
def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Subject = form.cleaned_data['customer_subject']
            body = {
                'Name':form.cleaned_data['customer_name'],
                'Email':form.cleaned_data['customer_email'],
                'Message':form.cleaned_data['customer_message']
            }
            message = "\n".join(body.values())

            try:
                send_mail(Subject, message, 'info@hawkvisum.com', ['careershawkvisum@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = ContactForm()
    return render(request, 'contact.html', {'form':form});

# Why Us #
def whypage(request):
    return render(request, 'why_us.html');

# Careers #
def careerpage(request):
    
    careers = career_content_dynamic.objects.all()
    return render(request, 'careers.html', {'careers': careers});    

def career_detail(request, slug):
    career = career_content_dynamic.objects.get(slug=slug)
    return render(request, 'career-detail.html', {'career': career})

# Blog Page #
def blogpage(request):
    blogs = blog_content_dynamic.objects.all()
    return render(request, 'blog.html', {'blogs': blogs});

def blog_detail(request, slug):
    blog = blog_content_dynamic.objects.get(slug=slug)
    return render(request, 'blog-detail.html', {'blog': blog})

# Pilot Product Page #
def pilotproductpage(request):
    return render(request, 'pilottraining_prod.html');

# Cabin Crew Product Page #
def cabincrewproductpage(request):
    return render(request, 'cabincrewtraining_prod.html');

# Engine Inspection Product Page #
def engineinspectionproductpage(request):
    return render(request, 'engineinspectiontraining_prod.html');

# Catalogue Download Page #
def cataloguepage(request):
    if request.method == "POST":
        Name = request.POST['input-section-name']
        Designation = request.POST['input-section-designation']
        Email = request.POST['input-section-email']
        Number = request.POST['input-section-number']
        Institution = request.POST['input-section-institution']
        Location = request.POST['input-section-location']
        Simulator = request.POST['input-section-simulator']
        Inputs = request.POST['input-section-inputs']

    return render(request, 'catalogue.html');
