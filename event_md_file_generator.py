import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
from mpl_toolkits.basemap import Basemap
from generating_figure import gen_accl_figure
import math

pesmos_db_loc = "/home/anis/Desktop/GitHub/Pesmos_Original/DataProcessing/"
pesmos_events_final = pickle.load( open(pesmos_db_loc+'pesmos_events_final.pickle','rb') )
pesmos_event_id_index_pd = pickle.load( open(pesmos_db_loc+'pesmos_event_id_index_pd.pickle','rb') )
station_data_from_file = pickle.load( open(pesmos_db_loc+'station_data_from_file.pickle','rb') )

main_dir = './'

def points2distance(start,  end):
  """
    Calculate distance (in kilometers) between two points given as (long, latt) pairs
    based on Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula).
    Implementation inspired by JavaScript implementation from 
    http://www.movable-type.co.uk/scripts/latlong.html
    Accepts coordinates as tuples (deg, min, sec), but coordinates can be given 
    in any form - e.g. can specify only minutes:
    (0, 3133.9333, 0) 
    is interpreted as 
    (52.0, 13.0, 55.998000000008687)
    which, not accidentally, is the lattitude of Warsaw, Poland.
  """
  start_long = np.radians(start[0])
  start_latt = np.radians(start[1])
  end_long = np.radians(end[0])
  end_latt = np.radians(end[1])
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = np.sin(d_latt/2)**2 + np.cos(start_latt) * np.cos(end_latt) * np.sin(d_long/2)**2
  c = 2 * math.atan2(np.sqrt(a),  np.sqrt(1-a))
  return 6371 * c

def md_figure_gen(location, description):
	return '\n![{0:s}]({1:s})\n\n'.format(description,location)

def india_basemap(main_dir):
    m = Basemap(width=800000000,height=700000000,
            resolution='c',projection='poly',\
            lon_0=85.0,lat_0=25.0,llcrnrlon=70.,llcrnrlat=20.,urcrnrlon=100,urcrnrlat=36)
    # m.etopo()
    m.drawparallels(np.arange(20,42,1.),labels=[True])
    m.drawmeridians(np.arange(66.,100.,1.),labels=[False,True,True,False])
    m.readshapefile(main_dir+'IndiaMapShapefile/'+'Admin2','states')
    return m

def event_md_file_generator(PESMOS_FILE_ID):
	if not(PESMOS_FILE_ID in pesmos_event_id_index_pd.keys()):
		return False
	event = pesmos_event_id_index_pd[PESMOS_FILE_ID]
