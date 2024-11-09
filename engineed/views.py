from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def researchers(request):
    return render(request, 'researchers.html')
