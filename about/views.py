from unicodedata import category
from django.shortcuts import render
from blog.models import Post
from .models import MDsMessage, AboutUs, Mission, Personel, Department, Functions, Objectives, Vision
from base.models import CallToActionPanel

# Create your views here.


def about_view(request):
    about_us = AboutUs.objects.filter(status=1)[:1]
    mission = Mission.objects.filter(status=1)[:1]
    leader = Personel.objects.filter(status=1, category=1).all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    objectives = Objectives.objects.filter(status=1)
    functions = Functions.objects.filter(status=1)
    vision = Vision.objects.filter(status=1)
    context = {
        'about_us': about_us,
        'mission': mission,
        'leader': leader,
        'cta': cta,
        'objectives': objectives,
        'functions': functions,
        'vision': vision,
    }
    return render(request, 'about.html', context)


def our_team_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    board_member = Personel.objects.filter(status=1, category=0).all()
    context = {
        'post': post,
        'board_members': board_member,
    }

    return render(request, 'team.html', context)


def departments_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    department = Department.objects.filter(status=1).all()
    context = {
        'post': post,
        'dept': department,
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
