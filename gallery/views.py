from django.shortcuts import render
from.models import PhotoGallery, VideoGallery
from base.forms import SubscriptionForm

# Create your views here.

def gallery_view(request):
    photo = PhotoGallery.objects.filter(status=1).all()
    video = VideoGallery.objects.filter(status=1).all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'photos': photo,
        'videos': video,
        'form': form,
    }
    return render(request, 'gallery.html', context)