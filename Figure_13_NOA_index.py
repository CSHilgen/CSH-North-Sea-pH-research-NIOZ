import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress

#%% # Import data

naoindex = pd.read_csv("data_nao/nao_index.csv")
naoindex = naoindex.rename(columns={'noa_index':'nao_index'})
naoindex[['year', 'month', 'day']] = naoindex['year'].str.split('-', expand=True)
naoindex['datetime'] = pd.to_datetime(naoindex[['year', 'month', 'day']], format='%YYYY%mm%dd')
naoindex['year'] = naoindex['year'].astype(int)
naoindex['datenum'] = mdates.date2num(naoindex.datetime)
naoindexyear = naoindex.set_index('datetime').resample('Y').mean()

#%% # Plot of NAO 

# Set logicals for linear regression lines
# L0 = (naoindex.year <= 1987)
# L1 = (naoindex.year >= 1986) & (naoindex.year <= 2010)
# L2 = (naoindex.year >= 2010) & (naoindex.year <= 2018)
# L3 = (naoindex.year >= 2018)

L0 = (naoindex.year <= 1989)
L1 = (naoindex.year >= 1989) & (naoindex.year <= 2010)
L2 = (naoindex.year >= 2010) & (naoindex.year <= 2018)
L3 = (naoindex.year >= 2018) & (naoindex.datenum <= 18747)

fig, ax = plt.subplots(dpi=300, figsize=(14,6))

slope, intercept, r, p, se = linregress(naoindex[L0]['datenum'], naoindex[L0]['nao_index'])
aslope, aintercept, ar, ap, ase = linregress(naoindex[L1]['datenum'], naoindex[L1]['nao_index'])
bslope, bintercept, br, bp, bse = linregress(naoindex[L2]['datenum'], naoindex[L2]['nao_index'])
cslope, cintercept, cr, cp, cse = linregress(naoindex[L3]['datenum'], naoindex[L3]['nao_index'])

sns.regplot(x='datenum', y='nao_index', data=naoindex[L0], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "black", 'label': f'y = {slope:.1e}x + {intercept:.2f}', 'linestyle': '--',})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L1], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "black", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L2], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "black", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L3], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "black", 'linestyle': 'dashdot', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})

width = 20

ax.plot('datenum', 'nao_index', c='xkcd:medium grey', data=naoindexyear, label='NAO index averaged per year')

P = (naoindex['nao_index'] >= 0)
M = (naoindex['nao_index'] < 0)
ax.bar(naoindex['datenum'][P], naoindex['nao_index'][P], width, color='b', alpha=0.6)
ax.bar(naoindex['datenum'][M], naoindex['nao_index'][M], width, color='r', alpha=0.6)

ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('NAO index', fontsize=14)
ax.grid(alpha=0.3)
ax.set_xlim(1825, 19000)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_13_nao_index.png")     
plt.show()

#%% # Plot of nao and T

# Import T data
RWStotalmeanT = pd.read_csv("dataframes_made/RWStotalmeanT_final.csv")
RWStotalmeanT['datetime'] = pd.to_datetime(RWStotalmeanT['datetime'])
RWStotalmeanTyear = RWStotalmeanT.set_index('datetime').resample('Y').mean()
RWStotalmeanTyear = RWStotalmeanTyear.reset_index()

L0 = (naoindex.datenum >= 1825) & (naoindex.datenum <= 5840)
L1 = (naoindex.datenum >= 5475) & (naoindex.datenum <= 14965)
L2 = (naoindex.datenum >= 14600) & (naoindex.datenum <= 17885)
L3 = (naoindex.datenum >= 17520)

fig, ax = plt.subplots(dpi=300, figsize=(14,6))

ax1=ax

width = 20

ax.plot('datenum', 'nao_index', c='xkcd:medium grey', data=naoindexyear, label='NAO index averaged per year')

P = (naoindex['nao_index'] >= 0)
M = (naoindex['nao_index'] < 0)
ax.bar(naoindex['datenum'][P], naoindex['nao_index'][P], width, color='b', alpha=0.2)
ax.bar(naoindex['datenum'][M], naoindex['nao_index'][M], width, color='r', alpha=0.2)

ax1.set_ylabel('NAO index', fontsize=14)
ax1.legend(loc='lower left')

ax2 = ax.twinx()
ax=ax2
ax2.plot('datenum', 'temperature', data=RWStotalmeanTyear, c='xkcd:pink', label='T$_{SW}$ RWS')

ax2.set_ylabel('Temperature (°C)', fontsize=14)
ax1.set_xlabel("Time (yrs)", fontsize=14)
ax2.legend()
ax1.grid(alpha=0.3)
ax1.set_xlim(1825, 19000)
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax1.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax1.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_S9_nao_T.png")     
plt.show()