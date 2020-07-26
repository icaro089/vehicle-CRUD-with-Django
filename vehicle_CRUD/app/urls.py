from django.urls import path
from .views import *

urlpatterns = [
    path('', vehicle_list),
    path('vehicles/', vehicle_list),
    path('vehicles/<vehicle_category>', vehicle_list, name='vehicle_list'),
    path('vehicle/detail/<pk>', vehicle_details, name='vehicle_details')
]
