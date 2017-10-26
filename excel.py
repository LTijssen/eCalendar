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

#creates datetime object
def createDatetime(date, time):
	return datetime.strptime(date+time, '%d%m%Y%H:%M')

#opens .xls file
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
 
    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    calendar = ical.ical()
    calendar.initCal("exceltest")

    # read data out of cells and make iCal
    for i in range(first_row,last_row):
    	date_cell = first_sheet.cell(i,date_col).value
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date_cell,book.datemode)
        day_data = '0' + str(day)
        month_data = '0' + str(month)
        year_data = str(year)
        date_data = day_data[-2:] + month_data[-2:] + year_data
    	time_begin_data = str(first_sheet.cell(i,time_begin_col).value)
    	time_end_data = str(first_sheet.cell(i,time_end_col).value)
    	subject_data = first_sheet.cell(i,course_col).value
    	location_data = first_sheet.cell(i,building_col).value + ' ' + first_sheet.cell(i,room_col).value
    	description_data = 'lecturer: ' + first_sheet.cell(i,lecturer_col).value
    	calendar.addEvent(createDatetime(date_data,time_begin_data),createDatetime(date_data,time_end_data),location_data,subject_data,description_data)
        calendar.deliverCal()
 
#----------------------------------------------------------------------
#if __name__ == "__main__":
    #path = "/home/lars/Documents/Jaar3/SE/files/Rooms master cs  fall 17-18.xls"
    #open_file(path)
    #print "Ical created"