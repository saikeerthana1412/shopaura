from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render()) 

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render()) 

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template=loader.get_template('register.html')
    return HttpResponse(template.render())

