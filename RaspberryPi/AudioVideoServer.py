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
    command = str(msg.payload)
    
    if(command == "1a"):
        os.system('omxplayer -o hdmi 1.wav')

    if(command == "2a"):
        os.system('omxplayer -o hdmi 2.wav')

    if(command == "3a"):
        os.system('omxplayer -o hdmi 3.wav')

    if(command == "4a"):
        os.system('omxplayer -o hdmi 4.wav')

    if(command == "5a"):
        os.system('omxplayer -o hdmi 5.wav')

    if(command == "6a"):
        os.system('omxplayer -o hdmi 6.wav')

    if(command == "1v"):
        os.system('sudo fbi -T 2 1.png')

    if(command == "2v"):
        os.system('sudo fbi -T 2 2.png')

    if(command == "3v"):
        os.system('sudo fbi -T 2 3.png')

    if(command == "4v"):
        os.system('sudo fbi -T 2 4.png')

    if(command == "5v"):
        os.system('sudo fbi -T 2 5.jpeg')
    
    if(command == "61v"):
        os.system('sudo fbi -T 2 61.png')

    if(command == "62v"):
        os.system('sudo fbi -T 2 62.png')



client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(host=HOST, port=PORT)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()