from tkinter import *
from turtle import Screen,Turtle
from Setup import *
#from gpiozero import Robot
#r = Robot(left=(7,8), right=(9,10))

destination = setup()



window = Tk()
window.title("Auto Delivery Bot")
window.minsize(width = 600 , height = 600)
window['bg'] = "#EEE4B1"
window.config(padx = 100 , pady = 100)



#create canva for the title

canva = Canvas(width = 200 ,height = 224)
canva.create_text(100 , 130 , text = "prototype of auto delivery bot" , font=('Helvetica', 10 , 'bold'))
canva.grid(column = 1 , row = 0)


#buttons for setting start, stop, destination and home location

set_destination = Button(text = "set destination" , command = destination.set_destination)
set_destination.grid(column = 0 , row = 1)

set_home = Button(text = "set home" , command = destination.set_home)
set_home.grid(column = 1 , row = 1)

start = Button(text = "START" , command = destination.manual_routing)
start.grid(column = 2 , row = 1)

stop = Button(text = "STOP" , command = None)
stop.grid(column = 3 , row = 1)


name = StringVar()
sender_mail = Entry(textvariable = name ,)
sender_mail.grid(column = 1 , row = 2 , columnspan = 2 , padx = 50 , pady = 50)

def doit():
    print(name.get())

validate = Button(text = "validate" ,command = doit)
validate.grid(column = 1 , row = 3 , columnspan = 2 , padx = 10 , pady = 10)



window.mainloop()
