from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Product, Comment


class CommentInline(admin.StackedInline):
    model = Comment

class ProductAdmin(ModelAdmin):
    list_display = ('name', 'value', 'desc',)
    search_fields = ('name', 'value',)
    inlines = [CommentInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)