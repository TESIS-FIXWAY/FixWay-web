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
        inventario['id'] = doc.id  # Incluye el ID del documento en los datos
        inventarios.append(inventario)

    return render(request, 'tienda/inventario.html', {'inventarios': inventarios})

# Detalle del producto
def detalle_producto(request, producto_id):
    db = firestore.client()

    try:
        documento = db.collection('inventario').document(producto_id).get()
        if documento.exists:
            producto = documento.to_dict()
            producto['id'] = documento.id  # Añade el ID del documento al producto
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
    cantidad = int(request.POST.get('cantidad', 1))  # Obtener la cantidad desde el formulario

    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += cantidad
    else:
        carrito[producto_id] = {
            'nombre': producto['nombreProducto'],
            'precio': producto['precioDetalle'],
            'imagen_url': producto.get('imagen_url', ''),  # Asegúrate de obtener la URL de la imagen
            'cantidad': cantidad,
        }

    request.session['cart'] = carrito

    return redirect('detalle_producto', producto_id=producto_id)

def get_cantidad_disponible(producto_id):
    db = firestore.client()
    documento = db.collection('inventario').document(producto_id).get()
    if documento.exists:
        producto = documento.to_dict()
        return producto.get('cantidadDisponible', 0)  # Devuelve 0 si no existe el campo
    return 0

def get_carrito_from_session(request):
    # Obtén el carrito desde la sesión, si no existe inicializa uno vacío
    carrito = request.session.get('cart', {})
    return carrito

def calcular_total(carrito):
    total = 0
    for item in carrito.values():
        # Asegúrate de que 'precio' y 'cantidad' son números antes de multiplicar
        precio = float(item['precio'])  # Convierte a float si es un número decimal
        cantidad = int(item['cantidad'])  # Convierte a entero para la cantidad
        total += precio * cantidad
    return total

# Vista del carrito
def carrito_view(request):
    carrito = request.session.get('cart', {})  # Obtener el carrito de la sesión
    total = calcular_total(carrito)  # Función para calcular el total

    # Pasar el carrito al contexto con la clave correcta
    context = {
        'carrito': carrito,  # Asegúrate de que se use 'cart' como clave
        'total': total,
    }
    return render(request, 'carrito/carrito.html', context)



# Eliminar del carrito
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('cart', {})

    if producto_id in carrito:
        del carrito[producto_id]
        request.session['cart'] = carrito
    
    return redirect('carrito_view')
