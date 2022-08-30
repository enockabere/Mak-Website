from django.shortcuts import render
from base.models import Carousel, Patner,CallToActionPanel, Empowerment
from blog.models import Post, Featured
from .forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory

# Create your views here.
def index_view(request):
    carousel = Carousel.objects.order_by('-created_on').filter(status=1)[:7]
    post = Post.objects.order_by('-created_on')[:4]
    patners = Patner.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    empowerment = Empowerment.objects.filter(status=1)[:1]
    featured = Featured.objects.filter(status=1).order_by('-created_on')[:6]
    category_names = 'Sand_Dams Check_Dams Garbions'.split()
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()
    projects = Project.objects.filter(category__category__in=category_names)
    

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'carousel': carousel,
        'post': post,
        'patners': patners,
        'cta': cta,
        'emp': empowerment,
        'form': form,
        'featured': featured,
        'publication_category': publication_category,
        'project_category': project_category,
        'projects': projects
    }
        
    return render(request, 'index.html', context)