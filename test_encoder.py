import RPi.GPIO as GPIO
import time

GPIO_ENCODER = 26
# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ENCODER, GPIO.IN)

try:
    while True:
        # Read the value of the GPIO pin
        pin_value = GPIO.input(GPIO_ENCODER)
        print("GPIO value:", pin_value)

        time.sleep(0.001)

except KeyboardInterrupt:
    # Clean up GPIO settings on interrupt
    GPIO.cleanup()
