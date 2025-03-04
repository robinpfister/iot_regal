from machine import Pin
import time

pin_in = Pin(1, mode=Pin.IN)

while True:
    print(f'RaindropSensor Value: {pin_in.value()}')
    time.sleep(1)