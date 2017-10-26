import excel
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class main:
  def __init__(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file('eCalendar.glade')
    self.builder.connect_signals(self)
    self.window = self.builder.get_object("window1")
    self.window.show()
    self.open_button = self.builder.get_object("open_buttond")
    self.path = "/home/lars/Documents/Jaar3/SE/files/Rooms master cs  fall 17-18.xls"

  def on_file_new_activate(self, menuitem, data=None):
    pass

  def on_file_open_activated(self, menuitem, data=None):
    print "geopend "
    self.fcd = Gtk.FileChooserDialog("Open...",
               None,
               Gtk.FILE_CHOOSER_ACTION_OPEN,
               (Gtk.STOCK_CANCEL, Gtk.RESPONSE_CANCEL, Gtk.STOCK_OPEN, Gtk.RESPONSE_OK))
    # 2 set the current folder in the file chooser
    self.fcd.set_current_folder(self.current_folder)
    if os.path.isdir(os.getenv("HOME")+'/linuxcnc/configs'):
      self.fcd.add_shortcut_folder(os.getenv("HOME")+'/linuxcnc/configs')
    self.response = self.fcd.run()
    if self.response == Gtk.RESPONSE_OK:
      print "Selected filepath: %s" % self.fcd.get_filename()
      print self.fcd.get_uri()
      # 3 if a file was choosen save the current folder
      self.current_folder = self.fcd.get_current_folder()
      self.fcd.destroy()

  def on_file_save_activate(self, menuitem, data=None):
    pass

  def on_file_save_as_activate(self, menuitem, data=None):
    pass

  def on_file_quit_activate(self, menuitem, data=None):
    pass

  def on_create(self, menuitem, data=None):
    excel.open_file(self.path)
    print "eCal created"

  def on_window1_destroy(self, object, data=None):
    print "quit with cancel"
    Gtk.main_quit()

if __name__ == "__main__":
  main = main()
  Gtk.main()