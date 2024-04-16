import tkinter
from turtle import Turtle,Screen

destination_set = False

cursor = Turtle()
screen = Screen()



# Function to bring turtle to cursor's location
def set_destination(x, y):
	global destination_set
	if destination_set == False:
		cursor.penup()
		cursor.goto(x, y)
		destination_point = Turtle()
		destination_point.shape("square")
		destination_point.penup()
		destination_point.goto(x, y)
		print(x,y)
		cursor.pendown()
	else:
		destination_set = True

def set_Home(x, y):
    cursor.penup()
    cursor.goto(x, y)
    print(x,y)
    cursor.pendown()
    

# Bind the function to the turtle screen
#screen.onscreenclick(set_destination)

# Keep the window open
screen.mainloop()
