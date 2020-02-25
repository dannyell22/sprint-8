from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=30,null=True)
    descripcion=models.CharField(max_length=30,null=True)
    precio=models.IntegerField(default=10,null=True)
    def __str__(self):
        return self.nombre

