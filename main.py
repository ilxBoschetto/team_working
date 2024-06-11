import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time
import laser.define_laser as laser
import peso.peso as peso
import engine.motori as motori
import engine.encoder as encoder
import threading as th
sys.path.append(os.path.abspath("script"))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO_sensor_laser_1 = 22
GPIO_sensor_weight = 4
address_sensore_laser_1 = 0x32
PIN_MOTORE = 18
in1 = 23
in2 = 24
GPIO_ENCODER = 26
frequenza_pwm = 1000

GPIO.setup(PIN_MOTORE, GPIO.OUT)
GPIO.setup(GPIO_ENCODER, GPIO.IN)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
PWM = GPIO.PWM(PIN_MOTORE, frequenza_pwm)
PWM.start(0)
ToF = laser.new_sensor(GPIO_sensor_laser_1,address_sensore_laser_1)

th_read_laser = th.Thread(target=laser.read, args=(ToF, ))
th_read_peso = th.Thread(target=peso.read, args=(GPIO_sensor_weight, ))
th_read_encoder = th.Thread(target=encoder.read, args=(GPIO_ENCODER, ))
# write in global variable
th_read_laser.start()
th_read_peso.start()
th_read_encoder.start()


while True:
    motori.set_direction(1, in1, in2)
    motori.set_engine_speed(PWM, 30)
    print(globals.distance_laser_1)
    #print(globals.weight_sensor_1)
    #print(globals.encoder_value_1)
    #if(globals.encoder_value_1 > 500):
        #motori.stop_engine(PWM)
    time.sleep(0.01)