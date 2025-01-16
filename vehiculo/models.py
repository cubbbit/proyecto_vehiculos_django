from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.marca
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.categoria

class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"
    