#	print pesmos_events_final[event]['Name'],pesmos_events_final[event]['Date']
	event_dir = main_dir+'/event_details/'+PESMOS_FILE_ID
	# Generating initial table about event
	f = open(event_dir+'/README.md', 'w')
	if not os.path.exists(event_dir):
		os.makedirs(event_dir)
	f.write('# {0:s},{1:s}, {2:s} [Mag Scale Unknown]\n'.format(pesmos_events_final[event]['Name'],\
		pesmos_events_final[event]['Date'].strftime("%A %d. %B %Y"),pesmos_events_final[event]['Magnitude in File']))
	if '-' in pesmos_events_final[event]['Name']:
	    event_name = pesmos_events_final[event]['Name'].split('-')[1]
	elif '_' in pesmos_events_final[event]['Name']:
	    event_name = pesmos_events_final[event]['Name'].split('_')[0]
	f.write('\n__Item__ | __Description__\n--- | ---\n')
	f.write('Events ID | {0:s}\n'.format( pesmos_events_final[event]['Event ID'] ))
	f.write('Filename in PESMOS database | {0:s}\n'.format(pesmos_events_final[event]['Name']))
	f.write('Date | {0:s}\n'.format(pesmos_events_final[event]['Date'].strftime("%A %d. %B %Y")))
	loc_str = 'Latitude:{0:7.3f}, Longitude:{1:7.3f}'.format(pesmos_events_final[event]['Location']['Latitude'],\
		pesmos_events_final[event]['Location']['Longitude'])
	f.write('Location | {0:s}\n'.format( loc_str ))
	station_list = ','.join(pesmos_events_final[event]['Stations'].keys())
	f.write('Station List | {0:s}\n'.format( station_list ))
	f.write('Magnitude in File [No Scale]| {0:s}\n'.format( pesmos_events_final[event]['Magnitude in File']))
	if 'USGS Data' in pesmos_events_final[event].keys():
		f.write('USGS ID | {0:s}\n'.format( pesmos_events_final[event]['USGS Data']['EventID']))
		mag_str = '{0:3.2f} {1:s}\n'.format( pesmos_events_final[event]['USGS Data']['Magnitude'],\
			pesmos_events_final[event]['USGS Data']['MagType'] )
		f.write('USGS Magnitude | {0:s}'.format(mag_str))
		loc_str = 'Latitude:{0:7.3f}, Longitude:{1:7.3f}'.format(pesmos_events_final[event]['USGS Data']['Latitude'],\
			pesmos_events_final[event]['USGS Data']['Longitude'])
		f.write('USGS Location | {0:s}\n'.format(loc_str))
		f.write('USGS Event Time | {0:s}\n'.format(pesmos_events_final[event]['USGS Data']['Time'].strftime("%A %d. %B %Y, %H:%M:%S")))
		f.write('USGS Depth | {0:.2f} km\n'.format(pesmos_events_final[event]['USGS Data']['Depth/km']))
	# Generating Event Location Figure
	plt.figure(figsize=(30,17))
	m = india_basemap(main_dir)
	file_loc_str = 'Location Reported in PESMOS File, Latitude:{0:7.3f}, Longitude:{1:7.3f}'.format(pesmos_events_final[event]['Location']['Latitude'],\
		pesmos_events_final[event]['Location']['Longitude'])
	m.scatter([ pesmos_events_final[event]['Location']['Longitude'] ],\
		[ pesmos_events_final[event]['Location']['Latitude'] ],s=90,latlon=True,marker='D',color='g', label=file_loc_str)
	if 'USGS Data' in pesmos_events_final[event].keys():
		usgs_loc_str = 'Location Reported in USGS Database, Latitude:{0:7.3f}, Longitude:{1:7.3f}'.format(pesmos_events_final[event]['USGS Data']['Latitude'],\
		pesmos_events_final[event]['USGS Data']['Longitude'])
		m.scatter([ pesmos_events_final[event]['USGS Data']['Longitude'] ],\
			[ pesmos_events_final[event]['USGS Data']['Latitude'] ],s=90,latlon=True,marker='D',color='r', label=usgs_loc_str)
	# Plot recorded station location
	for station in pesmos_events_final[event]['Stations']:
		m.scatter([ station_data_from_file[station]['Longitude'] ],\
		[ station_data_from_file[station]['Latitude'] ],s=90,latlon=True,marker='*', label=station)
	plt.legend(scatterpoints=1)
	plt.savefig(event_dir+'/event_loc.png')
	plt.close('all')
	f.write(md_figure_gen('event_loc.png', 'Location of Event and Stations Records'))
	# Generationg Station Data For Each Station
	for station in pesmos_events_final[event]['Stations']:
		fig = gen_accl_figure(pesmos_events_final[event]['Stations'][station])
		fig.savefig(event_dir+'/'+station+'.png')
		plt.close('all')
	# MD for Each Station
	for station in pesmos_events_final[event]['Stations']:
		f.write('\n## {0:s}, Station Data\n'.format(station))
		f.write(md_figure_gen(station+'.png', 'Accelaration data from {0:s} station'.format(station)))
		f.write('\n__Item__ | __Description__\n--- | ---\n')
		f.write('Station ID | {0:s}\n'.format( station ))
		f.write('Site Class | {0:s}\n'.format( station_data_from_file[station]['Site Class'][:-2] ))
		f.write('Location | Latitude:{0:7.3f}, Longitude:{1:7.3f}\n'.format(station_data_from_file[station]['Latitude'],\
			station_data_from_file[station]['Longitude']))
		distance_usgs = points2distance([pesmos_events_final[event]['USGS Data']['Longitude'],pesmos_events_final[event]['USGS Data']['Latitude']],  \
			[station_data_from_file[station]['Longitude'], station_data_from_file[station]['Latitude']])
		distance = points2distance([pesmos_events_final[event]['Location']['Longitude'],pesmos_events_final[event]['Location']['Latitude']],  \
			[station_data_from_file[station]['Longitude'], station_data_from_file[station]['Latitude']])
		f.write('Distance (km) | {0:10.4f} (PESMOS),{1:10.4f} (USGS) \n'.format( distance, distance_usgs ))
	f.close()
	return True

if __name__ == "__main__":
    event_md_file_generator('PESMOS0229')
    event_md_file_generator('PESMOS021900')