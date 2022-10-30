from django.urls import path
from . import views

urlpatterns=[
    path('viewmenu/',views.viewallrestaurant),
    path('viewmenu/(?P<Restaurantid>[0-9]+)/',views.viewrestaurantmenu),
   

]