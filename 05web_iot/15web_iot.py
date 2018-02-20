from flask import Flask, request, redirect
from flask_socketio import SocketIO, send
import RPi.GPIO as GPIO
import Adafruit_DHT, json, time
import threading
import sys



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app,async_mode='threading')

GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11

pin_dht11 = 18
pin_led = 23
pin_btn = 24

GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

@app.route('/')
def main():
    return redirect('/static/gpio.html')

@app.route('/monitor')
def monitoring():
    try:
        print('/monitor')
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
        obj = {'humi' : humidity, 'temp' : temperature}
        return json.dumps(obj)
    except Exception as e:
        print('err', e)

@app.route('/operate/<cmd>')
def op(cmd):
    val = request.values['val']   
    if cmd == "led":
        val = request.values['val']   
        print('/operate/', cmd, val) 
        if val == 'on':
            GPIO.output(pin_led, True)
            print(pin_led, 'on')
        elif val == 'off':
            GPIO.output(pin_led, False)
        return 'OK'

@socketio.on('connect')
def connect():
    send({'data': 'welcom'})


class BtnThread(threading.Thread):
    flag = True
    
    def run(self):
            val = -1
            while True :
                if not self.flag:
                    print('Btn thead killed')
                    break
                read = GPIO.input(pin_btn)
                if val != read:
                    print(val, read)
                    val = read
                    
                    if val == 1:
                        socketio.send( {'data': '1' })
                    else:
                        socketio.send({'data': '0'})
                        print('btn pressed', 0)
                time.sleep(0.1)

if __name__ == '__main__':
    try:
        th = BtnThread()
        th.start()
        socketio.run(app, host='0.0.0.0')
    finally:
        print('cleaning up')
        th.flag = False
        GPIO.cleanup()
