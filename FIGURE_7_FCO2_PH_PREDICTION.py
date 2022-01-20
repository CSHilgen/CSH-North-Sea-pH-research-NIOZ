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

#%% # 

Lg = combinedmean['dataset'] == str('glodapnsmean')
Ld = combinedmean['dataset'] == str('D366mean')
Lc = combinedmean['dataset'] == str('Cefasmean')
Lr = combinedmean['dataset'] == str('RWSnmean')

#%% # fCO2 prediction (TA and DIC)

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
socatnsmeanair = socatnsmean.dropna(axis='rows', how='all', subset=['fCO2'])
bslope, bintercept, br, bp, bse = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])
combinedmeanfco2_sea = combinedmean.dropna(axis='rows', how='all', subset=['fCO2'])
aslope, aintercept, ar, ap, ase = linregress(combinedmeanfco2_sea['datenum'], combinedmeanfco2_sea['fCO2'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "xkcd:goldenrod"}, line_kws={"color": "xkcd:goldenrod", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='SOCAT sea')
sns.regplot(x='datenum', y='fCO2', data=socatnsmeanair, ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "xkcd:black"}, line_kws={"color": "xkcd:black", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, label='SOCAT air')
sns.regplot(x='datenum', y='fCO2', data=combinedmean, ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
ax.scatter('datenum', 'fCO2', data=combinedmean[Lg], edgecolors='xkcd:light violet', facecolors='None', label='GLODAP$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'fCO2', data=combinedmean[Ld], edgecolors='xkcd:neon pink', facecolors='None', label='D366$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'fCO2', data=combinedmean[Lc], edgecolors='xkcd:orange', facecolors='None', label='CEFAS$_{pred}$', s=50, linewidth=2)
ax.scatter('datenum', 'fCO2', data=combinedmean[Lr], edgecolors='xkcd:evergreen', facecolors='None', label='RWS$_{pred}$', s=50, linewidth=2)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('fCO$_2$ (µatm)', fontsize=14)
ax.set_ylim(200,550)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
handles, labels = ax.get_legend_handles_labels()
order = [3, 0, 4, 1, 5, 2, 6, 7, 8]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], ncol=6, loc="lower left", mode = "expand")

plt.tight_layout()
plt.savefig("figures/Final_plots/fCO2_TA_DICair.png") 

#%% # pH prediction (TA and DIC)

RWSomeanpH = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
combinedmeanpH = combinedmean.dropna(axis='rows', how='all', subset=['pH_total'])

L1 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
L2 = (RWSomeanpH.year >= 2010)
L0 = (RWSomeanpH.pH_total > 7.5)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])

S1 = (combinedmeanpH.year <= 2011)
S2 = (combinedmeanpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(combinedmeanpH[S1]['datenum'], combinedmeanpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(combinedmeanpH[S2]['datenum'], combinedmeanpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total', data=combinedmeanpH[S1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, x_ci="sd")
sns.regplot(x='datenum', y='pH_total', data=combinedmeanpH[S2], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'}, x_ci="sd")
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total', data=combinedmean[Lg], edgecolors='xkcd:light violet', facecolors='None', label='GLODAP$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=combinedmean[Ld], edgecolors='xkcd:neon pink', facecolors='None', label='D366$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=combinedmean[Lc], edgecolors='xkcd:orange', facecolors='None', label='CEFAS$_{pred}$', s=50, linewidth=2)
ax.scatter('datenum', 'pH_total', data=combinedmean[Lr], edgecolors='xkcd:evergreen', facecolors='None', label='RWS$_{pred}$', s=50, linewidth=2)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('pH$_{total}$', fontsize=14)
ax.set_ylim(7, 8.5)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
handles, labels = ax.get_legend_handles_labels()
order = [4, 0, 5, 1, 6, 2, 7, 3, 8]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], ncol=5, loc="lower left", mode = "expand")

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_TA_DIC.png")    
plt.show()

#%% # Predict pH based on nTA and nDIC

#combinedmean = combinedmean.reset_index()

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

#%% # # pH prediction (nTA and nDIC)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])

resultscombinedmeanNpH = resultscombinedmeanN.dropna(axis='rows', how='all', subset=['pH_total'])
S1 = (resultscombinedmeanNpH.year <= 2011)
S2 = (resultscombinedmeanNpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(resultscombinedmeanNpH[S1]['datenum'], resultscombinedmeanNpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(resultscombinedmeanNpH[S2]['datenum'], resultscombinedmeanNpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNpH[S1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNpH[S2], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'}, x_ci="sd")
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[LRg], edgecolors='xkcd:light violet', facecolors='None', label='GLODAP$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[LRd], edgecolors='xkcd:neon pink', facecolors='None', label='D366$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[LRc], edgecolors='xkcd:orange', facecolors='None', label='CEFAS$_{pred}$', s=50, linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanN[LRr], edgecolors='xkcd:evergreen', facecolors='None', label='RWS$_{pred}$', s=50, linewidth=2)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('pH$_{total}$', fontsize=14)
ax.set_ylim(7, 8.5)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
handles, labels = ax.get_legend_handles_labels()
order = [4, 0, 5, 1, 6, 2, 7, 3, 8]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], ncol=5, loc="lower left", mode = "expand")

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_nTA_nDIC.png")    
plt.show()

#%% # Predict pH based on nTA and corrected nDIC

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

#%% # pH prediction (nTA and corrected nDIC)

slope, intercept, r, p, se = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
dslope, dintercept, dr, dp, dse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])

resultscombinedmeanNCpH = resultscombinedmeanNC.dropna(axis='rows', how='all', subset=['pH_total'])
S1 = (resultscombinedmeanNCpH.year <= 2011)
S2 = (resultscombinedmeanNCpH.year >= 2010)
bslope, bintercept, br, bp, bse = linregress(resultscombinedmeanNCpH[S1]['datenum'], resultscombinedmeanNCpH[S1]['pH_total'])
cslope, cintercept, cr, cp, cse = linregress(resultscombinedmeanNCpH[S2]['datenum'], resultscombinedmeanNCpH[S2]['pH_total'])

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, x_ci="sd")
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][L0], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "blue", 'label': f'y = {dslope:.1e}x + {dintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNCpH[S1], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}'}, x_ci="sd")
sns.regplot(x='datenum', y='pH_total', data=resultscombinedmeanNCpH[S2], ax=ax, x_estimator=np.mean,
            scatter_kws={"color": "None"}, line_kws={"color": "grey", 'linestyle': 'dotted', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})
ax.scatter('datenum', 'pH_total', data=RWSomean, c='xkcd:water blue', label='RWS')
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[LRg], edgecolors='xkcd:light violet', facecolors='None', label='GLODAP$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[LRd], edgecolors='xkcd:neon pink', facecolors='None', label='D366$_{pred}$', s=50,linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[LRc], edgecolors='xkcd:orange', facecolors='None', label='CEFAS$_{pred}$', s=50, linewidth=2)
ax.scatter('datenum', 'pH_total', data=resultscombinedmeanNC[LRr], edgecolors='xkcd:evergreen', facecolors='None', label='RWS$_{pred}$', s=50, linewidth=2)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('pH$_{total}$', fontsize=14)
ax.set_ylim(7, 8.5)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
handles, labels = ax.get_legend_handles_labels()
order = [4, 0, 5, 1, 6, 2, 7, 3, 8]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], ncol=5, loc="lower left", mode = "expand")

plt.tight_layout()
plt.savefig("figures/Final_plots/pH_nTA_ncDIC.png")  
plt.show()