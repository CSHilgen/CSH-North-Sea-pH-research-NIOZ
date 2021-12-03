# fCO2

#%% # fCO2 - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter('datetime', 'fCO2', c='xkcd:goldenrod', data=socatnsairmean, label='Socat', s=20, alpha=0.4)
#ax.scatter('datetime', 'fCO2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)
ax.scatter('datetime', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ air data - Datasets North Sea')
ax.set_title('Delta fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
#plt.savefig("figures/fCO2_air_mean_time_datasets.png")
plt.savefig("figures/Delta_fCO2_mean_time_datasets.png")
plt.show()

#%% # fCO2 - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
#sc = ax.scatter('datetime', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsairmean, s=20)
#sc = ax.scatter('datetime', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)
sc = ax.scatter('datetime', 'deltafco2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ air data - Seasons North Sea')
ax.set_title('Delta fCO$_2$ data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
#plt.savefig("figures/fCO2_air_mean_time_seasons.png")
plt.savefig("figures/Delta_fCO2_mean_time_seasons.png")
plt.show()

#%% # fCO2 - Time - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
# x = socatnsairmean['datetime']
# y = socatnsairmean['fCO2']
x = socatnsmean['datetime']
#y = socatnsmean['fCO2']
y = socatnsmean['deltafco2']

L0 = (socatnsmean['distance_to_shore'] > 0) & (socatnsmean['distance_to_shore'] <=4)
L1 = (socatnsmean['distance_to_shore'] > 4) & (socatnsmean['distance_to_shore'] <=10)
L2 = (socatnsmean['distance_to_shore'] > 10) & (socatnsmean['distance_to_shore'] <=20)
L3 = (socatnsmean['distance_to_shore'] > 20) & (socatnsmean['distance_to_shore'] <=30)
L4 = (socatnsmean['distance_to_shore'] > 30) & (socatnsmean['distance_to_shore'] <=50)
L5 = (socatnsmean['distance_to_shore'] > 50) & (socatnsmean['distance_to_shore'] <=70)
L6 = (socatnsmean['distance_to_shore'] > 70) & (socatnsmean['distance_to_shore'] <=100)
L7 = (socatnsmean['distance_to_shore'] > 100) & (socatnsmean['distance_to_shore'] <=150)
L8 = (socatnsmean['distance_to_shore'] > 150) & (socatnsmean['distance_to_shore'] <=200)
L9 = (socatnsmean['distance_to_shore'] > 200) & (socatnsmean['distance_to_shore'] <=250)
L10 = (socatnsmean['distance_to_shore'] > 250) & (socatnsmean['distance_to_shore'] <=300)

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
ax.set_ylabel('fCO$_2$ (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_title('fCO$_2$ sea data - Regions North Sea')
ax.set_title('Delta fCO$_2$ data - Regions North Sea')

plt.tight_layout()
#plt.savefig("figures/fCO2_sea_mean_time_regions.png")
plt.savefig("figures/Delta_fCO2_mean_time_regions.png")
plt.show()

#%% # fCO2 - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter('dayofyear', 'fCO2', c='xkcd:goldenrod', data=socatnsairmean, label='Socat', s=20, alpha=0.4)
#ax.scatter('dayofyear', 'fCO2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)
ax.scatter('dayofyear', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ sea data - Datasets North Sea')
ax.set_title('Delta fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
#plt.savefig("figures/fCO2_sea_mean_dayofyear_datasets.png")
plt.savefig("figures/Delta_fCO2_mean_dayofyear_datasets.png")
plt.show()

#%% # fCO2 - Dayofyear - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
x = socatnsairmean['dayofyear']
y = socatnsairmean['fCO2']
# x = socatnsmean['dayofyear']
# y = socatnsmean['fCO2']
#y = socatnsmean['deltafco2']

L0 = (socatnsairmean['distance_to_shore'] > 0) & (socatnsairmean['distance_to_shore'] <=4)
L1 = (socatnsairmean['distance_to_shore'] > 4) & (socatnsairmean['distance_to_shore'] <=10)
L2 = (socatnsairmean['distance_to_shore'] > 10) & (socatnsairmean['distance_to_shore'] <=20)
L3 = (socatnsairmean['distance_to_shore'] > 20) & (socatnsairmean['distance_to_shore'] <=30)
L4 = (socatnsairmean['distance_to_shore'] > 30) & (socatnsairmean['distance_to_shore'] <=50)
L5 = (socatnsairmean['distance_to_shore'] > 50) & (socatnsairmean['distance_to_shore'] <=70)
L6 = (socatnsairmean['distance_to_shore'] > 70) & (socatnsairmean['distance_to_shore'] <=100)
L7 = (socatnsairmean['distance_to_shore'] > 100) & (socatnsairmean['distance_to_shore'] <=150)
L8 = (socatnsairmean['distance_to_shore'] > 150) & (socatnsairmean['distance_to_shore'] <=200)
L9 = (socatnsairmean['distance_to_shore'] > 200) & (socatnsairmean['distance_to_shore'] <=250)
L10 = (socatnsairmean['distance_to_shore'] > 250) & (socatnsairmean['distance_to_shore'] <=300)

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
ax.set_ylabel('fCO$_2$ (uatm)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('fCO$_2$ air data - Regions North Sea')
#ax.set_title('Delta fCO$_2$ data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_air_mean_dayofyear_regions.png")
#plt.savefig("figures/Delta_fCO2_mean_dayofyear_regions.png")
plt.show()

#%% fCO2 - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
sc = ax.scatter('dayofyear', 'fCO2',  c="year", data=socatnsairmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
#sc = ax.scatter('dayofyear', 'fCO2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
#sc = ax.scatter('dayofyear', 'deltafco2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('fCO$_2$ (uatm)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('fCO$_2$ air data - Year North Sea')
#ax.set_title('Delta fCO$_2$ data - Year North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_air_mean_dayofyear_year.png")
#plt.savefig("figures/Delta_fCO2_mean_dayofyear_year.png")
plt.show()

#%% # fCO2 - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter('distance_to_shore', 'fCO2', c='xkcd:goldenrod', data=socatnsairmean, label='Socat', s=20, alpha=0.4)
#ax.scatter('distance_to_shore', 'fCO2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='Socat', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ air data - Datasets North Sea')
ax.set_title('Delta fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
#plt.savefig("figures/fCO2_air_mean_regions_datasets.png")
plt.savefig("figures/Delta_fCO2_mean_regions_datasets.png")
plt.show()

#%% # fCO2 - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
#sc = ax.scatter('distance_to_shore', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsairmean, s=20)
#sc = ax.scatter('distance_to_shore', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)
sc = ax.scatter('distance_to_shore', 'deltafco2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ air data - Seasons North Sea')
ax.set_title('Delta fCO$_2$ data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
#plt.savefig("figures/fCO2_air_mean_regions_seasons.png")
plt.savefig("figures/Delta_fCO2_mean_regions_seasons.png")
plt.show()

#%% fCO2 - Regions - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
#sc = ax.scatter('distance_to_shore', 'fCO2',  c="year", data=socatnsairmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
#sc = ax.scatter('distance_to_shore', 'fCO2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'deltafco2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Distance to shore (km)')
ax.set_ylabel('fCO$_2$ (uatm)')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
#ax.set_title('fCO$_2$ sea data - Year North Sea')
ax.set_title('Delta fCO$_2$ data - Year North Sea')

plt.tight_layout()
#plt.savefig("figures/fCO2_sea_mean_regions_year.png")
plt.savefig("figures/Delta_fCO2_mean_regions_year.png")
plt.show()

#%% # ALL fCO2 - Time - Datasets (Data generated with pyCO2sys)

fig, ax = plt.subplots(dpi=300)

ax = ax
glodapnsmean.plot.scatter("datetime", "fCO2", c="b", ax=ax, s=20, alpha=0.4, label='GLODAP')
Cefasmean.plot.scatter('datetime', 'fCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4, label='Cefas')
D366mean.plot.scatter('datetime', 'fCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4, label='D366')
RWSnmean.plot.scatter('datetime', 'fCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4, label='RWSn')
socatnsmean.plot.scatter('datetime', 'fCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4, label='SOCAT sea')
socatnsairmean.plot.scatter('datetime', 'fCO2', c='black', ax=ax, s=20, alpha=0.4, label='SOCAT air')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.set_ylim([150, 550])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('All fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_all_mean_datasets.png")
plt.show()

