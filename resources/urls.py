from django.urls import path
from resources import views

urlpatterns = [
    path('resource-center/downloads', views.publication_view, name='publication'),
    path('faq', views.faq_view, name='faq'),
    path('terms-of-service', views.terms, name='terms'),
    path('privacy-policy', views.privacy, name='privacy')
]
