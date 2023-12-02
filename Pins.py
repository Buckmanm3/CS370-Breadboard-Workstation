import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0-7
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)
chan5 = AnalogIn(mcp, MCP.P5)
chan6 = AnalogIn(mcp, MCP.P6)
chan7 = AnalogIn(mcp, MCP.P7)

currChannel = chan0;

#function for selecting pins
def SelectChannel(pinNumber):
    match pinNumber:
        case 'A':
            currChannel = chan0;
        case 'B':
            currChannel = chan1;
        case 'C':
            currChannel = chan2;
        case 'D':
            currChannel = chan3;
        case 'E':
            currChannel = chan4;
        case 'F':
            currChannel = chan5;
        case 'G':
            currChannel = chan6;
        case 'H':
            currChannel = chan7;

#read a single time
def readOnce():
    print("Raw ADC Value: ", currChannel.value)
    print("ADC Voltage: " + str(currChannel.voltage) + "V")

#read for a duration (specified in seconds)
def readDuration(duration):
    while duration > 0:
        print("Raw ADC Value: ", currChannel.value)
        print("ADC Voltage: " + str(currChannel.voltage) + "V")
        duration-.5;
        time.sleep(.5)


#function to read forever (every half a second)
def readForever():
    while True:
        print("Raw ADC Value: ", currChannel.value)
        print("ADC Voltage: " + str(currChannel.voltage) + "V")
        time.sleep(.5)