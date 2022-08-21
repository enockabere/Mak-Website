from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, EmailInput
from .models import  Subscription

class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['email' ]

        widgets = {
            

            'email': EmailInput(attrs={ 
                'placeholder': 'e.g. subscribe@example.com*'
                }),

        }
    
