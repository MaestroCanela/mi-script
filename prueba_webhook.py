import requests
import json

# 🚨 PARA PRUEBAS: tu webhook directo (no subir a GitHub así)
url = "https://open.larksuite.com/open-apis/bot/v2/hook/924799cc-88d7-4ad4-994f-b170c0c0f30d"

# Mensaje simple tipo text (para confirmar que funciona)
body = {
    "msg_type": "text",
    "content": {"text": "¡Hola equipo! Esto es una prueba desde Python 🐍"}
}

res = requests.post(url=url, json=body)

print("--- Respuesta del Servidor ---")
print(res.text)
