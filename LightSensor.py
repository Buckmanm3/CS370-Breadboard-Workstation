import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from gpiozero import LED


# define GPIO pin for reading LED
LED_PIN = 17
led = LED(LED_PIN)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

led.on()

while True:
	print("Raw ADC Value: ", chan.value)
	print("ADC Voltage: " + str(chan.voltage) + "V")
	time.sleep(.5)

