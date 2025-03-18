import machine, onewire, ds18x20, time

# Set up the sensor on GPIO 22 (change as needed)
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Scan for devices on the bus
roms = ds_sensor.scan()
print('Found DS devices:', roms)

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp_c = ds_sensor.read_temp(rom)
        temp_f = temp_c * (9/5) + 32
        print(f'Temperature: {temp_c:.2f}°C / {temp_f:.2f}°F')
    time.sleep(5)
