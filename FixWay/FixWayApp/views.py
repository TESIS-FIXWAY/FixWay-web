from django.shortcuts import render, get_object_or_404
from django.conf import settings  # Importa la configuración desde django.conf
from firebase_admin import firestore
from django.http import Http404  # Para manejar errores 404

def index_view(request):
    return render(request, 'index.html')  

def inventario_view(request):
    # Obtén el cliente Firestore desde la configuración
    db = firestore.client()

    coleccion_inventario = db.collection('inventario')
    documentos = coleccion_inventario.stream()

    inventarios = []
    for doc in documentos:
        inventario = doc.to_dict()
        inventario['id'] = doc.id  # Incluye el ID del documento en los datos
        inventarios.append(inventario)

    return render(request, 'tienda/inventario.html', {'inventarios': inventarios})

def detalle_producto(request, producto_id):
    # Obtén el cliente Firestore desde la configuración
    db = firestore.client()

    # Busca el documento en la colección 'inventario'
    try:
        documento = db.collection('inventario').document(producto_id).get()
        if documento.exists:
            producto = documento.to_dict()
        else:
            raise Http404("Producto no encontrado")
    except:
        raise Http404("Error al obtener los detalles del producto")

    return render(request, 'tienda/detalleProducto.html', {'producto': producto})
