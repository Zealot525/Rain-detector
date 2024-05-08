import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("API_KEY")
sending_phone = os.environ.get("SENDING_PHONE")
receiving_phone = os.environ.get("RECEIVING_PHONE")
latitude = os.environ.get("LATITUDE")
longitude = os.environ.get("LONGITUDE")

ids = []
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric",
    "cnt": 7
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()


is_rain = False
for hour_data in weather_data["list"]:
    ids = hour_data["weather"][0]["id"]
    if ids <= 600:
        is_rain = True

if is_rain:
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body="It's going to rain today! Remember to bring an ☂️!",
    from_=f"{sending_phone}",
    to= f"{receiving_phone}"
    )

    print(message.status)