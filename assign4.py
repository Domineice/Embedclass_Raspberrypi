import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
GPIO.setmode(GPIO.BOARD)


adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,100)
p.start(0)

while True:
    value =adc.read_adc(0,gain=GAIN)
    if value <0:
        value = 0
    elif value > 25000:
        value =25000
    normalize_value = (value*100)/(25000)
    print(value)
    #print(normalize_value)
    p.ChangeDutyCycle(normalize_value)
    time.sleep(0.05)

