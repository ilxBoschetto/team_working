import RPi.GPIO as GPIO
import time
import globals

def read(GPIO_ENCODER):
    try:
        while True:
            current_value = GPIO.input(GPIO_ENCODER)
            if current_value != globals.encoder_value_1:
                globals.encoder_value_1 += 1
            time.sleep(0.01)

    except Exception as e:
            print("Error : ",e)
