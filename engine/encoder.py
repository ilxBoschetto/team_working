import RPi.GPIO as GPIO
import time

# GPIO pins connected to encoder outputs
ENCODER_PIN = 0
ENCODER_PIN_2 = 1

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENCODER_PIN, GPIO.IN)
GPIO.setup(ENCODER_PIN_2, GPIO.IN)

# Initialize variables
pulse_count = 0
pulse_count_2 = 0
start_time = time.time()

# Callback function for encoder pin 1
def callback_encoder1(channel):
    global pulse_count
    pulse_count += 1

# Callback function for encoder pin 2
def callback_encoder2(channel):
    global pulse_count_2
    pulse_count_2 += 1

# Add event detection for rising edges on encoder pins
GPIO.add_event_detect(ENCODER_PIN, GPIO.RISING, callback=callback_encoder1)
GPIO.add_event_detect(ENCODER_PIN_2, GPIO.RISING, callback=callback_encoder2)

try:
    while True:
        # Check if 1 seconds has passed
        if time.time() - start_time >= 1:
            # Calculate frequency for encoder pin 1
            frequency = pulse_count
            print("Frequency (Pin 1):", round(frequency, 0), "Hz")

            # Calculate frequency for encoder pin 2
            frequency_2 = pulse_count_2
            print("Frequency (Pin 2):", round(frequency_2, 0), "Hz")

            # Reset variables
            pulse_count = 0
            pulse_count_2 = 0
            start_time = time.time()

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
