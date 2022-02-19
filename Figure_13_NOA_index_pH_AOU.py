import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress

#%% # Import dataframes

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")

RWSomeanpH = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
RWSnmeanpH = RWSnmean.dropna(axis='rows', how='all', subset=['pH_total_spectro_out'])
RWSomeanpH['datetime'] = pd.to_datetime(RWSomeanpH['datetime'])
RWSnmeanpH['datetime'] = pd.to_datetime(RWSnmeanpH['datetime'])

naoindex = pd.read_csv("data_nao/nao_index.csv")
naoindex = naoindex.rename(columns={'noa_index':'nao_index'})
naoindex[['year', 'month', 'day']] = naoindex['year'].str.split('-', expand=True)
naoindex['datetime'] = pd.to_datetime(naoindex[['year', 'month', 'day']], format='%YYYY%mm%dd')
naoindex['year'] = naoindex['year'].astype(int)
naoindex['datenum'] = mdates.date2num(naoindex.datetime)

#%%

fig, ax = plt.subplots(dpi=300, figsize=(14,4))

P = RWSomeanpH.pH_total > 7.5

RWSomeanpHyear = RWSomeanpH[P].set_index('datetime').resample('Y').mean()
RWSnmeanpHyear = RWSnmeanpH.set_index('datetime').resample('Y').mean()

ax=ax
L0 = (RWSomeanpH.year <= 1986)
L1 = (RWSomeanpH.year >= 1986) & (RWSomeanpH.year <= 2010)
L2 = (RWSomeanpH.year >= 2010)
P = (RWSomeanpH.pH_total >= 7.6) 

slope, intercept, r, p, se = linregress(RWSomeanpH[L0]['datenum'], RWSomeanpH[L0]['pH_total'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
bslope, bintercept, br, bp, bse = linregress(RWSomeanpH[L2][P]['datenum'], RWSomeanpH[L2][P]['pH_total'])    
nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

ax.plot('datenum', 'pH_total', c='xkcd:black', data=RWSomeanpHyear, label='pH RWS averaged per year')

ax.scatter('datenum', 'pH_total', data=RWSomeanpH, c='xkcd:water blue', alpha=0.8, label='pH RWS')
ax.scatter('datenum', 'pH_total_spectro_out', data=RWSnmeanpH, c='xkcd:cobalt blue', alpha=0.8, label='pH$_{spectro}$ RWS')

sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L0], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2][P], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "xkcd:dark blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.1f}'})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('pH$_{total}$', fontsize=14)
ax.set_ylim(7.15, 8.75)
ax.set_xlim(1825, 19000)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

handles, labels = ax.get_legend_handles_labels()
order = [5,6,0,1,2,3,4]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=7, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

ax.plot('datenum', 'pH_total_spectro_out', c='xkcd:black', data=RWSnmeanpHyear, label=None)

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_13_pH.png")     
plt.show()

#%%

fig, ax = plt.subplots(dpi=300, figsize=(14,4))

ax=ax
RWSomeanAOU = RWSomean.dropna(axis='rows', how='all', subset=['aou'])
RWSomeanAOU['datetime'] = pd.to_datetime(RWSomeanAOU['datetime'])
RWSomeanAOUyear = RWSomeanAOU.set_index('datetime').resample('Y').mean()
L0 = (RWSomeanAOU.year <= 1985)
L1 = (RWSomeanAOU.year >= 1985) & (RWSomeanAOU.year <= 2010)
L2 = (RWSomeanAOU.year >= 2010)

slope, intercept, r, p, se = linregress(RWSomeanAOU[L0]['datenum'], RWSomeanAOU[L0]['aou'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeanAOU[L1]['datenum'], RWSomeanAOU[L1]['aou'])
bslope, bintercept, br, bp, bse = linregress(RWSomeanAOU[L2]['datenum'], RWSomeanAOU[L2]['aou'])    

ax.plot('datenum', 'aou', c='xkcd:black', data=RWSomeanAOUyear, label='AOU RWS averaged per year')

ax.scatter(RWSomeanAOU['datenum'][RWSomeanAOU.aou >=0], RWSomeanAOU['aou'][RWSomeanAOU.aou >=0], c='xkcd:steel grey', label='Hetetrophic (p<r)')
ax.scatter(RWSomeanAOU['datenum'][RWSomeanAOU.aou <0], RWSomeanAOU['aou'][RWSomeanAOU.aou <0], c='xkcd:pea green', label='Autotrophic (p>r)')

sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L0], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='AOU RWS')
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L1], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L2], ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel("AOU (µmol/kg)", fontsize=14)
ax.set_xlim(1825, 19000)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [4,5,0,1,2,3]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=6, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_13_AOU2.png")     
plt.show()

#%%%

fig, ax = plt.subplots(dpi=300, figsize=(14,4))

naoindexyear = naoindex.set_index('datetime').resample('Y').mean()

ax=ax
L0 = (naoindex.year <= 1989)
L1 = (naoindex.year >= 1989) & (naoindex.year <= 2010)
L2 = (naoindex.year >= 2010) & (naoindex.year <= 2018)
L3 = (naoindex.year >= 2018) & (naoindex.datenum <= 18747)

slope, intercept, r, p, se = linregress(naoindex[L0]['datenum'], naoindex[L0]['nao_index'])
aslope, aintercept, ar, ap, ase = linregress(naoindex[L1]['datenum'], naoindex[L1]['nao_index'])
bslope, bintercept, br, bp, bse = linregress(naoindex[L2]['datenum'], naoindex[L2]['nao_index'])
cslope, cintercept, cr, cp, cse = linregress(naoindex[L3]['datenum'], naoindex[L3]['nao_index'])

sns.regplot(x='datenum', y='nao_index', data=naoindex[L0], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}', 'linestyle': '--',})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L1], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L2], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='nao_index', data=naoindex[L3], ax=ax, x_ci='sd',
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'linestyle': 'dashdot', 'label': f'y = {cslope:.1e}x + {cintercept:.1f}'})

width = 20

ax.plot('datenum', 'nao_index', c='xkcd:black', data=naoindexyear, label='NAOI averaged per year')

P = (naoindex['nao_index'] >= 0)
M = (naoindex['nao_index'] < 0)
ax.bar(naoindex['datenum'][P], naoindex['nao_index'][P], width, color='xkcd:light blue', alpha=0.9, label='+ NAO')
ax.bar(naoindex['datenum'][M], naoindex['nao_index'][M], width, color='xkcd:light red', alpha=0.9, label='- NAO')

ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('NAO index', fontsize=14)
ax.grid(alpha=0.3)
ax.set_xlim(1825, 19000)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
handles, labels = ax.get_legend_handles_labels()
order = [5,6,4,0,1,2,3]
fig.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc="lower center", ncol=7, bbox_to_anchor=(.075, 0.95, 0.9, 1.02), borderaxespad=0, mode='expand', fontsize=9)

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_13_nao.png")     
plt.show()