from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Vehicle


def vehicle_list(request, vehicle_category='all', template_name='vehicle_list.html'):
    query = request.GET.get("search", '')
    order = request.GET.get("order", '')
    page_number = request.GET.get("page", '')

    if vehicle_category != 'all':
        vehicle = Vehicle.objects.filter(category=vehicle_category)
        base_url = vehicle_category + '?'
    else:
        vehicle = Vehicle.objects.all()
        base_url = '?'
    if query:
        vehicle = vehicle.filter(model__icontains=query)
        base_url += '&search=' + query
    if order:
        vehicle = vehicle.order_by(order)
        base_url += '&order=' + order

    paginate_result = do_paginate(vehicle, page_number)
    paginated_vehicle = paginate_result[0]
    paginator = paginate_result[1]

    numeros = {'veiculos': paginated_vehicle, 'paginator': paginator, 'base_url': base_url}
    return render(request, template_name, numeros)


def do_paginate(data_list, page_number):
    ret_data_list = data_list
    result_per_page = 1
    paginator = Paginator(ret_data_list, result_per_page)
    try:
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]


def vehicle_details(request, pk, template_name='vehicle_details.html'):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, template_name, {'vehicle': vehicle})
