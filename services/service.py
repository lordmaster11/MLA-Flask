#!/usr/bin/env python3

import requests
import json

def get_json(url):
    response = requests.get(url)

    if response.status_code == 200:
        response_json = json.loads(response.text)

        return response_json

def get_categories():
    url = 'https://api.mercadolibre.com/sites/MLA/categories'
    response = get_json(url)
    categories = []

    for category in response:
        categories.append(category)

    return categories

def get_category(id):
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=' + id + '&official_store_id=all'
    response = get_json(url)
    category= []

    for productos in response['results']:
        category.append(productos)

    return category