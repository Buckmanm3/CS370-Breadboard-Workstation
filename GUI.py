import tkinter as tk
import Camera

def onclick():
    print("what Name would you like for the picture?")
    Camera.takeImage("imagetest")

root = tk.Tk()
picbutton = tk.Button(root, text="Take Picture", command=onclick)
picbutton.pack()
root.mainloop()