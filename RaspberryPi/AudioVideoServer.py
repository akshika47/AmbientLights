import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

HOST = 'io.adafruit.com'
PORT = 1883
USERNAME = 'akshika47'
PASSWORD = '95c18e999ffc4bf79c62ef42c812fcc7'


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("akshika47/feeds/onoff")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    os.system('omxplayer -o hdmi 1.MP4')



client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(host=HOST, port=PORT)
client.on_connect = on_connect
client.on_message = on_message


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()