from django.contrib import admin
from .models import User
from api import models

# Register your models here.

admin.site.register(models.Persona)
admin.site.register(models.Productos)
admin.site.register(models.Cliente)
admin.site.register(models.Credito)

class UserAdmin(admin.ModelAdmin):

    list_display = ('pk','username','email',)
    list_display_links = ('pk','username','email',)

    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_activate',
        'is_staff',
        'date_joined',
        'modified',
    )

    readonly_fields = ('date_joined','modified',)