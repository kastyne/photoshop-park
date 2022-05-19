from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from database.models.user import PsUser
from .forms import UserRegisterationForm
from django.contrib import messages
from django.views import generic

from database.models.artwork import Artwork
from database.models.course import Course

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"Welcome to Photoshop Park, {username}!")
            return redirect('homepage')
    else:
        form = UserRegisterationForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request, username=None):
    if username: user = PsUser.objects.get(username=username)
    else: user = request.user

    if user == request.user: me = True
    else: me = False
        
    return render(request, 'users/profile.html', { 
        'currUser': user,
        'me': me,
        'art_list': Artwork.objects.filter(authors=user.id).all(),
        'course_list': user.enrollment.all()
    })