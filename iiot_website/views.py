from django.http import HttpResponse
from django.shortcuts import render
from notifications.models import Notifications


# def home(request):
#     return HttpResponse('Welcome to IIoT Startup Project')

def home(request):
    notif = Notifications.objects.all()

    context = { 
        'notif' : notif
    }
    return render(request,'home.html', context)