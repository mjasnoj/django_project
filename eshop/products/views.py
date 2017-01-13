# encoding: utf-8
from random import randint

from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Comment
from .forms import CommentForm, CommentModelForm
# Create your views here.


def index(request):
    #return HttpResponse('Hello')
    all_products = Product.available.all()
    if 'k' not in request.session:
        request.session['k'] = randint(1, 10000)
    if 'q' in request.GET:
        all_products = all_products.filter(name__contains=request.GET['q'])
    product = Paginator(all_products, 2).page(request.GET.get('page', 1))
    return render(request, 'index.html', {
        'products': product,
        'num_pages': Paginator(all_products, 2).num_pages,
        'q': request.GET.get('q', ''),
        'k': request.session['k'],
    })

def detail(request, product_id):
    #return HttpResponse(product_id)
    # try:
    #     Product.objects.get(pk=int(product_id))
    # except:
    #     raise Http404
    product = get_object_or_404(Product, pk=int(product_id))
    comments = Comment.objects.filter(product=product)
    # form = CommentForm()
    form = CommentModelForm()
    if request.method == 'POST':
        # form = CommentForm(request.POST)
        form = CommentModelForm(request.POST)
        if form.is_valid():
            print "Ok"
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            messages.info(request, "Comment added successfully")
            return redirect('/products/detail/{}'.format(product_id))
    return render(request, 'detail.html', {
        'product': product,
        'form': form,
        'comments': comments,
    })
