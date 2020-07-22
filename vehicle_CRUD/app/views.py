from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def vehicle_list(request, template_name='vehicle_list.html'):
    query = request.GET.get("search", '')
    page = request.GET.get("page", '')
    order = request.GET.get("order", '')
    if query:
        vehicle = Vehicle.objects.filter(model__icontains=query)
    else:
        try:
            if order:
                vehicle = Vehicle.objects.all().order_by(order)
            else:
                vehicle = Vehicle.objects.all()
            vehicle = Paginator(vehicle, 1)
            vehicle = vehicle.page(page)
        except PageNotAnInteger:
            vehicle = vehicle.page(1)
        except EmptyPage:
            vehicle = paginator.page(paginator.num_pages)
    vehicles = {'list': vehicle}
    return render(request,template_name, vehicles)