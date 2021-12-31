import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import linregress
from scipy.optimize import least_squares
import tools.seasonalfitting as SF_tools

#%% # Import datasets

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean_final.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean_final.csv")
D366mean = pd.read_csv("dataframes_made/D366mean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")

#%% # Temperature - Time - Datasets - LINEAR REGRESSION

fig, axs = plt.subplots(dpi=300, nrows=2)

RWSomeanlr = RWSomean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(RWSomeanlr['datenum'], RWSomeanlr['temperature'])

ax = axs[0]
ax.scatter('datenum', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
sns.regplot(x='datenum', y='temperature', data=RWSomean, ax=ax,
            scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.4f}x + {intercept:.1f}'})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Datasets North Sea')

combinedmeanlr = combinedmean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(combinedmeanlr['datenum'], combinedmeanlr['temperature'])

ax = axs[1]
ax.scatter("datenum", "temperature", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:greenish', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:dark orange', data=RWSnmean, label='RWS', s=20, alpha=0.4)
sns.regplot(x='datenum', y='temperature', data=combinedmean, ax=ax,
            scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.4f}x + {intercept:.1f}'})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
plt.tight_layout()
plt.savefig("figures/T_mean_time_datasets_LR.png")
plt.show()

#%% # Temperature - Time - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('datenum', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Datasets North Sea')

