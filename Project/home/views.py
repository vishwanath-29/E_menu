from django.shortcuts import redirect, render
from django.contrib.auth.models import auth

def home(request):
    return render(request,'home/home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')