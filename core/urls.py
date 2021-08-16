from django.urls import path, include
from rest_framework import routers
from .views import InventoryViewSet, Inventory_Api, current_user, UserList, UserViewSet 
from core import views

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('inventory/', Inventory_Api)
]

