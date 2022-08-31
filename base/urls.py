from django.urls import path
from base import views

urlpatterns = [
    path('', views.index_view, name='index'),
    # path('404', views.error_500, name='404')
]