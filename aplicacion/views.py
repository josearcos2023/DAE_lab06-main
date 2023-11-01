from django.shortcuts import render
from .models import Producto,Categoria
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Categoria
from .serializer import CategoriaSerializer,ProductoSerializer

def index(request):
    product_list=Producto.objects.order_by('nombre')
    category_list=Categoria.objects.order_by('nombre')
    context={
        'product_list':product_list,
        'category_list':category_list
    }
    return render(request,'index.html', context)

def monitores(request):
    product_list=Producto.objects.order_by('nombre')
    context={
            'product_list':product_list
        }
    return render(request,'monitores.html',context)

def teclados(request):
    product_list=Producto.objects.order_by('nombre')
    context={
            'product_list':product_list
        }
    return render(request,'teclados.html', context)

def almacenamiento(request):
    product_list=Producto.objects.order_by('nombre')
    context={
            'product_list':product_list
        }
    return render(request,'almacenamiento.html',context)

def producto(request):
    return render(request,'producto.html')

def detalle(request,codigo):
    producto=Producto.objects.get(id=codigo)
    context={
        'producto':producto
    }
    return render(request,"detalles.html",context)



class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class CategoriasView(APIView):
    
    def get(self,request):
        dataCategorias = Categoria.objects.all()
        serCategorias = CategoriaSerializer(dataCategorias,many=True)
        return Response(serCategorias.data)
    
    def post(self,request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        
        return Response(serCategoria.data)
    
class CategoriaDetailView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)
    
    def put(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)
    
    def delete(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)


class ProductosView(APIView):
    
    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductoSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class ProductoDetailView(APIView):
    
    def get(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)
