from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about_view, name='about'),
    path('team', views.our_team_view, name='team'),
    path('departments', views.departments_view, name='departments'),
    path('md', views.md_message_view, name='md'),
]