from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

# Home y login
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
            return render(request, 'tienda/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'tienda/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito.")
    return redirect('home')



def crear_categoria(request):
    categoria_creada = None

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria_creada = form.save()
            form = CategoriaForm()  

    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(request, 'tienda/categorias.html', {
        'form': form,
        'categorias': categorias,
        'categoria_creada': categoria_creada
    })

def lista_categorias(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/categorias.html', {'categorias': categorias, 'form': form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'tienda/formulario_categoria.html', {'form': form})

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('lista_categorias')

# CRUD de Producto
def lista_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/productos.html', {'productos': productos, 'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/formulario_producto.html', {'form': form, 'tipo': 'Producto'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/formulario_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')

# CRUD de Cliente
def lista_clientes(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'tienda/clientes.html', {'clientes': clientes, 'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado con éxito.")
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'tienda/formulario_cliente.html', {'form': form, 'tipo': 'Cliente'})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'tienda/formulario_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')
