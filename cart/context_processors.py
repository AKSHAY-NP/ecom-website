from .models import *
from .views import cart_id

def counter(request):
    item_count=0
    try:
        if 'admin' in request.path:
            return {}
        else:
            cart=Cart.objects.filter(cart_id=cart_id(request)).first()
            cart_items=CartItem.objects.filter(cart_id=cart.id).all()
            for item in cart_items:
                item_count+=item.quantity
    except Cart.DoesNotExist:
        item_count=0
    return dict(item_count=item_count)