from turtle import Turtle,Screen


def get_mouse_click_coor(x,y):
    if -250<=x<=-150 and 100<=y<=200:
        print(0,3)
    elif -150<=x<=-50 and 100<=y<=200:
        print(1,3)
    elif -50<=x<=50 and 100<=y<=200:
        print(2,3)
    elif 50<=x<=150 and 100<=y<=200:
        print(3,3)
    elif 150<=x<=250 and 100<=y<=200:
        print(4,3)
    elif -250<=x<=-150 and 0<=y<=100:
        print(0,2)
    elif -150<=x<=-50 and 0<=y<=100:
        print(1,2)
    elif -50<=x<=50 and 0<=y<=100:
        print(2,2)
    elif 50<=x<=150 and 0<=y<=100:
        print(3,2)
    elif 150<=x<=250 and 0<=y<=100:
        print(4,2)
    elif -250<=x<=-150 and -100<=y<=0:
        print(0,1)
    elif -150<=x<=-50 and -100<=y<=0:
        print(1,1)
    elif -50<=x<=50 and -100<=y<=0:
        print(2,1)
    elif 50<=x<=150 and -100<=y<=0:
        print(3,1)
    elif 150<=x<=250 and -100<=y<=0:
        print(4,1)
    elif -250<=x<=-150 and -200<=y<=-100:
        print(0,0)
    elif -150<=x<=-50 and -200<=y<=-100:
        print(1,0)
    elif -50<=x<=50 and -200<=y<=-100:
        print(2,0)
    elif 50<=x<=150 and -200<=y<=-100:
        print(3,0)
    elif 150<=x<=250 and -200<=y<=-100:
        print(4,0)


def grid():
    grid = Turtle()
    grid.speed(0)
    grid.pencolor("blue")
    grid.width(5)
    grid.penup()
    grid.goto(-250,200)
    grid.pendown()
    grid.forward(500)
    grid.left(270)
    grid.forward(400)
    grid.left(270)
    grid.forward(500)
    grid.goto(-250,200)
    grid.left(180)
    grid.forward(100)
    grid.left(270)
    grid.forward(400)
    grid.left(90)
    grid.forward(100)
    grid.left(90)
    grid.forward(400)
    grid.left(270)
    grid.forward(100)
    grid.left(270)
    grid.forward(400)
    grid.left(90)
    grid.forward(100)
    grid.left(90)
    grid.forward(400)
    grid.goto(-250,200)
    grid.left(180)
    grid.forward(100)
    grid.left(90)
    grid.forward(500)
    grid.left(270)
    grid.forward(100)
    grid.left(270)
    grid.forward(500)
    grid.left(90)
    grid.forward(100)
    grid.left(90)
    grid.forward(500)


grid()
s = Screen()
s.setup(width=512, height=512)
s.bgpic('map1.gif')
s.onscreenclick(get_mouse_click_coor)

s.mainloop()

