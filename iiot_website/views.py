from django.http import HttpResponse
from django.shortcuts import render

from notifications.models import Notifications
from notifications.forms import NofificationForm


# def home(request):
#     return HttpResponse('Welcome to IIoT Startup Project')

def home(request):
    notif = Notifications.objects.all()
    form = NofificationForm()

    context = { 
        'notif' : notif,
        'notif_form' : form
    }
    return render(request,'home.html', context)