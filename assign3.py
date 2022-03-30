import RPi.GPIO as GPIO
import time
#6213129 Posawat Tangon
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
btnpin=5
prev=0
GPIO.setup(3,GPIO.OUT)
GPIO.setup(btnpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def button_press(channel):
    print("Press")
    global prev
    if prev == 0:
        GPIO.output(3,GPIO.HIGH)
        time.sleep(0.1)
        prev=1
    elif prev ==1:
        GPIO.output(3,GPIO.LOW)
        time.sleep(0.1)
        prev=0
GPIO.add_event_detect(btnpin,GPIO.FALLING,callback=button_press,bouncetime = 200)

try:
    message = input("Enter to quit")
    GPIO.cleanup()
except:
    print("End")
