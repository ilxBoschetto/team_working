
import time

while True:
    text_file = open('/script/globals.py','r')
    text = text_file.read().splitlines()
    for line in text:
        if 'distance_laser_1' in line:
            print(line)
        elif 'distance_laser_2' in line:
            print(line)
        elif 'distance_ultrasound_1' in line:
            print(line)
        elif 'distance_ultrasound_2' in line:
            print(line)
        print('')
    text_file.close()
    time.sleep(1)
