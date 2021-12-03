# Nutrients

RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_ammonia'])

#%% # Nutrients - Time - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Datasets North Sea') 

ax = axs[0,0]
ax.scatter('datetime', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
ax.scatter('datetime', 'total_phosphate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")

ax = axs[1,0]
ax.scatter('datetime', 'total_nitrate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
ax.scatter('datetime', 'total_silicate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")

ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_datasets_RWSo.png")
plt.show()

#%% # Nutrients - Time - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Seasons North Sea') 
cm = plt.cm.get_cmap('twilight')

ax = axs[0,0]
sc = ax.scatter('datetime', 'total_ammonia', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
sc = ax.scatter('datetime', 'total_phosphate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,0]
sc = ax.scatter('datetime', 'total_nitrate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
sc = ax.scatter('datetime', 'total_silicate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_seasons_RWSo.png")
plt.show()

#%% # Nutrients - Time - Regions

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

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Regions North Sea') 
x = RWSomean['datetime']

ax = axs[0,0]
y = RWSomean['total_ammonia']

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

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
y = RWSomean['total_phosphate']

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

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax = axs[1,0]
y = RWSomean['total_nitrate']

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

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
y = RWSomean['total_silicate']

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

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

#plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_regions_RWSo.png")
plt.show()

#%% # Nutrients - Dayofyear - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Datasets North Sea') 

ax = axs[0,0]
ax.scatter('dayofyear', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
ax.scatter('dayofyear', 'total_phosphate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")

ax = axs[1,0]
ax.scatter('dayofyear', 'total_nitrate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
ax.scatter('dayofyear', 'total_silicate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_datasets_RWSo.png")
plt.show()

#%% # Nutrients - Dayofyear - Regions

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

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Regions North Sea') 
x = RWSomean['dayofyear']

ax = axs[0,0]
y = RWSomean['total_ammonia']

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

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
y = RWSomean['total_phosphate']

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

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax = axs[1,0]
y = RWSomean['total_nitrate']

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

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
y = RWSomean['total_silicate']

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

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

#plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_regions_RWSo.png")
plt.show()

#%% # Nutrients - Dayofyear - Year

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Year North Sea') 

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = axs[0,0]
sc = ax.scatter('dayofyear', 'total_ammonia', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
ax.scatter('dayofyear', 'total_phosphate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,0]
ax.scatter('dayofyear', 'total_nitrate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
ax.scatter('dayofyear', 'total_silicate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=axs, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_year_RWSo.png")
plt.show()

#%% # Nutrients - Regions - Datasets

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Datasets North Sea') 

ax = axs[0,0]
ax.scatter('distance_to_shore', 'total_ammonia', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
ax.scatter('distance_to_shore', 'total_phosphate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")

ax = axs[1,0]
ax.scatter('distance_to_shore', 'total_nitrate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
ax.scatter('distance_to_shore', 'total_silicate', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_datasets_RWSo.png")
plt.show()

#%% # Nutrients - Regions - Seasons

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Seasons North Sea') 
cm = plt.cm.get_cmap('twilight')

ax = axs[0,0]
sc = ax.scatter('distance_to_shore', 'total_ammonia', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
sc = ax.scatter('distance_to_shore', 'total_phosphate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,0]
sc = ax.scatter('distance_to_shore', 'total_nitrate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
sc = ax.scatter('distance_to_shore', 'total_silicate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_seasons_RWSo.png")
plt.show()

#%% # Nutrients - Regions - Year

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)
fig.suptitle('Nutrient RWSo data - Year North Sea') 

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = axs[0,0]
sc = ax.scatter('distance_to_shore', 'total_ammonia', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Ammonium")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[0,1]
ax.scatter('distance_to_shore', 'total_phosphate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Phosphate")
ax.set_ylim(0, 0.12)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,0]
ax.scatter('distance_to_shore', 'total_nitrate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Nitrate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1,1]
ax.scatter('distance_to_shore', 'total_silicate', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Silicate")
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=axs, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_year_RWSo.png")
plt.show()






#%% # COMBINED Nutrients - Time - Datasets

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Datasets North Sea') 

ax = axs[0]
ax.scatter("datetime", "total_nitrate", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datetime', 'total_nitrate', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('datetime', 'total_nitrate', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datetime', 'total_nitrate', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter("datetime", "total_phosphate", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datetime', 'total_phosphate', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('datetime', 'total_phosphate', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datetime', 'total_phosphate', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
ax.scatter("datetime", "total_silicate", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datetime', 'total_silicate', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('datetime', 'total_silicate', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datetime', 'total_silicate', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_datasets_combined.png")
plt.show()

#%% # COMBINED Nutrients - Time - Seasons

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Seasons North Sea') 
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('datetime', 'total_nitrate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
sc = ax.scatter('datetime', 'total_phosphate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
sc = ax.scatter('datetime', 'total_silicate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_seasons_combined.png")
plt.show()

#%% # COMBINED Nutrients - Time - Regions

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

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Regions North Sea') 
x = combinedmean['datetime']

ax = axs[0]
y = combinedmean['total_nitrate']

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

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax = axs[1]
y = combinedmean['total_phosphate']

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

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
y = combinedmean['total_silicate']

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

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

#plt.tight_layout()
plt.savefig("figures/Nutrients_mean_time_regions_combined.png")
plt.show()

#%% # COMBINED Nutrients - Dayofyear - Datasets

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Datasets North Sea') 

ax = axs[0]
ax.scatter('dayofyear', 'total_nitrate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('dayofyear', 'total_phosphate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)
ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
ax.scatter('dayofyear', 'total_silicate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)
ax.set_ylabel("Silicate")

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_datasets_combined.png")
plt.show()

#%% # COMBINED Nutrients - Dayofyear - Regions

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

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Regions North Sea') 
x = combinedmean['dayofyear']

ax = axs[0]
y = combinedmean['total_nitrate']
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

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax = axs[1]
y = combinedmean['total_phosphate']

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

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
y = combinedmean['total_silicate']

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

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_regions_combined.png")
plt.show()

#%% # COMBINED Nutrients - Dayofyear - Year

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Year North Sea') 

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = axs[0]
sc = ax.scatter('dayofyear', 'total_nitrate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
sc = ax.scatter('dayofyear', 'total_phosphate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
sc = ax.scatter('dayofyear', 'total_silicate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=axs, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_dayofyear_year_combined.png")
plt.show()

#%% # COMBINED Nutrients - Regions - Datasets

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Datasets North Sea') 

ax = axs[0]
ax.scatter('distance_to_shore', 'total_nitrate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
ax.scatter('distance_to_shore', 'total_phosphate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
ax.scatter('distance_to_shore', 'total_silicate', c='xkcd:aqua', data=combinedmean, label='combined', s=20, alpha=0.4)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_datasets_combined.png")
plt.show()

#%% # COMBINED Nutrients - Regions - Seasons

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Seasons North Sea') 
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
sc = ax.scatter('distance_to_shore', 'total_nitrate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
sc = ax.scatter('distance_to_shore', 'total_phosphate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
sc = ax.scatter('distance_to_shore', 'total_silicate', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
cbar=fig.colorbar(sc, ax=axs, orientation='vertical', location='right')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_seasons_combined.png")
plt.show()

#%% # Nutrients - Regions - Year

fig, axs = plt.subplots(dpi=300, nrows=3)
fig.suptitle('Nutrient combined data - Year North Sea') 

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = axs[0]
sc = ax.scatter('distance_to_shore', 'total_nitrate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Nitrate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[1]
sc = ax.scatter('distance_to_shore', 'total_phosphate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Phosphate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

ax = axs[2]
sc = ax.scatter('distance_to_shore', 'total_silicate', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("Silicate")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

fig.subplots_adjust(right=1.2)
ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=axs, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions_year_combined.png")
plt.show()