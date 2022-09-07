from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from database.models.user import PsUser as User


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email address"
        self.fields['email'].help_text = "Used to recover your account if you lose your password."
        self.fields['password2'].label = "Password Confirmation"

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'PhotoshopEnjoyer'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))


# class UserAddCourse(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#