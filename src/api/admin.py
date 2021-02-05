from django.contrib import admin
from .models import User
from api import models

# Register your models here.

admin.site.register(models.Usuarios)
admin.site.register(models.Productos)
