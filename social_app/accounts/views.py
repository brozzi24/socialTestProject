from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import forms

# Create your views here.
def register(request):
    # Make sure user can only access when signed out
    if request.user.is_authenticated:
        return redirect("feed")

    if request.method == "POST":
        # Get form data
        form = forms.RegisterForm(request.POST)

        # Check if form input is valid
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been registered, please sign in!"
            )
            return redirect("signIn")
        else:
            # Return back to the register page with the error messages
            return render(request, "accounts/register.html", {"form": form})
    else:
        form = forms.RegisterForm
        context = {
            "form": form,
        }
        return render(request, "accounts/register.html", context)


def signIn(request):
    # Make sure user can only access when signed out
    if request.user.is_authenticated:
        messages.success(request, "You are already signed in")
        return redirect("feed")
    if request.method == "POST":
        # Get form data
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, "You are now signed in!")
            return redirect("feed")
        else:
            return render(request, "accounts/signIn.html", {"form": form})
    else:
        form = forms.SignInForm
        return render(request, "accounts/signIn.html", {"form": form})


def signOut(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("signIn")
    else:
        return redirect("signIn")
