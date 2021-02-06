import smbus as sb
import matplotlib.pyplot as plt
from time import sleep
from random import randint
Bus = sb.SMBus(1)
Bus.pec = 1 #enables Packet Error Checking byte
devAdd1 = 0x23 #device address for weird power brick
devAdd2 = 0x7f #device address for normal power brick


#with sb.SMBus(1) as Bus:
#curr = (2 **-4) * (Bus.read_i2c_block_data(devAdd, 0x8c, 2) & 0x07FF) #current (amps)
#v_out = (2 ** -12) * Bus.read_i2c_block_data(devAdd, 0x8b, 2) #voltage out (volts)
    #v_in = Bus.read_byte_data(devAdd, 0x88) #voltage in
#temp = (2 ** - 2) * (Bus.read_i2c_block_data(devAdd, 0x8d, 2) & 0x07FF) #temperature (degrees Celsius)
#Bus.write_byte(devAdd, 0x03)

#Bus.write_byte_data(devAdd, 0x02, 0x1d)
#print(Bus.read_i2c_block_data(devAdd, 0x7e, 1))

#x=0
#if x == 1:
#    z_2 = Bus.read_byte_data(devAdd, 0x20)
#    print("0x%x" % z_2)

#y=0
#if y == 1:
#    oper = Bus.read_i2c_block_data(devAdd, 0x79, 2) #reads byte from Operation command
#    print("0x%x" % oper[0])
#    print("0x%x" % oper[1])

def FaultsRW(devAdd0, actionB, writeB):
    Bus.write_byte_data(devAdd0, actionB, writeB)
    f = Bus.read_byte_data(devAdd0, actionB)
    print("0x%x" % f)
def IOutOCFaultResponseRead(devAdd0):
    f = Bus.read_byte_data(devAdd0, 0x47)
    print("0x%x" % f)

def IOutOCFaultResponseRW(devAdd0):
    Bus.write_byte_data(devAdd0, 0x47, 0xc0)
    f = Bus.read_byte_data(devAdd0, 0x47)
    print("0x%x" % f)

def VOutMode(devAdd0):
    f = Bus.read_byte_data(devAdd0, 0x20)
    print("0x%x" % f)
#IOutFault(0x23)
def ReadVOut(devAdd0):
    v = Bus.read_i2c_block_data(devAdd0, 0x8b, 2) #list of bytes
    #print(v)
    hiB = v[1] << 8 #high byte is second element shifted 8 bits
    loB = v[0] #low byte
    manT = hiB + loB #mantissa
    v_out = (2 ** -12) * manT #value from mantissa
    #print(f'At device {devAdd0}: {v_out} volts')
    return v_out

def readTemperature1(devAdd0):
    t = Bus.read_i2c_block_data(devAdd0, 0x8d, 2)
    #print(t)
    hiT = (t[1] & 0x7)<<8
    loT = t[0]
    manTemp = hiT + loT
    temp = manTemp * (2**-2)
    tempF = 1.8*temp + 32
    #print(f'At device {devAdd0}: {1.8*temp+32} F')
    return tempF
    
def ReadVIn(devAdd0):
    vIn = Bus.read_i2c_block_data(devAdd0, 0x88, 2)
    #print(v_in)
    hiV = (vIn[1] & 0x7)<<8
    loV = vIn[0]
    manVin = hiV + loV
    v_in = manVin * (2**-3)
    #print(f'At device {devAdd0}: {vIn} volts')
    return v_in
def ReadIOut(devAdd0):
    curr = Bus.read_i2c_block_data(devAdd0, 0x8c, 2)
    #print(curr)
    hiI = (curr[1] & 0x7) << 8
    loI = curr[0]
    manCurr = hiI + loI
    current = manCurr * (2 ** -4)
    print(current)
    return current

#def readIVT(devAdd, )
def StatusWord(devAdd0):
    word = Bus.read_i2c_block_data(devAdd0, 0x79, 2)
    print(f'At device {devAdd0}: {word}')

def StatusCML(devAdd):
    commState = Bus.read_i2c_block_data(devAdd, 0x7e, 1)
    print(commState)
def VInOffRead(devAdd0):
    v_in = Bus.read_i2c_block_data(devAdd0, 0x36, 2)
    print(f'At device {devAdd0}: {v_in} volts')
    hiV = (v_in[1] & 0x7)<<8
    loV = v_in[0]
    manVin = hiV + loV
    vIn = manVin * (2**-3)
    #print(f'At address {devAdd0}: {vIn}')

def VInOffWrite(devAdd0):
    Bus.write_i2c_block_data(devAdd0, 0x36, [233, 16])
def StatusInput(devAdd0):
    vinStat = Bus.read_i2c_block_data(devAdd0, 0x7c, 1)
    print(f'At device {devAdd0}: {vinStat}')
def VOutCommand(devAdd0):
    v = Bus.read_i2c_block_data(devAdd0, 0x21, 2) #list of bytes
    #print(v)
    hiB = v[1] << 8 #high byte is second element shifted 8 bits
    loB = v[0] #low byte
    manT = hiB + loB #mantissa
    v_out = (2 ** -12) * manT #value from mantissa
    print(f'At device {devAdd0}: {v_out} volts')


#yes = 'f'
#while yes == 't':
#    actB = int(input('Enter byte for data to read in hexadecimal: '), 16)
#    writeB = int(input('Enter byte to write to register in hex: '), 16)
#    FaultsRW(devAdd2, actB, writeB)
#    yes = input("run again? (y/n)")
#    if yes.lower() == 'y':
#        yes = 't'
#    elif yes.lower() == 'n':
#        yes = 'f'
#y1 = False
#while y1 == True:
#    VOutMode(devAdd2)
#y2 = False
#vals = []
#while y2 == True:
#    vals.append(ReadIOut(devAdd2))
#print(max(vals))
#readWord(devAdd2)
def plotRead(devAdd, tDelay):
    read = int(input('Enter 0 (V_OUT), 1 (TEMP), 2 (V_IN), 3 (CURR)'))
    time = []
    vals = []
    title = ''
    try:
        t = 0  # time
        while True:
            if read == 0: #Vout
                val = randint(1,100)#ReadVOut(devAdd)
                unit = 'volt'
                title = "Voltage Out"
            elif read == 1: #temp
                val = randint(1,100)#readTemperature1(devAdd)
                unit = 'F'
                title = "Temperature"
            elif read == 2: #Vin
                val = randint(1,100)#ReadVIn(devAdd)
                unit = 'volt'
                title = "Voltage In"
            elif read == 3: # curr
                val = randint(1,100)#ReadIOut(devAdd)
                unit = 'amp'
                title = "Current"
            time.append(t)
            vals.append(val)
            sleep(tDelay)
            t += tDelay
    except KeyboardInterrupt:
        pass

    fig, ax = plt.subplots()
    ax.plot(time, vals)
    ax.set_title(title)
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel(f"{title} ({unit})")
    plt.show()

plotRead(devAdd2, 0.05)
