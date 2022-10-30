from django.shortcuts import render
from django.contrib.auth.models import User,auth
def welcome_page(request):
    User=request.user
    print(User)
    return render(request,'restaurant/welcome_page.html',{"Userdetails":User})