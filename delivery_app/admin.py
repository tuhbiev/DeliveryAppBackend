from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category__name']
    list_display = ['name', 'category', 'price']
