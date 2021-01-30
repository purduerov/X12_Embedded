import smbus as sb

Bus = sb.SMBus(1)
Bus.pec = 1 #enables Packet Error Checking byte
devAdd = 0x23 #device address


#with sb.SMBus(1) as Bus:
#curr = (2 **-4) * (Bus.read_i2c_block_data(devAdd, 0x8c, 2) & 0x07FF) #current (amps)
#v_out = (2 ** -12) * Bus.read_i2c_block_data(devAdd, 0x8b, 2) #voltage out (volts)
    #v_in = Bus.read_byte_data(devAdd, 0x88) #voltage in
#temp = (2 ** - 2) * (Bus.read_i2c_block_data(devAdd, 0x8d, 2) & 0x07FF) #temperature (degrees Celsius)
#Bus.write_byte(devAdd, 0x03)

#Bus.write_byte_data(devAdd, 0x02, 0x1d)
#print(Bus.read_i2c_block_data(devAdd, 0x7e, 1))

x=0
if x == 1:
    z_2 = Bus.read_byte_data(devAdd, 0x20)
    print("0x%x" % z_2)

y=0
if y == 1:
    oper = Bus.read_i2c_block_data(devAdd, 0x79, 2) #reads byte from Operation command
    print("0x%x" % oper[0])
    print("0x%x" % oper[1])
def IOutFault(devAdd0):
    Bus.write_byte_data(devAdd0, 0x47, 0xc0)
    f = Bus.read_byte_data(devAdd0, 0x47)
    print("0x%x" % f)
IOutFault(0x23)
def readVOut(devAdd0):
    v = Bus.read_i2c_block_data(devAdd0, 0x8b, 2) #list of bytes
    #print(v)
    hiB = v[1] << 8 #high byte is second element shifted 8 bits
    loB = v[0] #low byte
    manT = hiB + loB #mantissa
    v_out = (2 ** -12) * manT #value from mantissa
    print(f'At device {devAdd0}: {v_out} volts')

def readTemp(devAdd0):
    t = Bus.read_i2c_block_data(devAdd0, 0x8d, 2)
    #print(t)
    hiT = (t[1] & 0x7)<<8
    loT = t[0]
    manTemp = hiT + loT
    temp = manTemp * (2**-2)
    print(f'At device {devAdd0}: {1.8*temp+32} F')
    
def readVIn(devAdd0):
    v_in = Bus.read_i2c_block_data(devAdd0, 0x88, 2)
    #print(v_in)
    hiV = (v_in[1] & 0x7)<<8
    loV = v_in[0]
    manVin = hiV + loV
    vIn = manVin * (2**-3)
    print(f'At device {devAdd0}: {vIn} volts')
def readCurr(devAdd0):
    curr = Bus.read_i2c_block_data(devAdd0, 0x8c, 2)
    #print(curr)
    hiI = (curr[1] & 0x7) << 8
    loI = curr[0]
    manCurr = hiI + loI
    current = manCurr * (2 ** -4)
    print(current)

#readTemp()
def readWord(devAdd0):
    word = Bus.read_i2c_block_data(devAdd0, 0x79, 2)
    print(f'At device {devAdd0}: {word}')

def readCommState():
    commState = Bus.read_i2c_block_data(devAdd, 0x7e, 1)
    print(commState)
def readVIn2(devAdd0):
    v_in = Bus.read_i2c_block_data(devAdd0, 0x36, 2)
    print(f'At device {devAdd0}: {v_in} volts')
    hiV = (v_in[1] & 0x7)<<8
    loV = v_in[0]
    manVin = hiV + loV
    vIn = manVin * (2**-3)
    #print(f'At address {devAdd0}: {vIn}')

def writeVIn2(devAdd0):
    Bus.write_i2c_block_data(devAdd0, 0x36, [233, 16])
def readVInStat(devAdd0):
    vinStat = Bus.read_i2c_block_data(devAdd0, 0x7c, 1)
    print(f'At device {devAdd0}: {vinStat}')
def VOutComm(devAdd0):
    v = Bus.read_i2c_block_data(devAdd0, 0x21, 2) #list of bytes
    #print(v)
    hiB = v[1] << 8 #high byte is second element shifted 8 bits
    loB = v[0] #low byte
    manT = hiB + loB #mantissa
    v_out = (2 ** -12) * manT #value from mantissa
    print(f'At device {devAdd0}: {v_out} volts')
    
while True:
    readCurr(0x7f)
    #readVInStat(0x7f)
    #readVInStat(0x23)
    #writeVIn2(0x7f)
    #readVIn2(0x7f)
    #writeVIn2(0x23)
    #readVIn2(0x23)
#VOutComm(0x7f)
    #readVOut(0x23)
    #readWord(0x7f)
    #readWord(0x23)
    #readVIn(0x7f)
    #readVIn(0x23)
#Bus.read_i2c_block_data(devAdd, 0x21, 2)
