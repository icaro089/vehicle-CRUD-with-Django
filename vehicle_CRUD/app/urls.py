from django.urls import path
from .views import *

urlpatterns = [
    path('vehicles/list/', vehicle_list, name='vehicle_list'),
]