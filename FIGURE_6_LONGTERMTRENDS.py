import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares
from matplotlib.ticker import FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import tools.seasonalfitting as SF_tools

#%% # Import datasets

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSomeanN = pd.read_csv("dataframes_made/RWSomeanN_final.csv")
RWSomeanP = pd.read_csv("dataframes_made/RWSomeanP_final.csv")
RWSomeanS = pd.read_csv("dataframes_made/RWSomeanS_final.csv")
RWStotalmeanT = pd.read_csv("dataframes_made/RWStotalmeanT_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
combinedmeansc_dic = pd.read_csv("dataframes_made/combinedmeansc_dic_final.csv")
socatnsmeandelta = pd.read_csv("dataframes_made/socatnsmeandelta_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
socatnsmeanair = pd.read_csv("dataframes_made/socatnsmeanair_final.csv")
RWSomeanChl = pd.read_csv("dataframes_made/RWSomeanChl_final.csv")
RWSomeano2 = pd.read_csv("dataframes_made/RWSomeano2_final.csv")
RWStotalmean = pd.read_csv("dataframes_made/RWStotalmean_final.csv")
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean_final.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean_final.csv")
D366mean = pd.read_csv("dataframes_made/D366mean_final.csv")

#%%
print('fCO2 air')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'fCO2', c='xkcd:black', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_{2AIR}$ (uatm)")
ax.set_xlim(0, 260)
ax.set_ylim(330, 430)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(20))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'fCO2', c='xkcd:black', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

# L1 = (socatnsmeanair.year >= 2000)

aslope, aintercept, ar, ap, ase = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])
print(f"p value from 2010 = {ap:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='fCO2', data=socatnsmeanair, ax=ax,
            scatter_kws={"color": "xkcd:black"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Initial fCO$_2$ air SOCAT')

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Time (yrs)')
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_fCO2air.png")
plt.show()

#%%
print('fCO2 sea')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'fco2_sea', c='xkcd:orange', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_{2SW}$ (uatm)")
ax.set_xlim(0, 260)
ax.set_ylim(150, 520)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'fco2_sea', c='xkcd:orange', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

# L1 = (socatnsmean.year >= 2000)

aslope, aintercept, ar, ap, ase = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])
print(f"p value from 1991-2020 = {ap:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax,
            scatter_kws={"color": "xkcd:orange"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Initial fCO$_2$ sea SOCAT')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_fCO2sea.png")
plt.show()

#%%
print('Delta fCO2')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'deltafco2', c='xkcd:dark orange', data=socatnsmeandelta, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("ΔfCO$_2$ (uatm)")
ax.set_xlim(0, 260)
ax.set_ylim(-270, 130)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'deltafco2', c='xkcd:dark orange', data=socatnsmeandelta, s=20, alpha=0.4)
ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

L1 = (socatnsmeandelta.year <= 2010)
L2 = (socatnsmeandelta.year >= 2010)

aslope, aintercept, ar, ap, ase = linregress(socatnsmeandelta[L1]['datenum'], socatnsmeandelta[L1]['deltafco2'])
bslope, bintercept, br, bp, bse = linregress(socatnsmeandelta[L2]['datenum'], socatnsmeandelta[L2]['deltafco2'])    
print(f"p value till 2010 = {ap:6f}")
print(f"p value from 2010 = {bp:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L1], ax=ax,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='ΔfCO$_2$ SOCAT')
sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L2], ax=ax,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [2,0,1]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=3, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_deltafco2.png")
plt.show()

#%%
print('DIC')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
dts = ax.scatter('distance_to_shore', 'dic', c='xkcd:purple', data=combinedmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("DIC (µmol/kg)")
ax.set_xlim(0, 260)
ax.set_ylim(2000, 2230)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
doy = ax.scatter('dayofyear', 'dic', c='xkcd:purple', data=combinedmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

L0 = (combinedmean.year <= 2011)
L1 = (combinedmean.year >= 2010)

aslope, aintercept, ar, ap, ase = linregress(combinedmean[L0]['datenum'], combinedmean[L0]['dic_correctd_final'])
bslope, bintercept, br, bp, bse = linregress(combinedmean[L1]['datenum'], combinedmean[L1]['dic_correctd_final'])
print(f"p value till 2010 = {ap:6f}")
print(f"p value from 2010 = {bp:6f}")

ax = axs[2]
ndic1 = sns.regplot(x='datenum', y='dic_correctd_final', data=combinedmean[L0], ax=ax,
            scatter_kws={"color": "xkcd:purple"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Corrected nDIC Combined')
ndic2 = sns.regplot(x='datenum', y='dic_correctd_final', data=combinedmean[L1], ax=ax,
            scatter_kws={"color": "xkcd:purple"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
labelz = ['Initial DIC Combined', 'Initial DIC Combined', f'y = {aslope:.1e}x + {aintercept:.1f}', f'y = {bslope:.1e}x + {bintercept:.1f}', 'nDIC Combined']
fig.legend([dts, doy, ndic1, ndic1, ndic2], labels=labelz, loc="lower center", ncol=5, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_DIC.png")
plt.show()

#%%
print('TA')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
dts = ax.scatter('distance_to_shore', 'alkalinity', c='xkcd:red', data=combinedmean, s=20, alpha=0.4, label='A$_T$ Combined')

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("A$_T$ (µmol/kg)")
ax.set_xlim(0, 260)
ax.set_ylim(2280, 2420)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(40))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
doy = ax.scatter('dayofyear', 'alkalinity', c='xkcd:red', data=combinedmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

aslope, aintercept, ar, ap, ase = linregress(combinedmean['datenum'], combinedmean['normalized_TA'])
print(f"p value from 2001-2021 = {ap:6f}")

ax = axs[2]
nta1 = sns.regplot(x='datenum', y='normalized_TA', data=combinedmean, ax=ax,
            scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='nTA Combined')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
labelz = ['Initial A$_T$ Combined', 'Initial A$_T$ Combined', f'y = {aslope:.1e}x + {aintercept:.1f}', 'nA$_T$ Combined']
fig.legend([dts, doy, nta1, nta1], labels=labelz, loc="lower center", ncol=5, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_TA.png")
plt.show()

#%%

print('AOU')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'aou', c='xkcd:spring green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("AOU (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(-150, 120)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'aou', c='xkcd:spring green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

RWSomeanAOU = RWSomean.dropna(axis='rows', how='all', subset=['aou'])
L0 = (RWSomeanAOU.year <= 1985)
L1 = (RWSomeanAOU.year >= 1985) & (RWSomeanAOU.year <= 2010)
L2 = (RWSomeanAOU.year >= 2010)

slope, intercept, r, p, se = linregress(RWSomeanAOU[L0]['datenum'], RWSomeanAOU[L0]['aou'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeanAOU[L1]['datenum'], RWSomeanAOU[L1]['aou'])
bslope, bintercept, br, bp, bse = linregress(RWSomeanAOU[L2]['datenum'], RWSomeanAOU[L2]['aou'])    
print(f"p value 1975-1985 = {p:6f}")
print(f"p value 1985-2010 = {ap:6f}")
print(f"p value from 2010 = {bp:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L0], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='AOU RWS')
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L1], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L2], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [3,1,2]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=3, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_AOU.png")
plt.show()

#%%
print('pH')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'pH_total', c='xkcd:water blue', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("pH$_{total}$")
ax.set_xlim(0, 75)
ax.set_ylim(7.15, 9.10)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'pH_total', c='xkcd:water blue', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

RWSomeanpH = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
RWSnmeanpH = RWSnmean.dropna(axis='rows', how='all', subset=['pH_total_spectro_out'])
L0 = (RWSomeanpH.year <= 1985)
L1 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
L2 = (RWSomeanpH.year >= 2010)

slope, intercept, r, p, se = linregress(RWSomeanpH[L0]['datenum'], RWSomeanpH[L0]['pH_total'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
bslope, bintercept, br, bp, bse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])    
nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])
print(f"p value 1975-1985 = {p:6f}")
print(f"p value 1985-2010 = {ap:6f}")
print(f"p value 2010-2018 = {bp:6f}")
print(f"p value 2018-2021 = {np:6f}")
      
ax = axs[2]
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L0], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial pH RWS')
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
            scatter_kws={"color": "xkcd:cobalt blue"}, line_kws={"color": "xkcd:cobalt blue", 'label': f'y = {nslope:.1e}x + {nintercept:.1f}', 'linestyle': 'dotted'}, label='Initial pH$_{spectro}$ RWS')
 
ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [4,5,1,2,3]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=5, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_pH.png")
plt.show()

#%%
print('Oxygen')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'oxygen umol/kg', c='xkcd:green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("O$_2$ (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(175, 425)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'oxygen umol/kg', c='xkcd:green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

L0 = (RWSomeano2.year <= 1985)
L1 = (RWSomeano2.year >= 1985) & (RWSomeano2.year <= 2010)
L2 = (RWSomeano2.year >= 2010)

slope, intercept, r, p, se = linregress(RWSomeano2[L0]['datenum'], RWSomeano2[L0]['oxygen umol/kg'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeano2[L1]['datenum'], RWSomeano2[L1]['oxygen umol/kg'])
bslope, bintercept, br, bp, bse = linregress(RWSomeano2[L2]['datenum'], RWSomeano2[L2]['oxygen umol/kg'])    
print(f"p value 1975-1985 = {p:6f}")
print(f"p value 1985-2010 = {ap:6f}")
print(f"p value from 2010 = {bp:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L0], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial O$_2$ RWS')
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L1], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L2], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [3,1,2]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=3, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_O2.png")
plt.show()

#%%
print('Chlorophyll')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'chlorophyll', c='xkcd:brown', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Chlorophyll-a (µg/L)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 30)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(5))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'chlorophyll', c='xkcd:brown', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
  
print(f"p value 1975-2018 = {p:6f}")
slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])

ax = axs[2]
sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl, ax=ax,
            scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Chl.png")
plt.show()

#%%
print('Ammonia')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_ammonia', c='xkcd:plum', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Ammonia (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 0.12)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'total_ammonia', c='xkcd:plum', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
   
RWSomeanA = RWSomean.dropna(axis='rows', how='all', subset=['total_ammonia'])
slope, intercept, r, p, se = linregress(RWSomeanA['datenum'], RWSomeanA['total_ammonia'])
print(f"p value 1975-2018 = {p:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomeanA, ax=ax,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial NH$_3$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Am.png")
plt.show()

#%%
print('Phosphate')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_phosphate', c='xkcd:apricot', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Phosphate (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 0.12)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'total_phosphate', c='xkcd:apricot', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

slope, intercept, r, p, se = linregress(RWSomeanP['datenum'], RWSomeanP['total_phosphate'])
print(f"p value 1975-2018 = {p:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='total_phosphate', data=RWSomeanP, ax=ax,
            scatter_kws={"color": "xkcd:apricot"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial PO$_4^{-3}$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Phos.png")
plt.show()

#%%
print('Nitrate')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_nitrate', c='xkcd:light violet', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Nitrate (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 0.75)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'total_nitrate', c='xkcd:light violet', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
 
slope, intercept, r, p, se = linregress(RWSomeanN['datenum'], RWSomeanN['total_nitrate'])
print(f"p value 1975-2017 = {p:6f}")
 
ax = axs[2]
sns.regplot(x='datenum', y='total_nitrate', data=RWSomeanN, ax=ax,
            scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial NO$_3^-$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Ni.png")
plt.show()

#%%
print('Silicate')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_silicate', c='xkcd:navy', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Silicate (µmol/kg)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 0.75)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'total_silicate', c='xkcd:navy', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

slope, intercept, r, p, se = linregress(RWSomeanS['datenum'], RWSomeanS['total_silicate'])
print(f"p value 1975-2018 = {p:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='total_silicate', data=RWSomeanS, ax=ax,
            scatter_kws={"color": "xkcd:navy"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial SiO$_4^{-4}$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Si.png")
plt.show()

#%%
print('Salinity')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'salinity', c='xkcd:golden', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Salinity")
ax.set_xlim(0, 75)
ax.set_ylim(27, 36.5)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(1))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'salinity', c='xkcd:golden', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

RWStotalmeanS = RWStotalmean.dropna(axis='rows', how='all', subset=['salinity'])
slope, intercept, r, p, se = linregress(RWStotalmeanS['datenum'], RWStotalmeanS['salinity'])
print(f"p value 1975-2021 = {p:6f}")
 
ax = axs[2]
sns.regplot(x='datenum', y='salinity', data=RWStotalmeanS, ax=ax,
            scatter_kws={"color": "xkcd:golden"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Salinity RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_S.png")
plt.show()

#%%
print('Temperature')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'temperature', c='xkcd:pink', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Temperature (°C)")
ax.set_xlim(0, 75)
ax.set_ylim(0, 22)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(5))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'temperature', c='xkcd:pink', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

RWStotalmeanT = RWStotalmean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])
print(f"p value 1975-2021 = {p:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT, ax=ax,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Temperature RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.set_xlim(10950, 19345)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [1,0]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=2, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_T.png")
plt.show()

#%%
print('Calcium')
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10.5,2.25), sharey=True)

RWSoCa = RWSo.dropna(axis='rows', how='all', subset=['calcium_corrected'])  
L0 = (RWSoCa.year <= 2014)
L1 = (RWSoCa.year >= 2015) & (RWSoCa.datenum <= 16996.3)
L2 = (RWSoCa.datenum >= 17014.4)  

ax = axs[0]
sc = ax.scatter('salinity', 'calcium_corrected', c='yellow', data=RWSoCa[L0],  s=20, label='Method 1$_{corr}$')
sc = ax.scatter('salinity', 'calcium_corrected', c='orange', data=RWSoCa[L1], s=20, label='Method 2')
sc = ax.scatter('salinity', 'calcium_corrected', c='green', data=RWSoCa[L2], s=20, label='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Relative Calcium (μmol/kg)")
ax.set_ylim(0, 7500)

ax = axs[1]
ax.scatter('dayofyear', 'calcium_corrected', c='yellow', data=RWSoCa[L0], s=20, label='Method 1$_{corr}$')
ax.scatter('dayofyear', 'calcium_corrected', c='orange', data=RWSoCa[L1], s=20, label='Method 2')
ax.scatter('dayofyear', 'calcium_corrected', c='green', data=RWSoCa[L2], s=20, label ='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Months of year")
month_fmt = DateFormatter('%b')
def m_fmt(x, pos=None):
    return month_fmt(x)[0]

ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
ax.set_ylim(None)
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

LR0 = (RWSoCa.datenum <= 16629)
LR1 = (RWSoCa.datenum >= 16500) & (RWSoCa.datenum <= 17315.6)
LR2 = (RWSoCa.datenum >= 17315.6)  

slope, intercept, r, p, se = linregress(RWSoCa[LR0]['datenum'], RWSoCa[LR0]['calcium_corrected'])
aslope, aintercept, ar, ap, ase = linregress(RWSoCa[LR1]['datenum'], RWSoCa[LR1]['calcium_corrected'])
bslope, bintercept, br, bp, bse = linregress(RWSoCa[LR2]['datenum'], RWSoCa[LR2]['calcium_corrected'])    
print(f"p value 2009-2015 = {p:6f}")
print(f"p value 2015-2017 = {ap:6f}")
print(f"p value 2017-2018 = {bp:6f}")

ax = axs[2]
sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[LR0], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1e}', 'linestyle': '--'})
sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[LR1], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1e}'})
sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[LR2], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1f}x + {bintercept:.1e}', 'linestyle': 'dotted'})
ax.scatter('datenum', 'calcium_corrected', c='yellow', data=RWSoCa[L0], s=20, label='Corrected M1 Ca RWS')
ax.scatter('datenum', 'calcium_corrected', c='orange', data=RWSoCa[L1], s=20, label='M2 Ca RWS')
ax.scatter('datenum', 'calcium_corrected', c='green', data=RWSoCa[L2], s=20, label='M3 Ca RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [3,4,5,0,1,2]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=6, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout(pad=0.5)
plt.savefig("figures/Final_plots/Longterm_Ca2.png")
plt.show()