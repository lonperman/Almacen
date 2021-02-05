from rest_framework import serializers
from .models import Productos, Usuarios,Cliente,Categoria,Proveedor,Venta,Credito


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id_persona','nombre_persona','password_persona','rol_usuario')

class CategoriaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_categoria','nombre_categoria','codigo_categoria')

class ProveedorSerializer(serializer.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id_proveedor','nombre_proveedor','cantidad_articulos','precio_producto')

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ('id_producto','nombre_producto',
                'codigo','id_proveedor','estado_producto',
                'cantidad_producto','precio_producto','imagen_producto')

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('id_cliente','nombre_cliente','cedula_cliente',
                'estado_cliente','telefono_cliente')

class VentaSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = Venta
        fields = ('id_venta','id_producto','id_cliente','id_usuario','monto_venta')

class CreditoSerializer(serializer.ModelSerializer):

    class Meta:
        model = Credito
        fields = ('id_credito','id_producto','id_cliente','saldo_pendiente')