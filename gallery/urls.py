from django.urls import path
from . import views


urlpatterns = [
    path('media-hub', views.gallery_view, name='gallery'),
]