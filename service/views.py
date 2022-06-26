from django.shortcuts import render

# Create your views here.

def service_view(request):
    return render(request, 'service.html')
