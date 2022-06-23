from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('post',  views.post_view, name='post'),
    path('post-detail', views.post_detail_view, name='post-detail')
]