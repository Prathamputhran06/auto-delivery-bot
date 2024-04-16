import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.OUT)


status = True

def route():
	while status:
		val = GPIO.input(3)
		if val == 0:
			GPIO.output(5,GPIO.LOW)
			print(val)
		else:
			GPIO.output(5,GPIO.HIGH)
			print(val)
			
