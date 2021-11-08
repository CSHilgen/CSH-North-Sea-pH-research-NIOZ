# Nutrient

#%% # RWSomean nutrients - Datasets

fig, axs = plt.subplots(dpi=300, nrows=3)

ax = axs[0]
RWSomean.plot.scatter('datetime', 'nitrate', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Nitrate")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('RWSo Nutrients data - Datasets North Sea')

ax = axs[1]
RWSomean.plot.scatter('datetime', 'total_phosphate', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Phosphate")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

ax = axs[2]
RWSomean.plot.scatter('datetime', 'total_silicate', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Silicate")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_datasets.png")
plt.show()

#%% # RWSomean nutrients - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

fig, axs = plt.subplots(dpi=300, nrows=3)

ax = axs[0]
rwss = ax.scatter('datetime', 'nitrate', c='dayofyear', data=RWSomean, cmap=cm, vmin=1, vmax=365, s=20)

plt.colorbar(rwss, ax=ax)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Nitrate")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.yaxis.set_ticks(np.arange(0, 1.1, 0.5))
ax.set_title('RWSo Nutrients data - Seasons North Sea')

ax = axs[1]
rwss = ax.scatter('datetime', 'total_phosphate', c='dayofyear', data=RWSomean, cmap=cm, vmin=1, vmax=365, s=20)

plt.colorbar(rwss, ax=ax)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Phosphate")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.yaxis.set_ticks(np.arange(0, 0.5, 0.1))

ax = axs[2]
rwss = ax.scatter('datetime', 'total_silicate', c='dayofyear', data=RWSomean, cmap=cm, vmin=1, vmax=365, s=20)

plt.colorbar(rwss, ax=ax)
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Silicate")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.yaxis.set_ticks(np.arange(0, 1.1, 0.5))

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_seasons.png")
plt.show()

#%% # RWSomean nutrients - Regions

x = RWSomean['datetime']
y = RWSomean['nitrate']
z = RWSomean['total_phosphate']
w = RWSomean['total_silicate']

#Choose different method periods
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

fig, axs = plt.subplots(dpi=300, nrows=3)

ax = axs[0]
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:salmon pink', edgecolor='none', label='10-20')
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
ax.set_ylabel('Nitrate')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('RWSo Nutrients - Regions North Sea')

ax = axs[1]
ax.scatter(x[L0], z[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], z[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], z[L2], alpha=0.5, s=40, c='xkcd:salmon pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], z[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], z[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], z[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], z[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], z[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], z[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], z[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], z[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Phosphate')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

ax = axs[2]
ax.scatter(x[L0], w[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], w[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], w[L2], alpha=0.5, s=40, c='xkcd:salmon pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], w[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], w[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], w[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], w[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], w[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], w[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], w[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], w[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Silicate')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/Nutrients_mean_regions.png")
plt.show()
