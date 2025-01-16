from django.contrib import admin
from .models import Marca, Categoria, Vehiculo

admin.site.site_header = "Proyecto Vehiculos - Dashboard"
admin.site.site_title = "Proyecto Vehiculos - Dashboard"
admin.site.index_title = "Proyecto Vehiculos - Dashboard"
# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca')
    search_fields = ('marca',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    search_fields = ('categoria',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo','serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    list_filter = ('marca', 'categoria')
    ordering = ('-fecha_creacion',)