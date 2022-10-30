import imp
from pydoc import importfile
from django.shortcuts import render
from Add_Edit_Items.models import Food
from accounts.models import restaurant
# Create your views here.
def viewallrestaurant(request):
    restaurant_objects=list(restaurant.objects.all().values())
    print(restaurant_objects)
    return render(request,"view_menu/restaurant_card.html",{'restaurant_details':restaurant_objects})

def viewrestaurantmenu(request,Restaurantid):
    food_data = Food.objects.filter(Restaurant_ID_id=Restaurantid).values()
    print(food_data)
    return render(request,"view_menu/card_page.html",{'food_details':food_data})