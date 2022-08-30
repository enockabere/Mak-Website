from django.urls import path
from . import views

urlpatterns = [
    path('projects/<int:pk>', views.projects_view, name='projects'),
    path('projects/<slug:slug>', views.project_detail_view, name='project-detail'),
    # path ('projects', views.ProjCategories.as_view(), name='projects'),
]