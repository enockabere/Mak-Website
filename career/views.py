from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobAdvert, Tender
from blog.models import Post
from base.forms import SubscriptionForm
from resources.models import PubCategory
from projects.models import ProjectCategory

# Create your views here.


class CareerList(ListView):
    template_name = 'career.html'
    paginate_by: int = 8
    queryset = JobAdvert.objects.filter(status=1).order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(CareerList, self).get_context_data(**kwargs)
        

        context['post'] = Post.objects.filter(
            status=1).order_by('-created_on')[:4]
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()

        return context


class careerDetail(DetailView):
    model = JobAdvert
    template_name = 'career-info.html'

    def get_context_data(self, **kwargs):
        context = super(careerDetail, self).get_context_data(**kwargs)
        context['post'] = Post.objects.filter(
            status=1).order_by('created_on')[:4]
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()

        return context


def tender_view(request):
    tender = Tender.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'tender': tender,
        'post': post,
        'form': form,
        'publication_category': publication_category,
        'project_category': project_category,
    }
    return render(request, 'tenders.html', context)
