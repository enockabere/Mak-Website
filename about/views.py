from django.shortcuts import render

# Create your views here.


def about_view(request):
    return render(request, 'about.html')


def our_team_view(request):
    return render(request, 'team.html')


def departments_view(request):
    return render(request, 'departments.html')


def md_message_view(request):
    return render(request, 'md-message.html')
