#!/usr/bin/env python

import pygtk
import gtk

class HelloWorld:

    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        print "delete_event"
        return False

    def destroy_event(self, widget, event, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy_event", self.destroy_event)
        self.window.set_border_width(10)
        self.button = gtk.Button("Hello")
        self.button.connect("clicked", self.hello, None)
        #self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        self.quit = gtk.Button("Quit")
        self.quit.connect("clicked", self.destroy_event, None)
        self.window.add(self.quit)
        self.button.show()
        self.quit.show()
        self.window.show()


    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    try:
        hello.main()
    except:
        print "That's all folks!!!"

