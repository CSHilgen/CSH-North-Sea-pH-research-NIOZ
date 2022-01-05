import pandas as pd, numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
from scipy.optimize import least_squares
import PyCO2SYS as pyco2
import tools.seasonalfitting as SF_tools
import tools.plots_spatial_variability as SV_plots

#%% # Import dataframes

resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")

# Get the salinity mean of 1975-2021
salinitymean = resultsRWSo['salinity'].mean()
print(f"Salinity mean value = {salinitymean:6f}") 

#%% # Apply salinity normalization on DIC data (combined dataset) 
# Based on the equation (2) of paper Friis et al. 2003

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['dic'])
print(f"DIC of rivers at 0 salinity endmember = {intercept:6f}") # Salinity river (zero) end member
salendmember = intercept

x = 35.5
DICopenocean = slope * x + intercept
print(f"DIC of open ocean at 35.5 salinity endmember = {DICopenocean:6f}") # Salinity open ocean end member

resultscombined['normalized_DIC'] = (((resultscombined['dic'] - salendmember) / 
                                 resultscombined['salinity']) * salinitymean) + salendmember
resultscombined['salinityeffect_DIC'] = resultscombined['dic'] - resultscombined['normalized_DIC']

combinedmean['normalized_DIC'] = (((combinedmean['dic'] - salendmember) / 
                                 combinedmean['salinity']) * salinitymean) + salendmember
combinedmean['salinityeffect_DIC'] = combinedmean['dic'] - combinedmean['normalized_DIC']

SV_plots.plot_salinity_vs_DIC(combinedmean)
SV_plots.plot_normalized_DIC(combinedmean)

#%% # Apply salinity normalization on TA data (combined dataset) 
# Based on the equation (2) of paper Friis et al. 2003

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])
print(f"TA of rivers at 0 salinity endmember = {intercept:6f}") # Salinity river (zero) end member
salendmember = intercept

x = 35.5
TAopenocean = slope * x + intercept
print(f"TA of open ocean at 35.5 salinity endmember = {TAopenocean:6f}") # Salinity open ocean end member

resultscombined['normalized_TA'] = (((resultscombined['alkalinity'] - salendmember) / 
                                 resultscombined['salinity']) * salinitymean) + salendmember
resultscombined['salinityeffect_TA'] = resultscombined['alkalinity'] - resultscombined['normalized_TA']

combinedmean['normalized_TA'] = (((combinedmean['alkalinity'] - salendmember) / 
                                 combinedmean['salinity']) * salinitymean) + salendmember
combinedmean['salinityeffect_TA'] = combinedmean['alkalinity'] - combinedmean['normalized_TA']

SV_plots.plot_salinity_vs_TA(combinedmean)
SV_plots.plot_normalized_TA(combinedmean)

#%% # Plot DIC against TA and NDIC against NTA for verification

SV_plots.plot_DIC_TA(combinedmean)
SV_plots.plot_DIC_TA_year(combinedmean)
SV_plots.plot_NDIC_NTA(combinedmean)
SV_plots.plot_NDIC_NTA_year(combinedmean)

#%% # pH verification model TA (combined) & pCO2 air (SOCAT) & fCO2 sea (SOCAT)

# Predict TA for the RWS dataset based on the linear relationship of S & TA (combined dataset)
slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])
combinedmean['predicted_alkalinity'] = (slope * combinedmean['salinity']) + intercept
RWSomean['predicted_alkalinity'] = (slope * RWSomean['salinity']) + intercept

# Predict pCO2 air & fCO2 sea for the RWS dataset based on the seasonal cycle (sin curve) of pCO2 air & fCO2 sea (SOCAT dataset)
socatnsmeanair = socatnsmean.dropna(axis='rows', how='all', subset=['pCO2'])
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmeanair['datenum'], socatnsmeanair['pCO2']))

combinedmean['predicted_pCO2_air'] = SF_tools.seasonalcycle_fit(opt_result['x'], combinedmean['datenum'])
RWSomean['predicted_pCO2_air'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomean['datenum'])

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fco2_sea']))

combinedmean['predicted_fCO2_sea'] = SF_tools.seasonalcycle_fit(opt_result['x'], combinedmean['datenum'])
RWSomean['predicted_fCO2_sea'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomean['datenum'])

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

SV_plots.predicted_fCO2_pCO2_alkalinity_RWSo(RWSomean) 
SV_plots.plot_pH_verification(RWSomean, RWSnmean, results_TA_fCO2, results_TA_pCO2)
SV_plots.plot_pH_predicted_vs_initial(RWSomean)

results_TA_pCO2 = results_TA_pCO2.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(results_TA_pCO2['datenum'], results_TA_pCO2['pH_total'])
print(f"Slope of pH predicted based on TA and pCO2AIR = {slope:6f}") 

results_TA_fCO2 = results_TA_fCO2.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(results_TA_pCO2['datenum'], results_TA_fCO2['pH_total'])
print(f"Slope of pH predicted based on TA and fCO2SW = {slope:6f}")

#%% # Save all datasets assessing the spatial variability

# resultsRWSo.to_csv("dataframes_made/resultsRWSo_final.csv")
# RWSomean.to_csv("dataframes_made/RWSomean_final.csv")
# resultscombined.to_csv("dataframes_made/resultscombined_final.csv")
# combinedmean.to_csv("dataframes_made/combinedmean_final.csv")
# socatnsmean.to_csv("dataframes_made/socatnsmean_final.csv")
# results_TA_pCO2.to_csv("dataframes_made/results_TA_pCO2_final.csv")
# results_TA_fCO2.to_csv("dataframes_made/results_TA_fCO2_final.csv")