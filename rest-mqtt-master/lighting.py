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


@app.route('/lights/1/on', methods=['POST'])
def light1on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="1on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/1/off', methods=['POST'])
def light1off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="1off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/2/on', methods=['POST'])
def light2on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="2on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/2/off', methods=['POST'])
def light2off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="2off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/3/on', methods=['POST'])
def light3on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="3on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/3/off', methods=['POST'])
def light3off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="3off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/4/on', methods=['POST'])
def light4on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="4on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/4/off', methods=['POST'])
def light4off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="4off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/5/on', methods=['POST'])
def light5on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="5on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/5/off', methods=['POST'])
def light5off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="5off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/6/on', methods=['POST'])
def light6on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="6on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/6/off', methods=['POST'])
def light6off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="6off")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/7/on', methods=['POST'])
def light7on():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="7on")
        print(topic)
        return {'hello': 'world'}


@app.route('/lights/7/off', methods=['POST'])
def light7off():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="7off")
        print(topic)
        return {'hello': 'world'}


@app.route('/video/1/play', methods=['POST'])
def videoplay1():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="1v")
        print(topic)
        return {'hello': 'world'}


@app.route('/audio/1/play', methods=['POST'])
def audioplay1():
    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="1a")
        print(topic)
        return {'hello': 'world'}


@app.route('/video/2/play', methods=['POST'])
def videoplay2():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="2v")
        print(topic)
        return {'hello': 'world'}


@app.route('/audio/2/play', methods=['POST'])
def audioplay2():
    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="2a")
        print(topic)
        return {'hello': 'world'}


@app.route('/video/3/play', methods=['POST'])
def videoplay3():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="3v")
        print(topic)
        return {'hello': 'world'}


@app.route('/audio/3/play', methods=['POST'])
def audioplay3():
    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="3a")
        print(topic)
        return {'hello': 'world'}


@app.route('/video/4/play', methods=['POST'])
def videoplay4():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="4v")
        print(topic)
        return {'hello': 'world'}


@app.route('/audio/4/play', methods=['POST'])
def audioplay4():
    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="4a")
        print(topic)
        return {'hello': 'world'}


@app.route('/video/5/play', methods=['POST'])
def videoplay5():

    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="5v")
        print(topic)
        return {'hello': 'world'}


@app.route('/audio/5/play', methods=['POST'])
def audioplay5():
    if request.method == 'POST':
        topic = '{}/feeds/onoff'.format(USERNAME)
        client.publish(topic, payload="5a")
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