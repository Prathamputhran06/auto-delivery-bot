#import RPi.GPIO as GPIO
from Setup import *

#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(3,GPIO.IN)
#GPIO.setup(5,GPIO.OUT)


status = True

def route():
	while status:
		d.manual_routing()
		val=0
#		val = GPIO.input(3)
		if val == 0:
#			GPIO.output(5,GPIO.LOW)
			print(val)
		else:
#			GPIO.output(5,GPIO.HIGH)
			print(val)
			

