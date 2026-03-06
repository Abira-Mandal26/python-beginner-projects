import requests

api_key = "16cb90d4b6492ad502214b44d8b5705f"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

# check if API returned success
if data.get("cod") == 200:
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", data["message"])