
from django.urls import path


from fron.views import buscar,home,ingreso,login,padre,vender
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="Home"),
    path('producto',vender,name="Producto"),
    path('login',login,name="Login"),
    path('buscar/',buscar,name="Buscar"),
    path('padre',padre,name="Padre"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)