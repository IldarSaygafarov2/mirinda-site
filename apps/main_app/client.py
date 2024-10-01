import requests


endpoint = 'http://127.0.0.1:8000/api/'


headers = {
    'Accept-Language': 'uz'
}

print(requests.get(endpoint + 'faqs/', headers=headers).json())
