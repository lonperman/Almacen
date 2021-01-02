from django.urls import path
from api import views

urlpatterns = [
    path('productos/', views.ProductosView.as_view()),
    path('productosDetail/<int:pk>', views.ProductosDetail.as_view()),
]