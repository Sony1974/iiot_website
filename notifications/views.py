from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from . forms import NofificationForm
from . models import Notifications

# Create your views here.


def notif_form(request):
    if request.method == 'POST':
        form = NofificationForm(request.POST)
        if form.is_valid():
            obj=Notifications()
            obj.machine = form.cleaned_data['machine']
            obj.category = form.cleaned_data['category']
            obj.description = form.cleaned_data['description']

            obj.save()

        return redirect("/")
        #return render(request, 'home.html')

    else:
        pass
        #form = NofificationForm()
