#!/usr/bin/env
############################################
# gpio_1.py
# Author: Paul Yang
# Date: June, 2016
# Brief:
############################################



import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup() 
GPIO.setmode(GPIO.BOARD)
class RPI_LED_P:
    def __init__(self,pin):
        GPIO.setup(pin,GPIO.OUT)
        self.led = GPIO.PWM(pin, 100)
        self.led.start(0)
    def on(self):
         self.led.ChangeDutyCycle(100)
    def off(self):
         self.led.ChangeDutyCycle(0)
    def blinking(self):
        self.on()
        sleep(0.4)
        self.off()
    def adjust_brightness(self,value):
        self.led.ChangeDutyCycle(value)
        sleep(0.02)
        
        
led_01 = RPI_LED_P(15)
led_01.adjust_brightness(20)
led_01.off()
led_01.on()
led_01.blinking()