from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
        
    def get_abs_url(self):
        return reverse('product:product_by_cat' ,args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)
    
    
class Product(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField(default=0)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    modeified=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products   '
        
    def __str__(self):
        return self.name
    
    def get_abs_url(self):
        return reverse('product:product_details',args=[self.category.slug,self.slug])
    