import email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from Add_Edit_Items.models import Food


# Create your views here.
def add_edit_page(request):
    user = request.user
    print(user)
    if(request.method=="POST"):
        food_name=request.POST['FoodName']
        food_description=request.POST['ShortDescription']
        food_isavailable=request.POST['isvegetarian']
        food_isbestseller=request.POST['isbestseller']
        food_isvegetarian=request.POST['isavailable']
        food_price=request.POST['price']
        food_category=request.POST['category']
      
        food=Food(Restaurant_ID=user,Food_Name=food_name,Short_Description=food_description,
        is_veg=food_isvegetarian,
        is_bestseller=food_isbestseller,
        is_available=food_isavailable,
        Price=food_price,
        Category=get_category(food_category),
        )
        food.save()
    return render(request,"add_edit/add_edit.html")

def hello(request):
    return render(request,"add_edit.html")
def get_category(category):
    if category=="1":
        return "Starters"
    elif category=="2":
        return "Soups"
    elif category=="3":
        return "Salads"
    elif category=="4":
        return "Main Course"
    elif category=="5":
        return "Sides"
    elif category=="6":
        return "Beverages"
    elif category=="7":
        return "Desserts"