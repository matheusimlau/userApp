from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CreateUSerForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
        ]
