import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time
import globals


def new_sensor(GPIO_PIN, address):
    try:
        GPIO.setup(GPIO_PIN, GPIO.OUT) # resets the pin (aka xshut)
        GPIO.output(GPIO_PIN, GPIO.LOW) # xshut of sensor 1 set as 0

        #sets up sensor 1
        sensor_1 = qwiic_vl53l1x.QwiicVL53L1X(0x29)

        #sets XSHUT HIGH
        GPIO.output(GPIO_PIN, GPIO.HIGH)

        sensor_1.set_i2c_address(address)
        ToF = qwiic_vl53l1x.QwiicVL53L1X(address)
        ToF.sensor_init()
        return ToF
    except Exception as e:
        print("Error : ",e)

def read(ToF):
    while True:
        try:
            ToF.start_ranging()
            time.sleep(0.01)
            globals.distance_laser_1 = ToF.get_distance()
            time.sleep(0.01)
            ToF.stop_ranging()
        except Exception as e:
            print("",e)