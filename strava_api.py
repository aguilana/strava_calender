from stravaio import strava_oauth2, StravaIO
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_and_store_access_token():
    STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
    STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

    strava_oauth2(
        client_id=STRAVA_CLIENT_ID,
        client_secret=STRAVA_CLIENT_SECRET,
    )


def get_strava_data():
    STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")

    if not STRAVA_ACCESS_TOKEN:
        print("Fetching access token...")
        fetch_and_store_access_token()
        print("Access token fetched!")

    strava = StravaIO(access_token=STRAVA_ACCESS_TOKEN)

    # Fetch activities (runs) for the year 2020
    activities = strava.get_logged_in_athlete_activities()

    # Filter activities to get runs from the year 2020
    runs_2020 = [
        activity
        for activity in activities
        if activity.type == "Run" and activity.start_date_local.startswith("2020")
    ]

    return runs_2020
