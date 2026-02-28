import requests

endpoint="http://localhost:8000/products/"
get_response=requests.get(endpoint,params={})

print(get_response.json())
print(get_response.status_code)