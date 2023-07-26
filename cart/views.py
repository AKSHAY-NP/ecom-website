from django.shortcuts import render,redirect
from product.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.filter(id=product_id).first()
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart(cart_id=cart_id(request))
        cart.save()
        
    try:
        cart_item = CartItem.objects.get(cart_id=cart.id, product_id =product.id)
        if cart_item and (cart_item.quantity < cart_item.product.stock):
            cart_item.quantity +=1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem(
            cart=cart,
            product=product,
            quantity=1
        )
        cart_item.save()
    return redirect('cart:cart_details')

def cart_details(request,total=0,counter=0,cart_item=None):
    context={}
    try:
        cart=Cart.objects.filter(cart_id=cart_id(request)).first()
        
        cart_items=CartItem.objects.filter(cart_id=cart.id,active=True).all()
        for item in cart_items:
            total=total+item.sub_total()
            counter+=item.quantity
    except ObjectDoesNotExist:
        pass
    
    context['cart_items']=cart_items
    context['total']=total
    context['counter']=counter
    return render(request,'cart.html',context)  

def remove_cart(request,product_id):
    product=Product.objects.filter(id=product_id).first()
    cart = Cart.objects.get(cart_id=cart_id(request))
    cart_item = CartItem.objects.get(cart_id=cart.id, product_id =product.id)
    if cart_item and (cart_item.quantity > 1):
            cart_item.quantity -=1
            cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_details')

def delete_cart(request,product_id):
    product=Product.objects.filter(id=product_id).first()
    cart = Cart.objects.get(cart_id=cart_id(request))
    CartItem.objects.get(cart_id=cart.id, product_id =product.id).delete()
    return redirect('cart:cart_details')

