from datetime import datetime
from icalendar import Calendar, Event, vCalAddress, vText
cal = Calendar()

class ical:
	def initCal(self, calname):
		cal.add('VERSION', '2.0')
		cal.add('X-WR-CALNAME', calname)
		cal.add('X-WR-TIMEZONE','Europe/Brussels' )

	def addEvent(self,dt_obj_start,dt_obj_end,location,subject,description):
		event = Event()
		event.add('dtstart', dt_obj_start)
		event.add('dtend', dt_obj_end)
		event.add('summary', subject)
		event.add('location', location)
		event.add('description', description)
		#event['uid'] = '20050115T101010/27346262376@mxm.dk'
		cal.add_component(event)

	def deliverCal(self):
		cal_content = cal.to_ical()
		with open("meeting.ics", 'wb') as f:
			f.write(cal_content)
