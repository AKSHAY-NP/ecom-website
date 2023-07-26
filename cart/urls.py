from django.urls import path
from . import views
app_name='cart'

urlpatterns = [
    path('cart-id',views.cart_id,name="cart_id"),
    path('add-cart/<slug:product_id>',views.add_cart,name="add_cart"),
    path('remove-cart/<slug:product_id>',views.remove_cart,name="remove_cart"),
    path('delete-cart/<slug:product_id>',views.delete_cart,name="delete_cart"),
    path('cart-details',views.cart_details,name="cart_details"),
]