import email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def add_edit_page(request):
    if(request.method=="POST"):
        print(request.POST["isavailable"])
    return render(request,"add_edit.html")

def hello(request):
    return render(request,"add_edit.html")
