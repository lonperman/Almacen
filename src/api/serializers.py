from rest_framework import serializers
from .models import Productos, Usuarios,Cliente,Categoria,Proveedor,Venta,Credito


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('pk','id_persona','nombre_persona','password_persona','rol_usuario')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk','id_categoria','nombre_categoria','codigo_categoria')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('pk','id_proveedor','nombre_proveedor','cantidad_articulos','precio_producto')

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ('pk','id_producto','nombre_producto',
                'codigo','id_proveedor','estado_producto',
                'cantidad_producto','precio_producto','imagen_producto')

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('pk','id_cliente','nombre_cliente','cedula_cliente',
                'estado_cliente','telefono_cliente')

class VentaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venta
        fields = ('pk',' id_venta','id_producto','id_cliente','id_usuario','monto_venta')

class CreditoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = ('pk','id_producto','id_cliente','saldo_pendiente')
