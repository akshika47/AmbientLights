from flask import Flask, render_template
from paho.mqtt import client
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/button')
def button():
    print("button")
    m = client.Client()
    username = ''
    password = ''
    m.username_pw_set(username, password)
    m.connect(host='io.adafruit.com', port=1883)
    m.loop_start()
    topic = '{}/feeds/onoff'.format(username)
    m.publish(topic, payload="blue")
    return "success"

if __name__ == '__main__':
    app.run()
