from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get the required form data
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request,'The email you entered is already in use')
            return redirect('register')
        else:
            # Check if username is already in use
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username {} is already take'.format(username))
                return redirect('register')
            else:
                # Check if passwords do not match
                if password1 != password2:
                    messages.error(request, 'The passwords you entered do not match')
                    return redirect('register')
                else:
                    # Everything looks good create user object and save
                    user = User.objects.create_user(email=email,username=username,password=password1)
                    user.save()
                    return render(request,'accounts/signIn.html')
    else:
        return render(request,'accounts/register.html')

def signIn(request):
    if request.method == 'POST':
        # Get the required form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('feed')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('signIn')
    else:
        return render(request, 'accounts/signIn.html')

def signOut(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('signIn')