from django.contrib import admin
from gallery.models import PhotoGallery, VideoGallery

# Register your models here.

admin.site.register(PhotoGallery)
admin.site.register(VideoGallery)