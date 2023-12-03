import os
from time import sleep

#default image name
default = "image"

def takeImage(name):
	os.system("libcamera-jpeg -o "+name+".jpg -n")

def setDefault(name):
	default = name;

takeImage(default)