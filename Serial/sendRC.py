##Python code to send Attitude and Throttle Values over serial port
## /dev/ttyACM0 (ArduPilot)

import serial

ser = serial.Serial('/dev/ttyACM0', '57600') ##
