from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from core.forms import CustomRegisterForm
from django.contrib import messages
from core import views

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}! Please log in.')
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'core/register.html', {'form': form})