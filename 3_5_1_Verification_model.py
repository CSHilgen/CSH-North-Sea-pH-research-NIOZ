import pandas as pd, numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
from scipy.optimize import least_squares
import PyCO2SYS as pyco2
import tools.seasonalfitting as SF_tools
import tools.plots_pH_verification as pHV_plots

#%% # Import dataframes

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
socatnsmeanair = pd.read_csv("dataframes_made/socatnsmeanair_final.csv")

#%% # pH verification model TA (combined) & pCO2 air (SOCAT) & fCO2 sea (SOCAT)

# Predict TA for the RWS dataset based on the linear relationship of S & TA (combined dataset)
slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['normalized_TA'])
combinedmean['predicted_alkalinity'] = (slope * combinedmean['salinity']) + intercept
RWSomean['predicted_alkalinity'] = (slope * RWSomean['salinity']) + intercept

# Predict pCO2 air & fCO2 sea for the RWS dataset based on the seasonal cycle (sin curve) of pCO2 air & fCO2 sea (SOCAT dataset)
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmeanair['datenum'], socatnsmeanair['pCO2']))

combinedmean['predicted_pCO2_air'] = SF_tools.seasonalcycle_fit(opt_result['x'], combinedmean['datenum'])
RWSomean['predicted_pCO2_air'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomean['datenum'])

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fco2_sea']))

combinedmean['predicted_fCO2_sea'] = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], combinedmean['datenum'])
RWSomean['predicted_fCO2_sea'] = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], RWSomean['datenum'])

# Predict pH based on TA (combined) & pCO2 air (SOCAT)
TA = RWSomean['predicted_alkalinity']
pCO2 = RWSomean['predicted_pCO2_air']
sal = RWSomean['salinity']
temp = RWSomean['temperature']
phos = RWSomean['total_phosphate']
sil = RWSomean['total_silicate']

kwargs = dict(
    par1 = TA,
    par2 = pCO2,
    par1_type = 1,
    par2_type = 4,
    salinity = sal,
    temperature = temp,
    total_phosphate = phos, 
    total_silicate = sil,
    opt_k_carbonic = 4,  
    opt_k_bisulfate = 1  
    )

results = pyco2.sys(**kwargs)
results_TA_pCO2 = pd.DataFrame.from_dict(results)
results_TA_pCO2['datetime'] = RWSomean['datetime']
results_TA_pCO2['longitude'] = RWSomean['longitude']
results_TA_pCO2['latitude'] = RWSomean['latitude']
results_TA_pCO2['distance_to_shore'] = RWSomean['distance_to_shore']
results_TA_pCO2['dayofyear'] = RWSomean['dayofyear']
results_TA_pCO2['month'] = RWSomean['month']
results_TA_pCO2['year'] = RWSomean['year']
results_TA_pCO2['datenum'] = RWSomean['datenum']
# results_TA_pCO2 = results_TA_pCO2.dropna(axis='rows', how='all', subset=['salinity'])

# Predict pH based on TA (combined) & fCO2 sea (SOCAT)
TA = RWSomean['predicted_alkalinity']
fCO2 = RWSomean['predicted_fCO2_sea']
sal = RWSomean['salinity']
temp = RWSomean['temperature']
phos = RWSomean['total_phosphate']
sil = RWSomean['total_silicate']

kwargs = dict(
    par1 = TA,
    par2 = fCO2,
    par1_type = 1,
    par2_type = 5,
    salinity = sal,
    temperature = temp,
    total_phosphate = phos, 
    total_silicate = sil,
    opt_k_carbonic = 4,  
    opt_k_bisulfate = 1  
    )

results = pyco2.sys(**kwargs)
results_TA_fCO2 = pd.DataFrame.from_dict(results)
results_TA_fCO2['datetime'] = RWSomean['datetime']
results_TA_fCO2['longitude'] = RWSomean['longitude']
results_TA_fCO2['latitude'] = RWSomean['latitude']
results_TA_fCO2['distance_to_shore'] = RWSomean['distance_to_shore']
results_TA_fCO2['dayofyear'] = RWSomean['dayofyear']
results_TA_fCO2['month'] = RWSomean['month']
results_TA_fCO2['year'] = RWSomean['year']
results_TA_fCO2['datenum'] = RWSomean['datenum']
# results_TA_fCO2 = results_TA_fCO2.dropna(axis='rows', how='all', subset=['pH_total'])

RWSomean['pH_pred_TA_pCO2'] = results_TA_pCO2['pH_total']
RWSomean['pH_pred_TA_fCO2'] = results_TA_fCO2['pH_total']

# Plot pH verification model results
pHV_plots.predicted_fCO2_pCO2_alkalinity_RWSo(RWSomean) 
pHV_plots.plot_pH_verification(RWSomean, RWSnmean, results_TA_fCO2, results_TA_pCO2)
pHV_plots.plot_pH_predicted_vs_initial(RWSomean)

results_TA_pCO2 = results_TA_pCO2.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(results_TA_pCO2['datenum'], results_TA_pCO2['pH_total'])
print(f"Slope of pH predicted based on TA and pCO2AIR = {slope:6f}") 

results_TA_fCO2 = results_TA_fCO2.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(results_TA_pCO2['datenum'], results_TA_fCO2['pH_total'])
print(f"Slope of pH predicted based on TA and fCO2SW = {slope:6f}")

#%% # Save all datasets assessing the pH verification model

resultsRWSo.to_csv("dataframes_made/resultsRWSo_final.csv")
RWSomean.to_csv("dataframes_made/RWSomean_final.csv")
resultscombined.to_csv("dataframes_made/resultscombined_final.csv")
combinedmean.to_csv("dataframes_made/combinedmean_final.csv")
socatnsmeanair.to_csv("dataframes_made/socatnsmeanair_final.csv")