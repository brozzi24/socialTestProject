from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def feed(request):
    # Check if user is sign in
    if request.user.is_authenticated:
        return render(request,'feed/feed.html')
    else:
        return redirect('signIn')

