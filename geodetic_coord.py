'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 20/01/2017
'''
from numpy import sqrt
class geodetic_coord():
	def __init__(self,latitude, longitude):
		if isinstance(latitude, str):
			if len(latitude.split()) > 1:
				if ('S' in latitude.split()[1]) or ('s' in latitude.split()[1]):
					latitude = -1.0 * float(latitude.split()[0])
				else:
					latitude = float(latitude.split()[0])
			else:
				latitude = float(latitude)
		if isinstance(longitude, str):
			if len(longitude.split()) > 1:
				if ('W' in longitude.split()[1]) or ('w' in longitude.split()[1]):
					longitude = -1.0 * float(longitude.split()[0])
				else:
					longitude = float(longitude.split()[0])
			else:
				longitude = float(longitude)
		self.location = [latitude, longitude]
	def distance_from_point(self, point):
		R = 6371.0*(22.0/7.0)/180.0
		return sqrt(sum((self.location - point.location)*R)**2)
	def __repr__(self):
		if self.location[0] < 0:
			str_latitude = "{0:9.4f} S".format(abs(self.location[0]))
		else:
			str_latitude = "{0:9.4f} N".format(abs(self.location[0]))
		if self.location[1] < 0:
			str_longitude = "{0:9.4f} W".format(abs(self.location[1]))
		else:
			str_longitude = "{0:9.4f} E".format(abs(self.location[1]))
		return "({0:s},{1:s})".format(str_latitude,str_longitude)
'''
Self test mechanism
'''
if __name__ == '__main__':
	print "\n\nThis is a python class for geodetic co-ordinate system ..."
	print "\t Written by,"
	print "\t\t Anis Mohammed Vengasseri"
	print "\t\t anis.mhd@gmail.com"
	print "\t\t https://github.com/anismhd\n\n"
	print "\tTesing begin.."
	print "Demo 1 : Initialising one point in geodetic co-ordinate system (21.0,63.1)"
	point1 = geodetic_coord(21.0,63.1)
	print point1
	print "Initialising same point using string input 21.0 N, 63.1 E"
	point2 = geodetic_coord('21.0 N', '63.1 E')
	print point2

