from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import reverse

# Homepage view
def index(request):
    return render(request, 'index.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Researchers page view
def researchers(request):
    return render(request, 'researchers.html')

# Login view
from django.shortcuts import render, redirect
from .forms import LoginForm  # Ensure this is correct
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process form data
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Students page view
def students(request):
    # Optionally, check if the user is authenticated before allowing access
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'students.html')
