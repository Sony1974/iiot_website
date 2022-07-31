from django.http import HttpResponse
from django.shortcuts import render, redirect

from notifications.models import Notifications
from notifications.forms import NofificationForm




# def home(request):
#     return HttpResponse('Welcome to IIoT Startup Project')

def home(request):
    # notif = Notifications.objects.all()
    notif = Notifications.objects.order_by('-created')[:5]
    form = NofificationForm()

    electrical_count = Notifications.objects.filter(category='Electrical').count() 
    mechanical_count = Notifications.objects.filter(category='Mechanical').count()
    total_count = electrical_count + mechanical_count

    context = { 
        'notif' : notif,
        'notif_form' : form,
        'notif_electrical': electrical_count,
        'notif_mechanical': mechanical_count,
        'notif_total': total_count
    }
    return render(request,'home.html', context)

def notif_list(request):
    notif = Notifications.objects.order_by('-created')
    context = { 
        'notif' : notif,
    }
    return render(request,'notif_list.html',context)
    

def notif_form(request):
    form = NofificationForm()
    context = { 
        'notif_form' : form
    }
    return render(request,'notif_form.html',context)
    