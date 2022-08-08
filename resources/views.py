from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobAdvert

# Create your views here.

class CareerList(ListView):
    template_name = 'career.html'
    paginate_by: int = 8
    queryset = JobAdvert.objects.filter(status=1).order_by('pub_date')


class careerDetail(DetailView):
    model = JobAdvert
    template_name = 'career-info.html'



def tender_view(request):
    return render(request, 'tenders.html')


def publication_view(request):
    return render(request, 'publications.html')


def faq_view(request):
    return render(request, 'faq.html')
