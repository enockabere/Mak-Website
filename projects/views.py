import imp
from turtle import title
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base import models
from .models import Project, ProjectCategory
from base.models import CallToActionPanel, Subscription
from base.forms import SubscriptionForm
from resources.models import PubCategory

# Create your views here.

def projects_view(request, pk):
    projects = Project.objects.filter(status=1, category=pk).all()
    project_category = ProjectCategory.objects.all()
    project_category_in = ProjectCategory.objects.get(id=pk)
    publication_category = PubCategory.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'projects': projects,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
        'project_category_in': project_category_in,
    }
    return render(request, 'projects.html', context)


def project_detail_view(request, slug):
    projects = Project.objects.get(slug=slug)
    project_category = ProjectCategory.objects.all()
    
    publication_category = PubCategory.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'projects': projects,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
        
    }
    return render(request, 'project-detail.html', context)    


# class ProjCategories(ListView):
#     template_name = 'projects.html'
#     model = ProjectCategory
#     context_object_name = 'all_categs'

#     def get_queryset(self):
#        return Project.objects.all().select_related('category')

#     def get_context_data(self):
#         context = super(ProjCategories, self).get_context_data()
#         context['projects'] = Project.objects.all()[:3]
       
#         return context

#     # def get_success_url(self):
#     #    return reverse('home') #add your path

