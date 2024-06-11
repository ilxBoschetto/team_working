import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO_TRIGGER = 17
GPIO_ECHO_SINISTRA = 27



PIN_MOTORE = 18
in1 = 23
in2 = 24
GPIO_ENCODER = 26


GPIO.setup(PIN_MOTORE, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)




GPIO.setup(GPIO_ENCODER, GPIO.IN)
GPIO.setup(GPIO_ECHO_SINISTRA, GPIO.IN)
frequenza_pwm = 1000
PWM = GPIO.PWM(PIN_MOTORE, frequenza_pwm)
PWM.start(0)

distance_cm = 0
previous_value = 0


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
   
    # engine speed 20-100
    if(velocita < 10):
        PWM.ChangeDutyCycle(0)
    else:
        velocita = max(20, min(100, velocita))
        PWM.ChangeDutyCycle(velocita)
    


def stop_engine(GPIO_ENGINE):
    PWM.stop()
   
def ultrasound_distance(GPIO_ULTRASOUND, GPIO_TRIGGER):

    # send the first signal from the sensor

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)


    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ULTRASOUND) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ULTRASOUND) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    print(distance)
    return distance

print("Programma ready!")

try:
    while True:
        dist_SINISTRA = ultrasound_distance(GPIO_ECHO_SINISTRA, GPIO_TRIGGER)
        set_direction(1, in1, in2)
        set_engine_speed(PWM, 10)
        pin_value = GPIO.input(GPIO_ENCODER)
        print(pin_value)
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()