ax = axs[1]
ax.scatter("datenum", "temperature", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:greenish', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datenum', 'temperature', c='xkcd:dark orange', data=RWSnmean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

plt.tight_layout()
plt.savefig("figures/T_mean_time_datasets.png")
plt.show()

#%% # Temperature - Time - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('datenum', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("RWSo Temperature (°C)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Seasons North Sea')

ax = axs[1]
sc = ax.scatter('datenum', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (°C)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
cbar.ax.tick_params(rotation=90)

plt.tight_layout()
plt.savefig("figures/T_mean_time_seasons.png")
plt.show()

#%% # Temperature - Time - Regions

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
x = RWSomean['datenum']
y = RWSomean['temperature']

L0 = (RWSomean['distance_to_shore'] > 0) & (RWSomean['distance_to_shore'] <=4)
L1 = (RWSomean['distance_to_shore'] > 4) & (RWSomean['distance_to_shore'] <=10)
L2 = (RWSomean['distance_to_shore'] > 10) & (RWSomean['distance_to_shore'] <=20)
L3 = (RWSomean['distance_to_shore'] > 20) & (RWSomean['distance_to_shore'] <=30)
L4 = (RWSomean['distance_to_shore'] > 30) & (RWSomean['distance_to_shore'] <=50)
L5 = (RWSomean['distance_to_shore'] > 50) & (RWSomean['distance_to_shore'] <=70)
L6 = (RWSomean['distance_to_shore'] > 70) & (RWSomean['distance_to_shore'] <=100)
L7 = (RWSomean['distance_to_shore'] > 100) & (RWSomean['distance_to_shore'] <=150)
L8 = (RWSomean['distance_to_shore'] > 150) & (RWSomean['distance_to_shore'] <=200)
L9 = (RWSomean['distance_to_shore'] > 200) & (RWSomean['distance_to_shore'] <=250)
L10 = (RWSomean['distance_to_shore'] > 250) & (RWSomean['distance_to_shore'] <=300)

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('RWSo Temperature (°C)')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Temperature data - Regions North Sea')

ax=axs[1]
x = combinedmean['datenum']
y = combinedmean['temperature']

L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Temperature (°C)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.get_legend().set_title("Km to shore")

#plt.tight_layout()
plt.savefig("figures/T_mean_time_regions.png")
plt.show()

#%% # Temperature - Dayofyear - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('dayofyear', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Datasets North Sea')

ax = axs[1]
ax.scatter("dayofyear", "temperature", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('dayofyear', 'temperature', c='xkcd:greenish', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
ax.scatter('dayofyear', 'temperature', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('dayofyear', 'temperature', c='xkcd:dark orange', data=RWSnmean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

plt.tight_layout()
plt.savefig("figures/T_mean_dayofyear_datasets.png")
plt.show()

#%% # Temperature - Dayofyear - Regions

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
x = RWSomean['dayofyear']
y = RWSomean['temperature']

L0 = (RWSomean['distance_to_shore'] > 0) & (RWSomean['distance_to_shore'] <=4)
L1 = (RWSomean['distance_to_shore'] > 4) & (RWSomean['distance_to_shore'] <=10)
L2 = (RWSomean['distance_to_shore'] > 10) & (RWSomean['distance_to_shore'] <=20)
L3 = (RWSomean['distance_to_shore'] > 20) & (RWSomean['distance_to_shore'] <=30)
L4 = (RWSomean['distance_to_shore'] > 30) & (RWSomean['distance_to_shore'] <=50)
L5 = (RWSomean['distance_to_shore'] > 50) & (RWSomean['distance_to_shore'] <=70)
L6 = (RWSomean['distance_to_shore'] > 70) & (RWSomean['distance_to_shore'] <=100)
L7 = (RWSomean['distance_to_shore'] > 100) & (RWSomean['distance_to_shore'] <=150)
L8 = (RWSomean['distance_to_shore'] > 150) & (RWSomean['distance_to_shore'] <=200)
L9 = (RWSomean['distance_to_shore'] > 200) & (RWSomean['distance_to_shore'] <=250)
L10 = (RWSomean['distance_to_shore'] > 250) & (RWSomean['distance_to_shore'] <=300)

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('RWSo Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Temperature data - Regions North Sea')

ax=axs[1]
x = combinedmean['dayofyear']
y = combinedmean['temperature']

L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

# plt.tight_layout()
plt.savefig("figures/T_mean_dayofyear_regions.png")
plt.show()

#%% Temperature - Dayofyear - Year

fig, axs = plt.subplots(dpi=300, nrows=2)

cm = plt.cm.get_cmap('rainbow')
vmin = 1970
vmax = 2021

ax=axs[0]
sc = ax.scatter('dayofyear', 'temperature',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 6)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([1970, 1980, 1990, 2000, 2010, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('RWSo Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Year North Sea')

ax=axs[1]
sc = ax.scatter('dayofyear', 'temperature',  c="year", data=glodapnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'temperature',  c="year", data=Cefasmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'temperature',  c="year", data=D366mean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'temperature',  c="year", data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

plt.tight_layout()
plt.savefig("figures/T_mean_dayofyear_year.png")
plt.show()

#%% # Temperature - Regions - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('distance_to_shore', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Datasets North Sea')

ax = axs[1]
ax.scatter("distance_to_shore", "temperature", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'temperature', c='xkcd:greenish', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'temperature', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'temperature', c='xkcd:dark orange', data=RWSnmean, label='RWS', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Temperature (°C)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

plt.tight_layout()
plt.savefig("figures/T_mean_regions_datasets.png")
plt.show()

#%% # Temperature - Regions - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('distance_to_shore', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("RWSo Temperature (°C)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Seasons North Sea')

ax = axs[1]
sc = ax.scatter('distance_to_shore', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Temperature  (°C)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
cbar.ax.tick_params(rotation=90)

plt.tight_layout()
plt.savefig("figures/T_mean_regions_seasons.png")
plt.show()

#%% Temperature - Regions - Year

fig, axs = plt.subplots(dpi=300, nrows=2)

cm = plt.cm.get_cmap('rainbow')
vmin = 1970
vmax = 2021

ax=axs[0]
sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 6)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([1970, 1980, 1990, 2000, 2010, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('RWSo Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)
ax.set_title('Temperature data - Year North Sea')

ax=axs[1]
sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=glodapnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=Cefasmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=D366mean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Temperature (°C)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(0, 22)

plt.tight_layout()
plt.savefig("figures/T_mean_regions_year.png")
plt.show()


#%% # Long Term Trend of Temperature RWSomean

print('Long term trend of Temperature RWSomean')

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['temperature'])
print("Linear regression Initial data")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomean['datenum'], RWSomean['temperature']))
RWSomean['sc_temperature'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomean['datenum']) # sc = seasoncal cycle
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomean['ms_temperature'] = RWSomean['temperature'] - RWSomean['sc_temperature'] # ms = minus seasonality

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='temperature', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Temperature RWS')

ax.set_title("RWSo Temperature data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
ax.set_ylim(0, 22)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['sc_temperature'])
print("Linear regression Seasonality Curve")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

ax = axs[1]
RWSomean.plot.scatter("datenum", "temperature", ax=ax, c='xkcd:pink', label='Initial Temperature RWS')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
ax.set_ylim(0, 22)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['ms_temperature'])
print("Linear regression Minus Seasonality")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

ax = axs[2]
sns.regplot(x='datenum', y='ms_temperature', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1e}'}, label='Seasonal corrected Temperature RWS')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Long_Term_Trends/Temperature_season_fitting_RWSomean.png")    
plt.show()

# temperature 2000-2021 
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(f"Change over 2001-2021: {changelongterm:6e}")
changeperyear = changelongterm / ((xend-xbegin)/365)
print(f"Change per year: {changeperyear:.6e}") 

# Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Long Term Trend of Temperature RWSomean (splitting up)

L0 = (RWSomean.year <= 1985)
L1 = (RWSomean.year >= 1985) & (RWSomean.year <= 2010)
L2 = (RWSomean.year >= 2010)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

slope, intercept, r, p, se = linregress(RWSomean[L0]['datenum'], RWSomean[L0]['temperature'])

ax = axs[0]
sns.regplot(x='datenum', y='temperature', data=RWSomean[L0], ax=ax,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Temperature RWS')

ax.set_title("RWSo Temperature data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Temperature (°C)')
ax.set_ylim(0, 22)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean[L1]['datenum'], RWSomean[L1]['temperature'])

ax = axs[1]
sns.regplot(x='datenum', y='temperature', data=RWSomean[L1], ax=ax,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Temperature RWS')

ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Temperature (°C)')
ax.set_ylim(0, 22)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean[L2]['datenum'], RWSomean[L2]['temperature'])

ax = axs[2]
sns.regplot(x='datenum', y='temperature', data=RWSomean[L2], ax=ax,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Temperature RWS')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
ax.set_ylim(0, 22)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Long_Term_Trends/Temperature_split_up_RWSomean.png")     
plt.show()
