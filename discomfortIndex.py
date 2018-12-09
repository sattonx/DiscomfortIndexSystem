#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import smbus2
import time
import sys
import signal
#from PyQt4 import QtGui
#import display
import led
import th02

led = led.LED()
th02 = th02.TH02()

def exit_handler(siglal, frame):
    #C-c is finish
    print("\nExit")
    time.sleep(0.5)
    led.clear()
    sys.exit(0)

def main():
    #app = QtGui.QApplication(sys.argv)
    signal.signal(signal.SIGINT, exit_handler)
    #d = display.display()
    while True:

        time.sleep(0.1)
        temp = th02.readTemp()
        time.sleep(0.1)
        temp = th02.readTemp()
        #temp = 0
        time.sleep(0.1)
        hum = th02.readHum()
        time.sleep(0.1)
        hum = th02.readHum()
        #print('tempureture: %.2f , humidity: %.2f' % (temp, hum))
        di = th02.outputDI(temp, hum)
        #print('不快指数: %.2f \n' % di)
        if di < 65:
            led.blue()
        elif di < 70:
            led.cyan()
        elif di < 75:
            led.green()
        elif di < 80:
            led.yellow()
        elif di < 85:
            led.magenta()
        elif di < 100:
            led.red()
        else:
            white()
        #d.initUI(temp, hum, di)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
