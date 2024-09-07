from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from firebase_admin import firestore
from django.http import Http404  # Para manejar errores 404

# Página de inicio
def index_view(request):
    return render(request, 'index.html')  

# Vista del inventario
def inventario_view(request):
    db = firestore.client()

    coleccion_inventario = db.collection('inventario')
    documentos = coleccion_inventario.stream()

    inventarios = []
    for doc in documentos:
        inventario = doc.to_dict()
        inventario['id'] = doc.id 
        inventarios.append(inventario)

    return render(request, 'tienda/inventario.html', {'inventarios': inventarios})

# Detalle del producto
def detalle_producto(request, producto_id):
    db = firestore.client()

    try:
        documento = db.collection('inventario').document(producto_id).get()
        if documento.exists:
            producto = documento.to_dict()
            producto['id'] = documento.id  
        else:
            raise Http404("Producto no encontrado")
    except Exception as e:
        raise Http404(f"Error al obtener los detalles del producto: {e}")

    return render(request, 'tienda/detalleProducto.html', {'producto': producto})

# Agregar al carrito
def agregar_al_carrito(request, producto_id):
    db = firestore.client()

    try:
        documento = db.collection('inventario').document(producto_id).get()
        if not documento.exists:
            raise Http404("Producto no encontrado")
        
        producto = documento.to_dict()
        producto['id'] = documento.id
    except Exception as e:
        raise Http404(f"Error al agregar el producto al carrito: {e}")

    carrito = request.session.get('cart', {})
    cantidad = int(request.POST.get('cantidad', 1))  

    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += cantidad
    else:
        carrito[producto_id] = {
            'nombre': producto['nombreProducto'],
            'precio': producto['precioDetalle'],
            'imagen_url': producto.get('imagen_url', ''), 
            'cantidad': cantidad,
        }

    request.session['cart'] = carrito

    return redirect('detalle_producto', producto_id=producto_id)

def get_cantidad_disponible(producto_id):
    db = firestore.client()
    documento = db.collection('inventario').document(producto_id).get()
    if documento.exists:
        producto = documento.to_dict()
        return producto.get('cantidadDisponible', 0) 
    return 0

def get_carrito_from_session(request):
    carrito = request.session.get('cart', {})
    return carrito

def calcular_total(carrito):
    total = 0
    for item in carrito.values():
        precio = float(item['precio'])  
        cantidad = int(item['cantidad'])  
        total += precio * cantidad
    return total

# Vista del carrito
def carrito_view(request):
    carrito = request.session.get('cart', {}) 
    total = calcular_total(carrito)  
    context = {
        'carrito': carrito, 
        'total': total,
    }
    return render(request, 'carrito/carrito.html', context)


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('cart', {})

    if producto_id in carrito:
        del carrito[producto_id]
        request.session['cart'] = carrito
    
    return redirect('carrito_view')


def mantenciones_por_patente_view(request):
    db = firestore.client()

    if request.method == 'POST':
        patente = request.POST.get('patente')  
        
        mantenciones_ref = db.collection('mantenciones').where('patente', '==', patente)
        mantenciones_docs = mantenciones_ref.stream()

        mantenciones = []
        for doc in mantenciones_docs:
            mantencion = doc.to_dict()
            mantencion['id'] = doc.id  
            mantenciones.append(mantencion)

        return render(request, 'servicios/mantenciones.html', {'mantenciones': mantenciones, 'patente': patente})
    return render(request, 'servicios/mantenciones.html', {'mantenciones': None})