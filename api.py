import requests
import json

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTQzN2FlOWYtOGQ5Ni00Y2UwLTkzZjktNTQyZDMyNDNhYzc0IiwidHlwZSI6ImFwaV90b2tlbiJ9.yOuMIUs4Ca0SBVrngCnFJGlYm9s9MVtjtImsdO0UzC8"}

url = "https://api.edenai.run/v2/text/named_entity_recognition"


def ner(text):

    payload = {
        "providers": "google,amazon",
        "language": "en",
        "text" :  text
    }
    response = requests.post(url, json=payload , headers=headers)
    result = json.loads(response.text)

    return result
