from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehiculo, Categoria, Marca

# Create your views here.
def v_index(request):
    return render(request, 'vehiculo/index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        marca_n = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serial_carroceria = request.POST.get('serial_carroceria')
        serial_motor = request.POST.get('serial_motor')
        categoria_n = request.POST.get('categoria')
        precio = float(request.POST.get('precio'))

        categoria = Categoria.objects.get(categoria=categoria_n)
        marca = Marca.objects.get(marca=marca_n)

        Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            serial_carroceria=serial_carroceria,
            serial_motor=serial_motor,
            categoria=categoria,
            precio=precio
        )
        return redirect('/vehiculo/add')
    context = {
        'categorias' : Categoria.objects.all(),
        'marcas' : Marca.objects.all(),
    }
    return render(request, 'vehiculo/agregar_vehiculo.html', context)

def listar_vehiculos(request):
    context = {
        "vehiculos": Vehiculo.objects.all()
    }
    # obtener el valor del query sort_by
    # Si no se entrega un valor, por defecto se usa "-"
    f_sort_by = request.GET.get("sort_by", "-")
    if f_sort_by == "marca":
        context['vehiculos'] = Vehiculo.objects.all().order_by("marca")
    elif f_sort_by == "modelo":
        context["vehiculos"] = Vehiculo.objects.all().order_by("modelo")
    elif f_sort_by == "categoria":
        context["vehiculos"] = Vehiculo.objects.all().order_by("categoria")
    elif f_sort_by == "precio":
        context["vehiculos"] = Vehiculo.objects.all().order_by("precio")
    return render(request, 'vehiculo/listar_vehiculos.html', context)