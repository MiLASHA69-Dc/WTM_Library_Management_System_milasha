from django import forms
from django .contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username","email","first_name","last_name"
        ]


class LoginForm(AuthenticationForm):
    pass