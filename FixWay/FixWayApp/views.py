# views.py

from django.shortcuts import render
from django.conf import settings  # Importa la configuración desde django.conf
from firebase_admin import firestore

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
        inventarios.append(inventario)

    return render(request, 'inventario.html', {'inventarios': inventarios})
