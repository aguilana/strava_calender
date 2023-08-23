import requests
from stravaio import strava_oauth2, StravaIO
import os
from dotenv import load_dotenv

load_dotenv()

STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

strava_oauth2(
    client_id=STRAVA_CLIENT_ID,
    client_secret=STRAVA_CLIENT_SECRET,
)

headers = {"Authorization": f"Bearer {STRAVA_ACCESS_TOKEN}"}

response = requests.get(
    "https://www.strava.com/api/v3/athlete/activities", headers=headers
)

print(response.status_code)
print(response.json())
