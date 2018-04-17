from flask_api import FlaskAPI
from flask import request
from paho.mqtt import client
import logging
import sys

HOST = 'io.adafruit.com'
PORT = 1883
USERNAME = ''
PASSWORD = ''

logger = logging.getLogger(__name__)
client = client.Client()
app = FlaskAPI(__name__)


@app.route('/lights/off', methods=['POST'])
def lightblue():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/on', methods=['POST'])
def lightgreen():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="on")
        print(topic)
        return {'hello': 'world'}


if __name__ == '__main__':

    if USERNAME == '' or PASSWORD == '':
        logger.error("No MQTT username or password set.")
        sys.exit(-1)

    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(host=HOST, port=PORT)
    client.loop_start()
    app.run()