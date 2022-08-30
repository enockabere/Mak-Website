
from django.shortcuts import render
from blog.models import Post
from .models import MDsMessage, AboutUs, Mission, Personel, Department, Functions, Objectives, Vision,ServiceCharter
from base.models import CallToActionPanel
from base.forms import SubscriptionForm
from projects.models import ProjectCategory
from resources.models import PubCategory

# Create your views here.


def about_view(request):
    about_us = AboutUs.objects.filter(status=1)[:1]
    mission = Mission.objects.filter(status=1)[:1]
    leader = Personel.objects.filter(status=1, category=1).all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    objectives = Objectives.objects.filter(status=1)
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    vision = Vision.objects.filter(status=1)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'about_us': about_us,
        'mission': mission,
        'leader': leader,
        'cta': cta,
        'objectives': objectives,
        
        'vision': vision,

        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'about.html', context)


def boardOfDirectorsView(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    board_member = Personel.objects.filter(status=1, category=0).all()
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'post': post,
        'board_members': board_member,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }

    return render(request, 'board-of-directors.html', context)

def ManagementView(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    board_member = Personel.objects.filter(status=1, category=1).all()
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'post': post,
        'board_members': board_member,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }

    return render(request, 'management.html', context)




def departments_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    project_category = ProjectCategory.objects.all()
    department = Department.objects.filter(status=1).all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'post': post,
        'dept': department,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'departments.html', context)


def md_message_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:5]
    message = MDsMessage.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'post': post,
        'message': message,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'md-message.html', context)


def core_values(request):
    mission = Mission.objects.filter(status=1)
    vision = Vision.objects.filter(status=1)
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'mission': mission,
        'vision': vision,    
        'cta': cta,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }

    return render(request, 'core-values.html', context)


def service_charter(request):
    charter = ServiceCharter.objects.filter(status=1).all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'charter': charter,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'service-chater.html', context)


def strategic_plan(request):
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'strategic-plan.html', context)


def functions_view(request):
    functions = Functions.objects.filter(status=1)
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'functions': functions,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'functions.html', context)


def strategic_plan_view(request):
    objectives = Objectives.objects.filter(status=1)
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'objectives': objectives,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'strategic-plan.html', context)