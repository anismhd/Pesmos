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
		self.location = {'location': None, 'loc_var': None, 'depth':None}
		if ('latitude' in kwarg.keys()) and ('longitude' in kwarg.keys()):
			self.location['location'] = geodetic_coord(kwarg['latitude'],kwarg['longitude'])
		if 'loc_var' in kwarg.keys():
			self.location['loc_var'] = kwarg['loc_var']
		if 'depth' in kwarg.keys():
			self.location['depth'] = kwarg['depth']
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
		if 'depth' in kwarg.keys():
			self.location['depth'] = kwarg['depth']
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
	# String maniplation, operation overloaded
	def __repr__(self):
		if self.name:
			string = "\t{0:20s} : {1:s} \n".format('Name',self.name)
		else:
			string = "\t{0:20s} : [None] \n".format('Name')
		if self.region:
			string = string + "\t{0:20s} : {1:s} \n".format('Region',self.region)
		else:
			string = string + "\t{0:20s} : [None] \n".format('Region')
		if self.datetime:
			string = string + "\t{0:20s} : {1:s} \n".format('Date',self.datetime)
		else:
			string = string + "\t{0:20s} : [None] \n".format('Date')
		if self.magnitude['mag']:
			string = string + "\t{0:20s} : {1:4.2f}".format('Magnitude',self.magnitude['mag'])
		else:
			string = string + "\t{0:20s} : [None]".format('Magnitude')
		if self.magnitude['mag_var']:
			string = string + " error {1:6.3f}".format(self.magnitude['mag_var'])
		else:
			string = string + " error [None]"
		if self.magnitude['mag_type']:
			string = string + " {1:s}\n".format(self.magnitude['mag_type'])
		else:
			string = string + " [None]\n"
		if self.location['location']:
			string = string + "\t{0:20s} : {1:s}".format('Location',str(self.location['location']))
		else:
			string = string + "\t{0:20s} : [None]".format('Location')
		if self.location['loc_var']:
			string = string + " erros {0:f}\n".format(self.location['loc_var'])
		else:
			string = string + " erros [None]\n"
		if self.location['depth']:
			string = string + "\t{0:20s} : {1:6.2f}".format('Depth',self.location['depth'])
		else:
			string = string + "\t{0:20s} : [None]".format('Depth')
		return string
if __name__ == '__main__':
	'''
	This is a self test for earthquake_event_class
	'''
	event1 = earthquake_event_class()
	print event1