from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def vehicle_list(request, template_name='vehicle_list.html'):
    vehicle = Vehicle.objects.all()
    vehicles = {'list': vehicle}
    return render(request,template_name, vehicles)