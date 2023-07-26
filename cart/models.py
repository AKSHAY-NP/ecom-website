from django.db import models
from product.models import *
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=50)
    created_date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table='Cart'
        ordering=['created_date']
        
    def __str__(self):
        return '{}'.format(self.cart_id)
    
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    
    class Meta:
        db_table='CartItem'
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)
    