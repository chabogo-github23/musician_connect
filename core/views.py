from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegisterForm, EmailLoginForm

User = get_user_model()

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'core/dashboard.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # Changed to authenticate with email
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")  # Generic error message
        else:
            messages.error(request, "Invalid form data")
    else:
        form = EmailLoginForm()

    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def complete_profile(request):
    return render(request, 'core/complete_profile.html')

def debug_base(request):
    try:
        home_template = get_template('core/home.html')
        print(f"[SUCCESS] Found home.html at: {home_template.origin.name}")
        
        try:
            base_template = get_template('base.html')
            print(f"[SUCCESS] Found base.html at: {base_template.origin.name}")
        except Exception as e:
            print(f"[ERROR] base.html search failed: {str(e)}")
            print("Django looked in these directories:")
            from django.template.engine import Engine
            for loader in Engine.get_default().template_loaders:
                print(f"- {loader.__class__.__name__}: {loader.get_dirs()}")
        
        return HttpResponse("Check your console for debug output")
    
    except Exception as e:
        print(f"[CRITICAL ERROR] {str(e)}")
        return HttpResponse(f"Debug error: {str(e)}")