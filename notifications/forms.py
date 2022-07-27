from django import forms

from . models import Notifications

class NofificationForm(forms.ModelForm):
    class Meta:
        model   = Notifications
        fields  = ['machine','category','description']
        labels  ={ 
            'category' : 'Elect/Mech/Util'
        }
