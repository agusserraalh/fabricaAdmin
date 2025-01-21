import os
import requests
from .models import Product


import os
import requests
from .models import Product

# Obtener productos desde la API
def getProductos(url, api_token):
    headers = { 
        'X-Api-Token': api_token,
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json',
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

# Actualizar productos en la base de datos
def updateProductos(response_json):
    data = response_json['data']
    for producto in data:
        product, created = Product.objects.get_or_create(
            id=producto.get('id'),
            defaults={
                'product_key': producto.get('product_key'),
                'price': producto.get('price'),
                'notes': producto.get('notes'),
                'is_deleted': producto.get('is_deleted'),
            }
        )

        # Actualizar campos si ya existe
        updated = False
        if not created:  # Solo verifica y actualiza si el producto ya existía
            if product.product_key != producto.get('product_key'):
                product.product_key = producto.get('product_key')
                updated = True
            if product.price != producto.get('price'):
                product.price = producto.get('price')
                updated = True
            if product.is_deleted != producto.get('is_deleted'):
                product.is_deleted = producto.get('is_deleted')
                updated = True
            if updated:
                product.save()


# Sincronizar productos con la API
def sincronizarProductos():
    api_token = os.environ.get("API_TOKEN")
    if not api_token:
        print("Error: API_TOKEN no está configurado en las variables de entorno.")
        return

    url_base = "https://invoicing.co/api/v1/products?"
    current_page = 1

    while True:
        url = f"{url_base}page={current_page}"
        response = getProductos(url, api_token)
        if not response:
            print("Sincronización abortada por error en la solicitud.")
            break

        response_json = response.json()
        updateProductos(response_json)

        pagination = response_json['meta'].get('pagination')
        total_pages = pagination.get('total_pages')

        if current_page >= total_pages:
            print("Sincronización completada con éxito.")
            break
        
        current_page += 1

    