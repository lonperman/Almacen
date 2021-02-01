from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter
#from api.views import Login,Logout

#Views
from api import views as user_views



urlpatterns = [
    path('productos/', views.ProductosView.as_view()),
    path('productosDetail/<int:pk>', views.ProductosDetail.as_view()),
    path('persona/', views.PersonaList.as_view(), name = 'persona_list'),
    path('productosCompra/', views.ProductosCompra.as_view(), name='Compra'),
    path('', include(router.urls))
]