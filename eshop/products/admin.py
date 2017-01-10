from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Product


class ProductAdmin(ModelAdmin):
    list_display = ('name', 'value', 'desc',)
    search_fields = ('name', 'value',)

admin.site.register(Product, ProductAdmin)