import Tkinter as tk
from Tkinter import *
import tkFileDialog as filedialog
from sys import platform
import os

if platform == "linux" or platform == "linux2":
    inidir = os.path.expanduser('~') + "/Documents"
    #print os.path.expanduser('~')
    print "linux!" # linux
elif platform == "darwin":
    print "OS X" # OS X
elif platform == "win32":
	inidir = os.path.expanduser('~') + "\Documents"
    #print "Windows" # Windows...

def donothing():
   x = 0

def openfile():
	#root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename(initialdir = inidir,title = "Selecteer bestand",filetypes = (("Microsoft Excel 1997-2003","*.xls"),("Microsoft Excel","*.xlsx"),("all files","*.*")))
	root.config(menu=menubar)
	root.mainloop()
 
root = Tk()
root.title("eCalendar")
root.geometry("500x400")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
 
root.config(menu=menubar)
root.mainloop()

print file_path