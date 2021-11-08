# DIC fitting
from scipy.interpolate import splev, splrep

#%% # Dubbel mean on combined dataset - mean by day of year

combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])
combined2mean = combinedmean.groupby(by=combinedmean['dayofyear']).mean()
combined2mean = combined2mean.reset_index()

#%% # DIC - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultscombined.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#combinedmean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#combined2mean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#combined2mean.plot('dayofyear','dic', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("DIC data - allpoints - Dayofyear")
#ax.set_title("DIC data - mean - Dayofyear")
#ax.set_title("DIC data - 2mean - Dayofyear")
#ax.set_title("DIC data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_2mean_scatter_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the dic mean, line as dic winter mean and dic - winter mean

resultscombinedwinter = resultscombined[(resultscombined["dayofyear"] >= 355) | (resultscombined["dayofyear"] <= 78)]
winterdicmean = resultscombinedwinter['dic'].mean() # Result is 2175.272
print("The mean of the DIC in the winter =")
print(winterdicmean)
resultscombined['dic-winterdicmean'] = resultscombined['dic'] - winterdicmean

# combinedmeanwinter = combinedmean[(combinedmean["dayofyear"] >= 355) | (combinedmean["dayofyear"] <= 78)]
# winterdic2mean = combinedmeanwinter['dic'].mean() # Result is 2204.358
# print("The mean of the DIC mean in the winter =")
# print(winterdic2mean)
# combinedmean['dic-winterdicmean'] = combinedmean['dic'] - winterdic2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
resultscombined.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
resultscombined.plot.scatter('dayofyear','dic-winterdicmean', c='year', cmap='magma', ax=ax)
plt.axhline(y=winterdicmean, color='r', linestyle='-')

# combinedmean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
# combinedmean.plot.scatter('dayofyear','dic-winterdicmean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winterdic2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")# - DIC winter mean")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("DIC data - allpoints - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_allpoints_dayofyear_wintermean.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_allpoints_dayofyear_minuswintermean.png")
plt.show()

#%% # Dubbel mean on RWSn dataset - mean by day of year

RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSn2mean = RWSnmean.groupby(by=RWSnmean['dayofyear']).mean()
RWSn2mean = RWSn2mean.reset_index()

#%% # RWSn DIC - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultsRWSn.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
RWSnmean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot('dayofyear','dic', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.set_title("RWSn DIC data - allpoints - Dayofyear")
#ax.set_title("RWSn DIC data - mean - Dayofyear")
#ax.set_title("RWSn DIC data - 2mean - Dayofyear")
ax.set_title("RWSn DIC data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_2mean_scatter_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the RWSn dic mean, line as dic winter mean and dic - winter mean

resultsRWSnwinter = resultsRWSn[(resultsRWSn["dayofyear"] >= 355) | (resultsRWSn["dayofyear"] <= 78)]
winterdicmean = resultsRWSnwinter['dic'].mean() # Result is 2207.291
print("The mean of the DIC in the winter =")
print(winterdicmean)
resultsRWSn['dic-winterdicmean'] = resultsRWSn['dic'] - winterdicmean

# RWSnmeanwinter = RWSnmean[(RWSnmean["dayofyear"] >= 355) | (RWSnmean["dayofyear"] <= 78)]
# winterdic2mean = RWSnmeanwinter['dic'].mean() # Result is 2204.358
# print("The mean of the DIC mean in the winter =")
# print(winterdic2mean)
# RWSnmean['dic-winterdicmean'] = RWSnmean['dic'] - winterdic2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultsRWSn.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
resultsRWSn.plot.scatter('dayofyear','dic-winterdicmean', c='year', cmap='magma', ax=ax)
#plt.axhline(y=winterdicmean, color='r', linestyle='-')

# RWSnmean.plot.scatter('dayofyear','dic', c='year', cmap='magma', ax=ax)
# RWSnmean.plot.scatter('dayofyear','dic-winterdicmean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winterdic2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC - DIC winter mean")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn DIC data - allpoints - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_allpoints_dayofyear_wintermean.png")
plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_allpoints_dayofyear_minuswintermean.png")
plt.show()


#%% # CURVE FITTING only RWSn !!! PART 2

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

interp_linear = interpolate.interp1d(x[L1], y[L1], bounds_error=False, kind='linear')
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_linear = interp_linear(x_interp)
ax.plot(x_interp, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x[L1], y[L1], extrapolate=False)
x_interp = np.linspace(np.min(x), np.max(x), num=100)
y_pchip = interp_pchip(x_interp)
ax.plot(x_interp, y_pchip, label='Pchip', c='pink')

# interp_smo = interpolate.splrep(x[L1], y[L1], s=100)
# x_interp = np.linspace(np.min(x), np.max(x), num=100)
# y_smo = splev(x_interp, interp_smo)
# ax.plot(x_interp, y_smo, label='Smoothing', c='red')

# ax.scatter(x,y, c='purple')
#ax.scatter(x[L0], y[L0], c='purple', label='2018')
ax.scatter(x[L1], y[L1], c='purple', label='2019')
#ax.scatter(x[L2], y[L2], c='purple', label='2020')
#ax.scatter(x[L3], y[L3], c='purple', label='2021')

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Interpolation")
# ax.plot(x, y)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
ax.set_xlim([0,365])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.set_title("RWSn - DIC data - mean - Dayofyear")
ax.set_title("RWSn - DIC data - 2019")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_Interpolation_2019.png")
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

ax = axs[1]
combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple')
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
            scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/DIC_season_fitting_tryOUT8.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)
