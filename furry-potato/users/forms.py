from django import forms
from django.contrib.auth.forms import UserCreationForm
from database.models.user import PsUser as User


class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
