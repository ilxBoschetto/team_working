import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIN = 15

# Set the GPIO pin as an input
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        # Read the state of the GPIO pin
        pin_state = GPIO.input(GPIO_PIN)
        print(f"GPIO 15 state: {pin_state}")
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up the GPIO pins on interrupt
    GPIO.cleanup()
