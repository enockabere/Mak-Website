from multiprocessing import context
from django.shortcuts import render
from base.models import CallToActionPanel

# Create your views here.

def service_view(request):
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    context = {
        'cta': cta,
    }
    return render(request, 'service.html', context)
