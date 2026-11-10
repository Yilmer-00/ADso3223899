import requests
URL = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 2.710,
"longitude": -76.6063,
"current": "temperature_2m,wind_speed_10m",
}

try:
    r = requests.get(URL, params=params, timeout=10)
    r.raise_for_status() # falla si el código no es 2xx
    actual = r.json()["current"]
    print("Temperatura:", actual["temperature_2m"], "°C")
    print("Viento:", actual["wind_speed_10m"], "km/h")
except requests.exceptions.RequestException:
    print("No se pudo consultar el clima")