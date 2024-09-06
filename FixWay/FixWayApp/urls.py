from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Ruta para la página principal
    path('inventario/', views.inventario_view, name='inventario'),  # Ruta para el inventario
]
