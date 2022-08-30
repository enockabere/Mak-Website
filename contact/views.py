from django.shortcuts import render
from base.models import CallToActionPanel
from .forms import FeedbackForm
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory

# Create your views here.


def contact_view(request):
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        form2 = FeedbackForm(request.POST)
        if form2.is_valid():
            form2.save()

    
    form = SubscriptionForm()
    form2 = FeedbackForm()
    cta = CallToActionPanel.objects.filter(status=1)[:1]

    context = {
        'form': form,
        'form2': form2,
        'cta': cta,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'contact.html', context)


def feedback_view(request):
    return render(request, 'feedback.html')