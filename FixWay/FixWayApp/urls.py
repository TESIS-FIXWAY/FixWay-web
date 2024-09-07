from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('producto/<str:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.carrito_view, name='carrito_view'),
    path('agregar-al-carrito/<str:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<str:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]