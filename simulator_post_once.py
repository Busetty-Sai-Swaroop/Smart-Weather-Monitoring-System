# simulator_post_once.py
# pip install requests
import os, random, requests, sys
from datetime import datetime

THINGSPEAK_WRITE_KEY = os.environ.get("THINGSPEAK_WRITE_KEY")
THINGSPEAK_UPDATE_URL = "https://api.thingspeak.com/update.json"
TEMP_MIN = 18.0
TEMP_MAX = 42.0
HUM_MIN = 20.0
HUM_MAX = 90.0

if not THINGSPEAK_WRITE_KEY:
    print("ERROR: THINGSPEAK_WRITE_KEY not set")
    sys.exit(1)

def generate_reading():
    temp = round(random.uniform(TEMP_MIN, TEMP_MAX), 2)
    hum = round(random.uniform(HUM_MIN, HUM_MAX), 2)
    return temp, hum

def post(temp, hum):
    payload = {"api_key": THINGSPEAK_WRITE_KEY, "field1": temp, "field2": hum}
    r = requests.post(THINGSPEAK_UPDATE_URL, data=payload, timeout=10)
    print(f"[{datetime.now().isoformat()}] POST status {r.status_code}, resp: {r.text}")
    return r.status_code == 200

if __name__ == "__main__":
    temp, hum = generate_reading()
    print(f"Generated -> temp: {temp}°C, hum: {hum}%")
    success = post(temp, hum)
    if not success:
        sys.exit(2)
