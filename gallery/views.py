from django.shortcuts import render
from.models import PhotoGallery, VideoGallery

# Create your views here.

def gallery_view(request):
    photo = PhotoGallery.objects.filter(status=1).all()
    video = VideoGallery.objects.filter(status=1).all()
    context = {
        'photos': photo,
        'videos': video
    }
    return render(request, 'gallery.html', context)