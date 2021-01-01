from django.urls import path
from api import views

urlpatterns = [
    path('productos/', views.productos_list),
    path('productos/<int:pk>', views.productos_detail),
]