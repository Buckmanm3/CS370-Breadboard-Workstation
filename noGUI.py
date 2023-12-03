import Pins
import Camera
import threading
import time
import io

c = threading.Condition()
printing = False
pinNum = "A"

class VoltagePrint(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global printing   #made global here
        global pinNum
        while True:
            while printing:
                print(Pins.readOnce(pinNum))
                time.sleep(.5)   

class Controller(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global printing
        global pinNum
        print("Starting Workspace:\nCommands:\nC - take photo\nV - display voltage (\'q\' to exit)\nP - select voltage")
        while True:
            UserInput = input(">>>")
            match UserInput:
                case 'c':
                    Camera.takeImage(Camera.default)
                case 'C':
                    Camera.takeImage(Camera.default)
                case 'V':
                    printing = True
                    while True:
                        pinNum = input()
                        if pinNum == 'q':
                            break
                    printing = False
                    print("Stopping...")
                case "Q":
                    c.release()
                case "q":
                    c.release()
                case default:
                    print("Error")

a = Controller("Controller")
b = VoltagePrint("Printer")

a.start()
b.start()

a.join()
