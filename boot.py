from machine import Pin
from blinker import Led
import utime
import network

SSID = ""
SSID_PASSWORD = ""

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSID_PASSWORD)
        while not sta_if.isconnected():
            print("Attempting to connect....")
            utime.sleep(1)
    print('Connected!\nNetwork config:', sta_if.ifconfig())
    

print("Connecting to your wifi...")
do_connect()
led = Led()
led.triple_blink()

