from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobAdvert, Tender
from blog.models import Post

# Create your views here.
class CareerList(ListView):
    template_name = 'career.html'
    paginate_by: int = 8
    queryset = JobAdvert.objects.filter(status=1).order_by('pub_date')


class careerDetail(DetailView):
    model = JobAdvert
    template_name = 'career-info.html'



def tender_view(request):
    tender = Tender.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    context = {
        'tender': tender,
        'post': post,
    }
    return render(request, 'tenders.html', context)