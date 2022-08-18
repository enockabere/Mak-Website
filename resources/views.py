from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Faq, Publication
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
