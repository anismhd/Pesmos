'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 20/01/2017

	fname  - Should be the file name without '.ns', '.ew' or '.vt' extension

	if '.' in fname:
		print "fname  - Should be the file name without '.ns', '.ew' or '.vt' extension"
		return None
	NS = fname + ".ns"
	EW = fname + ".ew"
	VT = fname + ".vt"
	f_NS = open(NS).readlines()
	f_EW = open(EW).readlines()
	f_VT = open(VT).readlines()
'''
from datetime import datetime
import numpy as np
import pandas as pd
import re

def geodetic_string_proccessor(lat_str, lon_str):
	if ('N' in lat_str) or ('n' in lat_str):
		lat = float(lat_str[:-2].strip())
	elif ('S' in lat_str) or ('s' in lat_str):
		lat = -1.0*float(lat_str[:-2].strip())
	else:
		lat = float(lat_str.strip())
	if ('E' in lon_str) or ('e' in lon_str):
		lon = float(lon_str[:-2].strip())
	elif ('W' in lon_str) or ('w' in lon_str):
		lon = -1.0*float(lon_str[:-2].strip())
	else:
		lon = float(lon_str.strip())
	return lat, lon

def time_stripper(time_str):
	if int(re.split('\.|-|/|:',time_str)[0]) == 0:
		return None
	else:
		if 'UTC' in time_str:
			date, time, utc = time_str.split()
		else:
			date, time = time_str.split()
		day, month, year = re.split('\.|-|/|:',date)
		hour, minute, second = re.split('-|/|:',time)
		microsecond = (float(second)-np.floor(float(second)))*10**6
		second = int(np.floor(float(second)))
		return datetime(int(year),int(month),int(day),int(hour), int(minute), int(second), int(microsecond))

def pesmos_reader(fname):
	data = open(fname).readlines()
	event = {}
	event['Origin Time'] = time_stripper(data[0].strip('Origin Time').strip())
#	event['Latitude'] = data[1].strip('Lat.').strip()
#	event['Longitude'] = data[2].strip('Long.').strip()
	lat_str = data[1].strip('Lat.').strip()
	lon_str = data[2].strip('Long.').strip()
	event['Latitude'], event['Longitude'] = geodetic_string_proccessor(lat_str, lon_str)
	event['Depth'] = data[3].strip('Depth (Km)').strip()
	event['Magnitude'] = data[4].strip('Magnitude').strip()
	event['Region'] = data[5].strip('Region').strip()
	event['Source of Event Data'] = data[6].strip()
	station = {}
	station['Code'] = data[8].strip('Station Code').strip()
	lat_str = data[9].strip('Station Lat.').strip()
	lon_str = data[10].strip('Station Long.').strip()
	station['Latitude'],station['Longitude'] = geodetic_string_proccessor(lat_str, lon_str)
#	station['Height'] = float(data[11].strip('Station Height(m)').strip())
	station['Site class'] = data[12].strip('Site Class').strip()
	station['Record time'] = time_stripper(data[13].strip('Record Time').strip())
	station['Sampling rate'] = float(data[14].strip('Sampling Rate').strip()[:-2])
	station['Record_duration'] = float(data[15].strip('Record Duration').strip()[:-4])
	station['Data direction'] = data[16].strip('Direction').strip()
	station['Data PGA'] = data[17].strip('Max. Acceleration').strip()
	station['Data filtering info'] = data[21].strip()
	station['Data unit'] = data[22].strip('Acceleration data in').strip()
	station['Data number'] = int(station['Sampling rate']*station['Record_duration'])
	station['Data series'] = np.zeros(station['Data number'])
	for i in range(station['Data number']):
		station['Data series'][i] = float(data[24+i].strip())
	return event, station
