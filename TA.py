# TA 

#%% # TA - Datasets

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
glodapnsmean.plot.scatter("datetime", "alkalinity", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
#mssmean.plot.scatter('datetime', 'alkalinity', c='xkcd:velvet', ax=ax, label="MSS", s=20, alpha=0.4)
Cefasmean.plot.scatter('datetime', 'alkalinity', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
D366mean.plot.scatter('datetime', 'alkalinity', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
RWSnmean.plot.scatter('datetime', 'alkalinity', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('TA data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/TA_mean_datasets.png")
plt.show()

#%% # TA - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = combinedmean.plot.scatter("datetime", "alkalinity", c="dayofyear", cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('TA data - Seasons North Sea')

plt.tight_layout()
plt.savefig("figures/TA_mean_seasons.png")
plt.show()

#%% # TA - Regions

x = combinedmean['datetime']
y = combinedmean['alkalinity']

#Choose different method periods
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
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Year')
ax.set_ylabel('Total alkalinity')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('TA - Regions North Sea')

plt.tight_layout()
#plt.savefig("figures/TA_mean_regions.png")
plt.show()

#%% # TA - mean & allpoints - Dayofyear

fig, ax = plt.subplots(dpi=300)

# glodapnsmean.plot.scatter('dayofyear', 'alkalinity',  c="b", ax=ax, label='GLODAP')
# Cefasmean.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:greenish", ax=ax, label='Cefas')
# D366mean.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:pink", ax=ax, label='D366')
# RWSnmean.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:dark orange", ax=ax, label='RWSn')

# RWSnmean.plot.scatter('dayofyear', 'alkalinity',  c="distance_to_shore", cmap='magma', vmax=80, vmin=0, ax=ax)

resultsglodapns.plot.scatter('dayofyear', 'alkalinity',  c="b", ax=ax, label='GLODAP')
resultsCefas.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:greenish", ax=ax, label='Cefas')
resultsD366.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:pink", ax=ax, label='D366')
resultsRWSn.plot.scatter('dayofyear', 'alkalinity',  c="xkcd:dark orange", ax=ax, label='RWSn')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.set_title('TA data - Day of Year North Sea')

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear_datasets.png")
plt.savefig("figures/DIC_TA_fitting/TA_allpoints_dayofyear_datasets.png")
plt.show()

#%% # Interpolation of sea TA (combined = D366, Cefas, RWSn, Glodap)

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['alkalinity'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], args=(combinedmean['datenum'], combinedmean['alkalinity']))

combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='alkalinity', data=combinedmean, ax=ax,
            scatter_kws={"color": "red"}, line_kws={"color": "blue"})
ax.set_title("TA - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Total alkalinity')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

# ax = axs[1]
# combinedmean.plot("datenum", "dic", ax=ax, c='red')
# fx = np.array([combinedmean.datenum.min(), combinedmean.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy, 'blue')

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('Total alkalinity')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
# plt.xticks(rotation=0)

ax = axs[1]
combinedmean.plot.scatter("datenum", "alkalinity", ax=ax, c='red')
fx = np.linspace(combinedmean.datenum.min(), combinedmean.datenum.max(), 10000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Total alkalinity')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

combinedmean['minusseasonality'] = combinedmean['alkalinity'] - combinedmean['seasoncycle']

ax = axs[2]
# si.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "red"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Total alkalinity')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_season_fitting.png")    

# Use the fit to predict TA in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # TA vs S scatter plots based all points or mean - Glodap, D366, Cefas, RWSn

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('rainbow')

vmin=2001
vmax=2021

sc= ax.scatter(glodapnsmean['salinity'], glodapnsmean['alkalinity'], c=glodapnsmean['year'], vmin=vmin, vmax=vmax, s=35, cmap=cm, edgecolor="None")
sc= ax.scatter(D366mean['salinity'], D366mean['alkalinity'], c=D366mean['year'], vmin=vmin, vmax=vmax, s=35, cmap=cm, edgecolor="None")
sc= ax.scatter(Cefasmean['salinity'], Cefasmean['alkalinity'], c=Cefasmean['year'], vmin=vmin, vmax=vmax, s=35, cmap=cm, edgecolor="None")
sc= ax.scatter(RWSnmean['salinity'], RWSnmean['alkalinity'], c=RWSnmean['year'], vmin=vmin, vmax=vmax, s=35, cmap=cm, edgecolor="None")

cbar=fig.colorbar(sc,ax=ax, orientation='horizontal')

cbar.set_label('Years')
# cbar.outline.set_edgecolor('Grey')
# label=[79,173,265,355]
label=[2001,2006,2011,2016,2021]
cbar.set_ticks(label)
# cbar.set_ticklabels(['', '', '', ''])

# spx=108
# y=135
# cbar.ax.text(spx,y, 'spring')
# sux=200
# y=135
# cbar.ax.text(sux,y, 'summer')
# sx=290
# y=135
# cbar.ax.text(sx,y, 'autumn')
# sx=10
# y=135
# cbar.ax.text(sx,y, 'winter')

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity")
# ax.set_xlim([26, 36])
# ax.set_ylim([0, 25])
ax.set_title('TA & S data - mean')

plt.tight_layout()
plt.savefig("figures/Sal_TA_plot_scatter_mean_year.png")
plt.show()