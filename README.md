

    pylab.rcParams['figure.figsize'] = (20, 15)
    from generating_figures import india_basemap
    import pickle
    import pandas as pd
    pd.set_option('display.max_rows', None)


    pickle_files_loc = '/home/anis/Desktop/GitHub/Pesmos_Original/DataProcessing/'
    station_data_from_file = pickle.load( open( pickle_files_loc+"station_data_from_file.pickle", "rb" ) )
    pesmos_stations_final_pd = pickle.load( open( pickle_files_loc+"pesmos_stations_final_pd.pickle", "rb" ) )
    pesmos_stations = pickle.load( open( pickle_files_loc+"pesmos_stations.pickle", "rb" ) )
    pesmos_event_pd = pickle.load( open( pickle_files_loc+"pesmos_event_pd.pickle", "rb" ) )
    EventsWithMagnitude = pickle.load( open( pickle_files_loc+"EventsWithMagnitude.pickle", "rb" ) )
    EventsWithMoreThanThreeRecords = pickle.load( open( pickle_files_loc+"EventsWithMoreThanThreeRecords.pickle", "rb" ) )

# Introduction

PESMOS is a project initiated by Earthquake Engineering Department of Indian
Institute of Technology Roorkee to study the ground motion characteristics of
Himalayan earthquakes using strong motion accelerographs. The project was funded
by Department of Science and Technology (DST), Government of India. The strong
motion accelarograph network covers various region of Indian seismic zones V, IV
and some thickly populated cities of seismic zone III. Out of 298 installed
accelarograms 193 station have recorded various earthquake events as shown in
Figure 1.


    station_color = {'A':'r','B':'g', 'C':'b', 'D':'y'}
    m = india_basemap('./')
    for station in pesmos_stations:
        m.scatter([pesmos_stations[station]['Longitude']],[pesmos_stations[station]['Latitude']],\
                  s=25,latlon=True,marker='D',color= station_color[pesmos_stations[station]['Site class']] )
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='r', label='Site Class A Vs30 between 700 m/sec to 1620 m/sec')
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='g', label='Site Class B Vs30 between 375 m/sec to 700 m/sec')
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='b', label='Site Class C Vs30 between 200 m/sec to 375 m/sec')
    title('Figure 1 :: Strong Motion Station of PESMOS')
    legend(scatterpoints=1)




    <matplotlib.legend.Legend at 0x7f6c9b71e790>




![png](README_files/README_4_1.png)


# Accelarograph Stations

Indian Institute of Technology Roorkee install approaximately 293 strong motion
accelarograph in and around the Himalayas. The sites where these accelarograph
stations located are in various classes of sites. These sites are classified
into Class A, Class B and Class C as shown in Figure 1. The accelarograph used
was AC-63 GeoSIG triaxial force-balanced accelerometers and GSR-18 GeoSIG
18-bit  digitizers  with  external  GPS. The recording for all instruments is in
trigger mode at a sampling frequency of 200 sps. The triggering threshold was
initially set at 0.005 g for all the instruments. List of accelarograph stations
are shown in Table 1. As one can observe from the table, only 135 station have
functioned or recorded events out of 293 recording stations.


    print "Table 1 : List of PESMOS Stations"
    display(pesmos_stations_final_pd[['Station ID','Name','Location','Site Class','Site Geology','Record Available?']])

    Table 1 : List of PESMOS Stations



