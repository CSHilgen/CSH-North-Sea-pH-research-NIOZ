# 5 + legend + no splitting up linear regression line + seasonal cycle

import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares
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

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'fCO2', c='xkcd:black', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_{2AIR}$ (uatm)")
ax.set_xlim(0, 300)
ax.set_ylim(330, 420)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(socatnsmeanair['datenum'], socatnsmeanair['fCO2']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
aslope, aintercept, ar, ap, ase = linregress(socatnsmeanair['datenum'], socatnsmeanair['fCO2'])
  
ax = axs[2]
sns.regplot(x='datenum', y='fCO2', data=socatnsmeanair, ax=ax,
            scatter_kws={"color": "xkcd:black"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Initial fCO$_2$ air SOCAT')

fx = np.linspace(socatnsmeanair.datenum.min(), socatnsmeanair.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_ylabel(None)
ax.set_xlabel('Time (yrs)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_fCO2air5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'fco2_sea', c='xkcd:orange', data=socatnsmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_{2SW}$ (uatm)")
ax.set_xlim(0, 300)
ax.set_ylim(150, 520)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_fco2_sea, [0.006, 386, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fco2_sea']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
aslope, aintercept, ar, ap, ase = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])

ax = axs[2]
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax,
            scatter_kws={"color": "xkcd:orange"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Initial fCO$_2$ sea SOCAT')

fx = np.linspace(socatnsmean.datenum.min(), socatnsmean.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_fCO2sea5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'deltafco2', c='xkcd:dark orange', data=socatnsmeandelta, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("ΔfCO$_2$ (uatm)")
ax.set_xlim(0, 300)
ax.set_ylim(-240, 130)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_fco2_sea, [0.006, 386, 162, 680], 
                           args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
aslope, aintercept, ar, ap, ase = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])

ax = axs[2]
sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta, ax=ax,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='ΔfCO$_2$ SOCAT')

fx = np.linspace(socatnsmeandelta.datenum.min(), socatnsmeandelta.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_deltafco25.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'dic_correctd_final', c='xkcd:purple', data=combinedmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("DIC (µmol/kg)")
ax.set_xlim(0, 300)
ax.set_ylim(2000, 2250)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'dic_correctd_final', c='xkcd:purple', data=combinedmean, s=20, alpha=0.4)

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

aslope, aintercept, ar, ap, ase = linregress(combinedmean['datenum'], combinedmean['dic_correctd_final'])

ax = axs[2]
sns.regplot(x='datenum', y='dic_correctd_final', data=combinedmean, ax=ax,
            scatter_kws={"color": "xkcd:purple"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Corrected nDIC Combined')
ax.scatter("datenum", "normalized_DIC", data=combinedmean, facecolors='none', edgecolor='xkcd:purple', label="nDIC Combined")
combinedmeansc_dic.plot('datenum', 'interpolator_dic', ax=ax, c='g', label='Seasonal cycle')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_DIC5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'normalized_TA', c='xkcd:red', data=combinedmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Alkalinity (µmol/kg)")
ax.set_xlim(0, 300)
ax.set_ylim(2280, 2430)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(100))
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'normalized_TA', c='xkcd:red', data=combinedmean, s=20, alpha=0.4)

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

ax = axs[2]
sns.regplot(x='datenum', y='normalized_TA', data=combinedmean, ax=ax,
            scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='nTA Combined')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_TA5.png")
plt.show()

#%%
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'aou', c='xkcd:spring green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("AOU (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(-150, 100)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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
slope, intercept, r, p, se = linregress(RWSomeanAOU['datenum'], RWSomeanAOU['aou'])

ax = axs[2]
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU, ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='AOU RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_AOU5.png")
plt.show()

#%%
fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'pH_total', c='xkcd:water blue', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("pH$_{total}$")
ax.set_xlim(0, 100)
ax.set_ylim(7.15, 9.10)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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
slope, intercept, r, p, se = linregress(RWSomeanpH['datenum'], RWSomeanpH['pH_total'])
nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

ax = axs[2]
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH, ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial pH RWS')
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.1f}'}, label='Initial pH$_{spectro}$ RWS')
 
ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_pH5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'oxygen umol/kg', c='xkcd:green', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("O$_2$ (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(175, 425)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg'])

ax = axs[2]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2, ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial O$_2$ RWS')

fx = np.linspace(RWSomeano2.datenum.min(), RWSomeano2.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_O25.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'chlorophyll', c='xkcd:brown', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Chlorophyll")
ax.set_xlim(0, 100)
ax.set_ylim(0, 30)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])

ax = axs[2]
sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl, ax=ax,
            scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

fx = np.linspace(RWSomeanChl.datenum.min(), RWSomeanChl.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_Chl5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_ammonia', c='xkcd:plum', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Ammonia (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 0.12)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

ax = axs[2]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomeanA, ax=ax,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial NH$_3$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_Am5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_phosphate', c='xkcd:apricot', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Phosphate (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 0.12)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanP['datenum'], RWSomeanP['total_phosphate']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWSomeanP['datenum'], RWSomeanP['total_phosphate'])

ax = axs[2]
sns.regplot(x='datenum', y='total_phosphate', data=RWSomeanP, ax=ax,
            scatter_kws={"color": "xkcd:apricot"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial PO$_4^{-3}$ RWS')

fx = np.linspace(RWSomeanP.datenum.min(), RWSomeanP.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_Phos5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_nitrate', c='xkcd:light violet', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Nitrate (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 0.75)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanN['datenum'], RWSomeanN['total_nitrate']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWSomeanN['datenum'], RWSomeanN['total_nitrate'])
 
ax = axs[2]
sns.regplot(x='datenum', y='total_nitrate', data=RWSomeanN, ax=ax,
            scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial NO$_3^-$ RWS')

fx = np.linspace(RWSomeanN.datenum.min(), RWSomeanN.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_Ni5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'total_silicate', c='xkcd:navy', data=RWSomean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Total Silicate (µmol/kg)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 0.75)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomeanS['datenum'], RWSomeanS['total_silicate']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWSomeanS['datenum'], RWSomeanS['total_silicate'])

ax = axs[2]
sns.regplot(x='datenum', y='total_silicate', data=RWSomeanS, ax=ax,
            scatter_kws={"color": "xkcd:navy"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial SiO$_4^{-4}$ RWS')

fx = np.linspace(RWSomeanS.datenum.min(), RWSomeanS.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_Si5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'salinity', c='xkcd:golden', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Salinity")
ax.set_xlim(0, 100)
ax.set_ylim(28, 36)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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
 
ax = axs[2]
sns.regplot(x='datenum', y='salinity', data=RWStotalmeanS, ax=ax,
            scatter_kws={"color": "xkcd:golden"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Salinity RWS')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_S5.png")
plt.show()

#%%

fig, axs = plt.subplots(dpi=300, ncols=3, gridspec_kw={'width_ratios': [1, 1, 5]}, figsize=(10,2.25), sharey=True)

ax = axs[0]
ax.scatter('distance_to_shore', 'temperature', c='xkcd:pink', data=RWStotalmean, s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Temperature (°C)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 22)
ax.minorticks_on()
ax.xaxis.set_major_locator(MultipleLocator(25))
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
opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWStotalmeanT['datenum'], RWStotalmeanT['temperature']))
slope, intercept, sine_stretch, sine_shift = opt_result['x']
slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])

ax = axs[2]
sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT, ax=ax,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Temperature RWS')

fx = np.linspace(RWStotalmeanT.datenum.min(), RWStotalmeanT.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
# ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
# ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.subplots_adjust(wspace=0.05, hspace=0.05)

plt.tight_layout()
plt.savefig("figures/Final_plots/Longterm_T5.png")
plt.show()
