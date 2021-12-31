# Not used scripts 

# DIC clustering
RWSnmeandicx = pd.DataFrame(x_plotting, columns=['dayofyear'])
RWSnmeandicy = pd.DataFrame(y_plotting, columns=['dic'])
RWSnmeandic = pd.concat([combineddic_x, combineddic_y], axis=1)

#%% # CURVE FITTING only RWSn !!! PART 1

fig, ax = plt.subplots(dpi=300)

x = RWSn2mean['dayofyear']
y = RWSn2mean['dic']

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
ax.set_ylabel("DIC")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn DIC data - curve fit - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_Interpolation_1.png")
plt.show()

#%% # Interpolation of sea DIC (RWSn)

slope, intercept, r, p, se = linregress(RWSnmean['datenum'], RWSnmean['dic'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], args=(RWSnmean['datenum'], RWSnmean['dic']))

#combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
# sns.regplot(x='datenum', y='dic', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})
sns.regplot(x='datenum', y='dic', data=RWSnmean, ax=ax,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

ax.set_title("RWSn DIC - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

# ax = axs[1]
# combinedmean.plot("datenum", "dic", ax=ax, c='purple')
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
# plt.xticks(rotation=30)

ax = axs[1]
# combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple')
# fx = np.linspace(RWSnmean.datenum.min(), RWSnmean.datenum.max(), 10000)
# fy = fco2_fit(opt_result['x'], fx)
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy, 'g')
x = RWSnmean['datenum']
y = RWSnmean['dic']

RWSnmean.plot.scatter("datenum", "dic", ax=ax, c='purple')

RWSn_linearx = pd.DataFrame(x_interp_linear, columns=['x_interp_linear'])
RWSn_lineary = pd.DataFrame(y_linear, columns=['y_linear'])
RWSn_linear = pd.concat([RWSn_linearx, RWSn_lineary], axis=1)
RWSn_linear['2015-2018'] = RWSn_linear['x_interp_linear'] - 1096
RWSn_linear['2012-2015'] = RWSn_linear['2015-2018'] - 1096
RWSn_linear['2009-2012'] = RWSn_linear['2012-2015'] - 1096
RWSn_linear['2006-2009'] = RWSn_linear['2009-2012'] - 1096
RWSn_linear['2003-2006'] = RWSn_linear['2006-2009'] - 1096
RWSn_linear['2000-2003'] = RWSn_linear['2003-2006'] - 1096

interp_linear = interpolate.interp1d(x, y, kind='linear')
x_interp_linear = np.linspace(np.min(x), np.max(x), num=19)
y_linear = interp_linear(x_interp_linear)
ax.plot(x_interp_linear, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x, y)
x_interp_pchip = np.linspace(np.min(x), np.max(x), num=19)
y_pchip = interp_pchip(x_interp_pchip)
ax.plot(x_interp_pchip, y_pchip, label='Pchip', c='pink')

RWSn_pchipx = pd.DataFrame(x_interp_linear, columns=['x_interp_pchip'])
RWSn_pchipy = pd.DataFrame(y_linear, columns=['y_pchip'])
RWSn_pchip = pd.concat([RWSn_pchipx, RWSn_pchipy], axis=1)

RWSn_linear.plot.scatter("x_interp_linear", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2015-2018", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2012-2015", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2009-2012", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2006-2009", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2003-2006", "y_linear", ax=ax, c='purple')
RWSn_linear.plot.scatter("2000-2003", "y_linear", ax=ax, c='purple')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

# combinedmean['minusseasonality'] = combinedmean['dic'] - combinedmean['seasoncycle']

ax = axs[2]
# sns.regplot(x='datenum', y='minusseasonality', data=combinedmean, ax=ax, ci=99.9,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})
# sns.regplot(x='datenum', y='minusseasonality', data=RWSnmean, ax=ax, ci=99.9,
#              scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/DIC_RWSn_Interpolation_Fitting_2.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%%
# ERROR on making a plot . year is one line in color.


#%% DIC and TA vs day of year (color is year) allpoints, mean, 2mean

fig, ax = plt.subplots(dpi=300)
x = RWSnmean['month']
y = RWSnmean['dic']

L0 = (RWSnmean['year'] == 2018)
L1 = (RWSnmean['year'] == 2019)
L2 = (RWSnmean['year'] == 2020)
L3 = (RWSnmean['year'] == 2021)
RWSnmean.plot.scatter(x[L0], y[L0], c='b', ax=ax)
RWSnmean.plot(x[L1], y[L1], c='r', ax=ax)
RWSnmean.plot(x[L2], y[L2], c='white', ax=ax)
RWSnmean.plot(x[L3], y[L3], c='xkcd:banana', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Month")
ax.set_ylabel("DIC")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

# ax=axs[1]
# RWSnmean.plot.scatter('month', 'alkalinity', c='year', cmap='magma', ax=ax)


# ax.grid(alpha=0.3)
# ax.set_xlabel("Month")
# ax.set_ylabel("Total alkalinity")
# # ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()

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
plt.savefig("figures/DIC_season_fitting/DIC_season_fitting.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

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