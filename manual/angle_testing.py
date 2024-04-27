from gpiozero import Robot
import math

#define the robot pins
r = Robot(left=(7,8), right=(9,10))


def calculate_angle(target_x, target_y):
    current_x = 0  # Assuming starting from (0,0)
    current_y = 0
    dx = target_x - current_x
    dy = target_y - current_y
    angle = math.atan2(dy, dx) * (180 / math.pi)
    return angle




def turn(robot, angle):
    # Calculate the time required to turn the specified angle
    # This may vary depending on your robot's characteristics
    # Adjust these values according to your robot's turning behavior
    turn_speed = 0.5  # Adjust as necessary
    turn_duration = abs(angle) / 90 * turn_speed  # Assuming 90 degrees takes turn_speed seconds

    # Determine the direction to turn based on the sign of the angle
    if angle > 0:
        # Turn right
        robot.right()
    elif angle < 0:
        # Turn left
        robot.left()

    # Sleep for the required duration to complete the turn
    sleep(turn_duration)

    # Stop the robot after turning
    robot.stop()


target_x = 10
target_y = 5
angle = calculate_angle(target_x, target_y)
turn(robot, angle)
