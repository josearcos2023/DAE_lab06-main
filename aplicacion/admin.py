from django.contrib import admin

from .models import Categoria,Producto

@admin.register(Categoria)
class AuthorAdmin(admin.ModelAdmin):
    list_display=["nombre","pub_date"]

@admin.register(Producto)
class AuthorAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","stock"]