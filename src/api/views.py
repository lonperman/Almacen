from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView, Response, status
#from rest_framework.authtoken.models import Token
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication
from .models import Productos, Persona, User
from .serializers import ProductosSerializer, PersonaSerializer, UserLoginSerializer, UserModelSerializer

#Registar Persona


#Personas
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
   # permission_classes = (IsAuthenticated,)
    #authentication_class = (TokenAuthentication,)

#Login
class Login(FormView):
    
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:persona_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)
        
    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)


class Logout(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status= status.HTTP_200_OK)

class ProductosView(APIView):
    #Api productos
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            producto_list = Productos.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(producto_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = ProductosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/productos/?page=' + str(nextPage), 'prevlink': '/api/productos/?page=' + str(previousPage)})
    
    def post(self, request):
        if request.method == 'POST':
            serializer = ProductosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductosDetail(APIView):

    def get(self,request, pk):
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductosSerializer(producto, context={'request': request})
            return Response(serializer.data)
    def put(self,request,pk):
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = ProductosSerializer(producto, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk): 
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ProductosCompra(generics.ListAPIView):

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            productoscompra = Productos.objects.filter(estado="Compra")
            page = request.GET.get('page',1)
            paginator = Paginator(productoscompra,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
            serializer = ProductosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/productosCompra/?page=' + str(nextPage), 'prevlink': '/api/productosCompra/?page=' + str(previousPage)})
    
   