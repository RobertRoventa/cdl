#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Hello:
    def __init__(self):
        self.w = gtk.window(gtk.WINDOW_TOPLEVEL)
	self.w.show()

    def main(self):
	gtk.main()

hello = Hello()
hello.main()
