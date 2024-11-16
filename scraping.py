import requests
from bs4 import BeautifulSoup

def scrape_amazon_products(url):
    """
    Extrae información de un listado de productos en Amazon.

    Args:
        url: La URL del listado de productos.

    Returns:
        Una lista de diccionarios, donde cada diccionario representa un producto.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for product in soup.find_all('div', {'data-cel-widget': 'search_result'}):
        product_dict = {}
        product_dict['title'] = product.h2.text.strip()
        product_dict['price'] = product.find('span', {'class': 'a-offscreen'}).text.strip()
        # Agrega aquí más selectores para extraer otros datos, como la calificación, el número de reseñas, etc.
        products.append(product_dict)

    return products

# Ejemplo de uso
url = 'https://www.amazon.com/s?k=celulares&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
products = scrape_amazon_products(url)

for product in products:
    print(product)