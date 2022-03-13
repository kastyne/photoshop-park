from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome to Photoshop Park, {username}!")
            return redirect('homepage')
    else:
        form = UserRegisterationForm()

    return render(request, 'users/register.html', {'form': form})
