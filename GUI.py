import tkinter as tk
from tkinter import *
from tkinter import font
import Camera
import Pins

def picture(): 
    userInput = pictureName.get()
    Camera.takeImage(userInput)

def voltage():
    voltage_value = Pins.readOnce(clicked.get())
    volt.config(text=f"Voltage: {voltage_value:.6f}")
    root.after(500, voltage)
def channel():
    Pins.readOnce(clicked.get())

root = tk.Tk()
custom_font = font.Font(size=16)

root.title("Computer Engineering Work Space")
label = tk.Label(root, text="What name would you like for this picture?", font=custom_font)
label.pack()
pictureName = tk.Entry(root, width=30) 
pictureName.pack()
picbutton = tk.Button(root, text="Take Picture", command=picture, font=custom_font)
picbutton.pack()
channelLabel = tk.Label(root, text="What channel are you using?", font=custom_font)
channelLabel.pack()
options = [ 
    "A", 
    "B", 
    "C", 
    "D", 
    "E", 
    "F", 
    "G",
    "H"
] 
clicked = StringVar()
clicked.set( "A" )
drop = OptionMenu( root , clicked , *options ) 
drop.pack()
dropButton = Button( root , text = "Set Channel" , command = channel )
dropButton.pack() 



volt = tk.Label(root, text="Voltage: 0.00", font=custom_font)
volt.pack()
root.after(0, voltage)
root.mainloop()