
from django.urls import path
from . import views

urlpatterns = [
    path('add_edit/', views.add_edit_page,name='add_edit'),
]
