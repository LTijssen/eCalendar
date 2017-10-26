import ical
from datetime import datetime
import xlrd

#first row and last row, later door eindgebruiker te bepalen
first_row = 4
last_row = 10

#columns with data
date_col = 2
time_begin_col = 3
time_end_col = 4
building_col = 5
room_col = 6
code_col = 7
course_col = 8
lecturer_col = 9

class excel:
	# creates datetime object
	def createDatetime(self, date, time):
		return datetime.strptime(date+time, '%d%m%Y%H:%M')

	# set integer to date DDMMYYY
	def intToDate(self, date_int, book):
		year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date_int,book.datemode)
		day_data = '0' + str(day)
		month_data = '0' + str(month)
		year_data = str(year)
		return day_data[-2:] + month_data[-2:] + year_data

	# reads .xls file
	def readExcel(self, open_file_path, save_file_path, cal_name):
		# Open and read an Excel file
		book = xlrd.open_workbook(open_file_path)

		# get the first worksheet
		first_sheet = book.sheet_by_index(0)

		calendar = ical.ical()
		calendar.initCal(cal_name)

		# read data out of cells and make iCal
		for i in range(first_row,last_row):
			date_data = self.intToDate(first_sheet.cell(i,date_col).value, book)
			time_begin_data = str(first_sheet.cell(i,time_begin_col).value)
			time_end_data = str(first_sheet.cell(i,time_end_col).value)
			subject_data = first_sheet.cell(i,course_col).value
			location_data = first_sheet.cell(i,building_col).value + ' ' + first_sheet.cell(i,room_col).value
			description_data = 'lecturer: ' + first_sheet.cell(i,lecturer_col).value
			calendar.addEvent(self.createDatetime(date_data,time_begin_data),
				self.createDatetime(date_data,time_end_data),
				location_data,
				subject_data,
				description_data)

		calendar.deliverCal(save_file_path)
		print "Ical created"
	 
	#----------------------------------------------------------------------
"""	
if __name__ == "__main__":
	path = "/home/lars/Documents/Jaar3/SE/files/Rooms master cs  fall 17-18.xls"
	exc = excel()
	exc.readExcel(path, "test123")
	#print "Ical created"

date_cell = first_sheet.cell(i,date_col).value
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date_cell,book.datemode)
        day_data = '0' + str(day)
        month_data = '0' + str(month)
        year_data = str(year)
        date_data = day_data[-2:] + month_data[-2:] + year_data
"""