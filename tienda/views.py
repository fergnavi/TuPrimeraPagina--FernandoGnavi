from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Categoria, Producto, Cliente

def home(request):
    return render(request, 'tienda/home.html')

def about(request):
    return render(request, 'tienda/about.html')

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'tienda/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada correctamente.')
    return redirect('home')

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/lista_categorias.html', {'categorias': categorias})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/lista_clientes.html', {'clientes': clientes})
