import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
sensor_1_GPIO = 22
sensor_2_GPIO = 10
sensor_3_GPIO = 9
sensor_4_GPIO = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_1_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.setup(sensor_2_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.setup(sensor_3_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.setup(sensor_4_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.output(sensor_1_GPIO, GPIO.LOW) # xshut of sensor 1 set as 0
GPIO.output(sensor_2_GPIO, GPIO.LOW) # xshut of sensor 2 set as 0
GPIO.output(sensor_3_GPIO, GPIO.LOW) # xshut of sensor 3 set as 0
GPIO.output(sensor_4_GPIO, GPIO.LOW) # xshut of sensor 4 set as 0

GPIO.output(sensor_1_GPIO, GPIO.HIGH)
sensor = qwiic_vl53l1x.QwiicVL53L1X()
sensor.set_i2c_address(0x35)
time.sleep(0.1)

GPIO.output(sensor_2_GPIO, GPIO.HIGH)
sensor_2 = qwiic_vl53l1x.QwiicVL53L1X()
sensor_2.set_i2c_address(0x38)
time.sleep(0.1)

GPIO.output(sensor_3_GPIO, GPIO.HIGH)
sensor_3 = qwiic_vl53l1x.QwiicVL53L1X()
sensor_3.set_i2c_address(0x41)
time.sleep(0.1)

GPIO.output(sensor_4_GPIO, GPIO.HIGH)
sensor_4 = qwiic_vl53l1x.QwiicVL53L1X()
sensor_4.set_i2c_address(0x44)