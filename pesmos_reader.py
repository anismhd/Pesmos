'''
Program by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	https://github.com/anismhd

	Started Date :: 20/01/2017

	fname  - Should be the file name without '.ns', '.ew' or '.vt' extension
'''
import time
import numpy as np
def pesmos_reader(fname):
	data = open(fname).readlines()
'''
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
	event_date_time = data[0].strip('Origin Time').strip()
	event_latitude = data[1].strip('Lat.').strip()
	event_longitude = data[2].strip('Long.').strip()
	event_depth = data[3].strip('Depth (Km)').strip()
	event_magnitude = data[4].strip('Magnitude').strip()
	event_region = data[5].strip('Region').strip()
	event_source = data[6].strip()
	station_code = data[8].strip('Station Code').strip()
	station_latitude = data[9].strip('Station Lat.').strip()
	station_longitude = data[10].strip('Station Long.').strip()
	station_height = data[11].strip('Station Height(m)').strip()
	station_site_class = data[12].strip('Site Class').strip()
	station_record_time = data[13].strip('Record Time').strip()
	station_record_duration = data[14].strip('Sampling Rate').strip()
	station_sampling_rate = data[15].strip('Record Duration').strip()
	station_data_direction = data[16].strip('Direction').strip()
	station_data_pga = data[17].strip('Max. Acceleration').strip()
	station_data_filtering_info = data[21].strip()
	station_data_unit = data[22].strip('Acceleration data in').strip()
	station_data_number = len(data)-25
	station_data = np.zeros(station_data_number)
	for i in range(station_data_number):
		station_data[i] = float(data[24+i].strip())