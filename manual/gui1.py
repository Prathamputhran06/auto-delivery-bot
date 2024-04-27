from tkinter import *
from Setup import *


window = Tk()
window.title("Auto Delivery Bot")
window.minsize(width = 600 , height = 600)
window['bg'] = "#EEE4B1"
window.config(padx = 100 , pady = 100)


destination = setup()

#create canva for the title

canva = Canvas(width = 200 ,height = 224)
canva.create_text(100 , 130 , text = "prototype of auto delivery bot" , font=('Helvetica', 10 , 'bold'))
canva.grid(column = 1 , row = 0)


#buttons for setting start, stop, destination and home location

set_destination = Button(text = "set destination" , command = destination.set_destination)
set_destination.grid(column = 0 , row = 1)

set_home = Button(text = "set home" , command = destination.set_home)
set_home.grid(column = 1 , row = 1)

start = Button(text = "START" , command = None)
start.grid(column = 2 , row = 1)

stop = Button(text = "STOP" , command = None)
stop.grid(column = 3 , row = 1)


window.mainloop()

