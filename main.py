import requests
from datetime import datetime
import smtplib
import time

# Replace with your own info
MY_LAT = 00.0000  # Your latitude
MY_LONG = 00.0000  # Your longitude
MY_EMAIL = "you@example.com"
TO_EMAIL = "to@example.com"
MY_PASSWORD = "your-email-password"

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # Check if ISS is within +/- 5 degrees of your location
    return (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_long <= (MY_LONG + 5)

def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour

    return time_now >= sunset or time_now <= sunrise

# Check every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:Look Up! 👨‍🚀\n\nThe ISS is above you in the sky!"
            )
