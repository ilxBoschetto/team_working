import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER_1 = 27
GPIO_ECHO_1 = 9
GPIO_TRIGGER_2 = 22
GPIO_ECHO_2 = 25
GPIO_TRIGGER_3 = 10
GPIO_ECHO_3 = 11
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_3, GPIO.OUT)
GPIO.setup(GPIO_ECHO_3, GPIO.IN)

def read_global_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_global_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def update_sensor_values(lines, distance1, distance2):
    found_distance1 = False
    found_distance2 = False
    
    for i in range(len(lines)):
        if "distance_ultrasound_1" in lines[i]:
            lines[i] = f"distance_ultrasound_1 = {round(distance1)}\n"
            found_distance1 = True
        elif "distance_ultrasound_2" in lines[i]:
            lines[i] = f"distance_ultrasound_2 = {round(distance2)}\n"
            found_distance2 = True
    
    if not found_distance1:
        lines.append(f"distance_ultrasound_1 = {round(distance1)}\n")
    if not found_distance2:
        lines.append(f"distance_ultrasound_2 = {round(distance2)}\n")
    return lines

def get_distance(GPIO_TRIGGER, GPIO_ECHO):
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime_SINISTRA = time.time()
    StopTime_SINISTRA = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime_SINISTRA = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime_SINISTRA = time.time()
    TimeElapsed = StopTime_SINISTRA - StartTime_SINISTRA
    distance = (TimeElapsed * 34300) / 2
    return distance
print('program started')
while True:
    try:

        dist_1 = get_distance(GPIO_TRIGGER_1, GPIO_ECHO_1)
        dist_2 = get_distance(GPIO_TRIGGER_2, GPIO_ECHO_2)
        file_path = '/script/globals.py'
        lines = read_global_file(file_path)
        updated_lines = update_sensor_values(lines, dist_1, dist_2)
        write_global_file(file_path, updated_lines)
        time.sleep(0.1)
    except Exception as e:
        print("Errore di lettura: ", e)