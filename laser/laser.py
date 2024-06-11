import qwiic_vl53l1x
import time

def read_global_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_global_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def update_sensor_values(lines, distance1, distance2):
    # Track whether the lines are found
    found_distance1 = False
    found_distance2 = False
    
    for i in range(len(lines)):
        if "distance_laser_1" in lines[i]:
            lines[i] = f"distance_laser_1 = {round(distance1)}\n"
            found_distance1 = True
        elif "distance_laser_2" in lines[i]:
            lines[i] = f"distance_laser_2 = {round(distance2)}\n"
            found_distance2 = True
    
    # Append the lines if they were not found
    if not found_distance1:
        lines.append(f"distance_laser_1 = {round(distance1)}\n")
    if not found_distance2:
        lines.append(f"distance_laser_2 = {round(distance2)}\n")
    
    return lines

ToF = qwiic_vl53l1x.QwiicVL53L1X(0x35)
ToF2 = qwiic_vl53l1x.QwiicVL53L1X(0x38)
#ToF3 = qwiic_vl53l1x.QwiicVL53L1X(0x41)
#ToF4 = qwiic_vl53l1x.QwiicVL53L1X(0x44)

try:
    ToF.sensor_init()
    ToF2.sensor_init()
    #ToF3.sensor_init()
    #ToF4.sensor_init()
except Exception as e:
    print("Errore nel collegamento dei sensori -> ", e)

print('program started')
while True:
    try:
        ToF.start_ranging()
        ToF2.start_ranging()
        #ToF3.start_ranging()
        #ToF4.start_ranging()

        distance1 = ToF.get_distance()
        distance2 = ToF2.get_distance()
        #distance3 = ToF3.get_distance()
        #distance4 = ToF4.get_distance()

        file_path = '/script/globals.py'
        lines = read_global_file(file_path)
        updated_lines = update_sensor_values(lines, distance1, distance2)
        write_global_file(file_path, updated_lines)
        
        time.sleep(0.1)
        
        ToF.stop_ranging()
        ToF2.stop_ranging()
        #ToF3.stop_ranging()
        #ToF4.stop_ranging()
    except Exception as e:
        print("Errore di lettura: ", e)
        time.sleep(0.1)
