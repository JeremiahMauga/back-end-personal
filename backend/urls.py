from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from core import views


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('api/', include(router.urls)),
]
