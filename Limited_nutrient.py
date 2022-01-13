import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#%% # Import dataset

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")

#%% # Determine Redfield ratio N:P (16:1)

RWSomean['nit/phos'] = RWSomean['total_nitrate'] / RWSomean['total_phosphate']
print(RWSomean['nit/phos'])

r = RWSomean['nit/phos'] >= 16
l = RWSomean['nit/phos'] < 16

RWSomeanabove16 = RWSomean[r].dropna(axis='rows', how='all', subset=['nit/phos'])
RWSomeanbelow16 = RWSomean[l].dropna(axis='rows', how='all', subset=['nit/phos'])

#%% # P limited time

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('datenum', 'total_nitrate', data=RWSomeanabove16, c='xkcd:light violet', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.legend()

ax=axs[1]
ax.scatter('datenum', 'total_phosphate', data=RWSomeanabove16, c='xkcd:apricot', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_xlabel('Time (yrs)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.legend()

plt.tight_layout()
plt.savefig("figures/Nutrient_limitation/When_P_limited_nutrient_time.png")
plt.show()

#%% # N limited time

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('datenum', 'total_nitrate', data=RWSomeanbelow16, c='xkcd:light violet', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.legend()

ax=axs[1]
ax.scatter('datenum', 'total_phosphate', data=RWSomeanbelow16, c='xkcd:apricot', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_xlabel('Time (yrs)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.legend()

plt.tight_layout(pad=0.5)
plt.savefig("figures/Nutrient_limitation/When_N_limited_nutrient_time.png")
plt.show()

#%% # P limited seasons

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('dayofyear', 'total_nitrate', data=RWSomeanabove16, c='xkcd:light violet', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.legend()

ax=axs[1]
ax.scatter('dayofyear', 'total_phosphate', data=RWSomeanabove16, c='xkcd:apricot', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_ylim(0, 0.15)
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Nutrient_limitation/When_P_limited_nutrient_dayofyear.png")
plt.show()

#%% # N limited seasons

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('dayofyear', 'total_nitrate', data=RWSomeanbelow16, c='xkcd:light violet', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.legend()

ax=axs[1]
ax.scatter('dayofyear', 'total_phosphate', data=RWSomeanbelow16, c='xkcd:apricot', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_xlabel('Months of year')
fmt = mdates.DateFormatter('%b')
ax.xaxis.set_major_locator(mdates.MonthLocator([2,5,8,11]))
ax.xaxis.set_major_formatter(FuncFormatter(fmt))
ax.set_xlim(0, 365)
ax.set_ylim(0, 0.15)
ax.legend()

plt.tight_layout(pad=0.5)
plt.savefig("figures/Nutrient_limitation/When_N_limited_nutrient_dayofyear.png")
plt.show()

#%% # P limited regions

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('distance_to_shore', 'total_nitrate', data=RWSomeanabove16, c='xkcd:light violet', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.legend()

ax=axs[1]
ax.scatter('distance_to_shore', 'total_phosphate', data=RWSomeanabove16, c='xkcd:apricot', label='P limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_xlabel('Distance to shore (km)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.legend()

plt.tight_layout()
plt.savefig("figures/Nutrient_limitation/When_P_limited_nutrient_region.png")
plt.show()

#%% # N limited regions

fig, axs = plt.subplots(dpi=300, nrows=2, sharex=True)

ax=axs[0]
ax.scatter('distance_to_shore', 'total_nitrate', data=RWSomeanbelow16, c='xkcd:light violet', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_xlabel(None)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.legend()

ax=axs[1]
ax.scatter('distance_to_shore', 'total_phosphate', data=RWSomeanbelow16, c='xkcd:apricot', label='N limited')

ax.grid(alpha=0.3)
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_xlabel('Distance to shore (km)')
ax.set_ylim(0, 0.15)
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.legend()

plt.tight_layout(pad=0.5)
plt.savefig("figures/Nutrient_limitation/When_N_limited_nutrient_region.png")
plt.show()