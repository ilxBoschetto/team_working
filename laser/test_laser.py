import qwiic_vl53l1x
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
sensor_1_GPIO = 22
sensor_2_GPIO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_1_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.output(sensor_1_GPIO, GPIO.LOW) # xshut of sensor 1 set as 0
GPIO.setup(sensor_2_GPIO, GPIO.OUT) # resets the pin (aka xshut)
GPIO.output(sensor_2_GPIO, GPIO.LOW) # xshut of sensor 2 set as 0

#sets up sensor 1
sensor_1 = qwiic_vl53l1x.QwiicVL53L1X(0x29)

#sets XSHUT HIGH
GPIO.output(sensor_1_GPIO, GPIO.HIGH)

address_sensor_1 = 0x36
sensor_1.set_i2c_address(address_sensor_1)
print(hex(sensor_1.address))

#sets XSHUT HIGH
GPIO.output(sensor_2_GPIO, GPIO.HIGH)

#sets up sensor 2
#sensor_2 = qwiic_vl53l1x.QwiicVL53L1X(0x29)



#address_sensor_2 = 0x38
#sensor_2.set_i2c_address(address_sensor_2)
#print(hex(sensor_2.address))
#
ToF = qwiic_vl53l1x.QwiicVL53L1X(address_sensor_1)
#ToF_2 = qwiic_vl53l1x.QwiicVL53L1X(address_sensor_2)
try:
    ToF.sensor_init()
    #ToF_2.sensor_init()
except Exception as e:
    print("Errore nel collegamento dei sensori -> ",e)

while True:
    try:
        ToF.start_ranging()
        #ToF_2.start_ranging()
        time.sleep(0.01)
        distance1 = ToF.get_distance()
        distance2 = 0 #ToF_2.get_distance()
        time.sleep(0.01)
        ToF.stop_ranging()
        #ToF_2.stop_ranging()
        print("1:       ", distance1, "mm", "       2:     ", distance2, "mm")
        #print(hex(sensor_1.address))
        #print(hex(sensor_2.address))
    except Exception as e:
        print("Errore di lettura : ",e)
