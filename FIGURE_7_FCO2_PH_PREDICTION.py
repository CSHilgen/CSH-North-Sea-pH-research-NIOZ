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

#%% # Logicals for colours in plots

Lg = combinedmean['dataset'] == str('glodapnsmean')
Ld = combinedmean['dataset'] == str('D366mean')
Lc = combinedmean['dataset'] == str('Cefasmean')
Lr = combinedmean['dataset'] == str('RWSnmean')

#%% # fCO2 prediction (TA and DIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
socatnsmeanair = socatnsmean.dropna(axis='rows', how='all', subset=['fCO2'])
bslope, bintercept, br, bp, bse = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])
aslope, aintercept, ar, ap, ase = linregress(combinedmean['datenum'], combinedmean['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:goldenrod"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='SOCAT$_{SW}$')
sns.regplot(x='datenum', y='fCO2', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:black"}, line_kws={"color": "xkcd:dark grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, label='SOCAT$_{AIR}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=combinedmean[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='fCO2', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})

ax.set_title("SOCAT & predicted fCO$_2$ sea based on A$_T$ & DIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_TA_DIC_air.png") 

#%% # pH prediction (TA and DIC)

RWSomeanpH = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(RWSomeanpH['datenum'], RWSomeanpH['pH_total'])
RWSnmeanpH = RWSnmean.dropna(axis='rows', how='all', subset=['pH_total_spectro_out'])
aslope, aintercept, ar, ap, ase = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])
combinedmeanpH = combinedmean.dropna(axis='rows', how='all', subset=['pH_total'])
bslope, bintercept, br, bp, bse = linregress(combinedmeanpH['datenum'], combinedmeanpH['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "xkcd:cobalt blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total_spectro_out', data=RWSnmean, c='xkcd:cobalt blue', label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='pH_total', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'})

ax.set_title("RWS & predicted pH based on A$_T$ & DIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH$_{total}$')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_TA_DIC.png")   

#%% # pH prediction (TA and DIC) - SPLIT UP

L1 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
L2 = (RWSomeanpH.year >= 2010)
L0 = (RWSomeanpH.pH_total > 7.5)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])
aslope, aintercept, ar, ap, ase = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

S1 = (combinedmeanpH.year <= 2011)
S2 = (combinedmeanpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(combinedmeanpH[S1]['datenum'], combinedmeanpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(combinedmeanpH[S2]['datenum'], combinedmeanpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmeanpH, ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "xkcd:cobalt blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total_spectro_out', data=RWSnmean, c='xkcd:cobalt blue', label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='pH_total', data=combinedmeanpH[S1], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=combinedmeanpH[S2], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})

ax.set_title("RWS & predicted pH based on A$_T$ & DIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH$_{total}$')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_TA_DIC_split.png") 

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
resultscombinedmeanN = pd.DataFrame.from_dict(results)
resultscombinedmeanN['datetime'] = combinedmean['datetime']
resultscombinedmeanN['longitude'] = combinedmean['longitude']
resultscombinedmeanN['latitude'] = combinedmean['latitude']
resultscombinedmeanN['dataset'] = combinedmean['dataset']
resultscombinedmeanN['datenum'] = combinedmean['datenum']
resultscombinedmeanN['year'] = combinedmean['year']

#%% # Logicals for colours in plots

LRg = resultscombinedmeanN['dataset'] == str('glodapnsmean')
LRd = resultscombinedmeanN['dataset'] == str('D366mean')
LRc = resultscombinedmeanN['dataset'] == str('Cefasmean')
LRr = resultscombinedmeanN['dataset'] == str('RWSnmean')

#%% # fCO2 prediction (nTA and nDIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
bslope, bintercept, br, bp, bse = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])

aslope, aintercept, ar, ap, ase = linregress(resultscombinedmeanN['datenum'], resultscombinedmeanN['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:goldenrod"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='SOCAT$_{SW}$')
# sns.regplot(x='datenum', y='fCO2', data=socatnsmean, ax=ax, ci=99.9,
#             scatter_kws={"color": "xkcd:black"}, line_kws={"color": "xkcd:dark grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, label='SOCAT$_{AIR}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanN[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanN[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanN[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanN[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='fCO2', data=resultscombinedmeanN, ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})

ax.set_title("SOCAT & predicted fCO$_2$ sea based on nA$_T$ & nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_nTA_nDIC.png") 

#%% # pH prediction (nTA and nDIC)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])

aslope, aintercept, ar, ap, ase = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

resultscombinedmeanNpH = resultscombinedmeanN.dropna(axis='rows', how='all', subset=['pH_total'])
S1 = (resultscombinedmeanNpH.year <= 2011)
S2 = (resultscombinedmeanNpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(resultscombinedmeanNpH[S1]['datenum'], resultscombinedmeanNpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(resultscombinedmeanNpH[S2]['datenum'], resultscombinedmeanNpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmeanpH, ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "xkcd:cobalt blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total_spectro_out', data=RWSnmean, c='xkcd:cobalt blue', label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNpH[S1], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNpH[S2], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})

ax.set_title("RWS & predicted pH based on nA$_T$ & nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH$_{total}$')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_nTA_nDIC_split.png")    

#%% # Use pyCO2sys to calculate pH and fCO2 sea based on nTA and corrected nDIC 
 
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
resultscombinedmeanNC = pd.DataFrame.from_dict(results)
resultscombinedmeanNC['datetime'] = combinedmean['datetime']
resultscombinedmeanNC['longitude'] = combinedmean['longitude']
resultscombinedmeanNC['latitude'] = combinedmean['latitude']
resultscombinedmeanNC['dataset'] = combinedmean['dataset']
resultscombinedmeanNC['datenum'] = combinedmean['datenum']
resultscombinedmeanNC['year'] = combinedmean['year']

#%% # Logicals for colours in plots

LRg = resultscombinedmeanNC['dataset'] == str('glodapnsmean')
LRd = resultscombinedmeanNC['dataset'] == str('D366mean')
LRc = resultscombinedmeanNC['dataset'] == str('Cefasmean')
LRr = resultscombinedmeanNC['dataset'] == str('RWSnmean')

#%% # fCO2 prediction (nTA and corrected nDIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
socatnsmeanair = socatnsmean.dropna(axis='rows', how='all', subset=['fCO2'])
bslope, bintercept, br, bp, bse = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])
aslope, aintercept, ar, ap, ase = linregress(resultscombinedmeanNC['datenum'], resultscombinedmeanNC['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:goldenrod"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='SOCAT$_{SW}$')
# sns.regplot(x='datenum', y='fCO2', data=socatnsmean, ax=ax, ci=99.9,
#             scatter_kws={"color": "xkcd:black"}, line_kws={"color": "xkcd:dark grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, label='SOCAT$_{AIR}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanNC[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanNC[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanNC[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'fCO2', data=resultscombinedmeanNC[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='fCO2', data=resultscombinedmeanNC, ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})

ax.set_title("SOCAT & predicted fCO$_{2SW}$ based on nA$_T$ & corrected nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_prediction_nTA_corrected_nDIC.png") 

#%% # pH prediction (nTA and corrected nDIC)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])
aslope, aintercept, ar, ap, ase = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

resultscombinedmeanNCpH = resultscombinedmeanNC.dropna(axis='rows', how='all', subset=['pH_total'])
S1 = (resultscombinedmeanNCpH.year <= 2011)
S2 = (resultscombinedmeanNCpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(resultscombinedmeanNCpH[S1]['datenum'], resultscombinedmeanNCpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(resultscombinedmeanNCpH[S2]['datenum'], resultscombinedmeanNCpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmeanpH, ax=ax,
            scatter_kws={"color": "None"}, line_kws={"color": "xkcd:cobalt blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total_spectro_out', data=RWSnmean, c='xkcd:cobalt blue', label='RWS$_{spectro}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[Lg], c='xkcd:violet', label='GLODAP$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[Ld], c='xkcd:neon pink', label='D366$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[Lc], c='xkcd:orange', label='CEFAS$_{pred}$')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[Lr], c='xkcd:evergreen', label='RWS$_{pred}$')
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNCpH[S1], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNCpH[S2], ax=ax, ci=99.9,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})

ax.set_title("RWS & predicted pH based on nA$_T$ & corrected nDIC data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH$_{total}$')
ax.set_ylim(7, 9)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_prediction_nTA_corrected_nDIC_split.png")    
