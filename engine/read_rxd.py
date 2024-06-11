import serial

# Open serial port
ser = serial.Serial(
    port='/dev/ttyS0',  # Replace with your serial port
    baudrate=9600,      # Set baud rate to match your device's specifications
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1           # Timeout in seconds for blocking read
)
print("Reading serial port")
try:
    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting to be read
            data = ser.readline().decode('utf-8').rstrip()  # Read the data and decode it
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("Exiting program")

ser.close()
