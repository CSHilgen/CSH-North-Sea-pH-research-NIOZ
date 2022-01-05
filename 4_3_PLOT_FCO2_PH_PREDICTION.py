import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import PyCO2SYS as pyco2
import matplotlib.dates as mdates
from scipy.stats import linregress

#%% # Import datasets

socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
combinedmean = combinedmean.rename(columns={list(combinedmean)[4]:'dataset'})

#%% # Use pyCO2sys to calculate pH and fCO2 sea based on nTA and corrected nDIC 
 
combinedmean = combinedmean.reset_index()

TA = combinedmean['normalized_TA']
DIC = combinedmean['dic_correctd_final']
temp = combinedmean['temperature']
sal = combinedmean['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature of the sample
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultscombinedmean = pd.DataFrame.from_dict(results)
resultscombinedmean['datetime'] = combinedmean['datetime']
resultscombinedmean['longitude'] = combinedmean['longitude']
resultscombinedmean['latitude'] = combinedmean['latitude']
resultscombinedmean['dataset'] = combinedmean['dataset']
resultscombinedmean['datenum'] = combinedmean['datenum']

#%% # Logicals for colours in plots

Lg = combinedmean['dataset'] == str('glodapnsmean')
Ld = combinedmean['dataset'] == str('D366mean')
Lc = combinedmean['dataset'] == str('Cefasmean')
Lr = combinedmean['dataset'] == str('RWSnmean')

LRg = resultscombinedmean['dataset'] == str('glodapnsmean')
LRd = resultscombinedmean['dataset'] == str('D366mean')
LRc = resultscombinedmean['dataset'] == str('Cefasmean')
LRr = resultscombinedmean['dataset'] == str('RWSnmean')

#%% # fCO2 prediction (nTA and corrected nDIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "goldenrod"}, line_kws={"color": "blue"}, label='SOCAT$_{initial}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRd], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRr], c='xkcd:evergreen', label='RWS$_{pred}$')

ax.set_title("SOCAT & predicted fCO$_{2SW}$ based on nA$_T$ & corrected nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_nTA_corrected_nDIC.png") 

#%% # pH prediction (nTA and corrected nDIC)

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
# sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax, ci=99.9,
#             scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue"}, label='RWS$_{iniital}$')
# sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
#             scatter_kws={"color": "xkcd:evergreen"}, line_kws={"color": "xkcd:blue"}, label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:ultramarine blue', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=RWSnmean, c='xkcd:evergreen', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRd], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRr], facecolor='None', edgecolor='xkcd:evergreen', label='RWS$_{pred}$')

ax.set_title("RWS & predicted pH based on nA$_T$ & corrected nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_nTA_corrected_nDIC.png")    

#%% # fCO2 prediction (TA and DIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "goldenrod"}, line_kws={"color": "blue"}, label='SOCAT$_{initial}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')

ax.set_title("SOCAT & predicted fCO$_2$ sea based on A$_T$ & DIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_TA_DIC.png") 

#%% # pH prediction (TA and DIC)

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
# sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax, ci=99.9,
#             scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue"}, label='RWS$_{iniital}$')
# sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
#             scatter_kws={"color": "xkcd:evergreen"}, line_kws={"color": "xkcd:blue"}, label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:ultramarine blue', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=RWSnmean, c='xkcd:banana', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lr], edgecolor='xkcd:evergreen', facecolor='None', label='RWS$_{pred}$')

ax.set_title("RWS & predicted pH based on A$_T$ & DIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_TA_DIC.png")   

#%% # Use pyCO2sys to calculate pH and fCO2 sea based on nTA and nDIC 

combinedmean = combinedmean.reset_index()

TA = combinedmean['normalized_TA']
DIC = combinedmean['normalized_DIC']
temp = combinedmean['temperature']
sal = combinedmean['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature of the sample
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultscombinedmean = pd.DataFrame.from_dict(results)
resultscombinedmean['datetime'] = combinedmean['datetime']
resultscombinedmean['longitude'] = combinedmean['longitude']
resultscombinedmean['latitude'] = combinedmean['latitude']
resultscombinedmean['dataset'] = combinedmean['dataset']
resultscombinedmean['datenum'] = combinedmean['datenum']

#%% # fCO2 prediction (nTA and nDIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "goldenrod"}, line_kws={"color": "blue"}, label='SOCAT$_{initial}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRd], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmean[LRr], c='xkcd:evergreen', label='RWS$_{pred}$')

ax.set_title("SOCAT & predicted fCO$_2$ sea based on nA$_T$ & nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_nTA_nDIC.png") 

#%% # pH prediction (nTA and nDIC)

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
# sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax, ci=99.9,
#             scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue"}, label='RWS$_{iniital}$')
# sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
#             scatter_kws={"color": "xkcd:evergreen"}, line_kws={"color": "xkcd:blue"}, label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:ultramarine blue', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=RWSnmean, c='xkcd:evergreen', label='RWS$_{iniital}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRg], c='xkcd:light violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRd], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmean[LRr], facecolor='None', edgecolor='xkcd:evergreen', label='RWS$_{pred}$')

ax.set_title("RWS & predicted pH based on nA$_T$ & nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_nTA_nDIC.png")    
