from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'about.html')


def our_team_view(request):
    return render(request, 'team.html')


def career_view(request):
    return render(request, 'career.html')


def career_info_view(request):
    return render(request, 'career-info.html')


def departments_view(request):
    return render(request, 'departments.html')

def tender_view(request):
    return render(request, 'tenders.html')
    
def md_message_view(request):
    return render(request, 'md-message.html')