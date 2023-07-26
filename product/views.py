from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from cart.models import *
# Create your views here.
# def index(request):
#     return HttpResponse("Hai Akshay")

def allproductcat(request,slug=None):
    context={}
    if slug is not None:
        catgry=get_object_or_404(Category,slug=slug)
        product_list=Product.objects.filter(category=catgry,available=True).all()
        context['category']=catgry
    else:
        product_list=Product.objects.filter(available=True).all()
    paginator=Paginator(product_list,6)
    try:
        page_count=int(request.GET.get('page','1'))
    except:
        page_count=1
    try:
        product=paginator.page(page_count)
    except (EmptyPage,InvalidPage):
        product=paginator.page(paginator.num_pages)
    context['products']=product
    return render(request,'category.html',context)

def prodetails(request,slug,pro_slug):
    context={}
    try:
        product=Product.objects.filter(category__slug=slug,slug=pro_slug)
        cartitem_qty=CartItem.objects.filter(product_id=product[0].id)
        context['product']=product
        context['out_of_stock']=False
        if int(product[0].stock) == int(cartitem_qty[0].quantity):
            context['out_of_stock']=True
    except Exception as e:
        print ("Error--------",e)
    return render(request,'product.html',context)