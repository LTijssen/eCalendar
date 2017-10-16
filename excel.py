import ical
from datetime import datetime

lokaal = 302
vak = "se"

#creates datetime object
def createDatetime(date, time):
	return datetime.strptime(date+time, '%d/%m/%Y%H:%M')

class Excel:
	def parseExcel(self):
		#loop over sheet

	def parseExcel(self, line):


	def 

#Hardcoded testdata
DTSTART = "20171012T130000Z"
datum = "12/10/2017"
dag,maand,jaar = datum.split('/')
begintijd = "08:00"
eindtijd = "17:00"

calendar = ical.ical()
calendar.initCal()
calendar.addEvent(createDatetime(datum,begintijd), 
	createDatetime(datum,eindtijd),
	"liacs", 
	"Meeting", 
	"testmeeting")
calendar.addEvent(createDatetime(datum,begintijd), createDatetime(datum,eindtijd),
	"liacs", "Meeting2", "testmeeting2")
calendar.deliverCal()
print "Ical createds"