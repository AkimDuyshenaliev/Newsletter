from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'Department', DepartmentViewSet)
router.register(r'User', UserViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='mailing'),
    path('api/', include(router.urls)),
]
