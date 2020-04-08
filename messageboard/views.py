from django.shortcuts import HttpResponse

def home(request):
  return HttpResponse('<p>Welcome to the message board!</p>')