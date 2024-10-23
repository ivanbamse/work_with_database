from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from unicodedata import category

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort')
    match sort_by:
        case "name":
            field_to_sort = 'name'
        case "min_price":
            field_to_sort = 'price'
        case "max_price":
            field_to_sort = '-price'
        case _:
            field_to_sort = 'id'
    template = 'catalog.html'
    context = {"phones": Phone.objects.all().values().order_by(field_to_sort)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
