from django.urls import path
from . import views


urlpatterns = [
    path('about/who-we-are', views.about_view, name='about'),
    path('about', views.about_view, name='about'),
    path('about/board-of-directors', views.boardOfDirectorsView, name='board'),
    path('about/management', views.ManagementView, name='management'),
    path('about/departments', views.departments_view, name='departments'),
    path('about/message-from-the-managing-director/', views.md_message_view, name='md'),
    path('about/mission-vision-corevalues/', views.core_values, name='values'),
    path('about/service-charter/', views.service_charter, name='service-charter'),
    path('about/strategic-plan/', views.strategic_plan, name='strategic-plan'),
    path('about/our-mandates-and-functions/', views.functions_view, name='functions'),
]