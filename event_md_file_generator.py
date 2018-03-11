import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

pesmos_db_loc = "/home/anis/Desktop/GitHub/Pesmos_Original/DataProcessing/"
pesmos_events_final = pickle.load( open(pesmos_db_loc+'pesmos_events_final.pickle','rb') )
pesmos_event_id_index_pd = pickle.load( open(pesmos_db_loc+'pesmos_event_id_index_pd.pickle','rb') )

main_dir = './'

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
	print pesmos_events_final[event].keys()
	event_dir = main_dir+'/event_details/'+PESMOS_FILE_ID
	f = open(event_dir+'/README.md', 'w')
	if not os.path.exists(event_dir):
		os.makedirs(event_dir)
	f.write('|Name | {0:s}|\n')
	f.close()
	return True

if __name__ == "__main__":
    event_md_file_generator('PESMOS0229')
    event_md_file_generator('PESMOS021900')