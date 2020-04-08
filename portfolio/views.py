from django.shortcuts import render
from portfolio.models import User
from django.shortcuts import HttpResponse

def home(request):
  return HttpResponse('<p>Portfolio Home</p>')

def contact(request):
    return HttpResponse('<p>Contact Me<p>')

def greet_by_name(request, name):
    return HttpResponse('<p>What is your name?<p>' + name)