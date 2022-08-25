import imp
from django.shortcuts import render
from .models import Project
from base.models import CallToActionPanel, Subscription
from base.forms import SubscriptionForm

# Create your views here.

def projects_view(request):
    projects = Project.objects.filter(status=1).all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'projects': projects,
        'form': form,
    }
    return render(request, 'projects.html', context)