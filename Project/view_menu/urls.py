from django.urls import path
from . import views

urlpatterns=[
    path('viewmenu/',views.viewallrestaurant),
    path('viewmenu/<str:Restaurantid>/',views.viewrestaurantmenu),
   

]