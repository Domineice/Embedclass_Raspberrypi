#6213129 Posawat Tangon
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

import lcddriver
import time
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
GPIO.setmode(GPIO.BOARD)
adc =Adafruit_ADS1x15.ADS1115()
GAIN=1
lcd = lcddriver.lcd()
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)
while True :
    lcd.lcd_clear()
    value =adc.read_adc(0,gain=GAIN)
    if value < 0 :
        value = 0
    print(value)
    seg.text = str(value)
    if value < 10000 :
        lcd.lcd_display_string("Low !!!",1)
    elif value > 25000 :
        lcd.lcd_display_string("High !!!",1)
    else:
        lcd.lcd_display_string("Medium !!!",1)
    time.sleep(1)