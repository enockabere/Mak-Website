from django.shortcuts import render
from base.models import Carousel, Patner,CallToActionPanel, Empowerment
from blog.models import Post

# Create your views here.
def index_view(request):
    carousel = Carousel.objects.order_by('-created_on').filter(status=1)
    post = Post.objects.order_by('created_on')[:4]
    patners = Patner.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    empowerment = Empowerment.objects.filter(status=1)[:1]
    context = {
        'carousel': carousel,
        'post': post,
        'patners': patners,
        'cta': cta,
        'emp': empowerment,
    }
        
    return render(request, 'index.html', context)