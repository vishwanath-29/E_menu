import imp
from pydoc import importfile
from django.shortcuts import render
from accounts.models import restaurant
# Create your views here.
def viewallrestaurant(request):
    restaurant_objects=list(restaurant.objects.all().values())
    print(restaurant_objects)
    return render(request,"view_menu/restaurant_card.html",{'restaurant_details':restaurant_objects})

def viewrestaurantmenu(request,Restaurantid):
    print("came form restaurant id "+Restaurantid)