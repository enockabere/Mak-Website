from django.urls import path
from resources import views

urlpatterns = [
    path('resource-center/downloads', views.publication_view, name='publication'),
    path('faq', views.faq_view, name='faq'),
]
