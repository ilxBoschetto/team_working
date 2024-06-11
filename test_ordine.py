import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time
import laser.define_laser as laser
import peso.peso as peso
import engine.motori as motori
import engine.encoder as encoder
import threading as th
import globals

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO_sensor_laser_1 = 22
GPIO_sensor_weight = 4
address_sensore_laser_1 = 0x32
PIN_MOTORE = 18
in1 = 23
in2 = 24
GPIO_ENCODER = 26
PIN_MOTORE_2 = 8
in3 = 7
in4 = 1
GPIO_ENCODER_2 = 16
frequenza_pwm = 1000

GPIO.setup(PIN_MOTORE, GPIO.OUT)
GPIO.setup(GPIO_ENCODER, GPIO.IN)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(PIN_MOTORE_2, GPIO.OUT)
GPIO.setup(GPIO_ENCODER_2, GPIO.IN)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
PWM = GPIO.PWM(PIN_MOTORE, frequenza_pwm)
PWM.start(0)
PWM_2 = GPIO.PWM(PIN_MOTORE_2, frequenza_pwm)
PWM_2.start(0)
ToF = laser.new_sensor(GPIO_sensor_laser_1,address_sensore_laser_1)

th_read_laser = th.Thread(target=laser.read, args=(ToF, ))
th_read_peso = th.Thread(target=peso.read, args=(GPIO_sensor_weight, ))
th_read_encoder = th.Thread(target=encoder.read, args=(GPIO_ENCODER, ))
th_read_encoder_2 = th.Thread(target=encoder.read, args=(GPIO_ENCODER_2, ))
# write in global variable
th_read_laser.start()
th_read_peso.start()
th_read_encoder.start()
th_read_encoder_2.start()

while globals.encoder_value_1 < 500:
    if(globals.weight_sensor_1 == 1):
        motori.set_direction(1, in1, in2)
        motori.set_engine_speed(PWM, 20)
        motori.set_direction(-1, in3, in4)
        motori.set_engine_speed(PWM_2, 20)
    else:
        motori.stop_engine(PWM)
# arrivato
motori.stop_engine(PWM)
while True:
    if(globals.weight_sensor_1 == 0):
        motori.set_direction(-1, in1, in2)
        motori.set_engine_speed(PWM, 30)
        motori.set_direction(-1, in3, in4)
        motori.set_engine_speed(PWM_2, 30)
    else:
        motori.stop_engine(PWM)
