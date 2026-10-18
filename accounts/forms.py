from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username","email","first_name","last_name"
        ]


class LoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type":"text",
                "class":"form-control",
                "id":"username",
                "placeholder":"Enter Username",
                "aria-describedby":"emailHelp"
            }
        )
    )

    password=forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type":"password",
                    "class":"form-control",
                    "id":"password",
                    "placeholder":"Enter Password",
                    "aria-describedby":"emailHelp"
                }
            )
        )