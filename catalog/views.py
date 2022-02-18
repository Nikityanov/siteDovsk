from django.shortcuts import render
from .models import Product

def catalog(request):
    catalog = Product.objects.all()
    return render(request, 'main/catalog.html', {'catalog':catalog})
