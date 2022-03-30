#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Example for seven segment displays.
"""

import time
import Adafruit_ADS1x15
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


adc =Adafruit_ADS1x15.ADS1115()
GAIN=1

def date(seg):
    now = datetime.now()
    seg.text = now.strftime("%y-%m-%d")


def clock(seg, seconds):
    interval = 0.5
    for i in range(int(seconds / interval)):
        now = datetime.now()
        seg.text = now.strftime("%H-%M-%S")

        if i % 2 == 0:
            seg.text = now.strftime("%H-%M-%S")
        else:
            seg.text = now.strftime("%H %M %S")

        time.sleep(interval)


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
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)
    while True :
        now = datetime.now()
        dt_string = now.strftime("  %H.%M.%S")
        print("date and time =", dt_string)
        seg.text = dt_string
        time.sleep(1)
        
if __name__ == '__main__':
    main()