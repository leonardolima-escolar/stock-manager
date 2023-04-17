from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ('name', 'price', 'quantity')
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
