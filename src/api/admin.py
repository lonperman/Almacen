from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Usuarios)
admin.site.register(models.Productos)
admin.site.register(models.Categoria)
