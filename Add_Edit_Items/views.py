import email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from Add_Edit_Items.models import Food


# Create your views here.
def add(request):
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
        food_image_link=request.POST['food_link']
        food=Food(Restaurant_ID=user,Food_Name=food_name,Short_Description=food_description,
        is_veg=food_isvegetarian,
        is_bestseller=food_isbestseller,
        is_available=food_isavailable,
        Price=food_price,
        Category=food_category,
        image_link=food_image_link
        )
        food.save()
    return render(request,"add_edit/add.html")


def edit(request):
    all_data = list(Food.objects.all().values())
    print(all_data)
    if request.method=="POST":
        print(request)
        get_food_id=request.POST['FoodId']
        print(get_food_id)
        food_data = Food.objects.filter(id=get_food_id).values()
        context=food_data.values().first()
        return render(request,"add_edit/edit.html",context)
    
    return render(request,"add_edit/card_page.html",{"food_details":all_data})   