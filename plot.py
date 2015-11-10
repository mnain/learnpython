# plot a function like y = sin(x) with Tkinter canvas and line
# tested with Python24  by     vegaseat      25oct2006

from Tkinter import *
import math
import random

root = Tk()
root.title("Simple plot using canvas and line")

width = 900
height = 300
center = height//2
x_increment = 1
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = 80

c = Canvas(width=width, height=height, bg='grey')
c.pack()

str1 = "sin(x)=blue  cos(x)=red"
c.create_text(10, 20, anchor=SW, text=str1)

center_line = c.create_line(0, center, width, center, fill='green')

# create the coordinate list for the sin() curve, have to be integers
xy1 = []
for x in range(width):
    # x coordinates
    xy1.append(x * x_increment)
    # y coordinates
    xy1.append(int(math.sin(x * x_factor) * y_amplitude) + center)

#sin_line = c.create_line(xy1, fill='blue')

# create the coordinate list for the cos() curve
xy2 = []
for x in range(width):
    # x coordinates
    xy2.append(x * x_increment)
    # y coordinates
    xy2.append(int(math.cos(x * x_factor) * y_amplitude) + center)

#cos_line = c.create_line(xy2, fill='red')

# create a random line
rl = []
for x in range(width):
	r = random.randint(1,height)
	rl.append(x * x_increment)
	rl.append(r)

rline = c.create_line(rl, fill='blue')
	
root.mainloop()

