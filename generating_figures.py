import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import pickle
import matplotlib.pyplot as plt

def india_basemap(main_dir):
    m = Basemap(width=800000000,height=700000000,
            resolution='c',projection='poly',\
            lon_0=85.0,lat_0=25.0,llcrnrlon=70.,llcrnrlat=20.,urcrnrlon=100,urcrnrlat=40)
    # m.etopo()
    m.drawparallels(np.arange(20,42,1.),labels=[True])
    m.drawmeridians(np.arange(66.,100.,1.),labels=[False,True,True,False])
    m.readshapefile(main_dir+'IndiaMapShapefile/'+'Admin2','states')
    return m

main_dir = '/home/anis/Desktop/GitHub/Pesmos/'

# Loading event and station dara from Pesmos-Events notebook
pesmos_events = pickle.load(open("pesmos_events.pickle","rb"))
station_data_from_file = pickle.load(open("station_data_from_file.pickle","rb"))
pesmos_stations = pickle.load( open( "pesmos_stations.pickle", "rb" ) )
for i in pesmos_events:
	plt.figure(figsize=(20,15))
	m = india_basemap(main_dir)
	m.scatter([ pesmos_events[i]['Location']['Longitude'] ],[ pesmos_events[i]['Location']['Latitude'] ],c='r',s=90,latlon=True,marker='*')
	for station in pesmos_events[i]['Stations']:
		m.scatter([ station_data_from_file[station]['Longitude'] ],[ station_data_from_file[station]['Latitude'] ],c='b',s=90,latlon=True,marker='D')
		x2, y2 = m( station_data_from_file[station]['Longitude'],station_data_from_file[station]['Latitude']-0.1)
		plt.text(x2, y2,station, fontweight='bold',horizontalalignment='center', verticalalignment='top')
	plt.savefig(pesmos_events[i]['Name']+'.png')
	plt.close('all')