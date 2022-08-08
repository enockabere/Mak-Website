from unicodedata import category
from django.shortcuts import render
from blog.models import Post
from .models import MDsMessage, AboutUs, Mission, Personel

# Create your views here.


def about_view(request):
    about_us = AboutUs.objects.filter(status=1)[:1]
    mission = Mission.objects.filter(status=1)[:1]
    leader = Personel.objects.filter(status=1, category=1)
    context = {
        'about_us': about_us,
        'mission': mission,
        'leader' : leader
    }
    return render(request, 'about.html', context)


def our_team_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    context = {
        'post': post
    }

    return render(request, 'team.html', context)


def departments_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    context = {
        'post': post
    }
    return render(request, 'departments.html', context)


def md_message_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    message = MDsMessage.objects.filter(status=1)[:1]
    context = {
        'post': post,
        'message': message
    }
    return render(request, 'md-message.html', context)
