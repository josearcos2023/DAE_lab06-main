from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.index,name='index'),
    path('monitores', views.monitores,name='monitores'),
    path('teclados', views.teclados,name='teclados'),
    path('almacenamiento', views.almacenamiento,name='almacenamiento'),
    path('producto/<codigo>', views.detalle,name='detalle'),
    path('categoria',views.CategoriasView.as_view(),name='series'),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('productos',views.ProductosView.as_view(),name='series'),
    path('productos/<int:producto_id>',views.ProductoDetailView.as_view())
]
