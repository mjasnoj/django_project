# encoding: utf-8
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    #return HttpResponse('Hello')
    product = Paginator(Product.objects.all(), 2).page(request.GET.get('page', 1))
    return render(request, 'index.html', {'products': product })