from machine import Pin, Timer
from umqtt.simple import MQTTClient
from blinker import Led
import dht
import time
import ujson

MQTT_BROKER = ''
CLIENT_ID = ''
PUBLISH_TOPIC = ''

def connect():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, 1883)
    try:
        print(f'Connecting to {MQTT_BROKER}')
        client.connect()
    except OSError:
        return(False)
    return client
    

sensor = dht.DHT22(Pin(13))
led = Led()  


while True:
    try:
        sensor.measure()
        data = {"t": sensor.temperature(), "h": sensor.humidity()}
        client = connect()
        while not client:
            led.on()
            print('Failed to connect. Retry in 5s...')
            time.sleep(5)
            client = connect()
        led.five_blinks()
        print('Connection successful!')         
        client.publish(PUBLISH_TOPIC, ujson.dumps(data).encode())
        print(data)
        client.disconnect()
        
        led.signal(60, 0.25)
        
    except OSError as e:
        print("Failed reception")
