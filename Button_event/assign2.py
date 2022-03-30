import RPi.GPIO as GPIO
import time
buttonPin=5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
count=0
GPIO.output(3,GPIO.LOW)
while True:
    for i in range(3):
        
        if GPIO.input(buttonPin)==0:
            print(count)
            if count == 3 :
                GPIO.output(3,GPIO.HIGH)
            while True:
                if GPIO.input(buttonPin)==1:
                    if count == 3 :
                        GPIO.output(3,GPIO.LOW)
                        count =0
                    else:
                        count = count + 1
                    break
