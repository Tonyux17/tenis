# landing/models.py

from django.db import models

class Product(models.Model):
    codigo = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.marca
