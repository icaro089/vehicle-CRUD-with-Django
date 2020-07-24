
from django.urls import path
from .views import *

urlpatterns = [
    path('vehicles/<vehicle_category>', vehicle_list, name='vehicle_list'),

]
