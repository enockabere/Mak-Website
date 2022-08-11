from django.shortcuts import render
from base.models import CallToActionPanel

# Create your views here.


def contact_view(request):
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    context = {
        'cta': cta,
    }
    return render(request, 'contact.html', context)


def feedback_view(request):
    return render(request, 'feedback.html')