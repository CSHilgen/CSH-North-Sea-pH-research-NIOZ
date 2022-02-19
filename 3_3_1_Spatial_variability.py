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

combinedmean['dicta_ratio'] = combinedmean['dic'] / combinedmean['alkalinity']
combinedmean['ndicta_ratio'] = combinedmean['normalized_DIC'] / combinedmean['normalized_TA']

#%% # Save all datasets assessing the spatial variability

resultsRWSo.to_csv("dataframes_made/resultsRWSo_final.csv")
RWSomean.to_csv("dataframes_made/RWSomean_final.csv")
resultscombined.to_csv("dataframes_made/resultscombined_final.csv")
combinedmean.to_csv("dataframes_made/combinedmean_final.csv")

