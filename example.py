import Pins
import Camera
import time
from gpiozero import LED

#declare led var (plugged into GPIO pin 17)
led = LED(17)

#infinte loop
while True:
    #read in voltage from ADC
    voltate = Pins.readOnce('A')
    
    #check value
    if voltate >= 1.5:
        #turn on light, take picture
        led.on()
        #take image using camera module
        Camera.takeImage("example")
        #sleep after taking pic
        time.sleep(1.5)
    else:
        #turn off light
        led.off()
    #print out voltage value    
    print("Voltage Value:" + str(voltate))
    
    #sleep for short period
    time.sleep(.5)