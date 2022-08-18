from django.urls import path
from .import views

urlpatterns = [
    path('articles', views.PostList.as_view(), name='post'),
    path('articles/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]