# DIC fitting
from scipy.interpolate import splev, splrep

#%% # Dubbel mean on combined dataset - mean by day of year

combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])
combined2mean = combinedmean.groupby(by=combinedmean['dayofyear']).mean()
combined2mean = combined2mean.reset_index()

#%% # DIC - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#sc = ax.scatter('dayofyear','dic', c='year', cmap='magma', data=resultscombined)
#sc = ax.scatter('dayofyear','dic', c='year', cmap='magma', data=combinedmean)
sc = ax.scatter('dayofyear','dic', c='year', cmap='magma', data=combined2mean)
sc = ax.plot('dayofyear','dic', c='r', data=combined2mean)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.set_title("DIC data - allpoints - Dayofyear")
#ax.set_title("DIC data - mean - Dayofyear")
#ax.set_title("DIC data - 2mean - Dayofyear")
ax.set_title("DIC data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_season_fitting/DIC_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_season_fitting/DIC_mean_dayofyear.png")
#plt.savefig("figures/DIC_season_fitting/DIC_2mean_scatter_dayofyear.png")
plt.savefig("figures/DIC_season_fitting/DIC_2mean_plot_dayofyear.png")
plt.show()

#%% # Dubbel mean on RWSn dataset - mean by day of year

RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSn2mean = RWSnmean.groupby(by=RWSnmean['dayofyear']).mean()
RWSn2mean = RWSn2mean.reset_index()

#%% # RWSn DIC - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultsRWSn.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#RWSnmean.plot.scatter('dayofyear','dic', c='year', cmap='rainbow', ax=ax)
#RWSn2mean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot('dayofyear','dic', c='r', ax=ax)
socatnsmean.plot.scatter('dayofyear','deltafco2', c='year', cmap='rainbow', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Delta fCO2")
ax.set_title("Delta fCO2 data - mean - Dayofyear")
# ax.set_ylabel("DIC")
# ax.set_title("RWSn DIC data - allpoints - Dayofyear")
#ax.set_title("RWSn DIC data - mean - Dayofyear")
#ax.set_title("RWSn DIC data - 2mean - Dayofyear")
#ax.set_title("RWSn DIC data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_longterm/DIC_RWSn_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_longterm/DIC_RWSn_mean_dayofyear_rainbow.png")
#plt.savefig("figures/DIC_longterm/DIC_RWSn_2mean_scatter_dayofyear.png")
#plt.savefig("figures/DIC_longterm/DIC_RWSn_2mean_plot_dayofyear.png")
plt.show()

#%% # DIC - curve dayofyear - RWSn 

fig, ax = plt.subplots(dpi=300)

L0 = (RWSnmean['year'] == 2018) 
L1 = (RWSnmean['year'] == 2019)
L2 = (RWSnmean['year'] == 2020) 
L3 = (RWSnmean['year'] == 2021) 

x = RWSnmean['dayofyear'] 
y = RWSnmean['dic']

# x = RWSn2mean['dayofyear'] 
# y = RWSn2mean['dic']

# interp_nearest = interpolate.interp1d(x, y, kind='nearest')
# x_interp = np.linspace(np.min(x), np.max(x), num=100)
# y_nearest = interp_nearest(x_interp)
# ax.plot(x_interp, y_nearest, label='Nearest', c='black')

interp_linear = interpolate.interp1d(x, y, bounds_error=False, kind='linear')
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_linear = interp_linear(x_interp)
ax.plot(x_interp, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x, y, extrapolate=False)
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_pchip = interp_pchip(x_interp)
ax.plot(x_interp, y_pchip, label='Pchip', c='pink')

# interp_smo = interpolate.splrep(x[L1], y[L1], s=100)
# x_interp = np.linspace(np.min(x), np.max(x), num=100)
# y_smo = splev(x_interp, interp_smo)
# ax.plot(x_interp, y_smo, label='Smoothing', c='red')

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
ax.set_ylabel("DIC")
ax.set_xlim([0,365])
ax.set_title("RWSn - DIC data - mean - Dayofyear")
#ax.set_title("RWSn - DIC data - 2021")

plt.tight_layout()
plt.savefig("figures/DIC_longterm/DIC_RWSn_Interpolation.png")
plt.show()

# interp_spline = interpolate.UnivariateSpline(x, y)
# x_interp = np.linspace(np.min(x), np.max(x), num=15)
# y_spline = interp_spline(x_interp)
# ax.plot(x_interp, y_spline, label='Spline', c='b')

# interp_cubic = interpolate.interp1d(x, y, kind='cubic')
# x_interp = np.linspace(np.min(x), np.max(x), num=15)
# y_cubic = interp_cubic(x_interp)
# ax.plot(x_interp, y_cubic, label='Cubic', c='red')

#%% # Interpolation of sea DIC (combined = D366, Cefas, RWSn, Glodap)

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['normalized_DIC'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], args=(combinedmean['datenum'], combinedmean['normalized_DIC']))

combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='normalized_DIC', data=combinedmean, ax=ax,
            scatter_kws={"color": "grey"}, line_kws={"color": "blue"})
ax.set_title("Normalized DIC - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

ax = axs[1]
combinedmean.plot.scatter("datenum", "normalized_DIC", ax=ax, c='grey')
combinedmeandic.plot('datenum', 'interpolator_dic', ax=ax, c='g', label='Seasonal cycle')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
# ax.get_legend().remove()

ax = axs[2]
#combinedmean['dic_minusseasonality'] = combinedmean['dic'] - combinedmean['point_on_seasoncycle']
sns.regplot(x='datenum', y='dicminusseason', data=combinedmeandic2, ax=ax, ci=99.9,
            scatter_kws={"color": "grey"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
#plt.savefig("figures/DIC_longterm/DIC_normalized_season_fitting.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%%

slope, intercept, r, p, se = linregress(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason'])
# Slope of the regression line
# Intercept of the regression line
# Correlation coefficient (rvalue)
# Wald Test with t-distribution of the test statistic - hypothesis test (pvalue)
# Standard error of the estimated slope (gradient) - residual normality

