

    pylab.rcParams['figure.figsize'] = (20, 15)
    from generating_figures import india_basemap
    import pickle


    station_data_from_file = pickle.load( open( "station_data_from_file.pickle", "rb" ) )

# Introduction

PESMOS is a project initiated by Earthquake Engineering Department of Indian
Institute of Technology Roorkee to study the ground motion characteristics of
Himalayan earthquakes using strong motion accelerographs. The project was funded
by Department of Science and Technology (DST), Government of India. The strong
motion accelarograph network covers various region of Indian seismic zones V, IV
and some thickly populated cities of seismic zone III. Out of 245 installed
accelarograms 193 station have recorded various earthquake events as shown in
Figure 1.


    station_color = {'A':'r','B':'g', 'C':'b', 'D':'y'}
    m = india_basemap('./')
    for station in station_data_from_file:
        site_cls = station_data_from_file[station]['Site Class'][0]
        if '200' in station_data_from_file[station]['Site Class']:
            site_cls = 'C'
        m.scatter([station_data_from_file[station]['Longitude']],[station_data_from_file[station]['Latitude']],\
                  s=100,latlon=True,marker='D',color=station_color[site_cls])
    m.scatter([0],[0], s=200,latlon=True,marker='D',color='r', label='Site Class A Vs30 between 700 m/sec to 1620 m/sec')
    m.scatter([0],[0], s=200,latlon=True,marker='D',color='g', label='Site Class B Vs30 between 375 m/sec to 700 m/sec')
    m.scatter([0],[0], s=200,latlon=True,marker='D',color='b', label='Site Class C Vs30 between 200 m/sec to 375 m/sec')
    title('Figure 1 :: Strong Motion Station of PESMOS')
    legend(scatterpoints=1)




    <matplotlib.legend.Legend at 0x7f9f3eee4490>




![png](README_files/README_4_1.png)



    len(station_data_from_file)




    193




    
