from rest_framework import serializers
from .models import Productos, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','apellido')

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ('pk','codigo','name','categoria','estado','descripcion')