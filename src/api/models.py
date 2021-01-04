from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

#Registrar User
""" class Usuarios(models.Model):
 
   
   email_user = models.EmailField(max_length=100)
   nombre_user = models.CharField(max_length=100)
   password = models.CharField(max_length=100)
   
    def __str__(self):
    return self.email

 """

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now=True)
    extract = RichTextField(null=True)
    phone = models.CharField(null=True, max_length=15)
    city = models.CharField(null=True, max_length=255)
    country = models.CharField(null=True, max_length=255)
    is_recruiter = models.BooleanField(default=False)

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

    LOAN_STATUS = (
        ('C','Compra'),
        ('V','Venta'),
        ('P','Pendiente'),
    )

    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100,choices=LOAN_STATUS,blank=True, default='C')
    cantidad = models.IntegerField()
    precio_uni = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    #Metada
    class Meta:
        ordering = ["name"]

    #Metodos
    def __str__(self):
        return self.name


#Cliente
class Cliente(models.Model):
    documento = models.CharField(max_length=100,null=False)
    nombre = models.CharField(max_length=100,null=False)
    createdAt = models.DateTimeField(auto_now_add=True)

 #Metada
    class Meta:
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

#Venta
class Venta(models.Model):
    productos_venta = models.ForeignKey(Productos,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productos_venta.name

    
#Credito
class Credito(models.Model):
    productos_credito = models.ForeignKey(Productos,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    saldo_pendiente = models.IntegerField() 
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productos_credito.name


#Proveedor
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    nombre_negocio = models.CharField(max_length=100)
    articulo = models.CharField(max_length=100)
    cantidad_articulos = models.IntegerField()




