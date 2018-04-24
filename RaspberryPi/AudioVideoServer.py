import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

HOST = 'io.adafruit.com'
PORT = 1883
USERNAME = ''
PASSWORD = ''


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("akshika47/feeds/onoff")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    command = str(msg.payload);
    
    if(command == "1a")
    	os.system('omxplayer -o hdmi 1.mp3')

    if(command == "2a")
    	os.system('omxplayer -o hdmi 2.mp3')

    if(command == "3a")
    	os.system('omxplayer -o hdmi 3.mp3')

    if(command == "4a")
    	os.system('omxplayer -o hdmi 4.mp3')

    if(command == "5a")
    	os.system('omxplayer -o hdmi 5.mp3')

    if(command == "1v")
    	os.system('omxplayer -o hdmi 1.MP4')

    if(command == "2v")
    	os.system('omxplayer -o hdmi 2.MP4')

    if(command == "3v")
    	os.system('omxplayer -o hdmi 3.MP4')

    if(command == "4v")
    	os.system('omxplayer -o hdmi 4.MP4')

    if(command == "5v")
    	os.system('omxplayer -o hdmi 5.MP4')

 
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