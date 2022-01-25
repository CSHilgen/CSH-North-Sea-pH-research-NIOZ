import pandas as pd, numpy as np
from scipy.stats import linregress
from scipy.optimize import least_squares
from sklearn.cluster import MeanShift
from scipy import interpolate
import matplotlib.dates as mdates
import tools.seasonalfitting as SF_tools
import tools.plots_temporal_variability as TV_plots

#%% # Import dataframes

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
RWStotalmean = pd.read_csv("dataframes_made/RWStotalmean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")

#%% # Seasonal correction for fCO2 air, fCO2 sea and ΔfCO2 (SOCAT)

# Seasonal cycle correction fCO2 air
socatnsmeanair = socatnsmean.dropna(axis='rows', how='all', subset=['fco2_air'])
slope, intercept, r, p, se = linregress(socatnsmeanair['datenum'], socatnsmeanair['fco2_air'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(socatnsmeanair['datenum'], socatnsmeanair['fco2_air']))
socatnsmeanair['sc_fco2_air'] = SF_tools.seasonalcycle_fit(opt_result['x'], socatnsmeanair['datenum']) # sc = seasoncal cycle
slope, intercept, sine_stretch, sine_shift = opt_result['x']
socatnsmeanair['ms_fco2_air'] = socatnsmeanair['fco2_air'] - socatnsmeanair['sc_fco2_air'] # ms = minus seasonality

# Seasonal cycle correction fCO2 sea
slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_fco2_sea, [0.006, 386, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fco2_sea']))
socatnsmean['sc_fco2_sea'] = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], socatnsmean['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
socatnsmean['ms_fco2_sea'] = socatnsmean['fco2_sea'] - socatnsmean['sc_fco2_sea']

# Seasonal cycle correction ΔfCO2 
socatnsmeandelta = socatnsmean.dropna(axis='rows', how='all', subset=['deltafco2'])
slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_fco2_sea, [0.006, 386, 162, 680], 
                           args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))
