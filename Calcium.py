# Calcium

#%% # Calcium - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datetime', 'calcium', c='xkcd:aqua', data=RWSo, label='RWSo', s=20, alpha=0.4)
sns.regplot(x='datenum', y='calcium', data=RWSo, ax=ax,
            scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_time_datasets_linear_regression.png")
plt.show()

#%% # Calcium - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('datetime', 'calcium', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSo, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Ca_mean_time_seasons.png")
plt.show()

#%% # Calcium - Time - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
x = RWSo['datetime']
y = RWSo['calcium']

L0 = (RWSo['distance_to_shore'] > 0) & (RWSo['distance_to_shore'] <=4)
L1 = (RWSo['distance_to_shore'] > 4) & (RWSo['distance_to_shore'] <=10)
L2 = (RWSo['distance_to_shore'] > 10) & (RWSo['distance_to_shore'] <=20)
L3 = (RWSo['distance_to_shore'] > 20) & (RWSo['distance_to_shore'] <=30)
L4 = (RWSo['distance_to_shore'] > 30) & (RWSo['distance_to_shore'] <=50)
L5 = (RWSo['distance_to_shore'] > 50) & (RWSo['distance_to_shore'] <=70)
L6 = (RWSo['distance_to_shore'] > 70) & (RWSo['distance_to_shore'] <=100)
L7 = (RWSo['distance_to_shore'] > 100) & (RWSo['distance_to_shore'] <=150)
L8 = (RWSo['distance_to_shore'] > 150) & (RWSo['distance_to_shore'] <=200)
L9 = (RWSo['distance_to_shore'] > 200) & (RWSo['distance_to_shore'] <=250)
L10 = (RWSo['distance_to_shore'] > 250) & (RWSo['distance_to_shore'] <=300)

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
ax.set_ylabel('Calcium')

# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Calcium data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_time_regions.png")
plt.show()

#%% # Calcium - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('dayofyear', 'calcium', c='xkcd:aqua', data=RWSo, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Calcium")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_dayofyear_datasets.png")
plt.show()

#%% # Calcium - Dayofyear - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
x = RWSo['dayofyear']
y = RWSo['calcium']

L0 = (RWSo['distance_to_shore'] > 0) & (RWSo['distance_to_shore'] <=4)
L1 = (RWSo['distance_to_shore'] > 4) & (RWSo['distance_to_shore'] <=10)
L2 = (RWSo['distance_to_shore'] > 10) & (RWSo['distance_to_shore'] <=20)
L3 = (RWSo['distance_to_shore'] > 20) & (RWSo['distance_to_shore'] <=30)
L4 = (RWSo['distance_to_shore'] > 30) & (RWSo['distance_to_shore'] <=50)
L5 = (RWSo['distance_to_shore'] > 50) & (RWSo['distance_to_shore'] <=70)
L6 = (RWSo['distance_to_shore'] > 70) & (RWSo['distance_to_shore'] <=100)
L7 = (RWSo['distance_to_shore'] > 100) & (RWSo['distance_to_shore'] <=150)
L8 = (RWSo['distance_to_shore'] > 150) & (RWSo['distance_to_shore'] <=200)
L9 = (RWSo['distance_to_shore'] > 200) & (RWSo['distance_to_shore'] <=250)
L10 = (RWSo['distance_to_shore'] > 250) & (RWSo['distance_to_shore'] <=300)

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
ax.set_ylabel('Calcium')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Calcium data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_dayofyear_regions.png")
plt.show()

#%% Calcium - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
sc = ax.scatter('dayofyear', 'calcium',  c="year", data=RWSo, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Calcium')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Year North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_dayofyear_year.png")
plt.show()

#%% # Calcium - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('distance_to_shore', 'calcium', c='xkcd:aqua', data=RWSo, label='RWSo', s=20, alpha=0.4)
#ax.scatter('distance_to_shore', 'calcium', c='xkcd:aqua', data=RWSo, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel('Calcium')
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_regions_datasets.png")
plt.show()

#%% # Calcium - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('distance_to_shore', 'calcium', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSo, s=20)
#sc = ax.scatter('distance_to_shore', 'calcium', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSo, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.set_ylabel('Calcium')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Ca_mean_regions_seasons.png")
plt.show()

#%% Calcium - Regions - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
sc = ax.scatter('distance_to_shore', 'calcium',  c="year", data=RWSo, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
#sc = ax.scatter('distance_to_shore', 'calcium',  c="year", data=RWSo, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Distance to shore (km)')
ax.set_ylabel('Calcium')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium data - Year North Sea')

plt.tight_layout()
plt.savefig("figures/Ca_mean_regions_year.png")
plt.show()



#%% # Ca difference

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

ax=ax
# sns.regplot(x='salinity', y='calcium', data=RWSo, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'calcium', c='dayofyear', cmap='twilight', data=RWSo, label='RWSo calcium', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Calcium")
ax.set_title("Ca and S data - North Sea")
ax.legend()
# ax.set_xlim([31,35.5])

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/S_longterm/Ca_S_scatter_seasons.png")
plt.show()

#%% # Ca difference

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('rainbow')

vmin = 2009
vmax = 2021

ax=ax
# sns.regplot(x='salinity', y='calcium', data=RWSo, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'calcium', c='year', cmap=cm, data=RWSo, label='RWSo calcium', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Calcium")
ax.set_title("Ca and S data - North Sea")
ax.legend()
# ax.set_xlim([31,35.5])

ticks = np.linspace(vmin, vmax, 4)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2006, 2011, 2016, 2021])
plt.tight_layout()
plt.savefig("figures/S_longterm/Ca_S_scatter_year.png")
plt.show()

