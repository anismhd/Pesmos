

    pylab.rcParams['figure.figsize'] = (20, 15)
    from generating_figures import india_basemap
    import pickle
    import pandas as pd
    pd.set_option('display.max_rows', None)


    station_data_from_file = pickle.load( open( "station_data_from_file.pickle", "rb" ) )
    pesmos_stations_final_pd = pickle.load( open( "pesmos_stations_final_pd.pickle", "rb" ) )
    pesmos_stations = pickle.load( open( "pesmos_stations.pickle", "rb" ) )

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
    for station in pesmos_stations:
        m.scatter([pesmos_stations[station]['Longitude']],[pesmos_stations[station]['Latitude']],\
                  s=25,latlon=True,marker='D',color= station_color[pesmos_stations[station]['Site class']] )
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='r', label='Site Class A Vs30 between 700 m/sec to 1620 m/sec')
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='g', label='Site Class B Vs30 between 375 m/sec to 700 m/sec')
    m.scatter([0],[0], s=25,latlon=True,marker='D',color='b', label='Site Class C Vs30 between 200 m/sec to 375 m/sec')
    title('Figure 1 :: Strong Motion Station of PESMOS')
    legend(scatterpoints=1)




    <matplotlib.legend.Legend at 0x7f6c9ab519d0>




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



    


    
