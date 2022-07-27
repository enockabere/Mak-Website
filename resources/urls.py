from django.urls import path
from . import views

urlpatterns = [
    path('career', views.career_view, name='career'),
    path('career-info', views.career_info_view, name='career-info'),
    path('tender', views.tender_view, name='tender'),
    path('publication', views.publication_view, name='publication'),
    path('faq', views.faq_view, name='faq'),
]
