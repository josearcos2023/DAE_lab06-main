from django.db import models
from rest_framework.serializers import ModelSerializer
from .models import Categoria,Producto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model=Categoria
        fields=('id','nombre','pub_date')

class ProductoSerializer(ModelSerializer):
    class Meta:
        model=Producto
        fields=('id','categoria','nombre','precio','stock','descripcion','pub_date')
