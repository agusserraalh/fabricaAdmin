import os
import requests
from .models import Product

def sincronizarProductos():
    api_token = os.environ.get("API_TOKEN")

    url = "https://invoicing.co/api/v1/products?status=active"

    payload = {}
    headers = { 
    'X-Api-Token': api_token ,
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json',
    'Cookie': '__cflb=02DiuEfyB3LaZ68PDyiaiNRbKQb1mWFBvDjHHq4ZZ1vNG'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        response_json = response.json() # diccionario
        data = response_json['data'] # diccionario con 
        for producto in data:
            if Product.objects.filter(id=producto.get('id')).exists():
                product = Product.objects.get(id=producto.get('id'))
                if product.product_key != producto.get('product_key'):
                    product.product_key = producto.get('product_key')
                    product.save()
                
                if product.price != producto.get('price'):
                    product.price = producto.get('price')
                    product.save
                
            else:
                product = Product()
                product.id = producto.get('id')
                product.product_key = producto.get('product_key')
                product.price = producto.get('price')
                product.notes = producto.get('notes')
                product.save()
    else:
        print(response.status_code)
