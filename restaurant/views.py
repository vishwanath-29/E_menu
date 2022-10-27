from django.shortcuts import render

def welcome_page(request):
    return render(request,'restaurant/welcome_page.html')