from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # list_filter = ['name', 'slug']
    # search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'available','stock', 'created', 'modeified']
    list_editable = ['stock', 'price']
    list_filter = ['name', 'category', 'available']
    # search_fields = ['name', 'category', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
admin.site.register(Product, ProductAdmin)
    

    
