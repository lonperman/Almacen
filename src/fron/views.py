from django.shortcuts import render
from django.http import HttpResponse

from api.models import Categoria,Cliente,Credito,Productos,Proveedor,Usuarios,Venta

# Create your views here.


def home(request):

    return render(request,"home.html")

def vender(request):
    
    producto=Productos.objects.all()

    return render(request,"productos.html",{"productos":producto})

def buscar(request):
    
    if request.GET["producto"]:

     producto=request.GET["producto"]
    
     articulo=Productos.objects.filter(nombre_producto__icontains=producto)

     return render(request,"resultados_pro.html",{"articulos":articulo,"query":producto})
    
    else:

     mensaje="No Hay Datos De Busqueda"    
     
    return HttpResponse(mensaje)        

def padre(request):

    return render(request,"padre.html")

def ingreso(request):
  
    if request.GET["Usuario"] and request.GET["Contraseña"]:
     
     User = request.GET["Usuario"]
     Contrasena = request.GET["Contraseña"]
    # usuario_registrado = Cliente.objects.filter(correo__icontains=User , password__icontains=Contrasena)
  
    
     return render(request,"home.html")

    else:

     mensaje="Error Usuario o Contraseña"

    return HttpResponse(mensaje)

def login(request):
    
    return render(request,"logueo.html")

