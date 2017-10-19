import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("gladetest1.glade")
builder.connect_signals(Handler())
#builder.title("eCalendar")

window = builder.get_object("window1")
window.show_all()
window.connect("delete-event", Gtk.main_quit)

#print file_open_path


open_window = builder.get_object("open_button")
open_file_path = ""

if open_file_path == " ":
	print "leeg"
else:
	print open_file_path
#open_window.connect

Gtk.main()