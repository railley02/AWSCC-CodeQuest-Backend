import requests

url = 'https://jsonplaceholder.typicode.com/posts'

headers = {'User-Agent': 'MyApp/1.0'}

response_get = requests.get(url, headers=headers)
print("GET Response:", response_get.status_code, response_get.headers, response_get.json())

post_data = {'title': 'New Post', 'body': 'This is the body of the new post.'}

response_post = requests.post(url, json=post_data, headers=headers)
print("\nPOST Response:", response_post.status_code, response_post.json())