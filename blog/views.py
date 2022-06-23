from django.shortcuts import render

# Create your views here.

def post_view(request):
    return render(request, 'post.html')


def post_detail_view(request):
    return render(request, 'post-detail.html')