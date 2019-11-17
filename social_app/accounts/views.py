from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request,'accounts/signIn.html')


def register(request):
    return render(request, 'accounts/register.html')