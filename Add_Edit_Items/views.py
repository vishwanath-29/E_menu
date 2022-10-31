import email
import re
import time
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from Add_Edit_Items.models import Food

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
def add(request):
    user = request.user
    print(user)
    if(request.method=="POST"):
        
        food_name=request.POST['FoodName']
        food_description=request.POST['ShortDescription']
        
        food_isavailable=request.POST.get('isavailable')
        food_isbestseller=request.POST.get('isbestseller')
        food_isvegetarian=request.POST.get('isvegetarian')
        print("Food Vegetrain "+food_isvegetarian)
        print("Food Best Seller "+food_isbestseller)
        print("Food Available "+food_isavailable)
        food_price=request.POST['price']
        
        food_image_link=request.POST['food_link']
        food=Food(Restaurant_ID=user,Food_Name=food_name,Short_Description=food_description,
        is_veg=food_isvegetarian,
        is_bestseller=food_isbestseller,
        is_available=food_isavailable,
        Price=food_price,
        
        image_link=food_image_link
        )
        food.save()
        return redirect("/restaurant")
    return render(request,"add_edit/add.html")


def edit(request):
    user = request.user
    all_data = list(Food.objects.filter(Restaurant_ID_id=user).values())
    print(all_data)
    if request.method=="POST":
        if "goto_edit" in request.POST:
            print(request)
            get_food_id=request.POST['FoodId']
            print(get_food_id)
            food_data = Food.objects.filter(id=get_food_id).values()
            context=food_data.values().first()
            return render(request,"add_edit/edit.html",context)
        elif "Save" in request.POST:
            get_food_id=request.POST['FoodId']
            food_name=request.POST['FoodName']
            food_description=request.POST['ShortDescription']
            food_isavailable=request.POST['isavailable']
            food_isbestseller=request.POST['isbestseller']
            food_isvegetarian=request.POST['isvegetarian']
            food_price=request.POST['price']
            
            food_image_link=request.POST['food_link']

            food=Food.objects.get(id=get_food_id)
            food.Food_Name=food_name
            food.Short_Description=food_description
            food.is_veg=food_isvegetarian
            food.is_bestseller=food_isbestseller
            food.is_available=food_isavailable
            food.Price=food_price
            food.image_link=food_image_link
            food.save()
            all_data = list(Food.objects.filter(Restaurant_ID_id=user).values())
            return render(request,"add_edit/card_page.html",{"food_details":all_data})   
        elif "Delete" in request.POST:
            get_food_id=request.POST['FoodId']
            food=Food.objects.get(id=get_food_id)
            food.delete()
            return render(request,"add_edit/card_page.html",{"food_details":all_data})   

        
    return render(request,"add_edit/card_page.html",{"food_details":all_data})   