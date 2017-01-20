'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 20/01/2017
'''
class geodetic_coord():
	def __init__(self,latitude, longitude):
		self.location = [latitude, longitude]
	def stringinit(self, str_latitude, str_longitude):
		if len(str_latitude.split()) > 1:
			if ('S' in str_latitude.split()[1]) or ('s' in str_latitude.split()[1]):
				latitude = -1.0 * float(str_latitude.split()[0])
			else:
				latitude = float(str_latitude.split()[0])
		else:
			latitude = float(str_latitude)
		if len(str_longitude.split()) > 1:
			if ('W' in str_longitude.split()[1]) or ('w' in str_longitude.split()[1]):
				longitude = -1.0 * float(str_longitude.split()[0])
			else:
				longitude = float(str_longitude.split()[0])
		else:
			longitude = float(str_longitude)
		self.location = [latitude, longitude]
