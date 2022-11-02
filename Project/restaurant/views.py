from typing import final
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from accounts.models import restaurant
def welcome_page(request):
    User=request.user
    rest_details=list(restaurant.objects.filter(Restaurant_Id_id=User).values())

    print(User)

    final_data=[{"Userdetails":User},{'Restname':rest_details}]
    print(final_data)
    return render(request,'restaurant/welcome_page.html',{'response':final_data})