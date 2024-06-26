import RPi.GPIO as GPIO
import time

def serv():
    servoPIN = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(12.5)
    time.sleep(5)
    p.ChangeDutyCycle(5)
    time.sleep(5)

GPIO.cleanup
