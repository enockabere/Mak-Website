from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_view, name='contact'),
    path('feedback', views.feedback_view, name='feedback'),
]

