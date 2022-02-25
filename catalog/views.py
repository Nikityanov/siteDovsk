from django.shortcuts import render
from .models import Product, Category

def catalog(request):
    catalog = Product.objects.all()
    categories = Category.objects.all()
    context = {'catalog':catalog, 'categories':categories}
    return render(request, 'main/catalog.html', context)

def by_category(request, id_category:int):
    catalog = Product.objects.filter(category=id_category)
    categories = Category.objects.all()
    current_category = Category.objects.get(id=id_category)
    context = {'catalog': catalog, 'categories': categories, 'current_category':current_category}
    return render(request, 'main/category.html', context)
