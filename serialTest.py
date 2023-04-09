import time
import serial

ser = serial.Serial('/dev/serial0', 115200, timeout=0.050)
count = 0