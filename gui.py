import Tkinter as tk
from Tkinter import *
import tkFileDialog as filedialog
import tkMessageBox as messagebox
from sys import platform
import os
import excel

class gui:
	# platform chooser
	if platform == "linux" or platform == "linux2":
		inidir = os.path.expanduser('~') + "/Documents"
	elif platform == "darwin":
		print "OS X" # OS X
	elif platform == "win32":
		inidir = os.path.expanduser('~') + "\Documents"
		print "Windows" # Windows...

	def openFile(self):
		open_file_path = filedialog.askopenfilename(initialdir = self.inidir,
			title = "Selecteer bestand",
			filetypes = (("Microsoft Excel 1997-2003","*.xls"),("Microsoft Excel","*.xlsx"),("Alle bestanden","*.*")))
		open_var.set(open_file_path)

	def saveFile(self):
		save_file_path = filedialog.asksaveasfilename(initialdir = self.inidir,
			title = "Opslaan als",
			filetypes = (("iCal bestand","*.ics"),("Alle bestanden","*.*")))
		save_var.set(save_file_path)

	def createFile(self):
		exc = excel.excel()
		open_file_path = open_textbox.get()
		save_file_path = save_textbox.get()
		cal_name = name_textbox.get()
		if open_file_path == "" or save_file_path == "" or cal_name == "":
			messagebox.showinfo("Niet alle velden gevuld", "Kies een bestand om uit te lezen en een locatie om het bestand op te slaan. Geef ook een naam aan het bestand.")
		else:
			exc.readExcel(open_file_path,save_file_path, cal_name)
			messagebox.showinfo("Bestand aangemaakt", cal_name + " is opgeslagen op: " + save_file_path)

	def createParameterWindow(self):
		para_window = tk.Toplevel(root)
		para_window.title("Parameters")
		
		first_row_label = Label(para_window, width = para_width, text="Eerste rij:")
		first_row_var = StringVar()
		first_row_textbox = Entry(para_window, width = para_width, textvariable=first_row_var)

		last_row_label = Label(para_window, width = para_width, text="Laatste rij:")
		last_row_var = StringVar()
		last_row_textbox = Entry(para_window, width = para_width, textvariable=last_row_var)

		column_label = Label(para_window, width = para_width, text="Kolom:")

		date_label = Label(para_window, width = para_width, text="Datum:")
		date_var = StringVar()
		date_textbox = Entry(para_window, width = para_width, textvariable=date_var)

		time_begin_label = Label(para_window, width = para_width, text="Begintijd:")
		time_begin_var = StringVar()
		time_begin_textbox = Entry(para_window, width = para_width, textvariable=time_begin_var)

		time_end_label = Label(para_window, width = para_width, text="Eindtijd:")
		time_end_var = StringVar()
		time_end_textbox = Entry(para_window, width = para_width, textvariable=time_end_var)

		building_label = Label(para_window, width = para_width, text="Gebouw:")
		building_var = StringVar()
		building_textbox = Entry(para_window, width = para_width, textvariable=building_var)

		room_label = Label(para_window, width = para_width, text="Kamer:")
		room_var = StringVar()
		room_textbox = Entry(para_window, width = para_width, textvariable=room_var)

		course_label = Label(para_window, width = para_width, text="Vak:")
		course_var = StringVar()
		course_textbox = Entry(para_window, width = para_width, textvariable=course_var)

		lecturer_label = Label(para_window, width = para_width, text="Docent:")
		lecturer_var = StringVar()
		lecturer_textbox = Entry(para_window, width = para_width, textvariable=lecturer_var)

		# make the grid
		first_row_label.grid(row=0,column=0)
		first_row_textbox.grid(row=0,column=1)
		last_row_label.grid(row=1,column=0)
		last_row_textbox.grid(row=1,column=1)
		column_label.grid(row=2,column=1)
		date_label.grid(row=3,column=0)
		date_textbox.grid(row=3,column=1)
		time_begin_label.grid(row=4,column=0)
		time_begin_textbox.grid(row=4,column=1)
		time_end_label.grid(row=5,column=0)
		time_end_textbox.grid(row=5,column=1)
		building_label.grid(row=6,column=0)
		building_textbox.grid(row=6,column=1)
		room_label.grid(row=7,column=0)
		room_textbox.grid(row=7,column=1)
		course_label.grid(row=8,column=0)
		course_textbox.grid(row=8,column=1)
		lecturer_label.grid(row=9,column=0)
		lecturer_textbox.grid(row=9,column=1)

root = Tk()
root.title("eCalendar")

GUI = gui()

# button parameters
textbox_width = 50
button_width = 10
para_width = 10

# create buttons
open_button = Button(text='Open', width = button_width, command=GUI.openFile)

save_button = Button(text='Opslaan als', width = button_width, command=GUI.saveFile)

create_button = Button(text='Maak iCal', width = button_width, command=GUI.createFile)

parameter_button = Button(text='Parameters', width = button_width, command=GUI.createParameterWindow)

open_var = StringVar()
open_textbox = Entry(root, width = textbox_width, textvariable=open_var)

save_var = StringVar()
save_textbox = Entry(root, width = textbox_width, textvariable=save_var)

name_var = StringVar()
name_textbox = Entry(root, width = textbox_width, textvariable=name_var)

open_label = Label(root, width = textbox_width, text="In te lezen bestand:")

save_label = Label(root, width = textbox_width, text="Bestand opslaan als:")

name_label = Label(root, width = textbox_width, text="Kalendernaam:")

# make the grid
open_label.grid(row=0,column=0)
open_button.grid(row=1,column=2)
open_textbox.grid(row=1,column=0)#,padx=10, pady=10)

save_label.grid(row=2,column=0)
save_button.grid(row=3,column=2)
save_textbox.grid(row=3,column=0)

name_label.grid(row=4,column=0)
name_textbox.grid(row=5,column=0)
parameter_button.grid(row=6,column=2)
create_button.grid(row=6,column=0)

root.mainloop()

"""
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
#root.config(menu=menubar)
"""