from django.shortcuts import render
from base.models import CallToActionPanel
from .forms import FeedbackForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()


    form = FeedbackForm()
    cta = CallToActionPanel.objects.filter(status=1)[:1]

    context = {
        'form': form,
        'cta': cta,
    }
    return render(request, 'contact.html', context)


def feedback_view(request):
    return render(request, 'feedback.html')