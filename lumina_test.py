import smbus
bus = smbus.SMBus(1)
addr = 0x23
luxRead = bus.read_i2c_block_data(addr,0x10)
print(luxRead[0]*256+luxRead[1]/1.2)
