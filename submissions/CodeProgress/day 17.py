import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")