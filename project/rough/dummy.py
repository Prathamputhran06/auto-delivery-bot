import RPi.GPIO as GPIO
import time
import math

# Ultrasonic sensor pins
TRIG = 23
ECHO = 24

# Motor pins
# Assuming you have motors connected to GPIO pins for controlling movement
# Adjust these pins according to your setup
LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 27
RIGHT_MOTOR_BACKWARD = 22

# Constants
DIST_THRESHOLD = 10  # Distance threshold to consider obstacle
TARGET_THRESHOLD = 1  # Threshold distance to consider target reached

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_BACKWARD, GPIO.OUT)

# Function to measure distance using ultrasonic sensor
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

# Function to move forward
def move_forward():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)

# Function to move backward
def move_backward():
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)

# Function to stop
def stop():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.LOW)

# Function to calculate angle between current and target position
def calculate_angle(target_x, target_y):
    current_x = 0  # Assuming starting from (0,0)
    current_y = 0
    dx = target_x - current_x
    dy = target_y - current_y
    angle = math.atan2(dy, dx) * (180 / math.pi)
    return angle

# Function to move towards target
def move_to_target(target_x, target_y):
    while True:
        distance = measure_distance()
        if distance > DIST_THRESHOLD:
            angle = calculate_angle(target_x, target_y)
            # Adjust robot's direction based on angle
            # Code to control motors and turn the robot
            # Implement your motor control logic here
            
            # Move forward
            move_forward()
            
            # Check if target reached
            if distance <= TARGET_THRESHOLD:
                stop()
                break
        else:
            # Obstacle detected, avoid it
            # Code to avoid obstacle
            # Implement your obstacle avoidance logic here
            pass

# Test the functions
target_x = 10  # Example target coordinates
target_y = 5
move_to_target(target_x, target_y)

# Cleanup GPIO
GPIO.cleanup()
