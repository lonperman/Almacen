from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation, authenticate
from .models import Productos, Persona,Cliente,User


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

class UserLoginSerializer(serializers.ModelSerializer):

    #campos requeridos
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    #Validamos los datos
    def validate(self, data):
        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son validas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','apellido')

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ('pk','codigo','name','categoria','estado','cantidad','precio_uni','descripcion')

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('documento','nombre','productos')