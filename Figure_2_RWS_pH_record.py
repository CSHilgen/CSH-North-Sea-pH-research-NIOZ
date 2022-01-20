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

#%% # Long Term Trend of pH RWSomean (splitting LR up)

L0 = (RWSomeanpH.year <= 1985)
L1 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
L2 = (RWSomeanpH.year >= 2010)

fig, ax = plt.subplots(dpi=300, figsize=(14,6))

slope, intercept, r, p, se = linregress(RWSomeanpH[L0]['datenum'], RWSomeanpH[L0]['pH_total'])
aslope, aintercept, ar, ap, ase = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
bslope, bintercept, br, bp, bse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])    
nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

ax = ax
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L0], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='pH RWS')
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
            scatter_kws={"color": "xkcd:cobalt blue"}, line_kws={"color": "xkcd:cobalt blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.1f}'}, label='pH$_{spectro}$ RWS')

ax.set_title("pH RWS data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)", fontsize=14)
ax.set_ylabel('pH$_{total}$', fontsize=14)
ax.set_ylim(7.15, 9.10)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Final_plots/Figure_2_pH_split_up.png")     
plt.show()