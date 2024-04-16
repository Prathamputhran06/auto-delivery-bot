from gpiozero import Robot
r = Robot(left=(7,8), right=(9,10))

# Example usage (modify as needed)
try:
    while True:
        command = input("Enter a command (f=forward, b=backward, l=left, r=right, s=stop): ")
        if command == 'd':
            r.forward()
        elif command == 'a':
            r.backward()
        elif command == 'w':
            r.left()
        elif command == 's':
            r.right()
        elif command == 'c':
            r.stop()

        else:
            print("Invalid command. Please try again.")

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on exit
    print("Program terminated.")
