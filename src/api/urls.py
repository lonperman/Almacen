from django.urls import path
from api import views

urlpatterns = [
    path('productos/', views.ProductosView.as_view()),
    path('productosDetail/<int:pk>', views.ProductosDetail.as_view()),
    path('persona/', views.PersonaList.as_view(), name = 'persona_list'),
    path('productosCompra/', views.ProductosCompra.as_view(), name='Compra')
]