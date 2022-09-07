from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import UserRegistrationForm, UserLoginForm
from database.models.artwork import Artwork
from database.models.course import Course
from database.models.user import PsUser


def addcourse(request):
    if request.method == 'POST':
        if username:
            user = PsUser.objects.get(username=username)
        else:
            user = request.user

        if user == request.user:
            me = True
        else:
            me = False


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            # messages.success(request, f"Welcome to Photoshop Park, {username}!")
            messages.add_message(request, messages.SUCCESS, f"Welcome to Photoshop Park, {username}!")
            return redirect('homepage')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('homepage')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        return

    return


def profile(request, username=None):
    if username:
        user = PsUser.objects.get(username=username)
    else:
        user = request.user

    if user == request.user:
        me = True
    else:
        me = False

    return render(request, 'users/profile.html', {
        'current_user': user,
        'me': me,
        'art_list': Artwork.objects.filter(authors=user.id).all(),
        'courses': user.enrollment.all()
    })
