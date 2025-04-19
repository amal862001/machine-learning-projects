import requests

url = "http://localhost:5000/classify"
payload = {
    "email_body": """Hello, my name is John Doe, and my email is johndoe@example.com."""
}

response = requests.post(url, json=payload)
print(response.json())