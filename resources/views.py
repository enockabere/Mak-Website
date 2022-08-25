from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Faq, Publication, Terms, Privacy
from blog.models import Post
import os

# Create your views here

def reports_view(request):
    publication = Publication.objects.filter(status=1, category=3).all()
    # filesize = os.path.getsize(fullfilepath)
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'pub': publication,
        'post': post,
        # 'filesize': filesize,
    }
    return render(request, 'reports.html', context)

def acts_view(request):
    publication = Publication.objects.filter(status=1, category=0).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'pub': publication,
        'post': post,
    }
    return render(request, 'acts.html', context)

def harvesting_view(request):
    publication = Publication.objects.filter(status=1, category=2).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'pub': publication,
        'post': post,
    }
    return render(request, 'harvesting.html', context)

def delers_view(request):
    publication = Publication.objects.filter(status=1, category=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'pub': publication,
        'post': post,
    }
    return render(request, 'dealers.html', context)

def faq_view(request):
    faq = Faq.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'faq': faq,
        'post': post,
    }
    return render(request, 'faq.html', context)


def terms(request):
    terms = Terms.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'terms': terms,
        'post': post,
    }
    return render(request, 'terms.html', context)


def privacy(request):
    privacy = Privacy.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'privacy': privacy,
        'post': post,
    }
    return render(request, 'privacy.html', context)