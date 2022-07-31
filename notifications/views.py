from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . forms import NofificationForm
from . models import Notifications

# Create your views here.
def form(request):
    if request.method == 'POST':
        form = NofificationForm(request.POST)
        if form.is_valid():
            obj=Notifications()
            obj.machine = form.cleaned_data['machine']
            obj.category = form.cleaned_data['category']
            obj.description = form.cleaned_data['description']
            obj.save()
        return redirect('home')

    else:
        pass



