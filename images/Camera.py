import os
from time import sleep

count = 0
path = "image"+str(count)+".jpg"

while True:
	os.system("libcamera-jpeg -o "+path)
	count+=1
	path = "image"+str(count)+".jpg"
	sleep(5)
