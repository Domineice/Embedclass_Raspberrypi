from flask import Flask,render_template,jsonify,request
import datetime
import RPi.GPIO as GPIO
#6213129 Posawat Tangon
import Adafruit_ADS1x15

app = Flask(__name__)
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
normal = 0
prev = 0
@app.route('/')
def index():
    print("Startweb")
    return render_template('index.html')


@app.route('/<action>')
def Control(action):
    print("Control")
    global normal
    global prev
    if prev == 1:
        normal = 0
        prev = 0
        print("Normal")
    elif prev == 0:
        normal = 1
        prev = 1
        print("Not normal")
    return jsonify(status = action)
        
@app.route('/sensorup')
def updateSensor():
    global normal
    adc = Adafruit_ADS1x15.ADS1115()
    print("Update sensor")
    value =adc.read_adc(0,gain=1)
    print("Value = "+str(value))
    if value < 0 :
        value = 0
    elif value > 25000:
        value = 25000
        
    if normal ==1:
        value = normalize(value)
        strval = '<0 - 100>' + str(value)
    else:
        strval = '<0 - 25000>' + str(value)
    return jsonify(sensorupdate=strval)
    
def normalize(x):
    return (x*100)/25000

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    app.run(debug=True,host='0.0.0.0',port = 80)