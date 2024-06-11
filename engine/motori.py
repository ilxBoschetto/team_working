import RPi.GPIO as GPIO
import time
import sys
import os
sys.path.append(os.path.abspath("script"))

def set_direction(direction, in1, in2):
   
    # direction 1 -> forwards
    # direction -1 -> backwards
    
    if direction == 1:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    elif direction == -1:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

def set_engine_speed(PWM, velocita):
    velocita = max(20, min(100, velocita))
    PWM.ChangeDutyCycle(velocita)

def stop_engine(PWM):
    PWM.ChangeDutyCycle(0)
    
try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    PIN_MOTORE = 18
    in1 = 21
    in2 = 20

    PIN_MOTORE_2 = 7
    in3 = 14
    in4 = 15
    frequenza_pwm = 1000

    GPIO.setup(PIN_MOTORE, GPIO.OUT)
    #GPIO.setup(GPIO_ENCODER, GPIO.IN)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(PIN_MOTORE_2, GPIO.OUT)
    #GPIO.setup(GPIO_ENCODER, GPIO.IN)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    PWM = GPIO.PWM(PIN_MOTORE, frequenza_pwm)
    PWM_2 = GPIO.PWM(PIN_MOTORE_2, frequenza_pwm)
    PWM.start(0)
    PWM_2.start(0)
    PWM_2.ChangeDutyCycle(100)
    PWM.ChangeDutyCycle(0)
    # direction 1 -> backwards
    # direction -1 -> forwards
    direction = -1
    if direction == 1:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
    elif direction == -1:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
