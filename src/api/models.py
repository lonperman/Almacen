from django.db import models


#Login
class Persona(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=200)

    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)

#Producto
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



