
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import RPi.GPIO as GPIO
import time
buttonPin=5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(3,GPIO.OUT)


SheetName = "Data logger online"
GSheet_OAUTH_JSON = "dark-mark-345606-fd993ed0e64b.json"
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(GSheet_OAUTH_JSON, scope)
client = gspread.authorize(credentials)
worksheet = client.open(SheetName).sheet1

row = ["Time","Light"]
index = 1
text = ""
worksheet.insert_row(row,index)
prev = 1

while True:
    if GPIO.input(buttonPin) == 0:
        prev = (prev+1)%2
        if prev == 0:
            GPIO.output(3,GPIO.HIGH) #LED_ON
            text = "ON"
        elif prev == 1:
            GPIO.output(3,GPIO.LOW) #LED_OUT
            text = "OFF"
        time.sleep(0.2)
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        try:
            worksheet.update_cell(2,1,timestamp)
            worksheet.update_cell(2,2,text)
        except Exception as ex:
            print("Google sheet login failed with error:",ex)
        time.sleep(0.2)
