from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_display_links = ('name', 'category', 'description')
    search_fields = ('name', 'description')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)