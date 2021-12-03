# TA fitting

#%% # Dubbel mean on combined dataset - mean by day of year

combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])
combined2mean = combinedmean.groupby(by=combinedmean['dayofyear']).mean()
combined2mean = combined2mean.reset_index()

#%% TA - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultscombined.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#combinedmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
combined2mean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
combined2mean.plot('dayofyear','alkalinity', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
#ax.set_title("TA data - allpoints - Dayofyear")
#ax.set_title("TA data - mean - Dayofyear")
#ax.set_title("TA data - 2mean - Dayofyear")
ax.set_title("TA data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_2mean_scatter_dayofyear.png")
plt.savefig("figures/DIC_TA_fitting/TA_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the alkalinity mean, line as alkanitity winter mean and alkalinity - winter mean

resultscombinedwinter = resultscombined[(resultscombined["dayofyear"] >= 355) | (resultscombined["dayofyear"] <= 78)]
winteralkalinitymean = resultscombinedwinter['alkalinity'].mean() # Result is 2336.949
print("The mean of the TA in the winter =")
print(winteralkalinitymean)
resultscombined['alkalinity-winteralkalinitymean'] = resultscombined['alkalinity'] - winteralkalinitymean

# combinedmeanwinter = combinedmean[(combinedmean["dayofyear"] >= 355) | (combinedmean["dayofyear"] <= 78)]
# winteralkalinity2mean = combinedmeanwinter['alkalinity'].mean() # Result is 2355.875
# combinedmean['alkalinity-winteralkalinitymean'] = combinedmean['alkalinity'] - winteralkalinity2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultscombined.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
resultscombined.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
#plt.axhline(y=winteralkalinitymean, color='r', linestyle='-')

# combinedmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
# combinedmean.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winteralkalinity2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("TA data - allpoints - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear_wintermean.png")
plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear_minuswintermean.png")
plt.show()

#%% # Dubbel mean on RWSn dataset - mean by day of year

RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSn2mean = RWSnmean.groupby(by=RWSnmean['dayofyear']).mean()
RWSn2mean = RWSn2mean.reset_index()

#%% # RWSn TA - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
resultsRWSn.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSnmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot('dayofyear','alkalinity', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - allpoints - Dayofyear")
#ax.set_title("RWSn TA data - mean - Dayofyear")
#ax.set_title("RWSn TA data - 2mean - Dayofyear")
#ax.set_title("RWSn TA data - 2mean - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_2mean_scatter_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the RWSn alkalinity mean, line as alkalinity winter mean and alkalinity - winter mean

resultsRWSnwinter = resultsRWSn[(resultsRWSn["dayofyear"] >= 355) | (resultsRWSn["dayofyear"] <= 78)]
winteralkalinitymean = resultsRWSnwinter['alkalinity'].mean() # Result is 2360.320
print("The mean of the TA in the winter =")
print(winteralkalinitymean)
resultsRWSn['alkalinity-winteralkalinitymean'] = resultsRWSn['alkalinity'] - winteralkalinitymean

# RWSnmeanwinter = RWSnmean[(RWSnmean["dayofyear"] >= 355) | (RWSnmean["dayofyear"] <= 78)]
# winteralkalinity2mean = RWSnmeanwinter['alkalinity'].mean() # Result is 2204.358
# print("The mean of the TA mean in the winter =")
# print(winteralkalinity2mean)
# RWSnmean['alkalinity-winteralkalinitymean'] = RWSnmean['alkalinity'] - winteralkalinity2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
resultsRWSn.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#resultsRWSn.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
plt.axhline(y=winteralkalinitymean, color='r', linestyle='-')

# RWSnmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
# RWSnmean.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winteralkalinity2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA - TA winter mean")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - allpoints - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear_wintermean.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear_minuswintermean.png")
plt.show()

#%% # CURVE FITTING only RWSn !!! PART 1

fig, ax = plt.subplots(dpi=300)

x = RWSn2mean['dayofyear']
y = RWSn2mean['alkalinity']

# define the true objective function
def objective(x, a, b , c):
 	return (a * x**3) - (b * x**2) + c
 
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c = popt
# plot input vs output
ax.scatter(x, y, c='purple')
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b, c)
# create a line plot for the mapping function
ax.plot(x_line, y_line, '--', color='red')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - curve fit - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_Interpolation_1.png")
plt.show()

#%% # CURVE FITTING only RWSn !!! PART 2

fig, ax = plt.subplots(dpi=300)

x = RWSn2mean['dayofyear']
y = RWSn2mean['alkalinity']

interp_spline = interpolate.UnivariateSpline(x, y)
x_interp = np.linspace(np.min(x), np.max(x), num=15)
y_spline = interp_spline(x_interp)
ax.plot(x_interp, y_spline, label='Spline', c='b')

interp_cubic = interpolate.interp1d(x, y, kind='cubic')
x_interp = np.linspace(np.min(x), np.max(x), num=15)
y_cubic = interp_cubic(x_interp)
ax.plot(x_interp, y_cubic, label='Cubic', c='red')

interp_nearest = interpolate.interp1d(x, y, kind='nearest')
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_nearest = interp_nearest(x_interp)
ax.plot(x_interp, y_nearest, label='Nearest', c='black')

interp_linear = interpolate.interp1d(x, y, kind='linear')
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_linear = interp_linear(x_interp)
ax.plot(x_interp, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x, y)
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_pchip = interp_pchip(x_interp)
ax.plot(x_interp, y_pchip, label='Pchip', c='pink')

ax.scatter(x, y)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Interpolation")
# ax.plot(x, y)

# # define the true objective function
# def objective(x, a, b , c):
#  	return (a * x**3) - (b * x**2) + c
# # summarize the parameter values
# a, b, c = popt
# # plot input vs output
# plt.scatter(x, y)
# # define a sequence of inputs between the smallest and largest known inputs
# x_line = arange(min(x), max(x), 1)
# # calculate the output for the range
# y_line = objective(x_line, a, b, c)
# # create a line plot for the mapping function
# plt.plot(x_line, y_line, '--', color='red')
# plt.show() 

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn - TA data - mean - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_Interpolation_2.png")
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
plt.savefig("figures/TA_normalization/TA_season_fitting.png")    

# Use the fit to predict TA in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Equation (1) of paper Friis et al. 2003: TRADITIONALLY

combinedmean['normalized_TA_t'] = ((combinedmean['alkalinity'] / 
                                 combinedmean['salinity']) * salinitymean)

combinedmean['salinityeffect_TA_t'] = combinedmean['alkalinity'] - combinedmean['normalized_TA_t']

#%% # TA normalized to salinity TRADITIONALLY

fig, ax = plt.subplots(dpi=300)

ax=ax
At = ax.scatter('datetime','normalized_TA_t', c='dayofyear', cmap='twilight', data=combinedmean)
#At = ax.scatter('datetime','alkalinity', c='dayofyear', cmap='twilight', data=combinedmean)
#At = ax.scatter('datetime','salinityeffect_TA_t', c='dayofyear', cmap='twilight', data=combinedmean)

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA data - Normalized to salinity (traditionally) North Sea")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_mean_normalized_t.png")
plt.show()

#%% # (Normalized) TA vs salinity TRADITIONALLY

fig, ax = plt.subplots(dpi=300)

ax=ax
At = ax.scatter('salinity', 'normalized_TA_t', c='dayofyear', cmap='twilight', data=combinedmean, marker='X', label='TA normalized')
At = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='TA')

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA and S data - Normalization to salinity (traditionally) North Sea")
ax.legend()

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_S_mean_normalized_t_scatter.png")
plt.show()


