import requests

url = input("URL: ")
response = requests.get(url)

try:
    server = response.headers["Server"]
    print(f"Server: {server}")
except KeyError:
    print("Error")
