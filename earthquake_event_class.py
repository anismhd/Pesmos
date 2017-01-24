'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 23/01/2017

	This module requires more detailed section ... may be a new repository exclusively
'''
from datetime import datetime
from geodetic_coord import geodetic_coord
class earthquake_event_class():
	"""
	An earthquake event class
	"""
	def __init__(self, **kwarg):
		''' Initialising self.datetime '''
		if (('year' in kwarg.keys()) and ('month' in kwarg.keys())) and ('day' in kwarg.keys()):
			if (('year' in kwarg.keys()) and ('month' in kwarg.keys())) and ('day' in kwarg.keys()):
				self.datetime = datetime(kwarg['year'],kwarg['month'],kwarg['day'],kwarg['hour'], \
					kwarg['minute'],kwarg['second'])
			else:
				self.datetime = datetime(kwarg['year'],kwarg['month'],kwarg['day'])
		else:
			self.datetime = None
		''' Initialising self.name '''
		if 'name' in kwarg.keys():
			self.name = kwarg['name']
		else:
			self.name = None
		''' Initialising self.region '''
		if 'region' in kwarg.keys():
			self.region = kwarg['region']
		else:
			self.region = None
		''' Initialising self.note '''
		if 'note' in kwarg.keys():
			self.note = kwarg['note']
		else:
			self.note = None
		''' Initialising self.magnitude '''
		self.magnitude = {'mag':None, 'mag_type':None, 'mag_var':None}
		if 'mag' in kwarg.keys():
			self.magnitude['mag'] = kwarg['mag']
		if 'mag_type' in kwarg.keys():
			self.magnitude['mag_type'] = kwarg['mag_type']
		if 'mag_var' in kwarg.keys():
			self.magnitude['mag_var'] = kwarg['mag_var']
		''' Initialising self.location '''
		self.location = {'location': None, 'loc_var': None}
		if ('latitude' in kwarg.keys()) and ('longitude' in kwarg.keys()):
			self.location['location'] = geodetic_coord(kwarg['latitude'],kwarg['longitude'])
		if 'loc_var' in kwarg.keys():
			self.location['loc_var'] = kwarg['loc_var']
	def eq_update_datetime(self, **kwarg):
		if (('year' in kwarg.keys()) and ('month' in kwarg.keys())) and ('day' in kwarg.keys()):
			if (('year' in kwarg.keys()) and ('month' in kwarg.keys())) and ('day' in kwarg.keys()):
				self.datetime = datetime(kwarg['year'],kwarg['month'],kwarg['day'],kwarg['hour'], \
					kwarg['minute'],kwarg['second'])
			else:
				self.datetime = datetime(kwarg['year'],kwarg['month'],kwarg['day'])
	def eq_update_location(self, **kwarg):
		if ('latitude' in kwarg.keys()) and ('longitude' in kwarg.keys()):
			self.location['location'] = geodetic_coord(kwarg['latitude'],kwarg['longitude'])
		if 'loc_var' in kwarg.keys():
			self.location['loc_var'] = kwarg['loc_var']
	def eq_update_name(self, name):
		self.name = name
	def eq_update_magnitude(self, **kwarg):
		if 'mag' in kwarg.keys():
			self.magnitude['mag'] = kwarg['mag']
		if 'mag_type' in kwarg.keys():
			self.magnitude['mag_type'] = kwarg['mag_type']
		if 'mag_var' in kwarg.keys():
			self.magnitude['mag_var'] = kwarg['mag_var']
	def eq_update_region(self, region):
		self.region = region
	def eq_update_note(self, note):
		self.note = note
if __name__ == '__main__':
	event1 = earthquake_event_class()