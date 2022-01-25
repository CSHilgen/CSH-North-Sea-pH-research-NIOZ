import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import json

#%% # Sunspot cycle

sunspot = pd.io.json.read_json('data_sun_spots/observed-solar-cycle-indices-1.json')
sunspot['datetime'] = pd.to_datetime(sunspot['time-tag'])
RWSomeano2 = pd.read_csv("dataframes_made/RWSomeano2_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWStotalmeanT = pd.read_csv("dataframes_made/RWStotalmeanT_final.csv")
RWStotalmean = pd.read_csv("dataframes_made/RWStotalmean_final.csv")

#%% # Space weather prediction center (NOAA: https://www.swpc.noaa.gov/products/solar-cycle-progression)

fig, ax = plt.subplots(dpi=300)

ax=ax
ax.scatter('datetime', 'ssn', data=sunspot, c='xkcd:banana')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Mean monthly S.I.D.C. sunspot number")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax.set_title('Sunspot data - NOAA')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Sunspot.png")
plt.show()

#%% # Solar Irradiance

tsi = pd.read_csv('data_sun_spots/tsi-ssi_v02r01_observed-tsi-composite_s19780101_e20210930_c20211021.txt', header=56, na_values=-99)
tsi['datetime'] = pd.to_datetime(tsi['; time (yyyy-MM-dd)'])
tsi = tsi.rename(columns={' TSI (W m-2)':'TSI (W m-2)', ' uncertainty (W m-2)': 'Uncertainty (W m-2)'})
tsi = tsi.dropna(axis='rows', how='all', subset=['TSI (W m-2)'])

#%% # Total Solar Irradiance CDR (NOAA: https://www.ncei.noaa.gov/products/climate-data-records/total-solar-irradiance)

fig, ax = plt.subplots(dpi=300)

ax=ax
#ax.plot('datetime', 'TSI (W m-2)', data=tsi, c='xkcd:golden')
ax.scatter('datetime', 'TSI (W m-2)', data=tsi, c='xkcd:golden', alpha=0.3)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total solar irradiance (W/m$^2$)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax.set_title('TSI data - NOAA')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Solar_Irradiance.png")
plt.show()

#%% # Sunspot & TSI

fig, ax = plt.subplots(dpi=300)

ax1=ax
ax.scatter('datetime', 'ssn', data=sunspot, s=20, alpha=0.4, c='xkcd:banana')

ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Sunspot number')
ax.grid(alpha=0.3)

ax2 = ax1.twinx()
ax=ax2
ax.scatter('datetime', 'TSI (W m-2)', data=tsi, s=20, alpha=0.4, c='xkcd:golden')

ax2.set_xlabel('Time (yrs)')
ax2.set_ylabel('Total Solar Irradiance (W/m$^2$)')

ax.grid(alpha=0.3)
ax.set_title('Sun data - NOAA')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/TSI_and_Sunspot.png")
plt.show()

#%% # Sunspot & O2

fig, ax1 = plt.subplots(dpi=300)

RWSomeano2['datetime'] = pd.to_datetime(RWSomeano2['datetime'])
RWSomeano2year = RWSomeano2.set_index('datetime').resample('Y').mean()
RWSomeano2year = RWSomeano2year.reset_index()

ax=ax1
#ax.scatter('datenum', 'oxygen umol/kg', data=RWSomeano2, s=20, alpha=0.4, c='xkcd:green')
ax.plot('datenum', 'oxygen umol/kg', data=RWSomeano2year, c='xkcd:green')
ax1.set_ylabel('Oxygen (µmol/kg)')

ax2 = ax1.twinx()
ax=ax2
ax.scatter('datetime', 'ssn', data=sunspot, s=20, alpha=0.4, c='xkcd:banana')
ax2.set_ylabel('Sunspot number')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax1.set_title('Oxygen RWS and Sunspot data - North Sea')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Relationships_Sunspot_O2.png")
plt.show()

#%% # Sunspot & AOU

fig, ax1 = plt.subplots(dpi=300)

RWSomeanAOU = RWSomean.dropna(axis='rows', how='all', subset=['aou'])
RWSomeanAOU['datetime'] = pd.to_datetime(RWSomeanAOU['datetime'])
RWSomeanAOUyear = RWSomeanAOU.set_index('datetime').resample('Y').mean()
RWSomeanAOUyear = RWSomeanAOUyear.reset_index()

ax=ax1
#ax.scatter('datenum', 'aou', data=RWSomeanAOU, s=20, alpha=0.4, c='xkcd:spring green')
ax.plot('datenum', 'aou', data=RWSomeanAOUyear, c='xkcd:spring green')
ax1.set_ylabel('AOU (µmol/kg)')

ax2 = ax1.twinx()
ax=ax2
ax.scatter('datetime', 'ssn', data=sunspot, s=20, alpha=0.4, c='xkcd:banana')
ax2.set_ylabel('Sunspot number')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax1.set_title('AOU RWS and Sunspot data - North Sea')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Relationships_Sunspot_AOU.png")
plt.show()

#%% # Sunspot & T

fig, ax1 = plt.subplots(dpi=300)

RWStotalmeanT['datetime'] = pd.to_datetime(RWStotalmeanT['datetime'])
RWStotalmeanTyear = RWStotalmeanT.set_index('datetime').resample('Y').mean()
RWStotalmeanTyear = RWStotalmeanTyear.reset_index()

ax=ax1
#ax.scatter('datenum', 'temperature', data=RWStotalmeanT, s=20, alpha=0.4, c='xkcd:pink')
ax.plot('datenum', 'ms_temperature', data=RWStotalmeanTyear, c='xkcd:pink')
ax1.set_ylabel('Temperature (°C)')

ax2 = ax1.twinx()
ax=ax2
ax.scatter('datetime', 'ssn', data=sunspot, s=20, alpha=0.4, c='xkcd:banana')
ax2.set_ylabel('Sunspot number')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax1.set_title('Temperature RWS and Sunspot data - North Sea')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Relationships_Sunspot_T.png")
plt.show()

#%% # Sunspot & S

fig, ax1 = plt.subplots(dpi=300)

RWStotalmeanS = RWStotalmean.dropna(axis='rows', how='all', subset=['salinity'])
RWStotalmeanS['datetime'] = pd.to_datetime(RWStotalmeanS['datetime'])
RWStotalmeanSyear = RWStotalmeanS.set_index('datetime').resample('Y').mean()
RWStotalmeanSyear = RWStotalmeanSyear.reset_index()

ax=ax1
#ax.scatter('datenum', 'salinity', data=RWStotalmeanS, s=20, alpha=0.4, c='xkcd:goldenrod')
ax.plot('datenum', 'salinity', data=RWStotalmeanSyear, c='xkcd:goldenrod')
ax1.set_ylabel('Salinity')

ax2 = ax1.twinx()
ax=ax2
ax.scatter('datetime', 'ssn', data=sunspot, s=20, alpha=0.4, c='xkcd:banana')
ax2.set_ylabel('Sunspot number')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax1.set_title('Salinity RWS and Sunspot data - North Sea')

plt.tight_layout()
plt.savefig("figures/Sunspot_cycle/Relationships_Sunspot_S.png")
plt.show()