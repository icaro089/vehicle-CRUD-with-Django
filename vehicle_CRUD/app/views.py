from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Vehicle

# Create your views here.


def vehicle_list(request, template_name='vehicle_list.html'):
    query = request.GET.get("search", '')
    page_number = request.GET.get('page', '')
    order = request.GET.get("order", '')
    base_url = '?'
    if query or order:
        if query and order:
            vehicle = Vehicle.objects.filter(model__icontains=query).order_by(order)
            base_url += 'search=' + query + '&order=' + order + '&'
        else:
            if query:
                vehicle = Vehicle.objects.filter(model__icontains=query)
                base_url += 'search=' + query + '&'
            if order:
                vehicle = Vehicle.objects.all().order_by(order)
                base_url += 'order=' + order + '&'
    else:
        vehicle = Vehicle.objects.all()
    paginate_result = do_paginate(vehicle, page_number)
    vehicle = paginate_result[0]
    paginator = paginate_result[1]
    vehicles = {'list': vehicle, 'paginator': paginator, 'base_url': base_url}
    return render(request,template_name, vehicles)


def do_paginate(data_list, page_number):
    ret_data_list = data_list
    result_per_page = 2
    paginator = Paginator(ret_data_list, result_per_page)
    try:
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]