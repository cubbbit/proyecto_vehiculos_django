from django.urls import path
from .views import v_index, agregar_vehiculo, listar_vehiculos

urlpatterns = [
    path('', v_index, name='index'),
    path('add/', agregar_vehiculo, name="agregar_vehiculo"),
    path('list/', listar_vehiculos, name="listar_vehiculos")
]