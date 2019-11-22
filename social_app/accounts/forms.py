from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib import messages


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # Grab data from form
        super(SignInForm, self).clean()

        # Get specific fields in form
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # Validate the user is a registered user
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("INVALID CREDENTIALS")

        # Return any errors if they are found
        return self.cleaned_data
