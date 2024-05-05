import RPi.GPIO as GPIO
import time
import math
from turtle import Screen
from mail import *
from servo import *
#from Setup import *
#from gpiozero import Robot
#r = Robot(left=(7,8), right=(9,10))

def left():
#        r.backward()
        print("moving left")

def right():
#	  r.forward()
        print("moving right")

def forward():
#	  r.left()
        print("moving forward")

def backward():
#	  r.right()
        print("moving backward")

def stop():
#	  r.stop()
        print("stop movement")

Travel = True
thresold_distance = 10

def route_back():
    pass

def latlon_to_cor():
    #convert the lat lon to coordinate corresponding to our grid
    #return x and y coordinate
    pass

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

def calculate_angle(target_x, target_y, current_x , current_y):
    dx = target_x - current_x
    dy = target_y - current_y
    angle = math.atan2(dy, dx) * (180 / math.pi)
    return angle



def move_to_target(destination_x , destination_y ):
    randomnum = sendmail()
    while Travel:
        # get x and y from latlon_to_cor
        current_x = int(input("Enter the current x coordinate"))
        current_y = int(input("Enter the current y coordinate"))
        otp = confirm(randomnum)
        if current_x == destination_x and current_y == destination_y and otp:
            Travel = False
            #deliver order
            serv()
            route_back()
            break
        distance = measure_distance()
        if distance > thresold_distance:
            angle = calculate_angle(target_x, target_y, current_x , current_y)
            #must make the bot to turn to given angle and move forward till destination reached
        else:
            #must stop and take back and turn right and then continue route
            pass
