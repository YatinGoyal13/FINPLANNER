from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileCreationForm, AccountUpdateForm
from .models import Profile
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in.')
            return redirect('login')
    else:
        form = ProfileCreationForm()
    return render(request, 'user/register.html', {'form': form})




@login_required 
def profile(request):
    return render(request, 'user/profile.html')
    


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated.')
            return render(request,'user/profile.html')
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, 'user/update_profile.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'user/view_profile.html', {'user': request.user})

