from django.db import models

# Create your models here.
class Productos(models.Model):
    #Crear el modelo para los productos
    codigo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



