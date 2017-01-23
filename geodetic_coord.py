'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 20/01/2017

	This module requires more detailed section ... may be a new repository exclusively
'''
from numpy import sqrt, array, floor
# Following functions will convert geodetic co-ordinate value to degree, minute, second
def value_to_degree_minute_second(value):
    if value < 0.0:
        direct = False
    else:
        direct = True
    degree = int(value)
    minute = int((value-degree)*60.0)
    second = ((value-degree)*60.0 - minute)*60.0
    return abs(degree), abs(minute), abs(second), direct
# Following function function will convert degree, minute and second to value
def degree_minute_second_to_value(degree,minute,second, direct):
    if direct:
        return degree + (minute+(second/60.0))/60.0
    else:
        return -1.0*(degree + (minute+(second/60.0))/60.0)
# The following function are designed to parse string of geodetic co-ordinates
def parsing_geodetic_half(string):
    ascii = [45,46,48,49,50,51,52,53,54,54,55,56,57,78,83,87,69,110,115,119,101]
    prv_flag = False
    start = 0
    data = {}
    data_index = 0
    for i in range(len(string.strip())):
        if (not prv_flag) and (ord(string.strip()[i]) in ascii):
            start = i
            prv_flag = True
            continue
        if prv_flag and (not(ord(string.strip()[i]) in ascii)):
            prv_flag = False
            data[data_index] = string.strip()[start:i]
            data_index = data_index + 1
            continue
    if prv_flag:
        data[data_index] = string.strip()[start:]
    if len(data) == 1:
        value = float(data[0])
        degree, minute, second, direct = value_to_degree_minute_second(value)
    if len(data) == 2:
        if data[1] in ['N','n','E','e']:
            value = float(data[0])
        else:
            value = -1.0*float(data[0])
        degree, minute, second, direct = value_to_degree_minute_second(value)
    if len(data) == 4:
        degree = int(data[0])
        minute = int(data[1])
        second = float(data[2])
        if data[3] in ['N','n','E','e']:
            direct = True
        else:
            direct = False
    return {'value':value,'degree':degree,'minute':minute,'second':second,'direct':direct}
class geodetic_coord():
	def __init__(self,latitude, longitude):
		if isinstance(latitude, str):
			lat = parsing_geodetic_half(latitude)
		else:
			degree, minute, second, direct = value_to_degree_minute_second(latitude)
			lat = {'value':latitude,'degree':degree,'minute':minute,'second':second,'direct':direct}
		if isinstance(longitude, str):
			lon = parsing_geodetic_half(longitude)
		else:
			degree, minute, second, direct = value_to_degree_minute_second(longitude)
			lon = {'value':longitude,'degree':degree,'minute':minute,'second':second,'direct':direct}
		self.location = array([lat['value'], lon['value']])
		self.geodetic = [lat,lon]
	def distance_from_point(self, point):
		R = 6371.0*(22.0/7.0)/180.0
		return sqrt(sum((self.location - point.location)*R)**2)
	def __repr__(self):
		deg_sgn= u'\N{DEGREE SIGN}'
		if self.geodetic[0]['direct']:
			lat_dir = 'N'
		else:
			lat_dir = 'S'
		if self.geodetic[1]['direct']:
			lon_dir = 'E'
		else:
			lon_dir = 'W'
		return "{0:10.6f} {1:s},{2:10.6f} {3:s}".format(abs(self.location[0]),lat_dir,abs(self.location[1]),lon_dir)
#		return ("{0:2i}"+deg_sgn+" {1:2i}\' {2:8.5f}\" {3:s},"+"{4:2i}"+deg_sgn+" {5:2i}\' {6:8.5f}\" {7:s}").format\
#				(self.geodetic[0]['degree'],self.geodetic[0]['minute'],self.geodetic[0]['second'],lat_dir,\
#					self.geodetic[1]['degree'],self.geodetic[1]['minute'],self.geodetic[1]['second'],lat_dir)
#		if self.location[0] < 0.0:
#			str_latitude = "{0:9.4f} S".format(abs(self.location[0]))
#		else:
#			str_latitude = "{0:9.4f} N".format(abs(self.location[0]))
#		if self.location[1] < 0.0:
#			str_longitude = "{0:9.4f} W".format(abs(self.location[1]))
#		else:
#			str_longitude = "{0:9.4f} E".format(abs(self.location[1]))
#		return "({0:s},{1:s})".format(str_latitude,str_longitude)
#	def str_in_degree_minute_seconds(self):
#		deg_sign= u'\N{DEGREE SIGN}'
#		latitude_degree = int(self.location[0])
#		latitude_minute = int((self.location[0]-latitude_degree)*60)
#		latitude_second = (self.location[0] - latitude_degree - (latitude_minute/60.0))*60.0
#		longitude_degree = int(self.location[1])
#		longitude_minute = int((self.location[1]-longitude_degree)*60)
#		longitude_second = (self.location[1] - longitude_degree - (longitude_minute/60.0))*60.0
#		dirc = ['N','E']
#		if self.location[0] < 0.0:
#			dirc[0] = 'S'
#		if self.location[1] < 0.0:
#			dirc[1] = 'W'
#		return ("{0:2i}"+deg_sign+" {1:2i}\' {2:8.5f}\", {3:2i}"+deg_sign+" {4:2i}\' {5:8.5f}\"").format(\
#			latitude_degree,latitude_minute,latitude_second,longitude_degree,longitude_minute, longitude_second)
'''
Self test mechanism
'''
if __name__ == '__main__':
	print "\n\nThis is a python class for geodetic co-ordinate system ..."
	print "\t Written by,"
	print "\t\t Anis Mohammed Vengasseri"
	print "\t\t anis.mhd@gmail.com"
	print "\t\t https://github.com/anismhd\n\n"
	print "\tTesting begin.."
	print "Demo 1 : Initializing point1 in geodetic co-ordinate system (21.0,63.1)"
	point1 = geodetic_coord(21.0,63.1)
	print point1
	print "{0:2d} degree {1:2d} minute {2:8.5f} second {3}".format(point1.geodetic[0]['degree'],\
		point1.geodetic[0]['minute'], point1.geodetic[0]['second'], point1.geodetic[0]['direct']),\
	"{0:2d} degree {1:2d} minute {2:8.5f} second {3}".format(point1.geodetic[1]['degree'],\
		point1.geodetic[1]['minute'], point1.geodetic[1]['second'], point1.geodetic[1]['direct'])
	print "\nInitializing same point2 using string input 21.0 N, 63.1 E"
	point2 = geodetic_coord('21.0 N', '63.1 E')
	print point2
	print "{0:2d} degree {1:2d} minute {2:8.5f} second {3}".format(point2.geodetic[0]['degree'],\
		point2.geodetic[0]['minute'], point2.geodetic[0]['second'], point2.geodetic[0]['direct']),\
	"{0:2d} degree {1:2d} minute {2:8.5f} second {3}".format(point2.geodetic[1]['degree'],\
		point2.geodetic[1]['minute'], point2.geodetic[1]['second'], point2.geodetic[1]['direct'])
	print "Distance between point1 and point2 using distance_from_point = {0:10.4f}\n".format(point1.distance_from_point(point2))