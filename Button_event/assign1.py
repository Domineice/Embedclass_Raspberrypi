import RPi.GPIO as GPIO
import time
buttonPin=5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while True:
	if GPIO.input(buttonPin) == 0:
		for i in range(3):
	        	GPIO.output(3,GPIO.HIGH) #LED_ON
            		time.sleep(1)
            		GPIO.output(3,GPIO.LOW) #LED_OUT
            		time.sleep(1)
