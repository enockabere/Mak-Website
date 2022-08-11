from django.shortcuts import render
from .models import Project
from base.models import CallToActionPanel

# Create your views here.

def projects_view(request):
    projects = Project.objects.filter(status=1).all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    context = {
        'cta': cta,
        'projects': projects,
    }
    return render(request, 'projects.html', context)