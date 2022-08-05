from django.urls import path
from .import views

urlpatterns = [
    path('post', views.PostList.as_view(), name='post'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]