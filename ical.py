from datetime import datetime
from icalendar import Calendar, Event, vCalAddress, vText
cal = Calendar()

class ical:
	def initCal(self, cal_name):
		cal.add('VERSION', '2.0')
		cal.add('X-WR-CALNAME', cal_name)
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

	def deliverCal(self, save_file_path):
		cal_content = cal.to_ical()
		with open(save_file_path, 'wb') as f:
			f.write(cal_content)