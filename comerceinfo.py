import http.client
import json

url = "http://20.244.56.144/test/companies/AMZ/categories/Laptop/products"
params = {
    "top-n": 10,
    "minPrice": 1,
    "maxPrice": 10000
}

response =http.client.get(url, params=params) # type: ignore


if response.status_code == 200:
    
    products = response.json()
    
    
    for product in products:
        print(f"Product Name: {product['productName']}")
        print(f"Price: {product['price']}")
        print(f"Rating: {product['rating']}")
        print(f"Discount: {product['discount']}")
        print(f"Availability: {product['availability']}")
        print("\n")
else:
    print(f"Failed to retrieve products. Status code: {response.status_code}")
