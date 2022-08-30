from django.shortcuts import render
from.models import PhotoGallery, VideoGallery
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory

# Create your views here.

def gallery_view(request):
    photo = PhotoGallery.objects.filter(status=1).all()
    video = VideoGallery.objects.filter(status=1).all()
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'photos': photo,
        'videos': video,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'gallery.html', context)