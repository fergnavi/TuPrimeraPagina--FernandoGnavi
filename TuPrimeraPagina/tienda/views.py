from django.shortcuts import render

from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})
