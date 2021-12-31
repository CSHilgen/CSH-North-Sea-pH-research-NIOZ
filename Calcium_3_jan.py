import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares

#%% # Import datasets

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combined_final.csv")

# Not mean per month -> all data is shown of RWSo
# Method 1 = analyse van metalen in opl.  atomaire emissiespectrometrie
# Method 2 = Bep v metalen mbv ICP/MS gelijkwaardig aan I17294-1/2 (HWL)
# Method 3 = Toep. van massaspectr. met inductief gekozen plasma ICP-MS

#%% # Corrected Calcium data based on the methods (Method 2 + 720)

L0 = (RWSo.year <= 2014)
L1 = (RWSo.year >= 2015) & (RWSo.datenum <= 16996.3)
L2 = (RWSo.datenum >= 17014.4)  

RWSoCa_corrected2 = pd.DataFrame(RWSo[L1]['calcium umol/kg'])
RWSoCa_corrected2['datenum'] = RWSo[L1]['datenum']
RWSoCa_corrected2['calcium umol/kg_corrected'] = RWSoCa_corrected2['calcium umol/kg'] + 720

#%% # Corrected Calcium data based on the methods (Method 3 - 720)

RWSoCa_corrected3 = pd.DataFrame(RWSo[L2]['calcium umol/kg'])
RWSoCa_corrected3['datenum'] = RWSo[L2]['datenum']
RWSoCa_corrected3['calcium umol/kg_corrected'] = RWSoCa_corrected3['calcium umol/kg'] - 720

#%% # Calcium - Time - Datasets

fig, ax = plt.subplots(dpi=300)

L0 = (RWSo.year <= 2014)
L1 = (RWSo.year >= 2015) & (RWSo.datenum <= 16996.3)
L2 = (RWSo.datenum >= 17014.4)      

ax = ax
# ax.scatter('datenum', 'calcium umol/kg', c='xkcd:aqua', data=RWSo, label='RWS', s=20, alpha=0.4)

ax.scatter('datenum', 'calcium umol/kg', edgecolors='yellow', facecolors='yellow', data=RWSo[L0], s=20, label='Method 1')

ax.scatter('datenum', 'calcium umol/kg', edgecolors='orange', facecolors='orange', data=RWSo[L1], s=20, label='Method 2')
# ax.scatter('datenum', 'calcium umol/kg_corrected', edgecolors='orange', facecolors='orange', data=RWSoCa_corrected2, s=20, label='Method 2')

