import os
import requests
import json

# Obtener webhook desde variable de entorno
url = os.environ.get("LARK_WEBHOOK_URL")

if not url:
    raise ValueError("No se encontró la variable de entorno LARK_WEBHOOK_URL")

card_json = r'''
{
  "config": {
    "wide_screen_mode": true
  },
  "header": {
    "template": "grey",
    "title": {
      "content": "📚Resultados KoM W38 (09/20 - 09/26)",
      "tag": "plain_text"
    }
  },
  "elements": [
    {
      "tag": "img",
      "img_key": "img_v3_02qr_429b119c-ef4c-4b65-9d56-449ed290f55h",
      "alt": {
        "tag": "plain_text",
        "content": ""
      },
      "mode": "fit_horizontal",
      "preview": true
    },
    {
      "tag": "div",
      "text": {
        "content": "**<at id=all></at> Buenas tardes equipo, queremos compartir con ustedes los resultados de KOM a nivel MARKET, con el objetivo de que podamos visualizar juntos cómo vamos avanzando de manera general:🎉**\n",
        "tag": "lark_md"
      }
    },
    {
      "tag": "hr"
    },
    {
      "tag": "column_set",
      "flex_mode": "stretch",
      "background_style": "default",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 2,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**KoM W38 LATAM: 89.51%**🎯 \n<font color='grey'>Si bien es cierto no llegamos al target nos quedamos muy cerca, con un 89.51% el cual demuestra que podemos llegar si nos lo proponemos, estamos mejorando mucho, subimos un 0.51% a comparacion de la semana pasada🥇</font>",
              "text_align": "center"
            },
            {
              "tag": "column_set",
              "flex_mode": "none",
              "background_style": "grey",
              "columns": [
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='green'> 91%</font>**\n<font color='black'> TARGET KoM</font>",
                      "text_align": "center"
                    }
                  ]
                },
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='red'> 89.51%</font>**\n<font color='black'> Resultado W38</font>",
                      "text_align": "center"
                    }
                  ]
                },
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='red'> - 1.49%</font>**\n<font color='black'> Diferencia</font>",
                      "text_align": "center"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "tag": "hr"
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "default",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 2,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**KoM W38 BR: 89.56%**🎯 \n<font color='grey'>Si bien es cierto no llegamos al target nos quedamos muy cerca, con un 89.56% el cual demuestra que podemos llegar si nos lo proponemos, estamos mejorando mucho, subimos un 4.45% a comparacion de la semana pasada🥇</font>",
              "text_align": "center"
            },
            {
              "tag": "column_set",
              "flex_mode": "none",
              "background_style": "grey",
              "columns": [
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='green'> 91%</font>**\n<font color='black'> TARGET KoM</font>",
                      "text_align": "center"
                    }
                  ]
                },
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='red'> 89.56%</font>**\n<font color='black'> Resultado W38</font>",
                      "text_align": "center"
                    }
                  ]
                },
                {
                  "tag": "column",
                  "width": "weighted",
                  "weight": 1,
                  "vertical_align": "top",
                  "elements": [
                    {
                      "tag": "markdown",
                      "content": "**<font color='red'> - 1.43%</font>**\n<font color='black'> Diferencia</font>",
                      "text_align": "center"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "tag": "note",
      "elements": [
        {
          "tag": "img",
          "img_key": "img_v2_0696adfa-962f-4835-9b1c-0311f48d6dah",
          "alt": {
            "tag": "plain_text",
            "content": ""
          }
        },
        {
          "tag": "plain_text",
          "content": "Estamos muy cerca del objetivo! vamos equipo!"
        }
      ]
    },
    {
      "tag": "img",
      "img_key": "img_v3_02qr_6c03bb83-5888-415e-a491-6fd6a22c110h",
      "alt": {
        "tag": "plain_text",
        "content": ""
      },
      "mode": "fit_horizontal",
      "preview": true
    }
  ]
}
'''

body_data = {"msg_type": "interactive", "card": json.loads(card_json)}
body = json.dumps(body_data)

headers = {"Content-Type": "application/json"}

print(f"Enviando tarjeta al webhook: {url}")
res = requests.post(url=url, data=body, headers=headers)

print("\n--- Respuesta del Servidor ---")
print("Cuerpo de la Solicitud Enviada:", res.request.body)
print("Respuesta del Servidor:", res.text)
print("----------------------------")
