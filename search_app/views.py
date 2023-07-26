from django.shortcuts import render
from product.models import Product
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    if 'search_item' in request.GET:
        context={}
        query=request.GET.get('search_item',None)
        products=Product.objects.filter(Q(name__icontains=query)).all()
        context['query']=query
        context['products']=products
        return render(request,'search.html',context)