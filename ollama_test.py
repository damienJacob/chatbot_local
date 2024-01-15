import requests
import pprint
import json

# URL de l'API FastAPI
url = "http://127.0.0.1:11434/api/chat"  # Remplacez par l'URL appropriée si votre API est hébergée ailleurs

# Données à envoyer
messages = [
    {
        "role": "user",
        "content": "Bonjour, qui es tu ?"
    }
]

data = {
    "model": "mistral7Binstruct",  # Remplacez par le texte que vous souhaitez traiter
    "messages": messages,
    "stream":False
    }

# En-têtes (headers), si nécessaire
headers = {
    "Content-Type": "application/json"
}

# Effectuer la demande POST
response = requests.post(url, headers=headers,data=json.dumps(data))

# Obtenir la réponse
print(response.json())