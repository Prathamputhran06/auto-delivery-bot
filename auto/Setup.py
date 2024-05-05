from turtle import *
from mail import *
#import RPi.GPIO as GPIO
import time
from main import *

dest_x = 0
dest_y = 0

class setup(Turtle):

    def __init__(self):
        self.destination_set = 0
        self.home_set = 0

    def Title(self):
        self.title = Turtle()
        self.title.penup()
        self.title.hideturtle()
        self.title.goto(-150,200)
        self.title.write("Route Map Grid", font=('Arial', 30, 'bold'))
#        self.grid()

    def set_destination_coordinates(self,x,y):
        if self.destination_set == 1:
            self.Title()
            self.cursor.penup()
            self.cursor.goto(x, y)
            self.cursor.pendown()
            self.text = Turtle()
            self.text.penup()
            self.text.hideturtle()
            self.text.goto(x,y-25)
            self.text.write("Destination", font=('Arial', 10, 'bold'))
            self.destination_set = 2
        else:
            pass

    def set_home_coordinates(self,x,y):
        if self.home_set == 1:
            self.cursor1.penup()
            self.cursor1.goto(x,y)
            self.cursor1.pendown()
            self.text1 = Turtle()
            self.text1.penup()
            self.text1.hideturtle()
            self.text1.goto(x,y-25)
            self.text1.write("Home", font=('Arial', 10, 'bold'))
            self.home_set = 2
        else:
            pass

    def set_destination(self):
        if self.destination_set == 0:
            self.cursor = Turtle()
            self.cursor.shape("square")
            self.cursor.color("green")
            self.screen = Screen()
            self.screen = Screen()
            self.screen.setup(width=512, height=512)
            self.screen.bgpic('map1.gif')
            self.destination_set = 1
            self.screen.onscreenclick(self.get_mouse_click_coor)
        else:
            pass

    def set_home(self):
        if self.home_set == 0:
            self.cursor1 = Turtle()
            self.cursor1.shape("square")
            self.cursor1.color("red")
            self.screen1 = Screen()
            self.screen1.onscreenclick(self.set_home_coordinates)
            self.home_set = 1
        else:
            pass

    def get_mouse_click_coor(self,x,y):
        if self.destination_set == 1:
            self.Title()
            self.cursor.penup()
            self.cursor.goto(x, y)
            self.cursor.pendown()
            self.text = Turtle()
            self.text.penup()
            self.text.hideturtle()
            self.text.goto(x,y-25)
            self.text.write("Destination", font=('Arial', 10, 'bold'))
            self.destination_set = 2
            if -250<=x<=-150 and 100<=y<=200:
                global dest_x,dest_y
                dest_x,dest_y = 0,3
            elif -150<=x<=-50 and 100<=y<=200:
                dest_x,dest_y = 1,3
            elif -50<=x<=50 and 100<=y<=200:
                dest_x,dest_y = 2,3
            elif 50<=x<=150 and 100<=y<=200:
                dest_x,dest_y = 3,3
            elif 150<=x<=250 and 100<=y<=200:
                dest_x,dest_y = 4,3
            elif -250<=x<=-150 and 0<=y<=100:
                dest_x,dest_y = 0,2
            elif -150<=x<=-50 and 0<=y<=100:
                dest_x,dest_y = 1,2
            elif -50<=x<=50 and 0<=y<=100:
                dest_x,dest_y = 2,2
            elif 50<=x<=150 and 0<=y<=100:
                dest_x,dest_y = 3,2
            elif 150<=x<=250 and 0<=y<=100:
                dest_x,dest_y = 4,2
            elif -250<=x<=-150 and -100<=y<=0:
                dest_x,dest_y = 0,1
            elif -150<=x<=-50 and -100<=y<=0:
                dest_x,dest_y = 1,1
            elif -50<=x<=50 and -100<=y<=0:
                dest_x,dest_y = 2,1
            elif 50<=x<=150 and -100<=y<=0:
                dest_x,dest_y = 3,1
            elif 150<=x<=250 and -100<=y<=0:
                dest_x,dest_y = 4,1
            elif -250<=x<=-150 and -200<=y<=-100:
                dest_x,dest_y = 0,0
            elif -150<=x<=-50 and -200<=y<=-100:
                dest_x,dest_y = 1,0
            elif -50<=x<=50 and -200<=y<=-100:
                dest_x,dest_y = 2,0
            elif 50<=x<=150 and -200<=y<=-100:
                dest_x,dest_y = 3,0
            elif 150<=x<=250 and -200<=y<=-100:
                dest_x,dest_y = 4,0
            print(dest_x,dest_y)


    def grid(self):
        self.grid = Turtle()
        self.grid.speed(0)
        self.grid.pencolor("blue")
#        self.s.onscreenclick(self.get_mouse_click_coor)
        self.grid.width(5)
        self.grid.penup()
        self.grid.goto(-250,200)
        self.grid.pendown()
        self.grid.forward(500)
        self.grid.left(270)
        self.grid.forward(400)
        self.grid.left(270)
        self.grid.forward(500)
        self.grid.goto(-250,200)
        self.grid.left(180)
        self.grid.forward(100)
        self.grid.left(270)
        self.grid.forward(400)
        self.grid.left(90)
        self.grid.forward(100)
        self.grid.left(90)
        self.grid.forward(400)
        self.grid.left(270)
        self.grid.forward(100)
        self.grid.left(270)
        self.grid.forward(400)
        self.grid.left(90)
        self.grid.forward(100)
        self.grid.left(90)
        self.grid.forward(400)
        self.grid.goto(-250,200)
        self.grid.left(180)
        self.grid.forward(100)
        self.grid.left(90)
        self.grid.forward(500)
        self.grid.left(270)
        self.grid.forward(100)
        self.grid.left(270)
        self.grid.forward(500)
        self.grid.left(90)
        self.grid.forward(100)
        self.grid.left(90)
        self.grid.forward(500)

    def mov(self):
        global dest_x,dest_y
        move_to_target(dest_x , dest_y )



