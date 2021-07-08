from django.shortcuts import render, redirect
from .forms import ProductoForm, AporteForm, UsuarioPForm
from .models import Producto, Usuario, Registro
from django.contrib.auth.decorators import login_required
from .decorators import admin_required


# Create your views here.

def home(request):
    return render(request, 'inventario_cooperativa/public/home.html')


def privacidad(request):
    return render(request, 'inventario_cooperativa/public/privacy.html')


def legal(request):
    return render(request, 'inventario_cooperativa/public/legal.html')


def cookies(request):
    return render(request, 'inventario_cooperativa/public/cookies.html')


def contacto(request):
    return render(request, 'inventario_cooperativa/public/contacto.html')


@admin_required
@login_required
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioPForm(request.POST)
        if form.is_valid():
            form.save()
            tmp = Usuario.objects.get(rut=form.cleaned_data["rut"])
            tmp.username = form.cleaned_data["rut"]
            tmp.save()
        return redirect('Home')
    else:
        form = UsuarioPForm()
    context = {
        'form': form,
    }
    return render(request, 'inventario_cooperativa/admin/crearUsuario.html', context)


@admin_required
@login_required
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            if Producto.objects.filter(nombre=form.cleaned_data["nombre"]).exists():
                return redirect('Home')
            else:
                form.save()
                tmp1 = Producto.objects.get(nombre=form.cleaned_data["nombre"])
                tmp = Registro(producto=tmp1, cantidad=form.cleaned_data["disponibilidad"])
                tmp.save()
            return redirect('Lista_Inventario')
    else:
        form = ProductoForm()
    context = {
        'form': form,
    }
    return render(request, 'inventario_cooperativa/admin/agregarProducto.html', context)


@admin_required
@login_required
def generar_aporte(request):
    if request.method == 'POST':
        form = AporteForm(request.POST)
        if form.is_valid():
            tmp = form.cleaned_data['producto']
            if Producto.objects.filter(nombre=tmp).exists():
                instanciaProducto = Producto.objects.get(nombre=tmp)
                instanciaProducto.disponibilidad += form.cleaned_data["cantidad"]
                if instanciaProducto.disponibilidad < 0:
                    return redirect('Agregar')
                else:
                    instanciaProducto.save()
                    form.save()
            else:
                return redirect('Agregar')
            return redirect('Lista_Registros')
    else:
        form = AporteForm()
    context = {
        'form': form,
    }
    return render(request, 'inventario_cooperativa/admin/generarAporte.html', context)


@login_required
def listar_registros(request):
    registros = Registro.objects.all()
    context = {
        'registros': registros,
    }
    return render(request, 'inventario_cooperativa/private/registros.html', context)


@login_required
def listar_inventario(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'inventario_cooperativa/private/listaProductos.html', context)


@admin_required
@login_required
def listar_socios(request):
    socios = Usuario.objects.filter(esSocio=True)
    context = {
        'socios': socios,

    }
    return render(request, 'inventario_cooperativa/admin/listaSocios.html', context)
