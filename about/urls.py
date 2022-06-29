from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about_view, name='about'),
    path('team', views.our_team_view, name='team'),
    path('career', views.career_view, name='career'),
    path('career-info', views.career_info_view, name='career-info'),
]