# DIC

#%% # DIC - Datasets

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
glodapnsmean.plot.scatter("datetime", "dic", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
#mssmean.plot.scatter('datetime', 'dic', c='xkcd:velvet', ax=ax, label="MSS", s=20, alpha=0.4)
Cefasmean.plot.scatter('datetime', 'dic', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
D366mean.plot.scatter('datetime', 'dic', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
RWSnmean.plot.scatter('datetime', 'dic', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("DIC")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('DIC data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/DIC_mean_datasets.png")
plt.show()

#%% # DIC - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = combinedmean.plot.scatter("datetime", "dic", c="dayofyear", cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("DIC")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('DIC data - Seasons North Sea')

plt.tight_layout()
plt.savefig("figures/DIC_mean_seasons.png")
plt.show()

#%% # DIC - Regions

x = combinedmean['datetime']
y = combinedmean['dic']

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
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('DIC')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('DIC data - Regions North Sea')

#plt.tight_layout()
plt.savefig("figures/DIC_mean_regions.png")
plt.show()

#%% # DIC - Regions

x = combined['dayofyear']
y = combined['DIC']

#Choose different method periods
L0 = (combined['distance_to_shore'] > 0) & (combined['distance_to_shore'] <=4)
L1 = (combined['distance_to_shore'] > 4) & (combined['distance_to_shore'] <=10)
L2 = (combined['distance_to_shore'] > 10) & (combined['distance_to_shore'] <=20)
L3 = (combined['distance_to_shore'] > 20) & (combined['distance_to_shore'] <=30)
L4 = (combined['distance_to_shore'] > 30) & (combined['distance_to_shore'] <=50)
L5 = (combined['distance_to_shore'] > 50) & (combined['distance_to_shore'] <=70)
L6 = (combined['distance_to_shore'] > 70) & (combined['distance_to_shore'] <=100)
L7 = (combined['distance_to_shore'] > 100) & (combined['distance_to_shore'] <=150)
L8 = (combined['distance_to_shore'] > 150) & (combined['distance_to_shore'] <=200)
L9 = (combined['distance_to_shore'] > 200) & (combined['distance_to_shore'] <=250)
L10 = (combined['distance_to_shore'] > 250) & (combined['distance_to_shore'] <=300)

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
ax.set_xlabel('Day of Year')
ax.set_ylabel('DIC')
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('DIC data - Regions North Sea')

#plt.tight_layout()
plt.savefig("figures/DIC_combined_regions.png")
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
plt.savefig("figures/DIC_TA_fitting/DIC_mean_dayofyear_datasets.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_allpoints_dayofyear_datasets.png")
plt.show()

#%% # Interpolation of sea DIC (combined = D366, Cefas, RWSn, Glodap)

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['dic'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], args=(combinedmean['datenum'], combinedmean['dic']))

combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='dic', data=combinedmean, ax=ax,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue"})
ax.set_title("DIC - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

# ax = axs[1]
# combinedmean.plot("datenum", "alkalinity", ax=ax, c='red')
# fx = np.array([combinedmean.datenum.min(), combinedmean.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy, 'blue')

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('DIC')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
# plt.xticks(rotation=0)

ax = axs[1]
combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple')
fx = np.linspace(combinedmean.datenum.min(), combinedmean.datenum.max(), 10000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

combinedmean['minusseasonality'] = combinedmean['dic'] - combinedmean['seasoncycle']

ax = axs[2]
# si.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/DIC_season_fitting.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)
