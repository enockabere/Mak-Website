from django.urls import path
from . import views


urlpatterns = [
    path('career', views.CareerList.as_view(), name='career'),
    path('career_info/<slug:slug>/', views.careerDetail.as_view(), name='career_info'),
    path('tender', views.tender_view, name='tender'),
]