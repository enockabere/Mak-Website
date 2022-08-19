from django.urls import path
from . import views


urlpatterns = [
    path('about/who-we-are', views.about_view, name='about'),
    path('about', views.about_view, name='about'),
    path('about/board-of-directors', views.our_team_view, name='team'),
    path('about/departments', views.departments_view, name='departments'),
    path('about/message-from-the-managing-director/', views.md_message_view, name='md'),
]