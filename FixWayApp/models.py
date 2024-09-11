from django.db import models

class Inventario(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Cambiado a CharField para coincidir con Firebase
    nombreProducto = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    marcaProducto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precioDetalle = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    marcaAutomovil = models.CharField(max_length=100)
    anoProductoUsoInicio = models.IntegerField()
    anoProductoUsoFin = models.IntegerField()
    origen = models.CharField(max_length=100)
