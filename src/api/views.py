# from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.views import Response, status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Productos
from .serializers import ProductosSerializer

@api_view(['GET','POST'])
def productos_list(request):

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        producto = Productos.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(producto,10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = ProductosSerializer(data, context={'request':request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data, 'count': paginator.count, 'numpages':paginator.num_pages, 'nextlink':'/api/productos/?page=' + str(nextPage), 'prevlink':'/api/productos/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def productos_detail(request, pk):

    try:
        producto = Productos.objects.get(pk=pk)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductosSerializer(producto, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductosSerializer(producto, data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)