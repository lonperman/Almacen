from django.db import models

#Usuarios
class Usuarios(models.Model):
    id_persona = models.AutoField(primary_key= True)
    nombre_persona = models.CharField('Nombre', max_length=100)
    password_persona = models.CharField(max_length=10)

    LOAN_STATUS = (
        ('A','admin'),
        ('O','operador')
    )

    rol_usuario =  models.CharField(max_length=100,choices=LOAN_STATUS,blank=True, default='O')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id_persona"]


    def __str__(self):
        return '{0},{1}'.format(self.nombre_persona)

#Categoria
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=10)
    nombre_categoria = models.CharField(max_length=10)
    codigo_categoria = models.CharField(primary_key=True,max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id_categoria"]

    #Metodos
    def __str__(self):
        return self.nombre_categoria


#Proveedor
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    cantidad_articulos = models.IntegerField()
    precio_producto = models.IntegerField() 
    createdAt = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ["id_proveedor"]

    #Metodos
    def __str__(self):
        return self.nombre_proveedor


#Producto
class Productos(models.Model):
    #Crear el modelo para los productos
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    LOAN_STATUS = (
        ('C','Compra'),
        ('V','Venta'),
        ('P','Pendiente'),
    )

    codigo =  models.ForeignKey(Categoria,on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    estado_producto = models.CharField(max_length=100,choices=LOAN_STATUS,blank=True, default='C')
    cantidad_producto = models.IntegerField()
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='productos_imagen')
    createdAt = models.DateTimeField(auto_now_add=True)

    #Metada
    class Meta:
        ordering = ["id_producto"]

    #Metodos
    def __str__(self):
        return self.nombre_producto


#Cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100,null=False)
    cedula_cliente = models.CharField(unique=True,max_length=100,null=False)

    LOAN_STATUS = (
        ('N','Nuevo'),
        ('A','Antiguo'),
    )

    estado_cliente =  models.CharField(max_length=100,choices=LOAN_STATUS,blank=True, default='N')
    telefono_cliente = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)

 #Metada
    class Meta:
        ordering = ["id_cliente"]
    
    def __str__(self):
        return self.nombre_cliente

#Venta
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    monto_venta = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)


    #Metada
    class Meta:
        ordering = ["id_venta"]

    def __str__(self):
        return self.id_cliente.nombre_cliente

    
#Credito
class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    saldo_pendiente = models.IntegerField() 
    createdAt = models.DateTimeField(auto_now_add=True)


     #Metada
    class Meta:
        ordering = ["id_cliente"]

    def __str__(self):
        return self.id_cliente




