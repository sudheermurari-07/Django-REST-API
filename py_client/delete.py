import requests

product_id =input("what id you want to be delete ?")

try: 
    product_id = int(product_id)
except:
    product_id = None
    print((f"{product_id} is not not valid id"))

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/destroy/"

get_response = requests.delete(endpoint)

# print(get_response.text)
print(get_response.status_code, get_response.status_code==204)

# print(get_response.json()) 