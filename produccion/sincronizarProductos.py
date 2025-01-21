import os
import requests
from .models import Product


def getProductos(url,api_token,  ):

    payload = {}
    headers = { 
    'X-Api-Token': api_token ,
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def updateProductos(response_json):

    data = response_json['data'] # diccionario con
    for producto in data:
        if Product.objects.filter(id=producto.get('id')).exists():
            product = Product.objects.get(id=producto.get('id'))
            if product.product_key != producto.get('product_key'):
                product.product_key = producto.get('product_key')
                product.save()
            
            if product.price != producto.get('price'):
                product.price = producto.get('price')
                product.save()
            
            if product.is_deleted != producto.get('is_deleted'):
                product.is_deleted = producto.get('is_deleted')
                product.save()
        else:
            product = Product()
            product.id = producto.get('id')
            product.product_key = producto.get('product_key')
            product.price = producto.get('price')
            product.notes = producto.get('notes')
            product.is_deleted = producto.get('is_deleted')
            product.save()
       

def sincronizarProductos():

    api_token = os.environ.get("API_TOKEN")
    url_base = "https://invoicing.co/api/v1/products?"
    response = getProductos(url_base,api_token)
    response_json = response.json()
    pagination = response_json['meta'].get('pagination')
    total_pages = pagination.get('total_pages')
    current_page = pagination.get('current_page')
    if response.status_code == 200:
        updateProductos(response_json)
        if total_pages > 1 :
            Flag = True
            while Flag:
                url = url_base + '&' + "page=" + str(current_page+1)
                response = getProductos(url,api_token)
                response_json = response.json()
                pagination = response_json['meta'].get('pagination')
                current_page = pagination.get('current_page')
                if response.status_code == 200:
                    updateProductos(response_json)
                    if current_page == total_pages:
                        Flag = False
                else:
                    print(response.status_code)
    else:
        print(response.status_code)
    