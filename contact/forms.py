from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailInput, TextInput, Select
from .models import  Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['type', 'name','email', 'subject', 'message' ]

        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'subject': _('Subject'),
            'message': _('Message'),

        }

        widgets = {
            

            'name': TextInput(attrs={
                'placeholder': 'e.g  John Doe*'
                }),

            'email': EmailInput(attrs={ 
                'placeholder': 'e.g. info@example.com*'
                }),

            'subject': TextInput(attrs={
                'placeholder': 'e.g Inqury*'
            }),

            'message': Textarea(attrs={
                'placeholder': 'message*'
            }),

        }
    
