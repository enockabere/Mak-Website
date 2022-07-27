from django.shortcuts import render

# Create your views here.


def career_view(request):
    return render(request, 'career.html')


def career_info_view(request):
    return render(request, 'career-info.html')


def tender_view(request):
    return render(request, 'tenders.html')


def publication_view(request):
    return render(request, 'publications.html')


def faq_view(request):
    return render(request, 'faq.html')