# ax.scatter('datenum', 'calcium umol/kg', edgecolors='green', facecolors='green', data=RWSo[L2], s=20, label='Method 3')
ax.scatter('datenum', 'calcium umol/kg_corrected', edgecolors='green', facecolors='green', data=RWSoCa_corrected3, s=20, label ='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium (μmol/kg)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium Method 3 corrected - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_time_datasets_method_corrected3.png")
plt.show()

#%% # Salinity vs Calcium seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

vmin = 1
vmax = 365

RWSomeanCa = RWSomean.dropna(axis='rows', how='all', subset=['calcium umol/kg'])

ax=ax
sns.regplot(x='salinity', y='calcium umol/kg', data=RWSo, ax=ax,
            scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'calcium umol/kg', c='dayofyear', cmap=cm, data=RWSo, label='RWS Ca', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Calcium (µmol/kg)")
ax.set_title("Ca and S RWS data - North Sea")
# ax.set_xlim([32, 34.5])

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
cbar.ax.tick_params(rotation=90)

plt.tight_layout()
plt.savefig("figures/Spatial_variability/Ca_S_scatter_seasons2.png")
plt.show()

#%% # Salinity vs Calcium year

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('rainbow')

vmin = 2009
vmax = 2021

ax=ax
sns.regplot(x='salinity', y='calcium umol/kg', data=RWSo, ax=ax,
            scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'calcium umol/kg', c='year', cmap=cm, data=RWSo, label='RWS Ca', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Calcium (µmol/kg)")
ax.set_title("Ca and S RWS data - North Sea")
# ax.set_xlim([32, 34.5])

ticks = np.linspace(vmin, vmax, 7)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2009, 2011, 2013, 2015, 2017, 2019, 2021])

plt.tight_layout()
plt.savefig("figures/Spatial_variability/Ca_S_scatter_year2.png")
plt.show()

#%% # Salinity vs Calcium methods

fig, ax = plt.subplots(dpi=300)

ax=ax
sns.regplot(x='salinity', y='calcium umol/kg', data=RWSo, ax=ax,
            scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'calcium umol/kg', c='yellow', cmap=cm, data=RWSo[L0],  label='Method 1')
sc = ax.scatter('salinity', 'calcium umol/kg', c='orange', cmap=cm, data=RWSo[L1], label='Method 2')
sc = ax.scatter('salinity', 'calcium umol/kg', c='green', cmap=cm, data=RWSo[L2], label='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Calcium (µmol/kg)")
ax.set_title("Ca and S RWS data - North Sea")
# ax.set_xlim([32, 34.5])
ax.legend()

plt.tight_layout()
plt.savefig("figures/Spatial_variability/Ca_S_scatter_method2.png")
plt.show()

#%% # Calcium - Time - Datasets - LINEAR REGRESSION LINE

fig, ax = plt.subplots(dpi=300)

RWSolr = RWSo.dropna(axis='rows', how='all', subset=['calcium umol/kg'])
slope, intercept, r, p, se = linregress(RWSolr['datenum'], RWSolr['calcium umol/kg'])

ax = ax
ax.scatter('datenum', 'calcium umol/kg', c='xkcd:aqua', data=RWSo, label='RWS', s=20, alpha=0.4)
sns.regplot(x='datenum', y='calcium umol/kg', data=RWSo, ax=ax,
            scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1f}'})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium (μmol/kg)")
ax.legend()#bbox_to_anchor=(1.0, 1.0), loc='upper left')
# ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
# plt.savefig("figures/Ca_time_datasets_LR.png")
plt.show()

#%% # Calcium - Time - Datasets

fig, ax = plt.subplots(dpi=300)

L0 = (RWSo.year <= 2014)
L1 = (RWSo.year >= 2015) & (RWSo.datenum <= 16996.3)
L2 = (RWSo.datenum >= 17014.4)      

ax = ax
ax.scatter('datenum', 'calcium umol/kg', c='xkcd:aqua', data=RWSo, label='RWS', s=20, alpha=0.4)

ax.scatter('datenum', 'calcium umol/kg', edgecolors='yellow', facecolors='yellow', data=RWSo[L0], s=20, label='Method 1')
ax.scatter('datenum', 'calcium umol/kg', edgecolors='orange', facecolors='orange', data=RWSo[L1], s=20, label='Method 2')
ax.scatter('datenum', 'calcium umol/kg', edgecolors='green', facecolors='green', data=RWSo[L2], s=20, label ='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium (μmol/kg)")
ax.legend()
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
# plt.savefig("figures/Ca_time_datasets.png")
plt.show()


#%% # Calcium - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('dayofyear', 'calcium umol/kg', edgecolors='yellow', facecolors='yellow', data=RWSo[L0], s=20, label='Method 1')
ax.scatter('dayofyear', 'calcium umol/kg', edgecolors='orange', facecolors='orange', data=RWSo[L1], s=20, label='Method 2')
ax.scatter('dayofyear', 'calcium umol/kg', edgecolors='green', facecolors='green', data=RWSo[L2], s=20, label ='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Calcium (μmol/kg)")
ax.legend()
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
# plt.savefig("figures/Ca_dayofyear_datasets.png")
plt.show()

#%% # Calcium - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('distance_to_shore', 'calcium umol/kg', edgecolors='yellow', facecolors='yellow', data=RWSo[L0], s=20, label='Method 1')
ax.scatter('distance_to_shore', 'calcium umol/kg', edgecolors='orange', facecolors='orange', data=RWSo[L1], s=20, label='Method 2')
ax.scatter('distance_to_shore', 'calcium umol/kg', edgecolors='green', facecolors='green', data=RWSo[L2], s=20, label ='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel('Calcium (μmol/kg)')
ax.legend()
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
# plt.savefig("figures/Ca_regions_datasets.png")
plt.show()

#%% # Long Term Trend of Calcium RWSomean

print('Long term trend of Calcium RWSo')

RWSo = RWSo.dropna(axis='rows', how='all', subset=['calcium umol/kg'])
slope, intercept, r, p, se = linregress(RWSo['datenum'], RWSo['calcium umol/kg'])
print("Linear regression Initial data")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

fig, ax = plt.subplots(dpi=300, figsize=(10,6))

ax = ax
sns.regplot(x='datenum', y='calcium umol/kg', data=RWSo, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Ca RWS')

ax.set_title("RWSo Calcium data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Calcium (µmol/kg)')
ax.set_ylim(7000, 14500)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
# plt.savefig("figures/Long_Term_Trends/Calcium_season_fitting_RWSo.png")    
plt.show()

# Calcium 2009-2018 
xbegin = 14287.4
xend = 17849.6

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(f"Change over 2009-2018: {changelongterm:6e}")
changeperyear = changelongterm / ((xend-xbegin)/365)
print(f"Change per year: {changeperyear:.6e}") 

# Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Long Term Trend of Calcium RWSo (splitting up)

L0 = (RWSo.year <= 2014)
L1 = (RWSo.year >= 2015) & (RWSo.year <= 2017)
L2 = (RWSo.year >= 2017)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

slope, intercept, r, p, se = linregress(RWSo[L0]['datenum'], RWSo[L0]['calcium'])

ax = axs[0]
sns.regplot(x='datenum', y='calcium umol/kg', data=RWSo[L0], ax=ax,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Ca RWS')

ax.set_title("RWSo Calcium data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Calcium (µmol/kg)')
ax.set_ylim(7000, 14500)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSo[L1]['datenum'], RWSo[L1]['calcium'])

ax = axs[1]
sns.regplot(x='datenum', y='calcium umol/kg', data=RWSo[L1], ax=ax,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Ca RWS')

ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Calcium (µmol/kg)')
ax.set_ylim(7000, 14500)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSo[L2]['datenum'], RWSo[L2]['calcium'])

ax = axs[2]
sns.regplot(x='datenum', y='calcium umol/kg', data=RWSo[L2], ax=ax,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial Ca RWS')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Calcium (µmol/kg)')
ax.set_ylim(7000, 14500)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
# plt.savefig("figures/Long_Term_Trends/Calcium_split_up_RWSo.png")     
plt.show()



