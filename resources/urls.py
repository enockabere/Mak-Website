from django.urls import path
from resources import views

urlpatterns = [
    path('resource-center/annual-financial-reports/', views.reports_view, name='publication'),
    path('resource-center/acts/', views.acts_view, name='acts'),
    path('resource-center/sand-harvesting-sites/', views.harvesting_view, name='harvesting'),
    path('resource-center/sand-dealers/', views.delers_view, name='dealers'),
    path('resource-center/faq/', views.faq_view, name='faq'),
    path('resource-center/terms-of-service/', views.terms, name='terms'),
    path('resource-center/privacy-policy/', views.privacy, name='privacy')
]
