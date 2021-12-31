
import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares
import tools.seasonalfitting as SF_tools

#%% # Import datasets

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")

#%% # Ammonia - Time - Datasets - LINEAR REGRESSION

fig, ax = plt.subplots(dpi=300)

RWSomeanlr = RWSomean.dropna(axis='rows', how='all', subset=['total_ammonia'])
slope, intercept, r, p, se = linregress(RWSomeanlr['datenum'], RWSomeanlr['total_ammonia'])

ax = ax
ax.scatter('datenum', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean, ax=ax,
            scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})

ax.set_title('Ammonia RWSo data - Datasets North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_time_datasets_LR.png")
plt.show()

#%% # Ammonia - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datenum', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.set_title('Ammonia RWSo data - Datasets North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_time_datasets.png")
plt.show()

#%% # Ammonia - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('datenum', 'total_ammonia', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_title('Ammonia RWSo data - Seasons North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
cbar.ax.tick_params(rotation=90)

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_time_seasons.png")
plt.show()

#%% # Ammonia - Time - Regions

fig, ax = plt.subplots(dpi=300)

ax = ax
x = RWSomean['datenum']
y = RWSomean['total_ammonia']

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

ax.set_title('Ammonia RWSo data - Regions North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

#plt.tight_layout()
plt.savefig("figures/Ammonia_mean_time_regions.png")
plt.show()

#%% # Ammonia - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('dayofyear', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.set_title('Ammonia RWSo data - Datasets North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_dayofyear_datasets.png")
plt.show()

#%% # Ammonia - Dayofyear - Regions

fig, ax = plt.subplots(dpi=300)

ax = ax
x = RWSomean['dayofyear']
y = RWSomean['total_ammonia']

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

ax.set_title('Ammonia RWSo data - Regions North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

#plt.tight_layout()
plt.savefig("figures/Ammonia_mean_dayofyear_regions.png")
plt.show()

#%% # Ammonia - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 1975
vmax = 2021

ax = ax
sc = ax.scatter('dayofyear', 'total_ammonia', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_title('Ammonia RWSo data - Year North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ticks = np.linspace(vmin, vmax, 10)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_dayofyear_year.png")
plt.show()

#%% # Ammonia - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('distance_to_shore', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)

ax.set_title('Ammonia RWSo data - Datasets North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_regions_datasets.png")
plt.show()

#%% # Ammonia - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('distance_to_shore', 'total_ammonia', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_title('Ammonia RWSo data - Seasons North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
cbar.ax.tick_params(rotation=90)

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_regions_seasons.png")
plt.show()

#%% # Ammonia - Regions - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 1975
vmax = 2021

ax = ax
sc = ax.scatter('distance_to_shore', 'total_ammonia', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_title('Ammonia RWSo data - Year North Sea') 
ax.set_ylabel("Ammonia (μmol/kg)")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ticks = np.linspace(vmin, vmax, 10)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Ammonia_mean_regions_year.png")
plt.show()

#%% # Long Term Trend of Ammonia RWSomean

print('Long term trend of Ammonia RWSomean')

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_ammonia'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_ammonia'])
print("Linear regression Initial data")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                           args=(RWSomean['datenum'], RWSomean['total_ammonia']))
RWSomean['sc_ammonia'] = SF_tools.seasonalcycle_fit(opt_result['x'], RWSomean['datenum']) # sc = seasoncal cycle
slope, intercept, sine_stretch, sine_shift = opt_result['x']
RWSomean['ms_ammonia'] = RWSomean['total_ammonia'] - RWSomean['sc_ammonia'] # ms = minus seasonality

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial NH$_3$ RWS')

ax.set_title("RWSo Total Ammonia data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['sc_ammonia'])
print("Linear regression Seasonality Curve")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_ammonia", ax=ax, c='xkcd:plum', label='Initial NH$_3$ RWS')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') 

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['ms_ammonia'])
print("Linear regression Minus Seasonality")
print(f"Slope: {slope:.6e}")
print(f"Intercept: {intercept:.6e}")
print(f"R-value: {r:.6e}")
print(f"R-squared: {r**2:.6e}")
print(f"P-value: {p:.6e}")
print(f"Standard error: {se:.6e}")

ax = axs[2]
sns.regplot(x='datenum', y='ms_ammonia', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1e}'}, label='Seasonal corrected NH$_3$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(-0.05, 0.1)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Long_Term_Trends/Ammonia_season_fitting_RWSomean.png")    
plt.show()

# Ammonia 2000-2021 
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

#%% # Long Term Trend of Ammonia RWSomean (splitting up)

L0 = (RWSomean.year <= 1985)
L1 = (RWSomean.year >= 1985) & (RWSomean.year <= 2010)
L2 = (RWSomean.year >= 2010)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

slope, intercept, r, p, se = linregress(RWSomean[L0]['datenum'], RWSomean[L0]['total_ammonia'])

ax = axs[0]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean[L0], ax=ax,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial NH$_3$ RWS')

ax.set_title("RWSo Total Ammonia data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean[L1]['datenum'], RWSomean[L1]['total_ammonia'])

ax = axs[1]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean[L1], ax=ax,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial NH$_3$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel(None)
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

slope, intercept, r, p, se = linregress(RWSomean[L2]['datenum'], RWSomean[L2]['total_ammonia'])

ax = axs[2]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean[L2], ax=ax,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial NH$_3$ RWS')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Long_Term_Trends/Ammonia_split_up_RWSomean.png")     
plt.show()
