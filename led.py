# -*- coding: utf-8 -*-
import pigpio
import time

class LED:
    GPIO_R = 5 
    GPIO_G = 26
    GPIO_B = 13
    
    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_mode(self.GPIO_R, pigpio.OUTPUT)
        self.pi.set_mode(self.GPIO_G, pigpio.OUTPUT)
        self.pi.set_mode(self.GPIO_B, pigpio.OUTPUT)
    def red(self):
        self.pi.write(self.GPIO_R, 1)
        self.pi.write(self.GPIO_G, 0)
        self.pi.write(self.GPIO_B, 0)
 
    def green(self):
        self.pi.write(self.GPIO_R, 0)
        self.pi.write(self.GPIO_G, 1)
        self.pi.write(self.GPIO_B, 0)

    def blue(self):
        self.pi.write(self.GPIO_R, 0)
        self.pi.write(self.GPIO_G, 0)
        self.pi.write(self.GPIO_B, 1)
  
    def magenta(self):
        self.pi.write(self.GPIO_R, 1)
        self.pi.write(self.GPIO_G, 0)
        self.pi.write(self.GPIO_B, 1)
 
    def cyan(self):
        self.pi.write(self.GPIO_R, 0)
        self.pi.write(self.GPIO_G, 1)
        self.pi.write(self.GPIO_B, 1)

    def yellow(self):
        self.pi.write(self.GPIO_R, 1)
        self.pi.write(self.GPIO_G, 1)
        self.pi.write(self.GPIO_B, 0)

    def white(self):
        self.pi.write(self.GPIO_R, 1)
        self.pi.write(self.GPIO_G, 1)
        self.pi.write(self.GPIO_B, 1)

    def clear(self):
        self.pi.write(self.GPIO_R, 0)
        self.pi.write(self.GPIO_G, 0)
        self.pi.write(self.GPIO_B, 0)
 
def main():
    led = LED()
    time.sleep(0.2)
    for i in range(5):
        led.red()
        time.sleep(1.0)
        led.green()
        time.sleep(1.0)
        led.blue()
        time.sleep(1.0)
        led.magenta()
        time.sleep(1.0)
        led.cyan()
        time.sleep(1.0)
        led.yellow()
        time.sleep(1.0)

    led.clear()
if __name__ == '__main__':
    main()
