import Adafruit_ADS1x15

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


SheetName = "Data logger online"
GSheet_OAUTH_JSON = "dark-mark-345606-fd993ed0e64b.json"
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(GSheet_OAUTH_JSON, scope)
client = gspread.authorize(credentials)
worksheet = client.open(SheetName).sheet1


import RPi.GPIO as GPIO
btnpin=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

worksheet.clear()
print("ready")
row = ["Time","Value","Status"]
index = 1
text = ""
worksheet.insert_row(row,index)

adc =Adafruit_ADS1x15.ADS1115()
GAIN=1

GPIO.setup(btnpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def button_press(channel):
    print("Press")
    worksheet.clear()
    worksheet.insert_row(row,index)
    
GPIO.add_event_detect(btnpin,GPIO.FALLING,callback=button_press,bouncetime = 1)


while True :
    value =adc.read_adc(0,gain=GAIN)
    if value < 0 :
        value = 0
    print(value)
    if value < 10000 :
        text = "Low"
    elif value > 25000 :
        text = "High"
    else:
        text = "Medium"
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    try:
        worksheet.append_row([timestamp, value,text])
    except Exception as ex:
        print("Google sheet login failed with error:",ex)
    time.sleep(2)