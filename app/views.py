from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def about(requests):
    return render(requests,'about.html')

def contact(requests):
    return render(requests,'contact.html')

def courses(requests):
    data=blog.objects.all()
    return render(requests,'courses.html',{'data':data})
def tcourses(requests,trainer):
    data=blog.objects.filter(name__name__icontains=trainer)
    return render(requests,'courses.html',{'data':data})

def detail(requests,id):
    data=blog.objects.get(id=id)
    return render(requests,'detail.html',{'data':data})

def events(requests):
    return render(requests,'events.html')

def index(requests):
    return render(requests,'index.html')

def pricings(requests):
    data=pricing.objects.all()


    return render(requests,'pricing.html',{'data':data})

def trainers(requests):
    data=trainer.objects.all()
    return render(requests,'trainers.html',{'data':data})