<div style="max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Station ID</th>
      <th>Name</th>
      <th>Location</th>
      <th>Site Class</th>
      <th>Site Geology</th>
      <th>Record Available?</th>
    </tr>
    <tr>
      <th>No</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>PDELH0004</td>
      <td>Dhaula Kuan</td>
      <td>Lat: 28.590,Lon: 77.170</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PDELH0005</td>
      <td>Raja Garden</td>
      <td>Lat: 28.660,Lon: 77.120</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PDELH0006</td>
      <td>Indraprastha University</td>
      <td>Lat: 28.660,Lon: 77.230</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PDELH0007</td>
      <td>IGNOU</td>
      <td>Lat: 28.490,Lon: 77.200</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PIITR0061</td>
      <td>Paonta Sahib</td>
      <td>Lat: 30.440,Lon: 77.620</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PIITR0018</td>
      <td>Dhumakot</td>
      <td>Lat: 29.750,Lon: 79.020</td>
      <td>A</td>
      <td>phyllites</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PIITR0019</td>
      <td>Garsain</td>
      <td>Lat: 30.050,Lon: 79.290</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>No</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PIITR0016</td>
      <td>Dhanaulti</td>
      <td>Lat: 30.430,Lon: 78.240</td>
      <td>B</td>
      <td>slates/siltstones/limestones/sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PIITR0017</td>
      <td>Dharchula</td>
      <td>Lat: 29.850,Lon: 80.550</td>
      <td>A</td>
      <td>phyllites/slates/limestones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PIITR0014</td>
      <td>Barkot</td>
      <td>Lat: 30.810,Lon: 78.210</td>
      <td>A</td>
      <td>granite/phyllite/slates</td>
      <td>No</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PIITR0015</td>
      <td>Chakrata</td>
      <td>Lat: 30.690,Lon: 77.900</td>
      <td>B</td>
      <td>slitstones/slates</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PIITR0012</td>
      <td>Udham Singh Nagar</td>
      <td>Lat: 29.000,Lon: 79.400</td>
      <td>C</td>
      <td>soil (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PIITR0013</td>
      <td>Uttarkashi</td>
      <td>Lat: 30.730,Lon: 78.440</td>
      <td>A</td>
      <td>quartzite/slates</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PIITR0010</td>
      <td>Rudraprayag</td>
      <td>Lat: 30.290,Lon: 78.980</td>
      <td>A</td>
      <td>quartzite/slates</td>
      <td>No</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PIITR0011</td>
      <td>Tehri</td>
      <td>Lat: 30.370,Lon: 78.430</td>
      <td>A</td>
      <td>phyllites</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PIITR0157</td>
      <td>Maharaj Ganj</td>
      <td>Lat: 27.140,Lon: 83.540</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PIITR0156</td>
      <td>Lucknow</td>
      <td>Lat: 26.850,Lon: 80.930</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PIITR0155</td>
      <td>Lakhimpur</td>
      <td>Lat: 27.950,Lon: 80.790</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PIITR0154</td>
      <td>KushuNagar</td>
      <td>Lat: 26.750,Lon: 83.760</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PIITR0153</td>
      <td>Kanpur</td>
      <td>Lat: 26.480,Lon: 80.350</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PIITR0152</td>
      <td>Kannauj</td>
      <td>Lat: 27.030,Lon: 79.920</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PIITR0151</td>
      <td>Jaunpur</td>
      <td>Lat: 25.730,Lon: 82.690</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PIITR0150</td>
      <td>Hathras</td>
      <td>Lat: 27.580,Lon: 77.980</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PIITR0221</td>
      <td>Purnia</td>
      <td>Lat: 25.770,Lon: 87.470</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PIITR0220</td>
      <td>Patna</td>
      <td>Lat: 25.620,Lon: 85.150</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PIITR0223</td>
      <td>Samastipur</td>
      <td>Lat: 25.860,Lon: 85.780</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PIITR0222</td>
      <td>Saharsa</td>
      <td>Lat: 25.890,Lon: 86.590</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PIITR0225</td>
      <td>Sitamari</td>
      <td>Lat: 26.560,Lon: 85.520</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PIITR0224</td>
      <td>Saupaul</td>
      <td>Lat: 26.130,Lon: 86.610</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PIITR0159</td>
      <td>Mathura</td>
      <td>Lat: 27.470,Lon: 77.690</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PIITR0158</td>
      <td>Mainpuri</td>
      <td>Lat: 27.240,Lon: 79.050</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>32</th>
      <td>PIITR0096</td>
      <td>Nakodar</td>
      <td>Lat: 31.120,Lon: 75.490</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>33</th>
      <td>PIITR0097</td>
      <td>Pathankot</td>
      <td>Lat: 32.270,Lon: 75.660</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>34</th>
      <td>PIITR0094</td>
      <td>Khanna</td>
      <td>Lat: 30.700,Lon: 76.240</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>35</th>
      <td>PIITR0095</td>
      <td>Mukerian</td>
      <td>Lat: 31.950,Lon: 75.610</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>36</th>
      <td>PIITR0092</td>
      <td>Dhar Kalan</td>
      <td>Lat: 32.410,Lon: 75.800</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>37</th>
      <td>PIITR0093</td>
      <td>GarhShankar</td>
      <td>Lat: 31.230,Lon: 76.130</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>38</th>
      <td>PIITR0090</td>
      <td>Dasua</td>
      <td>Lat: 31.810,Lon: 75.660</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>39</th>
      <td>PIITR0091</td>
      <td>Dera Baba Nanak</td>
      <td>Lat: 32.040,Lon: 75.020</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>40</th>
      <td>PIITR0180</td>
      <td>Chandpur</td>
      <td>Lat: 29.150,Lon: 78.260</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>41</th>
      <td>PDELH0003</td>
      <td>University of Delhi</td>
      <td>Lat: 28.690,Lon: 77.210</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>42</th>
      <td>PIITR0098</td>
      <td>Phagwara</td>
      <td>Lat: 31.210,Lon: 75.770</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>43</th>
      <td>PIITR0099</td>
      <td>Ambala</td>
      <td>Lat: 30.370,Lon: 76.770</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>44</th>
      <td>PIITR0278</td>
      <td>Dimapur</td>
      <td>Lat: 25.900,Lon: 93.730</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>No</td>
    </tr>
    <tr>
      <th>45</th>
      <td>PIITR0240</td>
      <td>Bongaigaon</td>
      <td>Lat: 26.470,Lon: 90.560</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>46</th>
      <td>PIITR0068</td>
      <td>Bhatinda</td>
      <td>Lat: 30.200,Lon: 74.950</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>47</th>
      <td>PIITR0023</td>
      <td>Kapkot</td>
      <td>Lat: 29.940,Lon: 79.900</td>
      <td>A</td>
      <td>dolomite/limestones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>48</th>
      <td>PIITR0022</td>
      <td>Joshimath</td>
      <td>Lat: 30.570,Lon: 79.580</td>
      <td>A</td>
      <td>granite/gneiss/quartzite</td>
      <td>No</td>
    </tr>
    <tr>
      <th>49</th>
      <td>PIITR0021</td>
      <td>Haldwani</td>
      <td>Lat: 29.220,Lon: 79.530</td>
      <td>C</td>
      <td>soil (slope washed)</td>
      <td>No</td>
    </tr>
    <tr>
      <th>50</th>
      <td>PIITR0020</td>
      <td>Ghansali</td>
      <td>Lat: 30.430,Lon: 78.660</td>
      <td>A</td>
      <td>quartzite/slates</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>51</th>
      <td>PIITR0027</td>
      <td>Laksar</td>
      <td>Lat: 29.740,Lon: 78.030</td>
      <td>C</td>
      <td>alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>52</th>
      <td>PIITR0026</td>
      <td>Kotdwar</td>
      <td>Lat: 29.750,Lon: 78.520</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>53</th>
      <td>PIITR0025</td>
      <td>Khatima</td>
      <td>Lat: 28.920,Lon: 79.970</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>54</th>
      <td>PIITR0024</td>
      <td>Kashipur</td>
      <td>Lat: 29.210,Lon: 78.960</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>55</th>
      <td>PIITR0140</td>
      <td>BulandShahar</td>
      <td>Lat: 28.400,Lon: 77.850</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>56</th>
      <td>PIITR0141</td>
      <td>Devria</td>
      <td>Lat: 26.500,Lon: 83.780</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>57</th>
      <td>PIITR0029</td>
      <td>Munsyari</td>
      <td>Lat: 30.070,Lon: 80.240</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>58</th>
      <td>PIITR0028</td>
      <td>Lansdown</td>
      <td>Lat: 29.840,Lon: 78.680</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>59</th>
      <td>PIITR0144</td>
      <td>Farrukhabad</td>
      <td>Lat: 27.360,Lon: 79.640</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>60</th>
      <td>PIITR0145</td>
      <td>Gaziabad</td>
      <td>Lat: 28.670,Lon: 77.450</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>61</th>
      <td>PIITR0146</td>
      <td>Gazipur</td>
      <td>Lat: 25.570,Lon: 83.570</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>62</th>
      <td>PIITR0147</td>
      <td>Gonda</td>
      <td>Lat: 27.130,Lon: 81.940</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>63</th>
      <td>PIITR0238</td>
      <td>Gangtok</td>
      <td>Lat: 27.350,Lon: 88.630</td>
      <td>A</td>
      <td>gneiss/schist</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>64</th>
      <td>PIITR0239</td>
      <td>Barpeta</td>
      <td>Lat: 26.330,Lon: 91.010</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>65</th>
      <td>PIITR0232</td>
      <td>Raxaul</td>
      <td>Lat: 26.980,Lon: 84.840</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>66</th>
      <td>PIITR0233</td>
      <td>Darjeeling</td>
      <td>Lat: 27.050,Lon: 88.260</td>
      <td>A</td>
      <td>gneiss/schist</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>67</th>
      <td>PIITR0230</td>
      <td>NarkatraGanj</td>
      <td>Lat: 27.100,Lon: 84.460</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>68</th>
      <td>PIITR0231</td>
      <td>Raghopur</td>
      <td>Lat: 26.300,Lon: 86.840</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>69</th>
      <td>PIITR0236</td>
      <td>Malda</td>
      <td>Lat: 25.000,Lon: 88.150</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>70</th>
      <td>PIITR0237</td>
      <td>Siliguri</td>
      <td>Lat: 26.710,Lon: 88.430</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>71</th>
      <td>PIITR0234</td>
      <td>Jalpaiguri</td>
      <td>Lat: 26.520,Lon: 88.730</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>72</th>
      <td>PIITR0235</td>
      <td>Kooch Vihar</td>
      <td>Lat: 26.320,Lon: 89.440</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>73</th>
      <td>PIITR0229</td>
      <td>Forbesganj</td>
      <td>Lat: 26.300,Lon: 87.250</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>74</th>
      <td>PIITR0228</td>
      <td>Bahadurganj</td>
      <td>Lat: 26.260,Lon: 87.830</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>75</th>
      <td>PIITR0050</td>
      <td>Dalhousie</td>
      <td>Lat: 32.520,Lon: 75.960</td>
      <td>A</td>
      <td>Quartzite, gneiss, schist, phyllite</td>
      <td>No</td>
    </tr>
    <tr>
      <th>76</th>
      <td>PIITR0007</td>
      <td>Nainital</td>
      <td>Lat: 29.380,Lon: 79.460</td>
      <td>B</td>
      <td>sandstones/slates/limestones/dolomites</td>
      <td>No</td>
    </tr>
    <tr>
      <th>77</th>
      <td>PIITR0266</td>
      <td>Nongstoin</td>
      <td>Lat: 25.520,Lon: 91.260</td>
      <td>A</td>
      <td>granite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>78</th>
      <td>PIITR0069</td>
      <td>Faridkot</td>
      <td>Lat: 30.680,Lon: 74.760</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>79</th>
      <td>PIITR0056</td>
      <td>Nathhpa</td>
      <td>Lat: 31.550,Lon: 77.920</td>
      <td>A</td>
      <td>gneissic complex</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>80</th>
      <td>PIITR0057</td>
      <td>Jogindernager</td>
      <td>Lat: 31.990,Lon: 76.800</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>81</th>
      <td>PIITR0034</td>
      <td>Didihat</td>
      <td>Lat: 29.770,Lon: 80.300</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>82</th>
      <td>PIITR0035</td>
      <td>Vikasnagar</td>
      <td>Lat: 30.450,Lon: 77.750</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>83</th>
      <td>PIITR0036</td>
      <td>Bilaspur</td>
      <td>Lat: 31.340,Lon: 76.760</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>84</th>
      <td>PIITR0037</td>
      <td>Chamba</td>
      <td>Lat: 32.550,Lon: 76.130</td>
      <td>A</td>
      <td>granitoids</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>85</th>
      <td>PIITR0030</td>
      <td>Patti</td>
      <td>Lat: 29.410,Lon: 79.930</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>86</th>
      <td>PIITR0031</td>
      <td>Ranikhet</td>
      <td>Lat: 29.640,Lon: 79.430</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>No</td>
    </tr>
    <tr>
      <th>87</th>
      <td>PIITR0032</td>
      <td>Rishikesh</td>
      <td>Lat: 30.120,Lon: 78.280</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>88</th>
      <td>PIITR0033</td>
      <td>Tanakpur</td>
      <td>Lat: 29.070,Lon: 80.110</td>
      <td>C</td>
      <td>alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>89</th>
      <td>PIITR0135</td>
      <td>Balia</td>
      <td>Lat: 25.770,Lon: 84.140</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>90</th>
      <td>PIITR0134</td>
      <td>Bahraich</td>
      <td>Lat: 27.570,Lon: 81.590</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>91</th>
      <td>PIITR0137</td>
      <td>Bareilly</td>
      <td>Lat: 28.340,Lon: 79.420</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>92</th>
      <td>PIITR0136</td>
      <td>Balrampur</td>
      <td>Lat: 27.440,Lon: 82.170</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>93</th>
      <td>PIITR0038</td>
      <td>Dharamshala</td>
      <td>Lat: 32.210,Lon: 76.320</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>94</th>
      <td>PIITR0039</td>
      <td>Hamirpur</td>
      <td>Lat: 31.690,Lon: 76.520</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>95</th>
      <td>PIITR0133</td>
      <td>Badaun</td>
      <td>Lat: 28.020,Lon: 79.130</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>96</th>
      <td>PIITR0132</td>
      <td>Azamgarh</td>
      <td>Lat: 26.060,Lon: 83.190</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>97</th>
      <td>PIITR0209</td>
      <td>Darbhanga</td>
      <td>Lat: 26.120,Lon: 85.900</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>98</th>
      <td>PIITR0208</td>
      <td>Chapra</td>
      <td>Lat: 25.780,Lon: 84.740</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>99</th>
      <td>PIITR0207</td>
      <td>Bihar Shariff</td>
      <td>Lat: 25.200,Lon: 85.520</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>100</th>
      <td>PIITR0206</td>
      <td>Bhagalpur</td>
      <td>Lat: 25.260,Lon: 86.990</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>101</th>
      <td>PIITR0205</td>
      <td>Bettiah</td>
      <td>Lat: 26.800,Lon: 84.520</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>102</th>
      <td>PIITR0204</td>
      <td>Banka</td>
      <td>Lat: 24.890,Lon: 86.910</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>103</th>
      <td>PIITR0203</td>
      <td>Araria</td>
      <td>Lat: 26.130,Lon: 87.470</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>104</th>
      <td>PIITR0058</td>
      <td>Nurpur</td>
      <td>Lat: 32.300,Lon: 75.880</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>105</th>
      <td>PIITR0201</td>
      <td>Utraula</td>
      <td>Lat: 27.310,Lon: 82.410</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>106</th>
      <td>PIITR0200</td>
      <td>Tulsipur(Jarwa)</td>
      <td>Lat: 27.530,Lon: 82.400</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>107</th>
      <td>PIITR0059</td>
      <td>Pachchhad</td>
      <td>Lat: 30.720,Lon: 77.190</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>108</th>
      <td>PIITR0003</td>
      <td>Chamoli</td>
      <td>Lat: 30.410,Lon: 79.320</td>
      <td>A</td>
      <td>quartzite, dolomites</td>
      <td>No</td>
    </tr>
    <tr>
      <th>109</th>
      <td>PIITR0197</td>
      <td>Sambhal</td>
      <td>Lat: 28.590,Lon: 78.580</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>110</th>
      <td>PIITR0008</td>
      <td>Pauri</td>
      <td>Lat: 30.150,Lon: 78.780</td>
      <td>A</td>
      <td>phyllites</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>111</th>
      <td>PIITR0196</td>
      <td>Pharenda</td>
      <td>Lat: 27.110,Lon: 83.270</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>112</th>
      <td>PIITR0160</td>
      <td>Meerut</td>
      <td>Lat: 28.990,Lon: 77.720</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>113</th>
      <td>PIITR0005</td>
      <td>Dehradun</td>
      <td>Lat: 30.320,Lon: 78.040</td>
      <td>C</td>
      <td>soil (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>114</th>
      <td>PIITR0085</td>
      <td>Taran Taran</td>
      <td>Lat: 31.450,Lon: 74.930</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>115</th>
      <td>PIITR0227</td>
      <td>Bagha</td>
      <td>Lat: 27.130,Lon: 84.060</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>116</th>
      <td>PIITR0004</td>
      <td>Champawat</td>
      <td>Lat: 29.330,Lon: 80.090</td>
      <td>A</td>
      <td>granite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>117</th>
      <td>PIITR0048</td>
      <td>Amb</td>
      <td>Lat: 31.690,Lon: 76.120</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>118</th>
      <td>PIITR0226</td>
      <td>Siwan</td>
      <td>Lat: 26.230,Lon: 84.360</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>119</th>
      <td>PIITR0256</td>
      <td>North Lakhimpur</td>
      <td>Lat: 27.240,Lon: 94.110</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>120</th>
      <td>PIITR0006</td>
      <td>Haridwar</td>
      <td>Lat: 29.970,Lon: 78.070</td>
      <td>C</td>
      <td>alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>121</th>
      <td>PIITR0128</td>
      <td>Car Nicobar</td>
      <td>Lat:  9.180,Lon: 92.820</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>122</th>
      <td>PIITR0129</td>
      <td>Port Blair</td>
      <td>Lat: 11.660,Lon: 92.740</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>123</th>
      <td>PIITR0126</td>
      <td>Hanumangarh</td>
      <td>Lat: 29.630,Lon: 74.290</td>
      <td>C</td>
      <td>Aeolian</td>
      <td>No</td>
    </tr>
    <tr>
      <th>124</th>
      <td>PIITR0127</td>
      <td>Jammu</td>
      <td>Lat: 32.730,Lon: 74.870</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>125</th>
      <td>PIITR0124</td>
      <td>Alwar</td>
      <td>Lat: 27.570,Lon: 76.590</td>
      <td>A</td>
      <td>gneiss/schist</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>126</th>
      <td>PIITR0125</td>
      <td>Bharatpur</td>
      <td>Lat: 27.210,Lon: 77.510</td>
      <td>C</td>
      <td>Aeolian</td>
      <td>No</td>
    </tr>
    <tr>
      <th>127</th>
      <td>PIITR0122</td>
      <td>Palwal</td>
      <td>Lat: 28.130,Lon: 77.330</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>128</th>
      <td>PIITR0123</td>
      <td>Sadhura</td>
      <td>Lat: 30.380,Lon: 77.220</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>129</th>
      <td>PIITR0120</td>
      <td>Hansi</td>
      <td>Lat: 29.090,Lon: 75.960</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>130</th>
      <td>PIITR0121</td>
      <td>Hodal</td>
      <td>Lat: 27.890,Lon: 77.380</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>131</th>
      <td>PIITR0041</td>
      <td>Kullu</td>
      <td>Lat: 31.960,Lon: 77.110</td>
      <td>A</td>
      <td>phyllite, quartzite, schist, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>132</th>
      <td>PIITR0040</td>
      <td>Keylong</td>
      <td>Lat: 32.560,Lon: 77.010</td>
      <td>A</td>
      <td>phyllite, quartzite, schist</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>133</th>
      <td>PIITR0043</td>
      <td>Nahan</td>
      <td>Lat: 30.560,Lon: 77.300</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>134</th>
      <td>PIITR0042</td>
      <td>Mandi</td>
      <td>Lat: 31.710,Lon: 76.930</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>135</th>
      <td>PIITR0045</td>
      <td>Shimla</td>
      <td>Lat: 31.110,Lon: 77.170</td>
      <td>A</td>
      <td>Quartzite, gneiss, schist</td>
      <td>No</td>
    </tr>
    <tr>
      <th>136</th>
      <td>PIITR0044</td>
      <td>RekongPeo</td>
      <td>Lat: 31.540,Lon: 78.270</td>
      <td>A</td>
      <td>granitoids and basic volcanics, gneiss and mag...</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>137</th>
      <td>PIITR0216</td>
      <td>Motihari</td>
      <td>Lat: 26.630,Lon: 84.900</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>138</th>
      <td>PIITR0217</td>
      <td>Munger</td>
      <td>Lat: 25.380,Lon: 86.460</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>139</th>
      <td>PIITR0218</td>
      <td>Muzzafarpur</td>
      <td>Lat: 26.120,Lon: 85.380</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>140</th>
      <td>PIITR0219</td>
      <td>Navada</td>
      <td>Lat: 24.890,Lon: 85.540</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>141</th>
      <td>PIITR0002</td>
      <td>Bageshwar</td>
      <td>Lat: 29.830,Lon: 79.770</td>
      <td>A</td>
      <td>quartzite, dolomites</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>142</th>
      <td>PDELH0011</td>
      <td>IIT Delhi</td>
      <td>Lat: 28.550,Lon: 77.190</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>143</th>
      <td>PIITR0210</td>
      <td>Gopalganj</td>
      <td>Lat: 26.470,Lon: 84.440</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>144</th>
      <td>PIITR0211</td>
      <td>Jamui</td>
      <td>Lat: 24.930,Lon: 86.230</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>145</th>
      <td>PDELH0002</td>
      <td>DCE, Bawana Road</td>
      <td>Lat: 28.800,Lon: 77.120</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>146</th>
      <td>PIITR0055</td>
      <td>Nalagarh</td>
      <td>Lat: 31.040,Lon: 76.720</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>147</th>
      <td>PIITR0212</td>
      <td>jehanabad</td>
      <td>Lat: 25.200,Lon: 84.990</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>148</th>
      <td>PIITR0213</td>
      <td>Katihar</td>
      <td>Lat: 25.560,Lon: 87.550</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>149</th>
      <td>PIITR0214</td>
      <td>kishanganj</td>
      <td>Lat: 26.100,Lon: 87.950</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>150</th>
      <td>PIITR0076</td>
      <td>Ludhiana</td>
      <td>Lat: 30.900,Lon: 75.840</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>151</th>
      <td>PIITR0215</td>
      <td>Madhubani</td>
      <td>Lat: 26.350,Lon: 86.070</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>152</th>
      <td>PIITR0113</td>
      <td>Panchkula</td>
      <td>Lat: 30.700,Lon: 76.870</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>153</th>
      <td>PIITR0112</td>
      <td>Panipat</td>
      <td>Lat: 29.400,Lon: 76.950</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>154</th>
      <td>PIITR0111</td>
      <td>Narnaul</td>
      <td>Lat: 28.060,Lon: 76.110</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>155</th>
      <td>PIITR0110</td>
      <td>Mewat</td>
      <td>Lat: 28.090,Lon: 77.000</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>156</th>
      <td>PIITR0117</td>
      <td>Sonipat</td>
      <td>Lat: 29.000,Lon: 77.000</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>157</th>
      <td>PIITR0047</td>
      <td>Una</td>
      <td>Lat: 31.470,Lon: 76.260</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>158</th>
      <td>PIITR0115</td>
      <td>Rohtak</td>
      <td>Lat: 28.900,Lon: 76.590</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>159</th>
      <td>PIITR0114</td>
      <td>Rewari</td>
      <td>Lat: 28.180,Lon: 76.610</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>160</th>
      <td>PIITR0119</td>
      <td>Ballabhgarh</td>
      <td>Lat: 28.340,Lon: 77.320</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>161</th>
      <td>PIITR0046</td>
      <td>Solan</td>
      <td>Lat: 30.910,Lon: 77.100</td>
      <td>A</td>
      <td>limestones, dolomite, sandstones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>162</th>
      <td>PIITR0087</td>
      <td>Anandpur Saheb</td>
      <td>Lat: 31.240,Lon: 76.490</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>163</th>
      <td>PIITR0052</td>
      <td>Jubbal</td>
      <td>Lat: 31.110,Lon: 77.660</td>
      <td>A</td>
      <td>granitoids and basic volcanics,gneiss and magm...</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>164</th>
      <td>PIITR0264</td>
      <td>Jowai</td>
      <td>Lat: 25.440,Lon: 92.200</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>165</th>
      <td>PIITR0199</td>
      <td>Shikohabad</td>
      <td>Lat: 27.110,Lon: 78.580</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>166</th>
      <td>PIITR0198</td>
      <td>Shamli</td>
      <td>Lat: 29.460,Lon: 77.340</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>167</th>
      <td>PIITR0261</td>
      <td>Boko</td>
      <td>Lat: 25.980,Lon: 91.230</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>168</th>
      <td>PIITR0260</td>
      <td>Tinsukia</td>
      <td>Lat: 27.500,Lon: 95.330</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>169</th>
      <td>PIITR0054</td>
      <td>Manali</td>
      <td>Lat: 32.250,Lon: 77.190</td>
      <td>A</td>
      <td>phyllite, quartzite, schist, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>170</th>
      <td>PIITR0262</td>
      <td>KataKhal</td>
      <td>Lat: 24.820,Lon: 92.620</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>171</th>
      <td>PIITR0193</td>
      <td>Nazibabad</td>
      <td>Lat: 29.610,Lon: 78.350</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>172</th>
      <td>PIITR0192</td>
      <td>Nautanwa</td>
      <td>Lat: 27.440,Lon: 83.420</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>173</th>
      <td>PIITR0191</td>
      <td>Nakur(Gangoh)</td>
      <td>Lat: 29.920,Lon: 77.300</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>174</th>
      <td>PIITR0190</td>
      <td>Mankapur</td>
      <td>Lat: 27.060,Lon: 82.210</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>175</th>
      <td>PIITR0269</td>
      <td>William nagar</td>
      <td>Lat: 25.510,Lon: 90.600</td>
      <td>A</td>
      <td>gneiss complex</td>
      <td>No</td>
    </tr>
    <tr>
      <th>176</th>
      <td>PIITR0268</td>
      <td>Tura</td>
      <td>Lat: 25.510,Lon: 90.220</td>
      <td>B</td>
      <td>sandstones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>177</th>
      <td>PIITR0195</td>
      <td>Palia</td>
      <td>Lat: 28.430,Lon: 80.580</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>178</th>
      <td>PIITR0194</td>
      <td>Nichlaul(Siswa)</td>
      <td>Lat: 27.310,Lon: 83.720</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>179</th>
      <td>PDELH0017</td>
      <td>Zakir Hussain College</td>
      <td>Lat: 28.640,Lon: 77.230</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>180</th>
      <td>PIITR0265</td>
      <td>Nongpoh</td>
      <td>Lat: 25.920,Lon: 91.880</td>
      <td>A</td>
      <td>granite</td>
      <td>No</td>
    </tr>
    <tr>
      <th>181</th>
      <td>PIITR0070</td>
      <td>Fathehgarh Saheb</td>
      <td>Lat: 30.650,Lon: 76.390</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>182</th>
      <td>PIITR0189</td>
      <td>Laharpur(Tambaur)</td>
      <td>Lat: 27.410,Lon: 80.890</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>183</th>
      <td>PIITR0188</td>
      <td>Kashganj</td>
      <td>Lat: 27.810,Lon: 78.640</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>184</th>
      <td>PIITR0071</td>
      <td>Firozpur</td>
      <td>Lat: 30.930,Lon: 74.610</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>185</th>
      <td>PDELH0016</td>
      <td>Jafarpur Kala</td>
      <td>Lat: 28.590,Lon: 76.910</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>186</th>
      <td>PIITR0072</td>
      <td>Gurdaspur</td>
      <td>Lat: 32.040,Lon: 75.410</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>187</th>
      <td>PIITR0104</td>
      <td>Hisar</td>
      <td>Lat: 29.130,Lon: 75.710</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>188</th>
      <td>PIITR0105</td>
      <td>Jhajjar</td>
      <td>Lat: 28.600,Lon: 76.660</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>189</th>
      <td>PIITR0106</td>
      <td>Jind</td>
      <td>Lat: 29.310,Lon: 76.340</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>190</th>
      <td>PIITR0107</td>
      <td>Kaithal</td>
      <td>Lat: 29.800,Lon: 76.420</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>191</th>
      <td>PIITR0100</td>
      <td>Bhiwani</td>
      <td>Lat: 28.810,Lon: 76.140</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>192</th>
      <td>PIITR0101</td>
      <td>Fatehabad</td>
      <td>Lat: 30.650,Lon: 76.390</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>193</th>
      <td>PIITR0102</td>
      <td>Faridabad</td>
      <td>Lat: 28.380,Lon: 77.320</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>194</th>
      <td>PIITR0103</td>
      <td>Gurgaon</td>
      <td>Lat: 28.450,Lon: 77.030</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>195</th>
      <td>PIITR0131</td>
      <td>Aligarh</td>
      <td>Lat: 27.910,Lon: 78.070</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>196</th>
      <td>PIITR0108</td>
      <td>Karnal</td>
      <td>Lat: 29.690,Lon: 77.000</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>197</th>
      <td>PIITR0109</td>
      <td>Kurukshetra</td>
      <td>Lat: 29.970,Lon: 76.870</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>198</th>
      <td>PIITR0130</td>
      <td>Agra</td>
      <td>Lat: 27.180,Lon: 78.010</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>199</th>
      <td>PIITR0276</td>
      <td>Yupia</td>
      <td>Lat: 27.150,Lon: 93.720</td>
      <td>B</td>
      <td>sandstones/shale</td>
      <td>No</td>
    </tr>
    <tr>
      <th>200</th>
      <td>PIITR0277</td>
      <td>Zero</td>
      <td>Lat: 27.540,Lon: 93.810</td>
      <td>B</td>
      <td>quartzite/schist/gneiss</td>
      <td>No</td>
    </tr>
    <tr>
      <th>201</th>
      <td>PIITR0274</td>
      <td>Itanagar</td>
      <td>Lat: 27.090,Lon: 93.610</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>202</th>
      <td>PIITR0064</td>
      <td>Saluni</td>
      <td>Lat: 32.700,Lon: 76.060</td>
      <td>A</td>
      <td>granitoids</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>203</th>
      <td>PIITR0272</td>
      <td>Bhalukpong</td>
      <td>Lat: 27.020,Lon: 92.640</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>204</th>
      <td>PIITR0273</td>
      <td>Bomdila</td>
      <td>Lat: 27.260,Lon: 92.420</td>
      <td>A</td>
      <td>gneiss/schist</td>
      <td>No</td>
    </tr>
    <tr>
      <th>205</th>
      <td>PIITR0270</td>
      <td>Aizawl</td>
      <td>Lat: 23.720,Lon: 92.730</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>206</th>
      <td>PIITR0271</td>
      <td>Kolasib</td>
      <td>Lat: 24.230,Lon: 92.680</td>
      <td>B</td>
      <td>sandstones</td>
      <td>No</td>
    </tr>
    <tr>
      <th>207</th>
      <td>PIITR0184</td>
      <td>Garh Mukteshwar</td>
      <td>Lat: 28.790,Lon: 78.090</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>208</th>
      <td>PIITR0185</td>
      <td>Gola Gokarnath</td>
      <td>Lat: 28.090,Lon: 80.460</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>209</th>
      <td>PIITR0186</td>
      <td>Hapur</td>
      <td>Lat: 28.730,Lon: 77.780</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>210</th>
      <td>PIITR0187</td>
      <td>Jansath(Khatauli)</td>
      <td>Lat: 29.330,Lon: 77.860</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>211</th>
      <td>PIITR0053</td>
      <td>Kasauli</td>
      <td>Lat: 30.900,Lon: 76.960</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>212</th>
      <td>PIITR0181</td>
      <td>Chhata(kosi)</td>
      <td>Lat: 29.720,Lon: 77.500</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>213</th>
      <td>PIITR0182</td>
      <td>Deoband</td>
      <td>Lat: 29.680,Lon: 77.680</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>214</th>
      <td>PIITR0183</td>
      <td>Dhampur</td>
      <td>Lat: 29.310,Lon: 78.500</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>215</th>
      <td>PIITR0171</td>
      <td>Sitapur</td>
      <td>Lat: 27.570,Lon: 80.680</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>216</th>
      <td>PIITR0084</td>
      <td>Mohali</td>
      <td>Lat: 30.730,Lon: 76.720</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>217</th>
      <td>PIITR0267</td>
      <td>Shilong</td>
      <td>Lat: 25.570,Lon: 91.890</td>
      <td>A</td>
      <td>quartzite</td>
      <td>No</td>
    </tr>
    <tr>
      <th>218</th>
      <td>PIITR0082</td>
      <td>Rupnagar</td>
      <td>Lat: 30.980,Lon: 76.520</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>219</th>
      <td>PDELH0001</td>
      <td>ANDC, Govindpuri</td>
      <td>Lat: 28.540,Lon: 77.260</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>220</th>
      <td>PIITR0116</td>
      <td>Sirsa</td>
      <td>Lat: 29.550,Lon: 75.050</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>221</th>
      <td>PIITR0148</td>
      <td>Gorakhpur</td>
      <td>Lat: 26.750,Lon: 83.370</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>222</th>
      <td>PIITR0001</td>
      <td>Almora</td>
      <td>Lat: 29.600,Lon: 79.660</td>
      <td>A</td>
      <td>schist, granodiorites, gneiss</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>223</th>
      <td>PIITR0088</td>
      <td>Batala</td>
      <td>Lat: 31.820,Lon: 75.200</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>224</th>
      <td>PIITR0078</td>
      <td>Moga</td>
      <td>Lat: 30.830,Lon: 75.150</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>225</th>
      <td>PIITR0079</td>
      <td>Muktsar</td>
      <td>Lat: 30.470,Lon: 74.540</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>226</th>
      <td>PIITR0249</td>
      <td>Jorhat</td>
      <td>Lat: 26.760,Lon: 94.210</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>227</th>
      <td>PIITR0248</td>
      <td>Hailakandi</td>
      <td>Lat: 24.680,Lon: 92.560</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>228</th>
      <td>PIITR0149</td>
      <td>Hardoi</td>
      <td>Lat: 27.400,Lon: 80.130</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>229</th>
      <td>PIITR0243</td>
      <td>Dibrugarh</td>
      <td>Lat: 27.470,Lon: 94.910</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>230</th>
      <td>PIITR0242</td>
      <td>Dhubri</td>
      <td>Lat: 26.020,Lon: 90.000</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>231</th>
      <td>PIITR0241</td>
      <td>Dhemaji</td>
      <td>Lat: 27.470,Lon: 94.560</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>232</th>
      <td>PIITR0073</td>
      <td>Hoshiarpur</td>
      <td>Lat: 31.520,Lon: 75.930</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>233</th>
      <td>PIITR0247</td>
      <td>Guwhati</td>
      <td>Lat: 26.190,Lon: 91.750</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>234</th>
      <td>PIITR0075</td>
      <td>Kapurthala</td>
      <td>Lat: 31.380,Lon: 75.380</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>235</th>
      <td>PDELH0020</td>
      <td>Ridge Observatory, IMD (NDI)</td>
      <td>Lat: 28.680,Lon: 77.210</td>
      <td>A</td>
      <td>Quartzite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>236</th>
      <td>PIITR0244</td>
      <td>Diphu</td>
      <td>Lat: 25.840,Lon: 93.440</td>
      <td>B</td>
      <td>shale/sandstones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>237</th>
      <td>PIITR0077</td>
      <td>Mansa</td>
      <td>Lat: 30.000,Lon: 75.410</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>238</th>
      <td>PIITR0170</td>
      <td>Sidharth Nagar</td>
      <td>Lat: 27.280,Lon: 83.070</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>239</th>
      <td>PIITR0173</td>
      <td>Anoop Sahar</td>
      <td>Lat: 28.350,Lon: 78.270</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>240</th>
      <td>PIITR0172</td>
      <td>SultanPur</td>
      <td>Lat: 26.260,Lon: 82.070</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>241</th>
      <td>PIITR0175</td>
      <td>Bansi</td>
      <td>Lat: 27.170,Lon: 82.930</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>242</th>
      <td>PIITR0174</td>
      <td>Baheri</td>
      <td>Lat: 28.780,Lon: 79.500</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>243</th>
      <td>PIITR0177</td>
      <td>Bisalpur</td>
      <td>Lat: 28.290,Lon: 79.800</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>244</th>
      <td>PIITR0176</td>
      <td>Baraut</td>
      <td>Lat: 29.100,Lon: 77.260</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>245</th>
      <td>PIITR0051</td>
      <td>Dehra</td>
      <td>Lat: 31.880,Lon: 76.220</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>246</th>
      <td>PIITR0178</td>
      <td>Biswan</td>
      <td>Lat: 27.490,Lon: 81.000</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>247</th>
      <td>PIITR0009</td>
      <td>Pithoragarh</td>
      <td>Lat: 29.580,Lon: 80.210</td>
      <td>A</td>
      <td>phyllites/slates/limestones blue with dots</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>248</th>
      <td>PDELH0008</td>
      <td>DJB, Karol Bagh</td>
      <td>Lat: 28.650,Lon: 77.190</td>
      <td>A</td>
      <td>Quartzite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>249</th>
      <td>PIITR0060</td>
      <td>Palampur</td>
      <td>Lat: 32.110,Lon: 76.540</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>250</th>
      <td>PIITR0202</td>
      <td>Ara</td>
      <td>Lat: 25.560,Lon: 84.660</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>251</th>
      <td>PIITR0118</td>
      <td>Yamunanagar</td>
      <td>Lat: 30.150,Lon: 77.290</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>252</th>
      <td>PDELH0009</td>
      <td>Alipur</td>
      <td>Lat: 28.800,Lon: 77.140</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>253</th>
      <td>PIITR0142</td>
      <td>Eta</td>
      <td>Lat: 27.560,Lon: 78.650</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>254</th>
      <td>PDELH0013</td>
      <td>NSIT, Dwarka.</td>
      <td>Lat: 28.610,Lon: 77.040</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>255</th>
      <td>PDELH0012</td>
      <td>JNU</td>
      <td>Lat: 28.540,Lon: 77.170</td>
      <td>A</td>
      <td>Quartzite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>256</th>
      <td>PIITR0139</td>
      <td>Bijnor</td>
      <td>Lat: 29.380,Lon: 78.130</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>257</th>
      <td>PDELH0010</td>
      <td>Jamia Millia Islamia</td>
      <td>Lat: 28.530,Lon: 77.270</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>258</th>
      <td>PIITR0258</td>
      <td>Silchar</td>
      <td>Lat: 24.830,Lon: 92.800</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>259</th>
      <td>PIITR0259</td>
      <td>Tejpur</td>
      <td>Lat: 26.620,Lon: 92.800</td>
      <td>B</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>260</th>
      <td>PDELH0015</td>
      <td>IGIPE, Vikas Puri</td>
      <td>Lat: 28.630,Lon: 77.070</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>261</th>
      <td>PDELH0014</td>
      <td>Maharaja Agrasen College, Mayur Vihar</td>
      <td>Lat: 28.600,Lon: 77.300</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>262</th>
      <td>PIITR0254</td>
      <td>Nalbari</td>
      <td>Lat: 26.450,Lon: 91.430</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>263</th>
      <td>PIITR0255</td>
      <td>Naogaon</td>
      <td>Lat: 26.350,Lon: 92.690</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>264</th>
      <td>PDELH0019</td>
      <td>Bhim Rao Ambedkar Colleger, Delhi</td>
      <td>Lat: 28.700,Lon: 77.290</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>265</th>
      <td>PIITR0257</td>
      <td>Sibsagar</td>
      <td>Lat: 26.990,Lon: 94.630</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>266</th>
      <td>PIITR0250</td>
      <td>Karimganj</td>
      <td>Lat: 24.870,Lon: 92.350</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>267</th>
      <td>PIITR0251</td>
      <td>Khokrajhar</td>
      <td>Lat: 26.400,Lon: 90.260</td>
      <td>C</td>
      <td>soils (slope washed)</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>268</th>
      <td>PIITR0252</td>
      <td>Mangaldai</td>
      <td>Lat: 26.440,Lon: 92.030</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>269</th>
      <td>PIITR0253</td>
      <td>Morigaon</td>
      <td>Lat: 26.250,Lon: 92.340</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>270</th>
      <td>PIITR0162</td>
      <td>MuzaffarNagar</td>
      <td>Lat: 29.470,Lon: 77.700</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>271</th>
      <td>PIITR0163</td>
      <td>Noida</td>
      <td>Lat: 28.510,Lon: 77.480</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>272</th>
      <td>PIITR0179</td>
      <td>Chandausi</td>
      <td>Lat: 29.460,Lon: 78.790</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>273</th>
      <td>PIITR0161</td>
      <td>Moradabad</td>
      <td>Lat: 28.850,Lon: 78.770</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>274</th>
      <td>PIITR0166</td>
      <td>Rai Bareilly</td>
      <td>Lat: 26.210,Lon: 81.250</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>275</th>
      <td>PIITR0167</td>
      <td>Rampur</td>
      <td>Lat: 28.790,Lon: 79.010</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>276</th>
      <td>PIITR0164</td>
      <td>Pratap Garh</td>
      <td>Lat: 25.920,Lon: 81.990</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>277</th>
      <td>PIITR0049</td>
      <td>Dadahu</td>
      <td>Lat: 30.600,Lon: 77.430</td>
      <td>B</td>
      <td>sandstones/shales</td>
      <td>No</td>
    </tr>
    <tr>
      <th>278</th>
      <td>PIITR0168</td>
      <td>Saharanpur</td>
      <td>Lat: 29.950,Lon: 77.550</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>279</th>
      <td>PIITR0169</td>
      <td>Shahjahanpur</td>
      <td>Lat: 27.890,Lon: 79.920</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>280</th>
      <td>PIITR0138</td>
      <td>Basti</td>
      <td>Lat: 26.790,Lon: 82.720</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>281</th>
      <td>PIITR0067</td>
      <td>Amritsar</td>
      <td>Lat: 31.640,Lon: 74.860</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>282</th>
      <td>PIITR0263</td>
      <td>Cherapunji</td>
      <td>Lat: 25.300,Lon: 91.700</td>
      <td>A</td>
      <td>quartzite</td>
      <td>No</td>
    </tr>
    <tr>
      <th>283</th>
      <td>PIITR0086</td>
      <td>Ajnala</td>
      <td>Lat: 31.840,Lon: 74.760</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>284</th>
      <td>PIITR0081</td>
      <td>Patiala</td>
      <td>Lat: 30.350,Lon: 76.380</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>285</th>
      <td>PIITR0080</td>
      <td>Nawanshahar</td>
      <td>Lat: 31.120,Lon: 76.120</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>286</th>
      <td>PIITR0083</td>
      <td>Sangrur</td>
      <td>Lat: 30.250,Lon: 75.840</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>287</th>
      <td>PIITR0066</td>
      <td>Tisa</td>
      <td>Lat: 32.840,Lon: 76.150</td>
      <td>A</td>
      <td>Phyllite, quartzite, schist</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>288</th>
      <td>PIITR0074</td>
      <td>Jallandhar</td>
      <td>Lat: 31.320,Lon: 75.590</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>289</th>
      <td>PIITR0089</td>
      <td>Chamkaur saheb</td>
      <td>Lat: 30.890,Lon: 76.420</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>290</th>
      <td>PIITR0065</td>
      <td>Sundernagar</td>
      <td>Lat: 31.520,Lon: 76.880</td>
      <td>A</td>
      <td>sandstones, shales, dolomite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>291</th>
      <td>PDELH0018</td>
      <td>NPTI, Badarpur</td>
      <td>Lat: 28.510,Lon: 77.300</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>292</th>
      <td>PIITR0275</td>
      <td>Seppa</td>
      <td>Lat: 27.280,Lon: 92.910</td>
      <td>A</td>
      <td>gneiss/schist</td>
      <td>No</td>
    </tr>
    <tr>
      <th>293</th>
      <td>PIITR0165</td>
      <td>Pilibhit</td>
      <td>Lat: 28.650,Lon: 79.820</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>294</th>
      <td>PIITR0246</td>
      <td>Golaghat</td>
      <td>Lat: 26.510,Lon: 93.970</td>
      <td>B</td>
      <td>sandstones</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>295</th>
      <td>PIITR0063</td>
      <td>Rampur</td>
      <td>Lat: 31.450,Lon: 77.630</td>
      <td>A</td>
      <td>granitoids and basic volcanics, phyllite</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>296</th>
      <td>PIITR0245</td>
      <td>Goalpara</td>
      <td>Lat: 26.160,Lon: 90.630</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>297</th>
      <td>PIITR0143</td>
      <td>Faizabad</td>
      <td>Lat: 26.770,Lon: 82.130</td>
      <td>C</td>
      <td>Alluvium</td>
      <td>No</td>
    </tr>
    <tr>
      <th>298</th>
      <td>PIITR0062</td>
      <td>Puh</td>
      <td>Lat: 31.760,Lon: 78.580</td>
      <td>A</td>
      <td>phyllite, quartzite, schist</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>


# Seimsic Events Recorded

The PESMOS stations located as shown in Figure 1 recorded 253 events. List of
events recorded by PESMOS stations and theis details are given in Table 2. Out
of 253 events only 170 records have magnitudes assigned to it. The 73 events
have more than three records.


    print "Table 2 : Events Recorded by Pesmos Stations"
    pesmos_event_pd

    Table 2 : Events Recorded by Pesmos Stations





<div style="max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Event ID</th>
      <th>Event Name</th>
      <th>Location</th>
      <th>Magnitude in Accl. File</th>
      <th>Recorded Stations</th>
      <th>Time Provided in Accl. File</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>231</th>
      <td>2005-12-14</td>
      <td>PESMOS0232</td>
      <td>20051214-Chamoli</td>
      <td>Lat: 30.90,Lon: 79.30</td>
      <td>5.2</td>
      <td>PIITR0027,PIITR0008,PIITR0004,PIITR0013,PIITR0...</td>
      <td>2005-12-14 07:09:48</td>
    </tr>
    <tr>
      <th>219</th>
      <td>2006-03-31</td>
      <td>PESMOS0220</td>
      <td>20060331-Jhajjar</td>
      <td>Lat: 28.70,Lon: 76.80</td>
      <td>3.4</td>
      <td>PIITR0115</td>
      <td>2006-03-31 11:25:39</td>
    </tr>
    <tr>
      <th>187</th>
      <td>2006-05-07</td>
      <td>PESMOS0188</td>
      <td>20060507-Jhajjar</td>
      <td>Lat: 28.70,Lon: 76.60</td>
      <td>4.1</td>
      <td>PIITR0115</td>
      <td>2006-05-07 16:01:00</td>
    </tr>
    <tr>
      <th>133</th>
      <td>2006-11-29</td>
      <td>PESMOS0134</td>
      <td>20061129-Alwar Earthquake</td>
      <td>Lat: 27.60,Lon: 76.70</td>
      <td>3.9</td>
      <td>PIITR0124</td>
      <td>2006-11-29 05:41:14</td>
    </tr>
    <tr>
      <th>105</th>
      <td>2006-12-10</td>
      <td>PESMOS0106</td>
      <td>20061210-Mandi Earthqake</td>
      <td>Lat: 31.50,Lon: 76.70</td>
      <td>3.5</td>
      <td>PIITR0042</td>
      <td>2006-12-10 08:19:29</td>
    </tr>
    <tr>
      <th>85</th>
      <td>2007-06-09</td>
      <td>PESMOS0086</td>
      <td>20070609-Bhagwanpur Earthquake</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0027</td>
      <td>None</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2007-06-22</td>
      <td>PESMOS0034</td>
      <td>20070622-Andaman</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0129</td>
      <td>None</td>
    </tr>
    <tr>
      <th>162</th>
      <td>2007-07-22</td>
      <td>PESMOS0163</td>
      <td>20070722-Uttarkashi</td>
      <td>Lat: 31.20,Lon: 78.20</td>
      <td>5.0</td>
      <td>PIITR0027,PIITR0056</td>
      <td>2007-07-22 23:02:12</td>
    </tr>
    <tr>
      <th>244</th>
      <td>2007-09-14</td>
      <td>PESMOS0245</td>
      <td>20070914-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>207</th>
      <td>2007-10-04</td>
      <td>PESMOS0208</td>
      <td>20071004-Chamba</td>
      <td>Lat: 32.50,Lon: 76.00</td>
      <td>3.8</td>
      <td>PIITR0037</td>
      <td>2007-10-04 05:14:15</td>
    </tr>
    <tr>
      <th>241</th>
      <td>2007-10-18</td>
      <td>PESMOS0242</td>
      <td>20071018-Noida</td>
      <td>Lat: 28.30,Lon: 77.60</td>
      <td>3.6</td>
      <td>PIITR0163</td>
      <td>2007-10-18 05:54:41</td>
    </tr>
    <tr>
      <th>82</th>
      <td>2007-10-28</td>
      <td>PESMOS0083</td>
      <td>20071028-Bilaspur</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0036</td>
      <td>None</td>
    </tr>
    <tr>
      <th>151</th>
      <td>2007-11-21</td>
      <td>PESMOS0152</td>
      <td>20071121-Morigaon</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0253</td>
      <td>None</td>
    </tr>
    <tr>
      <th>224</th>
      <td>2007-11-25</td>
      <td>PESMOS0225</td>
      <td>20071125-DELHI, Haryana Border Region</td>
      <td>Lat: 28.60,Lon: 77.00</td>
      <td>4.3</td>
      <td>PDELH0011,PIITR0117,PDELH0016,PDELH0014,PIITR0...</td>
      <td>2007-11-25 23:12:20</td>
    </tr>
    <tr>
      <th>98</th>
      <td>2007-12-14</td>
      <td>PESMOS0099</td>
      <td>20071214-Nathpa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0056</td>
      <td>None</td>
    </tr>
    <tr>
      <th>77</th>
      <td>2007-12-15</td>
      <td>PESMOS0078</td>
      <td>20071215-Nathpa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0056</td>
      <td>None</td>
    </tr>
    <tr>
      <th>111</th>
      <td>2007-12-16</td>
      <td>PESMOS0112</td>
      <td>20071216-Nathpa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0056</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2008-03-02</td>
      <td>PESMOS0004</td>
      <td>20080302-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>238</th>
      <td>2008-03-13</td>
      <td>PESMOS0239</td>
      <td>20080313-DARRANG, ASSAM</td>
      <td>Lat: 26.60,Lon: 91.80</td>
      <td>4.0</td>
      <td>PIITR0265,PIITR0253</td>
      <td>2008-03-13 15:42:38</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2008-03-18</td>
      <td>PESMOS0049</td>
      <td>20080318-Morigaon</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0253</td>
      <td>None</td>
    </tr>
    <tr>
      <th>243</th>
      <td>2008-03-19</td>
      <td>PESMOS0244</td>
      <td>20080319-Cooch Vihar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0235</td>
      <td>None</td>
    </tr>
    <tr>
      <th>101</th>
      <td>2008-03-21</td>
      <td>PESMOS0102</td>
      <td>20080321-Rampur</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0063</td>
      <td>None</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2008-03-22</td>
      <td>PESMOS0064</td>
      <td>20080322-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>227</th>
      <td>2008-04-28</td>
      <td>PESMOS0228</td>
      <td>20080428-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>100</th>
      <td>2008-05-24</td>
      <td>PESMOS0101</td>
      <td>20080524-Cooch Vihar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0235</td>
      <td>None</td>
    </tr>
    <tr>
      <th>124</th>
      <td>2008-05-29</td>
      <td>PESMOS0125</td>
      <td>20080529-DARRANG, ASSAM</td>
      <td>Lat: 26.60,Lon: 91.80</td>
      <td>4.2</td>
      <td>PIITR0265,PIITR0253</td>
      <td>2008-05-29 10:34:46</td>
    </tr>
    <tr>
      <th>239</th>
      <td>2008-05-29</td>
      <td>PESMOS0240</td>
      <td>20080529-Chamba(N.L.)</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>145</th>
      <td>2008-06-07</td>
      <td>PESMOS0146</td>
      <td>20080607-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2008-06-27</td>
      <td>PESMOS0011</td>
      <td>20080627-Andaman Island</td>
      <td>Lat: 11.00,Lon: 91.60</td>
      <td>6.7</td>
      <td>PIITR0129</td>
      <td>2008-06-27 11:40:16</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2008-07-07</td>
      <td>PESMOS0085</td>
      <td>20080707-NAGALAND ( INDIA) -- MYANMAR BORDER R...</td>
      <td>Lat: 26.10,Lon: 95.10</td>
      <td>5.1</td>
      <td>PIITR0260</td>
      <td>2008-07-07 02:50:36</td>
    </tr>
    <tr>
      <th>208</th>
      <td>2008-07-17</td>
      <td>PESMOS0209</td>
      <td>20080717-Cooch Vihar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0235</td>
      <td>None</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2008-07-26</td>
      <td>PESMOS0073</td>
      <td>20080726-Bangladesh India border</td>
      <td>Lat: 24.80,Lon: 90.60</td>
      <td>4.8</td>
      <td>PIITR0240</td>
      <td>2008-07-26 18:51:53</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2008-08-10</td>
      <td>PESMOS0065</td>
      <td>20080810-Andaman Island</td>
      <td>Lat: 11.10,Lon: 91.60</td>
      <td>6.0</td>
      <td>PIITR0129</td>
      <td>2008-08-10 08:20:34</td>
    </tr>
    <tr>
      <th>250</th>
      <td>2008-08-19</td>
      <td>PESMOS0251</td>
      <td>20080819-PITHORAGARH, Uttarakhand</td>
      <td>Lat: 30.10,Lon: 80.10</td>
      <td>4.3</td>
      <td>PIITR0023,PIITR0004,PIITR0029,PIITR0009</td>
      <td>2008-08-19 10:54:26</td>
    </tr>
    <tr>
      <th>172</th>
      <td>2008-09-04</td>
      <td>PESMOS0173</td>
      <td>20080904-(UTTARAKHAND)-TIBET Border</td>
      <td>Lat: 30.10,Lon: 80.40</td>
      <td>5.1</td>
      <td>PIITR0023,PIITR0022,PIITR0020,PIITR0009,PIITR0...</td>
      <td>2008-09-04 12:53:21</td>
    </tr>
    <tr>
      <th>93</th>
      <td>2008-09-06</td>
      <td>PESMOS0094</td>
      <td>20080906-Hindukush</td>
      <td>Lat: 36.70,Lon: 70.60</td>
      <td>5.8</td>
      <td>PIITR0041,PIITR0036</td>
      <td>2008-09-06 05:47:33</td>
    </tr>
    <tr>
      <th>118</th>
      <td>2008-10-19</td>
      <td>PESMOS0119</td>
      <td>20081019-Sonipat</td>
      <td>Lat: 29.10,Lon: 76.90</td>
      <td>3.2</td>
      <td>PIITR0117</td>
      <td>2008-10-19 07:56:48</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2008-10-21</td>
      <td>PESMOS0104</td>
      <td>20081021-Kullu</td>
      <td>Lat: 31.50,Lon: 77.30</td>
      <td>4.5</td>
      <td>PIITR0041,PIITR0042,PIITR0063</td>
      <td>2008-10-21 15:09:06</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2008-11-19</td>
      <td>PESMOS0068</td>
      <td>20081119-Khokhrajhar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0251</td>
      <td>None</td>
    </tr>
    <tr>
      <th>216</th>
      <td>2008-12-02</td>
      <td>PESMOS0217</td>
      <td>20081202-Khokhrajhar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0251</td>
      <td>None</td>
    </tr>
    <tr>
      <th>60</th>
      <td>2008-12-26</td>
      <td>PESMOS0061</td>
      <td>20081226-Diphu</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0244</td>
      <td>None</td>
    </tr>
    <tr>
      <th>195</th>
      <td>2008-12-31</td>
      <td>PESMOS0196</td>
      <td>20081231-Nathpa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0056</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2009-01-03</td>
      <td>PESMOS0002</td>
      <td>20090103-HINDUKUSH REGION,AFGHANISTAN</td>
      <td>Lat: 36.50,Lon: 70.80</td>
      <td>6.4</td>
      <td>PIITR0040</td>
      <td>2009-01-03 20:23:19</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2009-01-09</td>
      <td>PESMOS0045</td>
      <td>20090109-Kinnaur</td>
      <td>Lat: 31.70,Lon: 78.30</td>
      <td>3.8</td>
      <td>PIITR0056,PIITR0044</td>
      <td>2009-01-09 12:40:18</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2009-01-11</td>
      <td>PESMOS0141</td>
      <td>20090111-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2009-01-13</td>
      <td>PESMOS0043</td>
      <td>20090113-Delhi</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PDELH0004,PDELH0001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>146</th>
      <td>2009-01-24</td>
      <td>PESMOS0147</td>
      <td>20090124-Nongstoin</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0265</td>
      <td>None</td>
    </tr>
    <tr>
      <th>121</th>
      <td>2009-01-31</td>
      <td>PESMOS0122</td>
      <td>20090131-Himachal</td>
      <td>Lat: 32.50,Lon: 75.90</td>
      <td>3.7</td>
      <td>PIITR0040,PIITR0037,PIITR0038</td>
      <td>2009-01-31 03:07:15</td>
    </tr>
    <tr>
      <th>202</th>
      <td>2009-02-14</td>
      <td>PESMOS0203</td>
      <td>20090214-Munsiary</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0029</td>
      <td>None</td>
    </tr>
    <tr>
      <th>127</th>
      <td>2009-02-15</td>
      <td>PESMOS0128</td>
      <td>20090215-Assam-Meghalara Border</td>
      <td>Lat: 26.00,Lon: 90.20</td>
      <td>4.4</td>
      <td>PIITR0242,PIITR0239,PIITR0240,PIITR0251,PIITR0268</td>
      <td>2009-02-15 07:35:55</td>
    </tr>
    <tr>
      <th>112</th>
      <td>2009-02-24</td>
      <td>PESMOS0113</td>
      <td>20090224-INDIA( NAGALAND) -- MYANMAR BORD. REG</td>
      <td>Lat: 25.90,Lon: 94.30</td>
      <td>4.8</td>
      <td>PIITR0256,PIITR0246,PIITR0244</td>
      <td>2009-02-24 17:46:13</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2009-02-25</td>
      <td>PESMOS0103</td>
      <td>20090225-ttarakhand</td>
      <td>Lat: 30.60,Lon: 79.30</td>
      <td>3.7</td>
      <td>PIITR0003</td>
      <td>2009-02-25 04:04:21</td>
    </tr>
    <tr>
      <th>73</th>
      <td>2009-03-18</td>
      <td>PESMOS0074</td>
      <td>20090318-Uttarkashi,Uttarakhand</td>
      <td>Lat: 30.90,Lon: 78.20</td>
      <td>3.3</td>
      <td>PIITR0013</td>
      <td>2009-03-18 11:22:42</td>
    </tr>
    <tr>
      <th>185</th>
      <td>2009-04-04</td>
      <td>PESMOS0186</td>
      <td>20090404-Golpara</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0245</td>
      <td>None</td>
    </tr>
    <tr>
      <th>193</th>
      <td>2009-04-10</td>
      <td>PESMOS0194</td>
      <td>20090410-Giolpara</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0245</td>
      <td>None</td>
    </tr>
    <tr>
      <th>58</th>
      <td>2009-04-17</td>
      <td>PESMOS0059</td>
      <td>20090417-Diphu</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0244</td>
      <td>None</td>
    </tr>
    <tr>
      <th>61</th>
      <td>2009-04-25</td>
      <td>PESMOS0062</td>
      <td>20090425-Kamrup</td>
      <td>Lat: 26.40,Lon: 91.70</td>
      <td>4.0</td>
      <td>PIITR0247,PIITR0261</td>
      <td>2009-04-25 14:29:29</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2009-05-04</td>
      <td>PESMOS0100</td>
      <td>20090504-Bongaigaon</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0264</td>
      <td>None</td>
    </tr>
    <tr>
      <th>71</th>
      <td>2009-05-06</td>
      <td>PESMOS0072</td>
      <td>20090506-Khokhrajhar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0251</td>
      <td>None</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2009-05-15</td>
      <td>PESMOS0144</td>
      <td>20090515-Chamoli, Uttarakhand</td>
      <td>Lat: 30.50,Lon: 79.30</td>
      <td>4.1</td>
      <td>PIITR0003</td>
      <td>2009-05-15 18:39:22</td>
    </tr>
    <tr>
      <th>211</th>
      <td>2009-05-16</td>
      <td>PESMOS0212</td>
      <td>20090516-Khokhrajhar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0251</td>
      <td>None</td>
    </tr>
    <tr>
      <th>54</th>
      <td>2009-06-04</td>
      <td>PESMOS0055</td>
      <td>20090604-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>249</th>
      <td>2009-06-19</td>
      <td>PESMOS0250</td>
      <td>20090619-Golpara</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0245</td>
      <td>None</td>
    </tr>
    <tr>
      <th>138</th>
      <td>2009-06-22</td>
      <td>PESMOS0139</td>
      <td>20090622-Diphu</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0244</td>
      <td>None</td>
    </tr>
    <tr>
      <th>90</th>
      <td>2009-07-13</td>
      <td>PESMOS0091</td>
      <td>20090713-Cooch Vihar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0235</td>
      <td>None</td>
    </tr>
    <tr>
      <th>62</th>
      <td>2009-07-17</td>
      <td>PESMOS0063</td>
      <td>20090717-Chamba</td>
      <td>Lat: 32.30,Lon: 76.10</td>
      <td>3.7</td>
      <td>PIITR0040,PIITR0037,PIITR0038</td>
      <td>2009-07-17 11:07:47</td>
    </tr>
    <tr>
      <th>201</th>
      <td>2009-07-26</td>
      <td>PESMOS0202</td>
      <td>20090726-Golpara</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0245</td>
      <td>None</td>
    </tr>
    <tr>
      <th>144</th>
      <td>2009-08-03</td>
      <td>PESMOS0145</td>
      <td>20090803-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2009-08-10</td>
      <td>PESMOS0019</td>
      <td>20090810-Andaman Island</td>
      <td>Lat: 14.10,Lon: 93.01</td>
      <td>7.8</td>
      <td>PIITR0129</td>
      <td>2009-08-10 19:55:35</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2009-08-11</td>
      <td>PESMOS0040</td>
      <td>20090811-Khokhrajhar(N.L.)</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0251</td>
      <td>None</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2009-08-11</td>
      <td>PESMOS0020</td>
      <td>20090811-MYANMAR-India Manipuir Border</td>
      <td>Lat: 24.40,Lon: 94.80</td>
      <td>5.6</td>
      <td>PIITR0248,PIITR0258,PIITR0259,PIITR0247,PIITR0...</td>
      <td>2009-08-11 21:43:39</td>
    </tr>
    <tr>
      <th>134</th>
      <td>2009-08-16</td>
      <td>PESMOS0135</td>
      <td>20090816-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>212</th>
      <td>2009-08-19</td>
      <td>PESMOS0213</td>
      <td>20090819-Sonitpur-Assam</td>
      <td>Lat: 26.60,Lon: 92.50</td>
      <td>4.9</td>
      <td>PIITR0247,PIITR0261</td>
      <td>2009-08-19 10:45:15</td>
    </tr>
    <tr>
      <th>123</th>
      <td>2009-08-27</td>
      <td>PESMOS0124</td>
      <td>20090827-Uttarakhand</td>
      <td>Lat: 30.00,Lon: 80.00</td>
      <td>3.9</td>
      <td>PIITR0023,PIITR0029,PIITR0002</td>
      <td>2009-08-27 16:54:15</td>
    </tr>
    <tr>
      <th>240</th>
      <td>2009-08-30</td>
      <td>PESMOS0241</td>
      <td>20090830-Manipur meghalaya Border Region</td>
      <td>Lat: 25.40,Lon: 94.80</td>
      <td>5.3</td>
      <td>PIITR0247,PIITR0256,PIITR0261,PIITR0268,PIITR0244</td>
      <td>2009-08-30 19:27:44</td>
    </tr>
    <tr>
      <th>235</th>
      <td>2009-09-03</td>
      <td>PESMOS0236</td>
      <td>20090903-Miyamar India Border Region</td>
      <td>Lat: 24.30,Lon: 94.60</td>
      <td>5.9</td>
      <td>PIITR0248,PIITR0258,PIITR0240,PIITR0247,PIITR0...</td>
      <td>2009-09-03 19:51:08</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2009-09-21</td>
      <td>PESMOS0013</td>
      <td>20090921-Uttarkashi</td>
      <td>Lat: 30.90,Lon: 79.10</td>
      <td>4.7</td>
      <td>PIITR0023,PIITR0020,PIITR0016,PIITR0028,PIITR0...</td>
      <td>2009-09-21 09:43:47</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2009-09-21</td>
      <td>PESMOS0003</td>
      <td>20090921-Bhutan</td>
      <td>Lat: 27.30,Lon: 91.50</td>
      <td>6.2</td>
      <td>PIITR0259,PIITR0255,PIITR0256,PIITR0240,PIITR0...</td>
      <td>2009-09-21 08:53:04</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2009-10-03</td>
      <td>PESMOS0010</td>
      <td>20091003-Bageshwar</td>
      <td>Lat: 30.00,Lon: 79.90</td>
      <td>4.3</td>
      <td>PIITR0023,PIITR0004,PIITR0002</td>
      <td>2009-10-03 05:20:54</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2009-10-22</td>
      <td>PESMOS0005</td>
      <td>20091022-Hindukush</td>
      <td>Lat: 36.50,Lon: 71.00</td>
      <td>6.3</td>
      <td>PIITR0040,PIITR0051,PIITR0063,PIITR0056,PIITR0053</td>
      <td>2009-10-22 19:51:25</td>
    </tr>
    <tr>
      <th>117</th>
      <td>2009-10-27</td>
      <td>PESMOS0118</td>
      <td>20091027-Patiala</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0081</td>
      <td>None</td>
    </tr>
    <tr>
      <th>158</th>
      <td>2009-10-29</td>
      <td>PESMOS0159</td>
      <td>20091029-Bhutan</td>
      <td>Lat: 27.30,Lon: 91.40</td>
      <td>5.2</td>
      <td>PIITR0266,PIITR0240,PIITR0251,PIITR0245,PIITR0268</td>
      <td>2009-10-29 17:00:35</td>
    </tr>
    <tr>
      <th>59</th>
      <td>2009-10-29</td>
      <td>PESMOS0060</td>
      <td>20091029-Khokhrajhar</td>
      <td>Lat: 26.60,Lon: 90.00</td>
      <td>4.2</td>
      <td>PIITR0266,PIITR0240,PIITR0251,PIITR0245,PIITR0268</td>
      <td>2009-10-29 19:56:58</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2009-10-29</td>
      <td>PESMOS0028</td>
      <td>20091029-Hindukush</td>
      <td>Lat: 36.40,Lon: 70.80</td>
      <td>6.0</td>
      <td>PIITR0063</td>
      <td>2009-10-29 17:44:30</td>
    </tr>
    <tr>
      <th>225</th>
      <td>2009-11-07</td>
      <td>PESMOS0226</td>
      <td>20091107-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2009-11-07</td>
      <td>PESMOS0097</td>
      <td>20091107-Gangtok1</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>126</th>
      <td>2009-11-10</td>
      <td>PESMOS0127</td>
      <td>20091110-Rampur</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0063</td>
      <td>None</td>
    </tr>
    <tr>
      <th>166</th>
      <td>2009-11-16</td>
      <td>PESMOS0167</td>
      <td>20091116-Guwahati</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0247</td>
      <td>None</td>
    </tr>
    <tr>
      <th>251</th>
      <td>2009-12-03</td>
      <td>PESMOS0252</td>
      <td>20091203-Tisa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0066</td>
      <td>None</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2009-12-06</td>
      <td>PESMOS0021</td>
      <td>20091206-China India Border (J&amp;K)</td>
      <td>Lat: 35.80,Lon: 77.30</td>
      <td>5.3</td>
      <td>PIITR0063</td>
      <td>2009-12-06 04:33:15</td>
    </tr>
    <tr>
      <th>167</th>
      <td>2009-12-29</td>
      <td>PESMOS0168</td>
      <td>20091229-Myamar India Border</td>
      <td>Lat: 24.50,Lon: 94.80</td>
      <td>5.5</td>
      <td>PIITR0248,PIITR0259,PIITR0240,PIITR0247,PIITR0...</td>
      <td>2009-12-29 09:01:42</td>
    </tr>
    <tr>
      <th>252</th>
      <td>2009-12-31</td>
      <td>PESMOS0253</td>
      <td>20091231-Bhutan</td>
      <td>Lat: 27.30,Lon: 91.40</td>
      <td>5.5</td>
      <td>PIITR0240,PIITR0247,PIITR0251,PIITR0245,PIITR0268</td>
      <td>2009-12-31 09:57:00</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2010-01-11</td>
      <td>PESMOS0038</td>
      <td>20100111-Tisa(N.L.)</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0066</td>
      <td>None</td>
    </tr>
    <tr>
      <th>68</th>
      <td>2010-01-11</td>
      <td>PESMOS0069</td>
      <td>20100111-Pithoragarh</td>
      <td>Lat: 29.70,Lon: 80.00</td>
      <td>3.9</td>
      <td>PIITR0004,PIITR0009,PIITR0017</td>
      <td>2010-01-11 05:15:18</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2010-01-29</td>
      <td>PESMOS0015</td>
      <td>20100129-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>114</th>
      <td>2010-02-15</td>
      <td>PESMOS0115</td>
      <td>20100215-Golpara</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0245</td>
      <td>None</td>
    </tr>
    <tr>
      <th>218</th>
      <td>2010-02-22</td>
      <td>PESMOS0219</td>
      <td>20100222-Bageshwar</td>
      <td>Lat: 30.00,Lon: 80.10</td>
      <td>4.7</td>
      <td>PIITR0023,PIITR0027,PIITR0004,PIITR0012,PIITR0...</td>
      <td>2010-02-22 17:23:43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2010-02-24</td>
      <td>PESMOS0017</td>
      <td>20100224-Rohtak</td>
      <td>Lat: 28.60,Lon: 76.90</td>
      <td>2.5</td>
      <td>PDELH0004,PDELH0005,PDELH0006,PDELH0007,PDELH0...</td>
      <td>2010-02-24 19:20:52</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2010-02-25</td>
      <td>PESMOS0016</td>
      <td>20100225-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>242</th>
      <td>2010-02-26</td>
      <td>PESMOS0243</td>
      <td>20100226-Tibet</td>
      <td>Lat: 28.50,Lon: 86.70</td>
      <td>5.4</td>
      <td>PIITR0240,PIITR0247,PIITR0251,PIITR0245,PIITR0...</td>
      <td>2010-02-26 04:42:33</td>
    </tr>
    <tr>
      <th>233</th>
      <td>2010-03-12</td>
      <td>PESMOS0234</td>
      <td>20100312-Myammar</td>
      <td>Lat: 23.00,Lon: 94.50</td>
      <td>5.6</td>
      <td>PIITR0248,PIITR0240,PIITR0247,PIITR0268,PIITR0245</td>
      <td>2010-03-12 23:19:54</td>
    </tr>
    <tr>
      <th>229</th>
      <td>2010-03-14</td>
      <td>PESMOS0230</td>
      <td>20100314-Punjab Himachal Border</td>
      <td>Lat: 31.70,Lon: 76.10</td>
      <td>4.6</td>
      <td>PIITR0027,PIITR0080,PIITR0083,PIITR0090,PIITR0...</td>
      <td>2010-03-14 06:53:21</td>
    </tr>
    <tr>
      <th>184</th>
      <td>2010-03-25</td>
      <td>PESMOS0185</td>
      <td>20100325-Tisa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0066</td>
      <td>None</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2010-03-28</td>
      <td>PESMOS0001</td>
      <td>20100328-Tura</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0268</td>
      <td>None</td>
    </tr>
    <tr>
      <th>74</th>
      <td>2010-05-01</td>
      <td>PESMOS0075</td>
      <td>20100501-Distt. Bageshwar Uttarakhand</td>
      <td>Lat: 29.90,Lon: 80.10</td>
      <td>4.6</td>
      <td>PIITR0023,PIITR0027,PIITR0019,PIITR0029,PIITR0...</td>
      <td>2009-05-01 22:36:25</td>
    </tr>
    <tr>
      <th>70</th>
      <td>2010-05-03</td>
      <td>PESMOS0071</td>
      <td>20100503-Uttarakhand</td>
      <td>Lat: 30.40,Lon: 78.40</td>
      <td>3.5</td>
      <td>PIITR0016,PIITR0014,PIITR0027,PIITR0011</td>
      <td>2010-05-03 17:15:08</td>
    </tr>
    <tr>
      <th>130</th>
      <td>2010-05-09</td>
      <td>PESMOS0131</td>
      <td>20100509-Tinsukia</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0260</td>
      <td>None</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2010-05-26</td>
      <td>PESMOS0022</td>
      <td>20100526-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>122</th>
      <td>2010-05-28</td>
      <td>PESMOS0123</td>
      <td>20100528-Himachal Pradesh</td>
      <td>Lat: 31.20,Lon: 77.90</td>
      <td>4.8</td>
      <td>PIITR0052,PIITR0014,PIITR0027,PIITR0047</td>
      <td>2010-05-28 07:25:06</td>
    </tr>
    <tr>
      <th>154</th>
      <td>2010-05-31</td>
      <td>PESMOS0155</td>
      <td>20100531-Almora District</td>
      <td>Lat: 30.00,Lon: 79.80</td>
      <td>3.6</td>
      <td>PIITR0004,PIITR0009</td>
      <td>2010-05-31 11:37:04</td>
    </tr>
    <tr>
      <th>148</th>
      <td>2010-06-11</td>
      <td>PESMOS0149</td>
      <td>20100611-Guwahati</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0247</td>
      <td>None</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2010-06-12</td>
      <td>PESMOS0033</td>
      <td>20100612-OFF WEST COAST OF NICOBAR ISLANDS,INDIA</td>
      <td>Lat:  7.90,Lon: 91.90</td>
      <td>7.8</td>
      <td>PIITR0129</td>
      <td>2010-06-12 19:26:46</td>
    </tr>
    <tr>
      <th>171</th>
      <td>2010-06-13</td>
      <td>PESMOS0172</td>
      <td>20100613-Tura</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0268</td>
      <td>None</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2010-06-19</td>
      <td>PESMOS0053</td>
      <td>20100619- Guwahati</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0247</td>
      <td>None</td>
    </tr>
    <tr>
      <th>135</th>
      <td>2010-06-21</td>
      <td>PESMOS0136</td>
      <td>20100621-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0037</td>
      <td>None</td>
    </tr>
    <tr>
      <th>53</th>
      <td>2010-06-21</td>
      <td>PESMOS0054</td>
      <td>20100621-Tisa</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0066</td>
      <td>None</td>
    </tr>
    <tr>
      <th>88</th>
      <td>2010-07-06</td>
      <td>PESMOS0089</td>
      <td>20100706-Nepal India Border Region</td>
      <td>Lat: 29.80,Lon: 80.40</td>
      <td>5.1</td>
      <td>PIITR0004,PIITR0029</td>
      <td>2010-07-06 19:08:20</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2010-07-10</td>
      <td>PESMOS0018</td>
      <td>20100710-Almora, Uttarakhand</td>
      <td>Lat: 29.90,Lon: 79.60</td>
      <td>4.1</td>
      <td>PIITR0023,PIITR0002,PIITR0027,PIITR0019</td>
      <td>2010-07-10 03:16:20</td>
    </tr>
    <tr>
      <th>248</th>
      <td>2010-07-26</td>
      <td>PESMOS0249</td>
      <td>20100726-Barpeta</td>
      <td>Lat: 26.50,Lon: 91.30</td>
      <td>4.1</td>
      <td>PIITR0247</td>
      <td>2010-07-26 19:43:27</td>
    </tr>
    <tr>
      <th>236</th>
      <td>2010-08-03</td>
      <td>PESMOS0237</td>
      <td>20100803-ANDAMAN ISLANDS REGION</td>
      <td>Lat: 11.20,Lon: 93.20</td>
      <td>5.2</td>
      <td>PIITR0129</td>
      <td>2010-08-03 01:48:11</td>
    </tr>
    <tr>
      <th>247</th>
      <td>2010-08-08</td>
      <td>PESMOS0248</td>
      <td>20100808-Amritsar</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0067</td>
      <td>None</td>
    </tr>
    <tr>
      <th>197</th>
      <td>2010-08-14</td>
      <td>PESMOS0198</td>
      <td>20100814-Dimapur</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0278</td>
      <td>None</td>
    </tr>
    <tr>
      <th>163</th>
      <td>2010-08-20</td>
      <td>PESMOS0164</td>
      <td>20100820-Guwahati</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0247</td>
      <td>None</td>
    </tr>
    <tr>
      <th>152</th>
      <td>2010-09-11</td>
      <td>PESMOS0153</td>
      <td>20100911-Meghalaya -Assam border</td>
      <td>Lat: 25.90,Lon: 90.20</td>
      <td>5.0</td>
      <td>PIITR0240,PIITR0247,PIITR0251</td>
      <td>2010-09-11 07:02:09</td>
    </tr>
    <tr>
      <th>120</th>
      <td>2010-09-17</td>
      <td>PESMOS0121</td>
      <td>20100917-Gangtok(N.L.)</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>87</th>
      <td>2010-09-17</td>
      <td>PESMOS0088</td>
      <td>20100917-Hindukush Rerion Afganistan</td>
      <td>Lat: 36.50,Lon: 70.80</td>
      <td>6.5</td>
      <td>PIITR0027,PIITR0040,PIITR0016,PIITR0014,PIITR0...</td>
      <td>2010-09-17 19:21:09</td>
    </tr>
    <tr>
      <th>131</th>
      <td>2010-10-05</td>
      <td>PESMOS0132</td>
      <td>20101005-Darjeeling</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0233</td>
      <td>None</td>
    </tr>
    <tr>
      <th>80</th>
      <td>2010-11-07</td>
      <td>PESMOS0081</td>
      <td>20101107-Chamoli</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0003</td>
      <td>None</td>
    </tr>
    <tr>
      <th>79</th>
      <td>2010-12-12</td>
      <td>PESMOS0080</td>
      <td>20101212-Manipur Assam Border</td>
      <td>Lat: 25.00,Lon: 93.30</td>
      <td>4.8</td>
      <td>PIITR0255,PIITR0250</td>
      <td>2010-12-12 01:40:04</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2010-12-17</td>
      <td>PESMOS0032</td>
      <td>20101217-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>232</th>
      <td>2011-01-18</td>
      <td>PESMOS0233</td>
      <td>20110118 -Southwestern Pakistan</td>
      <td>Lat: 28.90,Lon: 64.00</td>
      <td>7.4</td>
      <td>PDELH0013,PDELH0017,PDELH0001,PDELH0015,PDELH0...</td>
      <td>2011-01-18 20:23:27</td>
    </tr>
    <tr>
      <th>137</th>
      <td>2011-01-26</td>
      <td>PESMOS0138</td>
      <td>20110126- Sonepat Baghpat Border</td>
      <td>Lat: 29.00,Lon: 77.20</td>
      <td>3.2</td>
      <td>PDELH0001</td>
      <td>2011-01-26 03:06:45</td>
    </tr>
    <tr>
      <th>55</th>
      <td>2011-02-04</td>
      <td>PESMOS0056</td>
      <td>20110204- India Myammar Border</td>
      <td>Lat: 24.80,Lon: 94.60</td>
      <td>6.4</td>
      <td>PIITR0249,PIITR0255,PIITR0257,PIITR0247,PIITR0...</td>
      <td>2011-02-04 13:53:39</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2011-02-10</td>
      <td>PESMOS0030</td>
      <td>20110210-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>198</th>
      <td>2011-02-18</td>
      <td>PESMOS0199</td>
      <td>20110218-Delhi</td>
      <td>Lat: 28.60,Lon: 77.30</td>
      <td>2.3</td>
      <td>PDELH0008,PDELH0001</td>
      <td>2011-02-18 14:44:14</td>
    </tr>
    <tr>
      <th>83</th>
      <td>2011-03-14</td>
      <td>PESMOS0084</td>
      <td>20110314-Chamoli</td>
      <td>Lat: 30.50,Lon: 79.10</td>
      <td>3.3</td>
      <td>PIITR0003</td>
      <td>2011-03-14 09:01:29</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2011-03-21</td>
      <td>PESMOS0012</td>
      <td>20110321-Hindukush Region</td>
      <td>Lat: 36.50,Lon: 70.90</td>
      <td>5.7</td>
      <td>PIITR0127,PIITR0014</td>
      <td>2011-03-21 09:48:59</td>
    </tr>
    <tr>
      <th>69</th>
      <td>2011-04-04</td>
      <td>PESMOS0070</td>
      <td>20110404-India Nepal Border</td>
      <td>Lat: 29.60,Lon: 80.80</td>
      <td>5.7</td>
      <td>PIITR0034,PDELH0004,PIITR0030,PIITR0019,PIITR0...</td>
      <td>2011-04-04 11:31:40</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2011-05-04</td>
      <td>PESMOS0024</td>
      <td>20110504-India Nepal Border</td>
      <td>Lat: 30.20,Lon: 80.40</td>
      <td>5.0</td>
      <td>PIITR0029</td>
      <td>2011-05-04 20:57:15</td>
    </tr>
    <tr>
      <th>237</th>
      <td>2011-05-13</td>
      <td>PESMOS0238</td>
      <td>20110513-Barkot</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0014</td>
      <td>None</td>
    </tr>
    <tr>
      <th>94</th>
      <td>2011-06-03</td>
      <td>PESMOS0095</td>
      <td>20110603-NEPAL - SIKKIM (INDIA) BORDER REGION</td>
      <td>Lat: 27.50,Lon: 88.00</td>
      <td>4.9</td>
      <td>PIITR0233,PIITR0238,PIITR0214,PIITR0237</td>
      <td>2011-06-03 00:53:21</td>
    </tr>
    <tr>
      <th>91</th>
      <td>2011-06-15</td>
      <td>PESMOS0092</td>
      <td>20110615-PITHORAGARH, UTTARAKHAND</td>
      <td>Lat: 30.60,Lon: 80.10</td>
      <td>3.4</td>
      <td>PIITR0023,PIITR0029</td>
      <td>2011-06-15 00:59:28</td>
    </tr>
    <tr>
      <th>107</th>
      <td>2011-06-20</td>
      <td>PESMOS0108</td>
      <td>20110620-Chamoli(N.L.)</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0003</td>
      <td>None</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2011-06-20</td>
      <td>PESMOS0110</td>
      <td>20110620-Chamoli,Uttarakhand</td>
      <td>Lat: 30.50,Lon: 79.40</td>
      <td>4.6</td>
      <td>PIITR0035,PIITR0027,PIITR0032,PIITR0019,PIITR0...</td>
      <td>2011-06-20 06:27:18</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2011-06-23</td>
      <td>PESMOS0126</td>
      <td>20110623-UTTRAKHAND (INDIA) - NEPAL BORDER REGION</td>
      <td>Lat: 30.00,Lon: 80.50</td>
      <td>3.2</td>
      <td>PIITR0017</td>
      <td>2011-06-23 22:13:46</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2011-07-28</td>
      <td>PESMOS0023</td>
      <td>20110728-J &amp; K</td>
      <td>Lat: 33.30,Lon: 76.00</td>
      <td>4.4</td>
      <td>PIITR0064</td>
      <td>2011-07-28 18:42:34</td>
    </tr>
    <tr>
      <th>230</th>
      <td>2011-08-23</td>
      <td>PESMOS0231</td>
      <td>20110823-Delhi</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PDELH0008,PDELH0001,PDELH0003</td>
      <td>None</td>
    </tr>
    <tr>
      <th>81</th>
      <td>2011-08-28</td>
      <td>PESMOS0082</td>
      <td>20110828-Uttarkashi</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0013</td>
      <td>None</td>
    </tr>
    <tr>
      <th>215</th>
      <td>2011-09-06</td>
      <td>PESMOS0216</td>
      <td>20110906-Dharchula</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0017</td>
      <td>None</td>
    </tr>
    <tr>
      <th>164</th>
      <td>2011-09-07</td>
      <td>PESMOS0165</td>
      <td>20110907-Sonipat</td>
      <td>Lat: 28.60,Lon: 77.00</td>
      <td>4.2</td>
      <td>PDELH0013,PDELH0017,PDELH0001,PIITR0102,PDELH0...</td>
      <td>2011-09-07 17:58:18</td>
    </tr>
    <tr>
      <th>196</th>
      <td>2011-09-18</td>
      <td>PESMOS0197</td>
      <td>20110918(157)-INDIA(SIKKIM)--NEPAL BORDER REGION3</td>
      <td>Lat: 27.60,Lon: 88.40</td>
      <td>4.2</td>
      <td>PIITR0238</td>
      <td>2011-09-18 21:51:52</td>
    </tr>
    <tr>
      <th>170</th>
      <td>2011-09-18</td>
      <td>PESMOS0171</td>
      <td>20110918-Gangtok</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>165</th>
      <td>2011-09-18</td>
      <td>PESMOS0166</td>
      <td>20110918-Gangtok1</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0238</td>
      <td>None</td>
    </tr>
    <tr>
      <th>191</th>
      <td>2011-09-18</td>
      <td>PESMOS0192</td>
      <td>20110918(154)-INDIA(SIKKIM)--NEPAL BORDER REGION</td>
      <td>Lat: 27.60,Lon: 88.20</td>
      <td>6.8</td>
      <td>PIITR0009,PIITR0004,PIITR0257,PIITR0250,PIITR0...</td>
      <td>2011-09-18 12:40:47</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2011-09-18</td>
      <td>PESMOS0093</td>
      <td>20110918(155)-INDIA(SIKKIM)--NEPAL BORDER REGION1</td>
      <td>Lat: 27.60,Lon: 88.50</td>
      <td>5.0</td>
      <td>PIITR0238,PIITR0235</td>
      <td>2011-09-18 13:11:59</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2011-09-18</td>
      <td>PESMOS0050</td>
      <td>20110918(156)-INDIA(SIKKIM)--NEPAL BORDER REGION2</td>
      <td>Lat: 27.50,Lon: 88.40</td>
      <td>4.5</td>
      <td>PIITR0238</td>
      <td>2011-09-18 13:54:17</td>
    </tr>
    <tr>
      <th>192</th>
      <td>2011-09-21</td>
      <td>PESMOS0193</td>
      <td>20110921-UTTARKASHI DIST.,UTTARANCHAL</td>
      <td>Lat: 30.90,Lon: 78.30</td>
      <td>3.1</td>
      <td>PIITR0014</td>
      <td>2011-09-21 02:24:36</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2011-09-22</td>
      <td>PESMOS0006</td>
      <td>20110922-Sikkim</td>
      <td>Lat: 27.60,Lon: 88.40</td>
      <td>3.9</td>
      <td>PIITR0238</td>
      <td>2011-09-22 16:44:43</td>
    </tr>
    <tr>
      <th>40</th>
      <td>2011-09-24</td>
      <td>PESMOS0041</td>
      <td>20110924-UTTARKASHI DIST, UTTARANCHAL</td>
      <td>Lat: 30.90,Lon: 78.30</td>
      <td>3.0</td>
      <td>PIITR0014</td>
      <td>2011-09-24 14:32:18</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2011-09-29</td>
      <td>PESMOS0077</td>
      <td>20110929-Barkot</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0014</td>
      <td>None</td>
    </tr>
    <tr>
      <th>209</th>
      <td>2011-10-26</td>
      <td>PESMOS0210</td>
      <td>20111026-Mandi</td>
      <td>Lat: 31.50,Lon: 76.80</td>
      <td>3.5</td>
      <td>PIITR0065</td>
      <td>2011-10-26 16:17:32</td>
    </tr>
    <tr>
      <th>46</th>
      <td>2011-11-21</td>
      <td>PESMOS0047</td>
      <td>20111121-INdia-Myanmar Border</td>
      <td>Lat: 25.10,Lon: 95.30</td>
      <td>5.8</td>
      <td>PIITR0247</td>
      <td>2011-11-21 03:15:33</td>
    </tr>
    <tr>
      <th>75</th>
      <td>2012-01-16</td>
      <td>PESMOS0076</td>
      <td>20120116-Pauri</td>
      <td>Lat: 29.70,Lon: 78.90</td>
      <td>3.6</td>
      <td>PIITR0008</td>
      <td>2012-01-16 05:01:00</td>
    </tr>
    <tr>
      <th>226</th>
      <td>2012-02-09</td>
      <td>PESMOS0227</td>
      <td>20120209-UTTARKASHI DISTRICT, UTTARAKHAND</td>
      <td>Lat: 30.90,Lon: 78.20</td>
      <td>5.0</td>
      <td>PIITR0041,PIITR0017,PIITR0065,PIITR0015,PIITR0013</td>
      <td>2011-02-09 19:17:29</td>
    </tr>
    <tr>
      <th>178</th>
      <td>2012-02-26</td>
      <td>PESMOS0179</td>
      <td>20120226-Nepal Border</td>
      <td>Lat: 29.60,Lon: 80.80</td>
      <td>4.3</td>
      <td>PIITR0030,PIITR0033</td>
      <td>2012-02-26 23:08:42</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2012-03-05</td>
      <td>PESMOS0105</td>
      <td>20120305-Bahadurgarh</td>
      <td>Lat: 28.70,Lon: 76.60</td>
      <td>4.9</td>
      <td>PDELH0013,PDELH0005,PDELH0006,PIITR0107,PIITR0...</td>
      <td>2012-03-05 07:41:05</td>
    </tr>
    <tr>
      <th>110</th>
      <td>2012-03-12</td>
      <td>PESMOS0111</td>
      <td>20120312-BAGHPAT</td>
      <td>Lat: 28.90,Lon: 77.30</td>
      <td>3.5</td>
      <td>PDELH0006,PDELH0001,PDELH0002,PDELH0003</td>
      <td>2012-03-12 22:07:20</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2012-03-27</td>
      <td>PESMOS0143</td>
      <td>20120327-India Nepal Border</td>
      <td>Lat: 26.10,Lon: 87.80</td>
      <td>4.9</td>
      <td>PIITR0203</td>
      <td>2012-03-27 23:40:08</td>
    </tr>
    <tr>
      <th>115</th>
      <td>2012-05-04</td>
      <td>PESMOS0116</td>
      <td>20120504-Dibrugarh</td>
      <td>Lat: 27.50,Lon: 95.10</td>
      <td>4.4</td>
      <td>PIITR0256</td>
      <td>2012-05-04 20:09:26</td>
    </tr>
    <tr>
      <th>149</th>
      <td>2012-05-10</td>
      <td>PESMOS0150</td>
      <td>20120510-Chamoli</td>
      <td>Lat: 30.20,Lon: 79.40</td>
      <td>3.9</td>
      <td>PIITR0019</td>
      <td>2012-05-10 22:00:40</td>
    </tr>
    <tr>
      <th>246</th>
      <td>2012-05-11</td>
      <td>PESMOS0247</td>
      <td>20120511-Assam</td>
      <td>Lat: 26.60,Lon: 93.00</td>
      <td>5.4</td>
      <td>PIITR0249,PIITR0251,PIITR0246</td>
      <td>2012-05-11 18:41:28</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2012-06-21</td>
      <td>PESMOS0035</td>
      <td>20120621-Dharchula</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0017</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2012-07-01</td>
      <td>PESMOS0008</td>
      <td>20120701-Nagaland</td>
      <td>Lat: 25.70,Lon: 94.60</td>
      <td>5.8</td>
      <td>PIITR0249,PIITR0260,PIITR0246</td>
      <td>2012-07-01 04:13:52</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2012-07-10</td>
      <td>PESMOS0052</td>
      <td>20120710-Assam</td>
      <td>Lat: 26.50,Lon: 93.20</td>
      <td>4.5</td>
      <td>PIITR0255</td>
      <td>2012-07-10 13:03:41</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2012-07-12</td>
      <td>PESMOS0039</td>
      <td>20120712-Hindukush</td>
      <td>Lat: 36.50,Lon: 70.90</td>
      <td>6.3</td>
      <td>PIITR0037</td>
      <td>2009-07-12 14:00:32</td>
    </tr>
    <tr>
      <th>175</th>
      <td>2012-07-14</td>
      <td>PESMOS0176</td>
      <td>20120714-Nagaland</td>
      <td>Lat: 25.50,Lon: 94.20</td>
      <td>5.5</td>
      <td>PIITR0255,PIITR0249,PIITR0246</td>
      <td>2012-07-14 19:55:18</td>
    </tr>
    <tr>
      <th>108</th>
      <td>2012-07-28</td>
      <td>PESMOS0109</td>
      <td>20120728-NEPAL -INDIA (UTTRAKHAND)_BORDER REGION</td>
      <td>Lat: 29.70,Lon: 80.70</td>
      <td>4.5</td>
      <td>PIITR0030</td>
      <td>2012-07-28 05:48:06</td>
    </tr>
    <tr>
      <th>174</th>
      <td>2012-08-04</td>
      <td>PESMOS0175</td>
      <td>20120804-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>157</th>
      <td>2012-08-13</td>
      <td>PESMOS0158</td>
      <td>20120813-J&amp;K Border</td>
      <td>Lat: 34.80,Lon: 73.70</td>
      <td>5.2</td>
      <td>PIITR0053</td>
      <td>2012-08-13 20:32:59</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2012-08-19</td>
      <td>PESMOS0205</td>
      <td>20120819-Tejpur</td>
      <td>Lat: 26.70,Lon: 92.50</td>
      <td>5.0</td>
      <td>PIITR0259</td>
      <td>2012-08-19 09:24:49</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2012-08-19</td>
      <td>PESMOS0031</td>
      <td>20120819-Sonitpur</td>
      <td>Lat: 26.70,Lon: 92.60</td>
      <td>4.0</td>
      <td>PIITR0259</td>
      <td>2012-08-19 19:04:56</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2012-08-23</td>
      <td>PESMOS0044</td>
      <td>20120823-Nepal</td>
      <td>Lat: 28.40,Lon: 82.70</td>
      <td>5.0</td>
      <td>PIITR0004,PIITR0030,PIITR0012</td>
      <td>2012-08-23 16:30:19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2012-10-02</td>
      <td>PESMOS0009</td>
      <td>20121002-Sonitpur</td>
      <td>Lat: 26.90,Lon: 92.80</td>
      <td>5.1</td>
      <td>PIITR0255,PIITR0257,PIITR0259</td>
      <td>2012-10-02 18:37:39</td>
    </tr>
    <tr>
      <th>228</th>
      <td>2012-10-02</td>
      <td>PESMOS0229</td>
      <td>20121002-Lahul Spiti1</td>
      <td>Lat: 32.30,Lon: 76.30</td>
      <td>4.9</td>
      <td>PIITR0037,PIITR0063</td>
      <td>2012-10-02 08:34:52</td>
    </tr>
    <tr>
      <th>161</th>
      <td>2012-10-02</td>
      <td>PESMOS0162</td>
      <td>20121002-Sonitpur-1</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0259</td>
      <td>None</td>
    </tr>
    <tr>
      <th>210</th>
      <td>2012-10-02</td>
      <td>PESMOS0211</td>
      <td>20121002-Lahul Spiti</td>
      <td>Lat: 32.40,Lon: 76.40</td>
      <td>4.5</td>
      <td>PIITR0037</td>
      <td>2012-10-02 03:45:28</td>
    </tr>
    <tr>
      <th>78</th>
      <td>2012-10-03</td>
      <td>PESMOS0079</td>
      <td>20121003-Lahul Spiti2</td>
      <td>Lat: 32.40,Lon: 76.30</td>
      <td>3.4</td>
      <td>PIITR0037</td>
      <td>2012-10-03 17:48:28</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2012-10-03</td>
      <td>PESMOS0096</td>
      <td>20121003-Lahul Spiti1</td>
      <td>Lat: 32.40,Lon: 76.30</td>
      <td>3.6</td>
      <td>PIITR0037</td>
      <td>2012-10-03 10:49:28</td>
    </tr>
    <tr>
      <th>41</th>
      <td>2012-10-03</td>
      <td>PESMOS0042</td>
      <td>20121003-Lahul Spiti</td>
      <td>Lat: 32.40,Lon: 76.30</td>
      <td>3.8</td>
      <td>PIITR0037</td>
      <td>2012-10-03 10:04:34</td>
    </tr>
    <tr>
      <th>213</th>
      <td>2012-10-30</td>
      <td>PESMOS0214</td>
      <td>20121030-Morigaon</td>
      <td>Lat: 26.20,Lon: 92.40</td>
      <td>3.9</td>
      <td>PIITR0255</td>
      <td>2012-10-30 01:40:24</td>
    </tr>
    <tr>
      <th>56</th>
      <td>2012-11-06</td>
      <td>PESMOS0057</td>
      <td>20121106-Kangra</td>
      <td>Lat: 32.30,Lon: 76.20</td>
      <td>4.1</td>
      <td>PIITR0037</td>
      <td>2012-11-06 12:21:12</td>
    </tr>
    <tr>
      <th>182</th>
      <td>2012-11-11</td>
      <td>PESMOS0183</td>
      <td>20121111-Kangra</td>
      <td>Lat: 32.30,Lon: 76.20</td>
      <td>4.0</td>
      <td>PIITR0037</td>
      <td>2012-11-11 20:23:12</td>
    </tr>
    <tr>
      <th>205</th>
      <td>2012-11-11</td>
      <td>PESMOS0206</td>
      <td>20121111- Western Nepal</td>
      <td>Lat: 29.20,Lon: 81.50</td>
      <td>5.0</td>
      <td>PIITR0004,PIITR0030,PIITR0009</td>
      <td>2012-11-11 18:39:19</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2012-11-15</td>
      <td>PESMOS0026</td>
      <td>20121115-Bageshwar</td>
      <td>Lat: 30.20,Lon: 80.10</td>
      <td>3.0</td>
      <td>PIITR0023</td>
      <td>2012-11-15 06:46:07</td>
    </tr>
    <tr>
      <th>223</th>
      <td>2012-11-19</td>
      <td>PESMOS0224</td>
      <td>20121119-Rohtak</td>
      <td>Lat: 28.70,Lon: 76.60</td>
      <td>3.5</td>
      <td>PIITR0115</td>
      <td>2012-11-19 06:25:21</td>
    </tr>
    <tr>
      <th>147</th>
      <td>2012-11-27</td>
      <td>PESMOS0148</td>
      <td>20121127-Uttarkashi</td>
      <td>Lat: 30.90,Lon: 78.40</td>
      <td>4.8</td>
      <td>PIITR0016,PIITR0015,PIITR0013,PIITR0011</td>
      <td>2012-11-27 12:15:15</td>
    </tr>
    <tr>
      <th>129</th>
      <td>2012-11-30</td>
      <td>PESMOS0130</td>
      <td>20121130-Sikkim</td>
      <td>Lat: 27.30,Lon: 88.30</td>
      <td>4.1</td>
      <td>PIITR0233</td>
      <td>2012-11-30 19:39:29</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2012-12-19</td>
      <td>PESMOS0027</td>
      <td>20121219-Jhajjar</td>
      <td>Lat: 28.60,Lon: 76.80</td>
      <td>2.9</td>
      <td>PDELH0004</td>
      <td>2012-12-19 22:32:00</td>
    </tr>
    <tr>
      <th>169</th>
      <td>2012-12-22</td>
      <td>PESMOS0170</td>
      <td>20121222-Myanmar</td>
      <td>Lat: 22.50,Lon: 94.80</td>
      <td>5.7</td>
      <td>PIITR0255</td>
      <td>2012-12-22 16:41:44</td>
    </tr>
    <tr>
      <th>159</th>
      <td>2013-01-02</td>
      <td>PESMOS0160</td>
      <td>20130102-Nepal</td>
      <td>Lat: 29.40,Lon: 81.10</td>
      <td>4.8</td>
      <td>PIITR0009,PIITR0030</td>
      <td>2013-01-02 17:42:15</td>
    </tr>
    <tr>
      <th>203</th>
      <td>2013-01-07</td>
      <td>PESMOS0204</td>
      <td>20130107-Arunachal Pradesh</td>
      <td>Lat: 28.10,Lon: 94.30</td>
      <td>4.5</td>
      <td>PIITR0260</td>
      <td>2013-01-07 05:32:46</td>
    </tr>
    <tr>
      <th>153</th>
      <td>2013-01-09</td>
      <td>PESMOS0154</td>
      <td>20130109-Myanmar</td>
      <td>Lat: 25.40,Lon: 94.90</td>
      <td>5.9</td>
      <td>PIITR0259,PIITR0255,PIITR0256,PIITR0251,PIITR0...</td>
      <td>2013-01-09 01:41:52</td>
    </tr>
    <tr>
      <th>194</th>
      <td>2013-01-09</td>
      <td>PESMOS0195</td>
      <td>20130109-Nepal</td>
      <td>Lat: 29.75,Lon: 81.74</td>
      <td>5.0</td>
      <td>PIITR0004,PIITR0030,PIITR0009,PIITR0033</td>
      <td>2013-01-09 07:44:20</td>
    </tr>
    <tr>
      <th>139</th>
      <td>2013-01-10</td>
      <td>PESMOS0140</td>
      <td>20130110-Pithoragarh</td>
      <td>Lat: 30.10,Lon: 80.40</td>
      <td>3.2</td>
      <td>PIITR0009</td>
      <td>2013-01-10 15:16:13</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2013-01-29</td>
      <td>PESMOS0051</td>
      <td>20130129-Nepal</td>
      <td>Lat: 30.00,Lon: 81.60</td>
      <td>4.0</td>
      <td>PIITR0009</td>
      <td>2013-01-29 19:42:52</td>
    </tr>
    <tr>
      <th>220</th>
      <td>2013-02-11</td>
      <td>PESMOS0221</td>
      <td>20130211-Uttarkashi</td>
      <td>Lat: 31.00,Lon: 78.40</td>
      <td>4.3</td>
      <td>PIITR0015,PIITR0027,PIITR0013</td>
      <td>2013-02-11 10:48:55</td>
    </tr>
    <tr>
      <th>222</th>
      <td>2013-02-17</td>
      <td>PESMOS0223</td>
      <td>20130217-Uttarkashi</td>
      <td>Lat: 30.90,Lon: 78.40</td>
      <td>3.2</td>
      <td>PIITR0013</td>
      <td>2013-02-17 16:27:07</td>
    </tr>
    <tr>
      <th>190</th>
      <td>2013-02-28</td>
      <td>PESMOS0191</td>
      <td>20130228-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2013-03-02</td>
      <td>PESMOS0029</td>
      <td>20130302-Karimganj</td>
      <td>Lat: 24.80,Lon: 92.20</td>
      <td>5.2</td>
      <td>PIITR0255,PIITR0239</td>
      <td>2013-03-02 01:30:40</td>
    </tr>
    <tr>
      <th>179</th>
      <td>2013-03-31</td>
      <td>PESMOS0180</td>
      <td>20130331-Pithoragarh</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0009</td>
      <td>None</td>
    </tr>
    <tr>
      <th>200</th>
      <td>2013-04-06</td>
      <td>PESMOS0201</td>
      <td>20130406-Rudraprayag</td>
      <td>Lat: 30.50,Lon: 79.10</td>
      <td>4.3</td>
      <td>PIITR0013</td>
      <td>2005-04-06 22:29:31</td>
    </tr>
    <tr>
      <th>206</th>
      <td>2013-04-10</td>
      <td>PESMOS0207</td>
      <td>20130410-Rohtak</td>
      <td>Lat: 29.00,Lon: 76.60</td>
      <td>3.5</td>
      <td>PDELH0002</td>
      <td>2012-04-10 20:10:01</td>
    </tr>
    <tr>
      <th>155</th>
      <td>2013-04-11</td>
      <td>PESMOS0156</td>
      <td>20130411-Delhi</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PDELH0004,PDELH0008,PDELH0003</td>
      <td>None</td>
    </tr>
    <tr>
      <th>128</th>
      <td>2013-04-16</td>
      <td>PESMOS0129</td>
      <td>20130416-Assam</td>
      <td>Lat: 26.30,Lon: 92.00</td>
      <td>4.6</td>
      <td>PIITR0243,PIITR0255,PIITR0239,PIITR0259</td>
      <td>2013-04-16 01:23:19</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2013-04-16</td>
      <td>PESMOS0014</td>
      <td>20130416-iran-pakistan</td>
      <td>Lat: 28.00,Lon: 62.10</td>
      <td>7.8</td>
      <td>PDELH0007,PDELH0016,PDELH0002,PDELH0003,PIITR0...</td>
      <td>2013-04-16 10:44:11</td>
    </tr>
    <tr>
      <th>199</th>
      <td>2013-05-01</td>
      <td>PESMOS0200</td>
      <td>20130501-East Srinagar</td>
      <td>Lat: 33.10,Lon: 75.80</td>
      <td>5.8</td>
      <td>PIITR0085,PIITR0078,PIITR0037,PIITR0027,PIITR0...</td>
      <td>2013-05-01 06:57:12</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2013-05-01</td>
      <td>PESMOS0025</td>
      <td>20130501-JK-Himachal Border</td>
      <td>Lat: 33.10,Lon: 75.80</td>
      <td>5.8</td>
      <td>PIITR0037,PIITR0027,PIITR0127,PIITR0015,PIITR0...</td>
      <td>2013-05-01 06:57:12</td>
    </tr>
    <tr>
      <th>168</th>
      <td>2013-06-04</td>
      <td>PESMOS0169</td>
      <td>20130604-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>57</th>
      <td>2013-06-04</td>
      <td>PESMOS0058</td>
      <td>20130604-Lahul Spiti</td>
      <td>Lat: 32.70,Lon: 76.70</td>
      <td>4.8</td>
      <td>PIITR0037</td>
      <td>2013-06-04 17:34:44</td>
    </tr>
    <tr>
      <th>188</th>
      <td>2013-06-05</td>
      <td>PESMOS0189</td>
      <td>20130605-Chamba</td>
      <td>Lat: 32.80,Lon: 76.30</td>
      <td>4.5</td>
      <td>PIITR0037</td>
      <td>2013-06-05 22:04:00</td>
    </tr>
    <tr>
      <th>160</th>
      <td>2013-06-12</td>
      <td>PESMOS0161</td>
      <td>20130612-Chamba</td>
      <td>Lat:  0.00,Lon:  0.00</td>
      <td>0.0</td>
      <td>PIITR0002</td>
      <td>None</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2013-07-09</td>
      <td>PESMOS0046</td>
      <td>20130709-HP-JK Border</td>
      <td>Lat: 32.90,Lon: 78.40</td>
      <td>5.1</td>
      <td>PIITR0037</td>
      <td>2013-07-09 13:49:13</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2013-07-13</td>
      <td>PESMOS0117</td>
      <td>20130713-Kangra</td>
      <td>Lat: 32.20,Lon: 76.30</td>
      <td>4.5</td>
      <td>PIITR0037</td>
      <td>2013-07-13 17:49:33</td>
    </tr>
    <tr>
      <th>181</th>
      <td>2013-07-15</td>
      <td>PESMOS0182</td>
      <td>20130715-Lahul Spiti</td>
      <td>Lat: 32.60,Lon: 76.70</td>
      <td>4.4</td>
      <td>PIITR0037</td>
      <td>2013-07-15 17:49:11</td>
    </tr>
    <tr>
      <th>86</th>
      <td>2013-08-02</td>
      <td>PESMOS0087</td>
      <td>20130802-J&amp;K Himachal Border</td>
      <td>Lat: 33.50,Lon: 75.50</td>
      <td>5.4</td>
      <td>PIITR0127,PIITR0037,PIITR0039</td>
      <td>2013-08-02 02:32:05</td>
    </tr>
    <tr>
      <th>119</th>
      <td>2013-08-02</td>
      <td>PESMOS0120</td>
      <td>20130802-J&amp;K Himachal Border1</td>
      <td>Lat: 33.40,Lon: 75.90</td>
      <td>5.2</td>
      <td>PIITR0127,PIITR0037</td>
      <td>2013-08-02 21:37:40</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2013-08-21</td>
      <td>PESMOS0037</td>
      <td>20130821-Sonitpur1</td>
      <td>Lat: 26.70,Lon: 92.40</td>
      <td>3.9</td>
      <td>PIITR0255,PIITR0259</td>
      <td>2013-08-21 08:41:51</td>
    </tr>
    <tr>
      <th>177</th>
      <td>2013-08-21</td>
      <td>PESMOS0178</td>
      <td>20130821-Sonitpur</td>
      <td>Lat: 26.70,Lon: 92.50</td>
      <td>4.2</td>
      <td>PIITR0259</td>
      <td>2013-08-21 06:57:20</td>
    </tr>
    <tr>
      <th>173</th>
      <td>2013-08-29</td>
      <td>PESMOS0174</td>
      <td>20130829-Punjab-HP Border</td>
      <td>Lat: 31.40,Lon: 76.10</td>
      <td>4.7</td>
      <td>PIITR0096,PIITR0087,PIITR0027,PIITR0093,PIITR0...</td>
      <td>2013-08-29 10:13:21</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2013-09-05</td>
      <td>PESMOS0036</td>
      <td>20130905-Uttarkshi</td>
      <td>Lat: 30.90,Lon: 78.50</td>
      <td>3.5</td>
      <td>PIITR0013</td>
      <td>2013-09-05 18:35:42</td>
    </tr>
    <tr>
      <th>136</th>
      <td>2013-10-07</td>
      <td>PESMOS0137</td>
      <td>20131007-Naogaon</td>
      <td>Lat: 26.30,Lon: 92.50</td>
      <td>3.7</td>
      <td>PIITR0255,PIITR0259</td>
      <td>2013-10-07 20:54:03</td>
    </tr>
    <tr>
      <th>89</th>
      <td>2013-10-20</td>
      <td>PESMOS0090</td>
      <td>20131020-China border</td>
      <td>Lat: 35.80,Lon: 77.50</td>
      <td>5.5</td>
      <td>PDELH0004,PDELH0007,PIITR0037,PDELH0003</td>
      <td>2013-10-20 19:45:05</td>
    </tr>
    <tr>
      <th>97</th>
      <td>2013-11-06</td>
      <td>PESMOS0098</td>
      <td>20131106-Punjab</td>
      <td>Lat: 31.40,Lon: 76.10</td>
      <td>4.9</td>
      <td>PIITR0037</td>
      <td>2013-11-06 14:53:08</td>
    </tr>
    <tr>
      <th>180</th>
      <td>2013-11-06</td>
      <td>PESMOS0181</td>
      <td>20131106-Assam</td>
      <td>Lat: 26.50,Lon: 93.50</td>
      <td>5.5</td>
      <td>PIITR0255,PIITR0256,PIITR0239,PIITR0259</td>
      <td>2013-11-06 04:16:16</td>
    </tr>
    <tr>
      <th>106</th>
      <td>2013-11-11</td>
      <td>PESMOS0107</td>
      <td>20131111-Delhi1911</td>
      <td>Lat: 28.50,Lon: 77.20</td>
      <td>3.1</td>
      <td>PDELH0004,PDELH0005,PDELH0006,PDELH0007,PDELH0...</td>
      <td>2013-11-11 19:11:18</td>
    </tr>
    <tr>
      <th>183</th>
      <td>2013-11-11</td>
      <td>PESMOS0184</td>
      <td>20131111-Delhi2025</td>
      <td>Lat: 28.40,Lon: 77.20</td>
      <td>2.5</td>
      <td>PDELH0004,PDELH0018</td>
      <td>2013-11-11 20:25:02</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2013-11-11</td>
      <td>PESMOS0066</td>
      <td>20131111-Delhi2011</td>
      <td>Lat: 28.40,Lon: 77.20</td>
      <td>3.3</td>
      <td>PDELH0013,PDELH0012,PDELH0006,PDELH0007,PDELH0...</td>
      <td>2013-11-11 20:11:30</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2013-11-11</td>
      <td>PESMOS0142</td>
      <td>20131111-Delhi2210</td>
      <td>Lat: 28.40,Lon: 77.20</td>
      <td>2.8</td>
      <td>PDELH0004,PDELH0005,PDELH0007,PDELH0002,PDELH0...</td>
      <td>2013-11-11 22:10:42</td>
    </tr>
    <tr>
      <th>189</th>
      <td>2013-12-25</td>
      <td>PESMOS0190</td>
      <td>20131225-Uttarkashi</td>
      <td>Lat: 31.20,Lon: 78.30</td>
      <td>4.0</td>
      <td>PIITR0013</td>
      <td>2013-12-25 02:56:52</td>
    </tr>
    <tr>
      <th>132</th>
      <td>2014-02-23</td>
      <td>PESMOS0133</td>
      <td>20140223-Kameng Arunachal</td>
      <td>Lat: 27.20,Lon: 92.50</td>
      <td>4.8</td>
      <td>PIITR0255,PIITR0259</td>
      <td>2014-02-23 17:04:50</td>
    </tr>
    <tr>
      <th>156</th>
      <td>2014-04-01</td>
      <td>PESMOS0157</td>
      <td>20140401-Naogaon Assam</td>
      <td>Lat: 26.40,Lon: 92.40</td>
      <td>4.4</td>
      <td>PIITR0255,PIITR0259</td>
      <td>2014-04-01 17:45:09</td>
    </tr>
    <tr>
      <th>234</th>
      <td>2014-05-30</td>
      <td>PESMOS0235</td>
      <td>20140530-khokhrajhar</td>
      <td>Lat: 26.50,Lon: 90.40</td>
      <td>4.5</td>
      <td>PIITR0239</td>
      <td>2014-05-30 06:37:50</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2014-06-17</td>
      <td>PESMOS0067</td>
      <td>20140617-Kangra</td>
      <td>Lat: 32.20,Lon: 76.10</td>
      <td>4.1</td>
      <td>PIITR0037,PIITR0038</td>
      <td>2014-06-17 17:31:08</td>
    </tr>
    <tr>
      <th>245</th>
      <td>2014-08-21</td>
      <td>PESMOS0246</td>
      <td>20140821-Distt. Kangra</td>
      <td>Lat: 32.30,Lon: 76.50</td>
      <td>5.0</td>
      <td>PIITR0037,PIITR0038</td>
      <td>2014-08-21 08:11:17</td>
    </tr>
    <tr>
      <th>150</th>
      <td>2014-09-12</td>
      <td>PESMOS0151</td>
      <td>20140912-Goalpara</td>
      <td>Lat: 26.10,Lon: 90.20</td>
      <td>4.2</td>
      <td>PIITR0239</td>
      <td>2014-09-12 07:56:44</td>
    </tr>
    <tr>
      <th>221</th>
      <td>2015-11-29</td>
      <td>PESMOS0222</td>
      <td>Chamoli_29112015</td>
      <td>Lat: 30.60,Lon: 79.60</td>
      <td>4.0</td>
      <td>PIITR0022,PIITR0010,PIITR0003,PIITR0019</td>
      <td>2015-11-29 02:47:38</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2016-09-25</td>
      <td>PESMOS0218</td>
      <td>rudp_25sept2016</td>
      <td>Lat: 30.50,Lon: 78.90</td>
      <td>3.7</td>
      <td>PIITR0020,PIITR0008,PIITR0019,PIITR0013,PIITR0...</td>
      <td>2016-09-25 21:41:36</td>
    </tr>
    <tr>
      <th>176</th>
      <td>2016-11-23</td>
      <td>PESMOS0177</td>
      <td>Dehradun_23112016</td>
      <td>Lat: 30.30,Lon: 78.00</td>
      <td>3.4</td>
      <td>PIITR0016,PIITR0011,PIITR0062,PIITR0010,PIITR0013</td>
      <td>2016-11-23 02:31:03</td>
    </tr>
    <tr>
      <th>113</th>
      <td>2016-12-01</td>
      <td>PESMOS0114</td>
      <td>Nepal_01122016</td>
      <td>Lat: 29.80,Lon: 80.60</td>
      <td>5.2</td>
      <td>PIITR0022,PIITR0008,PIITR0019,PIITR0010,PIITR0...</td>
      <td>2016-12-01 16:52:48</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-12-13</td>
      <td>PESMOS0007</td>
      <td>Uttarkashi_13122016</td>
      <td>Lat: 30.30,Lon: 79.40</td>
      <td>3.2</td>
      <td>PIITR0019,PIITR0016,PIITR0014,PIITR0013,PIITR0...</td>
      <td>2017-01-10 15:27:41</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2016-12-13</td>
      <td>PESMOS0215</td>
      <td>Dehradun_13122016</td>
      <td>Lat: 30.80,Lon: 78.00</td>
      <td>3.9</td>
      <td>PIITR0016,PIITR0014,PIITR0013,PIITR0010,PIITR0...</td>
      <td>2016-12-13 19:14:04</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2016-12-19</td>
      <td>PESMOS0048</td>
      <td>Uttarkashi_19122016</td>
      <td>Lat: 30.90,Lon: 78.00</td>
      <td>3.4</td>
      <td>PIITR0014,PIITR0260,PIITR0003,PIITR0013</td>
      <td>2016-12-19 04:31:56</td>
    </tr>
    <tr>
      <th>186</th>
      <td>2016-12-26</td>
      <td>PESMOS0187</td>
      <td>Dehradun_26122016</td>
      <td>Lat: 30.80,Lon: 77.90</td>
      <td>3.5</td>
      <td>PIITR0014,PIITR0013</td>
      <td>2016-12-26 08:45:48</td>
    </tr>
  </tbody>
</table>
</div>



# Parsing PESMOS Records
The pesmos datas are freely available through [website](http://pesmos.in/2011/
"PESMOS") for download. Although it is required for the users to obtain a log in
credention for downloading data. The log in credential could be optained through
registration. After registration web admistator will review your application and
will send confirmation mail upon successful approval of registration. After log
in to wesite, the users are required to go to Downloads tab for downloading
data. The data are available in two section. First section, "View/Download
Ground Motion Reconds" provides events from 2005 to 2014. Second section,
"View/Download Earthquake Early Warning System Data (EEWS)" provides events from
2015 to 2017. For each event ".zip" file is available containing station
records. For each station three direction data, NS, EW and Z-directional are
available. A typical format of accelaration record file is shown below

    Origin Time       31/03/2006 11:25:39
    Lat.              28.7 N
    Long.             76.8 E
    Depth (Km)         22.0
    Magnitude         3.4
     Region           JHAJJAR-HARYANA
     Above details taken from IMD

    Station Code      ROH
    Station Lat.       28.896  N
    Station Long.      76.593  E
    Station Height(m)  225.0
    Site Class        C   Vs30 between 200 m/sec to 375 m/sec *
    Record Time       31.03.2006 11:25:26.529
    Sampling Rate     200. Hz
     Record Duration   29.995 Sec.
     Direction         E-W (E positive)
    Max. Acceleration      4.799 cm/sec**2

      * For reference see Site Classification link of website

     Base Line Corrected and Low Pass Filtered (Cut Off at 35 Hz) Time History
     Acceleration data in cm/sec**2

           0.228
           0.017
          -0.067
          -0.050
          -0.004
           0.018
           0.008
           .
           .
           .

These files are parsed using a python script.

'''python
'''
Program by
        Anis Mohammed Vengasseri
        anis.mhd@gmail.com
        https://github.com/anismhd

        Started Date :: 20/01/2017

        fname  - Should be the file name without '.ns', '.ew' or '.vt' extension

        if '.' in fname:
                print "fname  - Should be the file name without '.ns', '.ew' or
'.vt' extension"
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
                return datetime(int(year),int(month),int(day),int(hour),
int(minute), int(second), int(microsecond))

def pesmos_reader(fname):
        data = open(fname).readlines()
        event = {}
        event['Origin Time'] = time_stripper(data[0].strip('Origin
Time').strip())
#       event['Latitude'] = data[1].strip('Lat.').strip()
#       event['Longitude'] = data[2].strip('Long.').strip()
        lat_str = data[1].strip('Lat.').strip()
        lon_str = data[2].strip('Long.').strip()
        event['Latitude'], event['Longitude'] =
geodetic_string_proccessor(lat_str, lon_str)
        event['Depth'] = data[3].strip('Depth (Km)').strip()
        event['Magnitude'] = data[4].strip('Magnitude').strip()
        event['Region'] = data[5].strip('Region').strip()
        event['Source of Event Data'] = data[6].strip()
        station = {}
        station['Code'] = data[8].strip('Station Code').strip()
        lat_str = data[9].strip('Station Lat.').strip()
        lon_str = data[10].strip('Station Long.').strip()
        station['Latitude'],station['Longitude'] =
geodetic_string_proccessor(lat_str, lon_str)
#       station['Height'] = float(data[11].strip('Station Height(m)').strip())
        station['Site class'] = data[12].strip('Site Class').strip()
        station['Record time'] = time_stripper(data[13].strip('Record
Time').strip())
        station['Sampling rate'] = float(data[14].strip('Sampling
Rate').strip()[:-2])
        station['Record_duration'] = float(data[15].strip('Record
Duration').strip()[:-4])
        station['Data direction'] = data[16].strip('Direction').strip()
        station['Data PGA'] = data[17].strip('Max. Acceleration').strip()
        station['Data filtering info'] = data[21].strip()
        station['Data unit'] = data[22].strip('Acceleration data in').strip()
        station['Data number'] = int(station['Sampling
rate']*station['Record_duration'])
        station['Data series'] = np.zeros(station['Data number'])
        for i in range(station['Data number']):
                station['Data series'][i] = float(data[24+i].strip())
        return event, station
'''


The events recorded by PESMOS station have few issues with respect to derived
values. Especially magnitude and location of event. In this section, magnitude
and locations reported by PESMOS are cross verified with respect to data from
USGS.

## Methodology
The pes

The events reported in USGS for the region of India after 2000 are downloaded
using python scripts. The data downloaded from USGS siite are parsed to obtain
information on location, magnitude, magnitude scale, date and time of event etc.
The parsed information are stored into a python pandas dataframe. Then,




    
