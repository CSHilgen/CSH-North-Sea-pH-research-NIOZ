# Sunny data
import json

#%% # Sunspot cycle

sunspot = pd.io.json.read_json('C:/Users/cecil/Documenten/Datasets/Sunspotcycle/observed-solar-cycle-indices-1.json')
sunspot['datetime'] = pd.to_datetime(sunspot['time-tag'])
# sunspot['f10.7'] = sunspot['f10.7'].apply(lambda x: "nan" if x == -1.0 else x)
# sunspot = sunspot.where(sunspot == '-1.0', "nan")

#%% # Space weather prediction center (NOAA: https://www.swpc.noaa.gov/products/solar-cycle-progression)

fig, ax = plt.subplots(dpi=300)

ax=ax
ax.plot('datetime', 'ssn', data=sunspot, c='xkcd:banana')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Mean monthly S.I.D.C. sunspot number")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_xlim(0, 19000)
ax.set_title('Sunspot data - NOAA')

plt.tight_layout()
plt.savefig("figures/Sun/Sunspot.png")
plt.show()

#%% # Solar Irradiance

tsi = pd.read_csv('C:/Users/cecil/Documenten/Datasets/Sunspotcycle/tsi-ssi_v02r01_observed-tsi-composite_s19780101_e20210930_c20211021.txt', header=56, na_values=-99)
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
plt.savefig("figures/Sun/Solar_Irradiance.png")
plt.show()

#%% # Sunspot & TSI

fig, ax = plt.subplots(dpi=300)#, figsize=[6,3])

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
plt.savefig("figures/Sun/TSI_and_Sunspot.png")
plt.show()