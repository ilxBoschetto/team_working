import RPi.GPIO as GPIO
import time
import globals

def read(GPIO_PIN):
    GPIO.setup(GPIO_PIN,GPIO.IN)
    while True:
        globals.weight_sensor_1 = GPIO.input(GPIO_PIN)
        time.sleep(0.01)