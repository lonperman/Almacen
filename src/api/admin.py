from django.contrib import admin
from .models import User
from api import models

# Register your models here.

admin.site.register(models.Persona)
admin.site.register(models.Productos)
admin.site.register(models.Cliente)
admin.site.register(models.Credito)

