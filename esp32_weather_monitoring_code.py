import network
import time
from umqtt.simple import MQTTClient
import dht
from machine import Pin

# ---------------------------
# USER SETTINGS
# ---------------------------
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASS = ""

AIO_USERNAME = "saiswaroop05" ## Adafruit username
AIO_KEY = "aio_SSUK185R8Cvp8xyekFPjuV6Qf" # adafruit aio key

AIO_FEED_TEMP = AIO_USERNAME + "/feeds/temperature"
AIO_FEED_HUM  = AIO_USERNAME + "/feeds/humidity"

# ---------------------------
# DHT22 SENSOR
# ---------------------------
dht_pin = Pin(15, Pin.IN)
sensor = dht.DHT22(dht_pin)

# ---------------------------
# CONNECT TO WIFI
# ---------------------------
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)

    print("Connecting to WiFi...", end="")
    while not wifi.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print(" Connected!")
    print(wifi.ifconfig())

# ---------------------------
# MQTT CONNECT
# ---------------------------
def connect_mqtt():
    client = MQTTClient(
        client_id="esp32_dht22",
        server="io.adafruit.com",
        user=AIO_USERNAME,
        password=AIO_KEY,
        ssl=False
    )
    client.connect()
    print("Connected to Adafruit IO!")
    return client

# ---------------------------
# MAIN PROGRAM
# ---------------------------
connect_wifi()
mqtt_client = connect_mqtt()

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print("Temp:", temperature, "°C  | Hum:", humidity, "%")

        # Publish to Adafruit IO
        mqtt_client.publish(AIO_FEED_TEMP, str(temperature))
        mqtt_client.publish(AIO_FEED_HUM,  str(humidity))

        print("Published to AIO!")

    except Exception as e:
        print("Sensor error:", e)

    time.sleep(10)   # Read every 5 seconds
