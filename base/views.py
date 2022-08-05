from django.shortcuts import render
from base.models import Carousel, Patner
from blog.models import Post

# Create your views here.
def index_view(request):
    carousel = Carousel.objects.order_by('-created_on')
    post = Post.objects.order_by('created_on')[:4]
    patners = Patner.objects.all()
    context = {
        'carousel': carousel,
        'post': post,
        'patners': patners,
    }
        
    
    return render(request, 'index.html', context)