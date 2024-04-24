import requests

# The API endpoint
# url = "https://jsonplaceholder.typicode.com/posts/1"
url = "Taken above is fake u can enter the user request "

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)