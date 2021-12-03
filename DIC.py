# DIC

#%% # DIC - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter("datetime", "dic", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('datetime', 'dic', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('datetime', 'dic', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('datetime', 'dic', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("DIC (µmol/kg)")
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
ax.set_title('DIC combined data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/DIC_mean_time_datasets_combined.png")
plt.show()

#%% # DIC - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('datetime', 'dic', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Seasons North Sea') 

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/DIC_mean_time_seasons_combined.png")
plt.show()

#%% # DIC - Time - Regions

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

fig, ax = plt.subplots(dpi=300)

ax = ax
x = combinedmean['datetime']
y = combinedmean['dic']

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

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Regions North Sea') 

plt.tight_layout()
plt.savefig("figures/DIC_mean_time_regions_combined.png")
plt.show()

#%% # DIC - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter("dayofyear", "dic", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('dayofyear', 'dic', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('dayofyear', 'dic', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('dayofyear', 'dic', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/DIC_mean_dayofyear_datasets_combined.png")
plt.show()

#%% # DIC - Dayofyear - Regions

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

fig, ax = plt.subplots(dpi=300)

ax = ax
x = combinedmean['dayofyear']
y = combinedmean['dic']

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

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Regions North Sea') 

plt.tight_layout()
plt.savefig("figures/DIC_mean_dayofyear_regions_combined.png")
plt.show()

#%% # DIC - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = ax
sc = ax.scatter('dayofyear', 'dic', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Year North Sea') 

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/DIC_mean_dayofyear_year_combined.png")
plt.show()

#%% # DIC - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter("distance_to_shore", "dic", c="b", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'dic', c='xkcd:greenish', data=Cefasmean, label='Cefas', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'dic', c='xkcd:pink', data=D366mean, label='D366', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'dic', c='xkcd:dark orange', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/DIC_mean_regions_datasets_combined.png")
plt.show()

#%% # DIC - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('distance_to_shore', 'dic', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Seasons North Sea') 

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/DIC_mean_regions_seasons_combined.png")
plt.show()

#%% # DIC - Regions - Year

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = ax
sc = ax.scatter('distance_to_shore', 'dic', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("DIC (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('DIC combined data - Year North Sea') 

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/DIC_mean_regions_year_combined.png")
plt.show()






#%% # DIC - mean & allpoints - Dayofyear

fig, ax = plt.subplots(dpi=300)

glodapnsmean.plot.scatter('dayofyear', 'dic',  c="b", ax=ax, label='GLODAP')
Cefasmean.plot.scatter('dayofyear', 'dic',  c="xkcd:greenish", ax=ax, label='Cefas')
D366mean.plot.scatter('dayofyear', 'dic',  c="xkcd:pink", ax=ax, label='D366')
RWSnmean.plot.scatter('dayofyear', 'dic',  c="xkcd:dark orange", ax=ax, label='RWSn')

# resultsglodapns.plot.scatter('dayofyear', 'dic',  c="b", ax=ax, label='GLODAP')
# resultsCefas.plot.scatter('dayofyear', 'dic',  c="xkcd:greenish", ax=ax, label='Cefas')
# resultsD366.plot.scatter('dayofyear', 'dic',  c="xkcd:pink", ax=ax, label='D366')
# resultsRWSn.plot.scatter('dayofyear', 'dic',  c="xkcd:dark orange", ax=ax, label='RWSn')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.set_title('DIC data - Day of Year North Sea')

plt.tight_layout()
#plt.savefig("figures/DIC_longterm/DIC_mean_dayofyear_datasets.png")
#plt.savefig("figures/DIC_longterm/DIC_allpoints_dayofyear_datasets.png")
plt.show()

#%% # DIC per RWSn-year

RWSnmean = RWSnmean.sort_values(by=['dayofyear'])
RWSnmean = RWSnmean.reset_index()

fig, ax = plt.subplots(dpi=300)

L0 = (RWSnmean['year'] == 2018) 
L1 = (RWSnmean['year'] == 2019)
L2 = (RWSnmean['year'] == 2020) 
L3 = (RWSnmean['year'] == 2021) 

x = RWSnmean['dayofyear'] 
y = RWSnmean['dic']

interp_linear = interpolate.interp1d(x, y, bounds_error=False, kind='linear')
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_linear = interp_linear(x_interp)
ax.plot(x_interp, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x, y, extrapolate=False)
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_pchip = interp_pchip(x_interp)
ax.plot(x_interp, y_pchip, label='Pchip', c='pink')

ax.scatter(x, y, c='purple')
#ax.scatter(x[L0], y[L0], c='purple', label='2018')
#ax.scatter(x[L1], y[L1], c='purple', label='2019')
#ax.scatter(x[L2], y[L2], c='purple', label='2020')
#ax.scatter(x[L3], y[L3], c='purple', label='2021')

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Interpolation")
#ax.plot(x, y)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC (μmol/kg)")
ax.set_xlim([0, 365])
ax.set_title("DIC RWSn data 2018-2021")

plt.tight_layout()
plt.savefig("figures/DIC_longterm/DIC_RWSn_Interpolation.png")
plt.show()
