from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.validators import RegexValidator


# This class defines a form for logging in to the application.
class LoginForm(forms.Form):
    # The `username` field is a text field that allows the user to enter their username.
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    # The `password` field is a password field that allows the user to enter their password.
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )




# This class defines a form for signing up for a new account.
class SignUpForm(UserCreationForm):
    # The `first_name` field is a text field that allows the user to enter their first name.
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # The `last_name` field is a text field that allows the user to enter their last name.
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # The `username` field is a text field that allows the user to enter their username.
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # The `password1` field is a password field that allows the user to enter their password.
    # The `password1` field is validated using a regular expression that ensures the password contains at least 8 characters and includes both letters and numbers.
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        validators = [
            RegexValidator(
                regex='^(?=.*\d)(?=.*[a-zA-Z]).{8,}$',
                message="Your password must contain at least 8 characters and include both letters and numbers."
            )
        ]
    )

    # The `password2` field is a password field that allows the user to confirm their password.
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # The `email` field is an email field that allows the user to enter their email address.
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # The `Meta` class defines the model and fields for the form.
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_student', 'is_tutor')
