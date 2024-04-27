from turtle import Screen
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
    
    
    
screen2 = Screen()
screen2.listen()


screen2.onkey(left,"a")
screen2.onkey(right,"d")
screen2.onkey(forward,"w")
screen2.onkey(backward,"s")
screen2.onkey(stop,"f")


screen2.exitonclick()
