from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Faq, Publication, Terms, Privacy
from blog.models import Post

# Create your views here

def publication_view(request):
    publication = Publication.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'pub': publication,
        'post': post,
    }
    return render(request, 'publications.html', context)


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