socatnsmeandelta['sc_deltafco2'] = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], socatnsmeandelta['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
socatnsmeandelta['ms_deltafco2'] = socatnsmeandelta['deltafco2'] - socatnsmeandelta['sc_deltafco2']

#%% # Seasonal correction for chlorophyll, oxygen umol/kg, total_ammonia, total_nitrate, total_phosphate, total_silicate

# Seasonal cycle correction Chlorophyll
RWSomeanChl = RWSomean.dropna(axis='rows', how='all', subset=['chlorophyll'])
slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll']))
RWSomeanChl['sc_chlorophyll'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomeanChl['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomeanChl['ms_chlorophyll'] = RWSomeanChl['chlorophyll'] - RWSomeanChl['sc_chlorophyll']

# Seasonal cycle correction Oxygen
RWSomeano2 = RWSomean.dropna(axis='rows', how='all', subset=['oxygen umol/kg'])
slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg']))
RWSomeano2['sc_oxygen umol/kg'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomeano2['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomeano2['ms_oxygen umol/kg'] = RWSomeano2['oxygen umol/kg'] - RWSomeano2['sc_oxygen umol/kg']

# Seasonal cycle correction Nitrate
RWSomeanN = RWSomean.dropna(axis='rows', how='all', subset=['total_nitrate'])
slope, intercept, r, p, se = linregress(RWSomeanN['datenum'], RWSomeanN['total_nitrate'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanN['datenum'], RWSomeanN['total_nitrate']))
RWSomeanN['sc_total_nitrate'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomeanN['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomeanN['ms_total_nitrate'] = RWSomeanN['total_nitrate'] - RWSomeanN['sc_total_nitrate']

# Seasonal cycle correction Phosphate
RWSomeanP = RWSomean.dropna(axis='rows', how='all', subset=['total_phosphate'])
slope, intercept, r, p, se = linregress(RWSomeanP['datenum'], RWSomeanP['total_phosphate'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanP['datenum'], RWSomeanP['total_phosphate']))
RWSomeanP['sc_total_phosphate'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomeanP['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomeanP['ms_total_phosphate'] = RWSomeanP['total_phosphate'] - RWSomeanP['sc_total_phosphate']

# Seasonal cycle correction Silicate
RWSomeanS = RWSomean.dropna(axis='rows', how='all', subset=['total_silicate'])
slope, intercept, r, p, se = linregress(RWSomeanS['datenum'], RWSomeanS['total_silicate'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanS['datenum'], RWSomeanS['total_silicate']))
RWSomeanS['sc_total_silicate'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomeanS['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomeanS['ms_total_silicate'] = RWSomeanS['total_silicate'] - RWSomeanS['sc_total_silicate']

#%% # Seasonal correction for Temperature

# Seasonal cycle correction Temperature
RWStotalmeanT = RWStotalmean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_T, [0.006, 386, 162, 680], 
                           args=(RWStotalmeanT['datenum'], RWStotalmeanT['temperature']))
RWStotalmeanT['sc_temperature'] = SF_tools.seasonalcycle_fit_T(opt_result['x'], RWStotalmeanT['datenum'])
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWStotalmeanT['ms_temperature'] = RWStotalmeanT['temperature'] - RWStotalmeanT['sc_temperature']

#%% # Seasonal correction for DIC

# Make new dateframe to get a cyclic curve
combinedmeandubbel = combinedmean.append(combinedmean.loc[[7] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[19] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[36] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[35] *1].assign(**{'dayofyear':-30}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[18] *1].assign(**{'dayofyear':0}), ignore_index=True)

x = combinedmeandubbel['dayofyear'].to_numpy()
y = combinedmeandubbel.normalized_DIC.to_numpy()
x_v = np.vstack(x)
clustering = MeanShift(bandwidth=5).fit(x_v)
cluster_labels = clustering.labels_

x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])
    
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
    
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

# Making a dateframe to plot the seasonal cycle for every year
combinedmeansc_dic = pd.DataFrame()
combinedmeansc_dic['datenum'] = np.arange(11330, 18993)
combinedmeansc_dic['datetime'] = mdates.num2date(combinedmeansc_dic.datenum)
combinedmeansc_dic['dayofyear'] = combinedmeansc_dic.datetime.dt.dayofyear
combinedmeansc_dic['interpolator_dic'] = interpolator(combinedmeansc_dic['dayofyear'])

# Calculate the corrected DIC and final values
combinedmean['sc_dic'] = interpolator(combinedmean['dayofyear'])
combinedmean['ms_dic'] = (combinedmean['normalized_DIC'] - combinedmean['sc_dic'])
combinedmean['dic_corrected'] = 0.0005 * combinedmean['datenum'] + 2131.4
combinedmean['dic_correctd_final'] = combinedmean['ms_dic'] + 2140.3

# Plot the clustered DIC seasonal cycle
TV_plots.plot_DIC_combined_clustering(combinedmeandubbel)

# Make new dateframe to get a cyclic curve
RWSnmeandubbel = RWSnmean.append(RWSnmean.loc[[11] *1].assign(**{'dayofyear':0, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[10] *1].assign(**{'dayofyear':-31, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[28] *1].assign(**{'dayofyear':-30, 'year':2021}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[0] *1].assign(**{'dayofyear':396, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[12] *1].assign(**{'dayofyear':396, 'year':2020}), ignore_index=True)

# Plot the DIC seasonal cycle from 2018-2021 per year
TV_plots.plot_DIC_dayofyear_cycle_RWSn(RWSnmeandubbel)

# Plot the clustered DIC seasonal cycle and RWS Chlorophyll
TV_plots.plot_DIC_and_Chl(combinedmeandubbel, RWSo)

#%% # Save all datasets assessing the temporal variability

combinedmean.to_csv("dataframes_made/combinedmean_final.csv")
socatnsmean.to_csv("dataframes_made/socatnsmean_final.csv")
RWStotalmean.to_csv("dataframes_made/RWStotalmean_final.csv")
combinedmeandubbel.to_csv("dataframes_made/combinedmeandubbel_final.csv")
combinedmeansc_dic.to_csv("dataframes_made/combinedmeansc_dic_final.csv")
socatnsmeanair.to_csv("dataframes_made/socatnsmeanair_final.csv")
socatnsmeandelta.to_csv("dataframes_made/socatnsmeandelta_final.csv")
RWSomeanChl.to_csv("dataframes_made/RWSomeanChl_final.csv")
RWSomeano2.to_csv("dataframes_made/RWSomeano2_final.csv")
RWSomeanN.to_csv("dataframes_made/RWSomeanN_final.csv")
RWSomeanP.to_csv("dataframes_made/RWSomeanP_final.csv")
RWSomeanS.to_csv("dataframes_made/RWSomeanS_final.csv")
RWStotalmeanT.to_csv("dataframes_made/RWStotalmeanT_final.csv")