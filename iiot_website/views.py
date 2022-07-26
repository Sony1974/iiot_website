from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse('Welcome to IIoT Startup Project')

def home(request):
    return render(request,'home.html')