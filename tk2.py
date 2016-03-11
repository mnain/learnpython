#!/usr/bin/env python

import Tkinter


def handleEntry():
	global lbl
	txt = entry.get()
	print "Entry:" + txt
	lbl.text = txt
	lbl.update()

root = Tkinter.Tk()
entry = Tkinter.Entry(width=45)
entry.pack(),
lbl = Tkinter.Label(width=80, text="NULL")
lbl.pack()
btn1 = Tkinter.Button(text="Submit", command=handleEntry)
btn1.pack()
quit = Tkinter.Button(text="Quit", command="exit")
quit.pack()
lbl.text = 'So far'
lbl.update()
root.mainloop()
