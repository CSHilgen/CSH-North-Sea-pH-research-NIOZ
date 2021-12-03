# Salinity

#%% # Salinity - Time - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('datetime', 'salinity', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Datasets North Sea')

ax = axs[1]
ax.scatter("datetime", "salinity", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datetime', 'salinity', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('datetime', 'salinity', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datetime', 'salinity', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

plt.tight_layout()
plt.savefig("figures/S_mean_time_datasets.png")
plt.show()

#%% # Salinity - Time - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('datetime', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("RWSo Salinity")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

ax = axs[1]
sc = ax.scatter('datetime', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Salinity")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/S_mean_time_seasons.png")
plt.show()

#%% # Salinity - Time - Regions

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
x = RWSomean['datetime']
y = RWSomean['salinity']

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
ax.set_ylabel('RWSo Salinity')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Salinity data - Regions North Sea')

ax=axs[1]
x = combinedmean['datetime']
y = combinedmean['salinity']

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
ax.set_ylabel('Salinity')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.get_legend().set_title("Km to shore")

#plt.tight_layout()
plt.savefig("figures/S_mean_time_regions.png")
plt.show()

#%% # Salinity - Dayofyear - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('dayofyear', 'salinity', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Datasets North Sea')

ax = axs[1]
ax.scatter("dayofyear", "salinity", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('dayofyear', 'salinity', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('dayofyear', 'salinity', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('dayofyear', 'salinity', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

plt.tight_layout()
plt.savefig("figures/S_mean_dayofyear_datasets.png")
plt.show()

#%% # Salinity - Dayofyear - Regions

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
x = RWSomean['dayofyear']
y = RWSomean['salinity']

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
ax.set_ylabel('RWSo Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Salinity data - Regions North Sea')

ax=axs[1]
x = combinedmean['dayofyear']
y = combinedmean['salinity']

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
ax.set_ylabel('Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

#plt.tight_layout()
plt.savefig("figures/S_mean_dayofyear_regions.png")
plt.show()

#%% Salinity - Dayofyear - Year

fig, axs = plt.subplots(dpi=300, nrows=2)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=axs[0]
sc = ax.scatter('dayofyear', 'salinity',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('RWSo Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Year North Sea')

ax=axs[1]
sc = ax.scatter('dayofyear', 'salinity',  c="year", data=glodapnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'salinity',  c="year", data=Cefasmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'salinity',  c="year", data=D366mean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'salinity',  c="year", data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

plt.tight_layout()
plt.savefig("figures/S_mean_dayofyear_year.png")
plt.show()

#%% # Salinity - Regions - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2)

ax = axs[0]
ax.scatter('distance_to_shore', 'salinity', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Datasets North Sea')

ax = axs[1]
ax.scatter("distance_to_shore", "salinity", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'salinity', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'salinity', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'salinity', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Salinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

plt.tight_layout()
plt.savefig("figures/S_mean_regions_datasets.png")
plt.show()

#%% # Salinity - Regions - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('distance_to_shore', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("RWSo Salinity")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

ax = axs[1]
sc = ax.scatter('distance_to_shore', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel("Salinity")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/S_mean_regions_seasons.png")
plt.show()

#%% Salinity - Regions - Year

fig, axs = plt.subplots(dpi=300, nrows=2)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=axs[0]
sc = ax.scatter('distance_to_shore', 'salinity',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Distance to shore (km)')
ax.set_ylabel('RWSo Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)
ax.set_title('Salinity data - Year North Sea')

ax=axs[1]
sc = ax.scatter('distance_to_shore', 'salinity',  c="year", data=glodapnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'salinity',  c="year", data=Cefasmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'salinity',  c="year", data=D366mean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'salinity',  c="year", data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Distance to shore (km)')
ax.set_ylabel('Salinity')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_ylim(28, 36)

plt.tight_layout()
plt.savefig("figures/S_mean_regions_year.png")
plt.show()
