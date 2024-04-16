from turtle import *

class setup(Turtle):

    def __init__(self):
        self.destination_set = 0
        self.home_set = 0

    def Title(self):
        self.title = Turtle()
        self.title.penup()
        self.title.hideturtle()
        self.title.goto(-150,230)
        self.title.write("Route Map Grid", font=('Arial', 30, 'bold'))

    def set_destination_coordinates(self,x,y):
        if self.destination_set == 0:
            self.Title()
            self.cursor.penup()
            self.cursor.goto(x, y)
            self.cursor.pendown()
            self.text = Turtle()
            self.text.penup()
            self.text.hideturtle()
            self.text.goto(x,y-25)
            self.text.write("Destination", font=('Arial', 10, 'bold'))
            self.destination_set = 1
        else:
            pass

    def set_home_coordinates(self,x,y):
        if self.home_set == 0:
            self.cursor1.penup()
            self.cursor1.goto(x,y)
            self.cursor1.pendown()
            self.text1 = Turtle()
            self.text1.penup()
            self.text1.hideturtle()
            self.text1.goto(x,y-25)
            self.text1.write("Home", font=('Arial', 10, 'bold'))
            self.home_set = 1
        else:
            pass

    def set_destination(self):
        self.cursor = Turtle()
        self.cursor.shape("square")
        self.cursor.color("green")
        self.screen = Screen()
        self.screen.onscreenclick(self.set_destination_coordinates)

    def set_home(self):
        self.cursor1 = Turtle()
        self.cursor1.shape("square")
        self.cursor1.color("red")
        self.screen1 = Screen()
        self.screen1.onscreenclick(self.set_home_coordinates)






