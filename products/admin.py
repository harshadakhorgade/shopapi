from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')   # show columns in admin list
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'created_at', 'category')
    list_filter = ('category', 'created_at')  # filter sidebar
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
