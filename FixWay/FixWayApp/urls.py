from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('producto/<str:producto_id>/', views.detalle_producto, name='detalle_producto'),  # Captura el ID como string
]
