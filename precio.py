import requests

# Consultamos el precio de Bitcoin usando la API de CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    # Hacemos la petición a internet
    respuesta = requests.get(url)
    
    # Convertimos la respuesta en un formato que Python entienda (JSON)
    datos = respuesta.json()
    
    # Extraemos el precio
    precio = datos["bitcoin"]["usd"]
    
    print("-" * 40)
    print(f"🚀 ¡Conexión exitosa!")
    print(f"💰 El precio actual de Bitcoin es: ${precio:,.2f} USD")
    print("-" * 40)

except Exception as e:
    print(f"❌ Hubo un problema al conectar: {e}")
