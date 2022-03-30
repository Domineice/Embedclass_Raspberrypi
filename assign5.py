#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Example for seven segment displays.
"""

import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


buttonPin=5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)

adc =Adafruit_ADS1x15.ADS1115()
GAIN=1

def show_message_vp(device, msg, delay=0.1):
    width = device.width
    padding = " " * width
    msg = padding + msg + padding
    n = len(msg)

    virtual = viewport(device, width=n, height=8)
    sevensegment(virtual).text = msg
    for i in reversed(list(range(n - width))):
        virtual.set_position((i, 0))
        time.sleep(delay)


def show_message_alt(seg, msg, delay=0.1):
    width = seg.device.width
    padding = " " * width
    msg = padding + msg + padding

    for i in range(len(msg)):
        seg.text = msg[i:i + width]
        time.sleep(delay)


def main():
    count = 0
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)
    while True :
        if GPIO.input(buttonPin) == 1:
            count = count + 1
            while True :
                if GPIO.input(buttonPin) == 0:
                    break      
        print(count)
        seg.text = str(count)
        time.sleep(0.02)
        
        
if __name__ == '__main__':
    main()