import machine
import time
import onewire, ds18x20

# the device is on GPIO12
dat = machine.Pin(12)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()




pin_D0 = machine.Pin(16, machine.Pin.OUT)
pin_D1 = machine.Pin(5,machine.Pin.OUT)
pin_D2 = machine.Pin(4,machine.Pin.OUT)
pin_D3 = machine.Pin(0,machine.Pin.OUT)
pin_D4 = machine.Pin(2,machine.Pin.OUT)
pin_D5 = machine.Pin(14,machine.Pin.OUT)



pin_D0.off()
pin_D1.off()
pin_D2.off()
pin_D3.off()
pin_D4.off()
pin_D5.off()



def DisplayBinary(decimalNumber):
    # format given decimal...convert to binary..Total number of bits is 6...zero padding....
    binaryString = '{0:06b}'.format(decimalNumber)
    pin_D0.value(int(binaryString[5]))
    pin_D1.value(int(binaryString[4]))
    pin_D2.value(int(binaryString[3]))
    pin_D3.value(int(binaryString[2]))
    pin_D4.value(int(binaryString[1]))
    pin_D5.value(int(binaryString[0]))




# the device is on GPIO12
dat = machine.Pin(12)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()


while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds.read_temp(rom), end=' ')
        DisplayBinary(int(ds.read_temp(rom)))
        print()
    


