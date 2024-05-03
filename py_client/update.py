import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data= {
    "title": "Hello world my old friend",
    "price": 123
}

get_response = requests.put(endpoint, json=data)

# print(get_response.text)
print(get_response.status_code)

print(get_response.json()) 