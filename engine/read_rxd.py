import serial
import sys
import time

def open_serial_port(port, baudrate):
    while True:
        try:
            ser = serial.Serial(
                port=port,
                baudrate=baudrate,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
            print(f"Opened serial port {port} at {baudrate} baud")
            return ser
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

def update_file(motor, value):
    filename = '/script/globals.py'
    motor_frequency_line = f"MOTOR_{motor}_FREQUENCY = {value}\n"
    
    # Read the file and update the relevant line if it exists
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    # Check if the line already exists
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f"MOTOR_{motor}_FREQUENCY"):
            lines[i] = motor_frequency_line
            updated = True
            break
    
    # If the line does not exist, add it to the lines
    if not updated:
        lines.append(motor_frequency_line)

    # Write the updated lines back to the file
    with open(filename, 'w') as f:
        f.writelines(lines)

def process_data(data):
    if data.startswith("1_"):
        value = data.split('_')[1]
        update_file(1, value)
    elif data.startswith("2_"):
        value = data.split('_')[1]
        update_file(2, value)

# Open serial port
ser = open_serial_port('/dev/ttyS0', 9600)  # Replace with your serial port

print("Reading serial port")
try:
    while True:
        try:
            if ser.in_waiting > 0:  # Check if there is data waiting to be read
                data = ser.readline().decode('utf-8').rstrip()  # Read the data and decode it
                if(data != ""):
                    process_data(data)
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            time.sleep(1)  # Sleep to avoid hammering the port in case of an error
        except OSError as e:
            ser.close()  # Close the port
            ser = open_serial_port('/dev/ttyS0', 9600)  # Attempt to reopen the port
except KeyboardInterrupt:
    print("Exiting program")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed")
