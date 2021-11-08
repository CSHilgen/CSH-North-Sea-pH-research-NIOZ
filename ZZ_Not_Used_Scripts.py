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

L = (combinedmean['year'] < 2018)

combinedmean['point_on_seasoncycle'].iloc[41] = combinedmean['dic'].iloc[41] + 38.077
combinedmean['point_on_seasoncycle'].iloc[42] = combinedmean['dic'].iloc[42] + 41.491
combinedmean['point_on_seasoncycle'].iloc[43] = combinedmean['dic'].iloc[43] + 101.96
combinedmean['point_on_seasoncycle'].iloc[44] = combinedmean['dic'].iloc[44] + 77.729
combinedmean['point_on_seasoncycle'].iloc[45] = combinedmean['dic'].iloc[45] + 36.691
combinedmean['point_on_seasoncycle'].iloc[46] = combinedmean['dic'].iloc[46] + 24.234
combinedmean['point_on_seasoncycle'].iloc[47] = combinedmean['dic'].iloc[47] + 36.847
combinedmean['point_on_seasoncycle'].iloc[5] = combinedmean['dic'].iloc[5] + 21.189
combinedmean['point_on_seasoncycle'].iloc[48] = combinedmean['dic'].iloc[48] + 22.899
combinedmean['point_on_seasoncycle'].iloc[6] = combinedmean['dic'].iloc[6] + 35.001
combinedmean['point_on_seasoncycle'].iloc[49] = combinedmean['dic'].iloc[49] + 23.081
combinedmean['point_on_seasoncycle'].iloc[0] = combinedmean['dic'].iloc[0] + 15.211
combinedmean['point_on_seasoncycle'].iloc[1] = combinedmean['dic'].iloc[1] + 12.799
combinedmean['point_on_seasoncycle'].iloc[2] = combinedmean['dic'].iloc[2] + 16.767
combinedmean['point_on_seasoncycle'].iloc[3] = combinedmean['dic'].iloc[3] + 12.761
combinedmean['point_on_seasoncycle'].iloc[4] = combinedmean['dic'].iloc[4] + 25.207

x1 = combinedmean['datenum']
y1 = combinedmean['point_on_seasoncycle']
ax.scatter(x1[L], y1[L], c='orange')

RWSn_cx = pd.DataFrame(x_clusters, columns=['doy_av_2018-2021'])
RWSn_cy = pd.DataFrame(y_clusters, columns=['dic_av_2018-2021'])
RWSn_c = pd.concat([RWSn_cx, RWSn_cy], axis=1)

RWSn_c['2001'] = RWSn_c['doy_av_2018-2021'] + (31*365)
RWSn_c['2002'] = RWSn_c['doy_av_2018-2021'] + (32*365)
RWSn_c['2003'] = RWSn_c['doy_av_2018-2021'] + (33*365)
RWSn_c['2004'] = RWSn_c['doy_av_2018-2021'] + (34*365)
RWSn_c['2005'] = RWSn_c['doy_av_2018-2021'] + (35*365)
RWSn_c['2006'] = RWSn_c['doy_av_2018-2021'] + (36*365)
RWSn_c['2007'] = RWSn_c['doy_av_2018-2021'] + (37*365)
RWSn_c['2008'] = RWSn_c['doy_av_2018-2021'] + (38*365)
RWSn_c['2009'] = RWSn_c['doy_av_2018-2021'] + (39*365)
RWSn_c['2010'] = RWSn_c['doy_av_2018-2021'] + (40*365)
RWSn_c['2011'] = RWSn_c['doy_av_2018-2021'] + (41*365)
RWSn_c['2012'] = RWSn_c['doy_av_2018-2021'] + (42*365)
RWSn_c['2013'] = RWSn_c['doy_av_2018-2021'] + (43*365)
RWSn_c['2014'] = RWSn_c['doy_av_2018-2021'] + (44*365)
RWSn_c['2015'] = RWSn_c['doy_av_2018-2021'] + (45*365)
RWSn_c['2016'] = RWSn_c['doy_av_2018-2021'] + (46*365)
RWSn_c['2017'] = RWSn_c['doy_av_2018-2021'] + (47*365)
RWSn_c['2018'] = RWSn_c['doy_av_2018-2021'] + (48*365)
RWSn_c['2019'] = RWSn_c['doy_av_2018-2021'] + (49*365)
RWSn_c['2020'] = RWSn_c['doy_av_2018-2021'] + (50*365)
RWSn_c['2021'] = RWSn_c['doy_av_2018-2021'] + (51*365)

RWSn_c.plot("2001", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2002", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2003", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2004", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2005", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2006", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2007", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2008", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2009", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2010", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2011", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2012", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2013", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2014", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2015", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2016", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2017", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2018", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2019", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2020", 'dic_av_2018-2021', ax=ax, c='orange')
RWSn_c.plot("2021", 'dic_av_2018-2021', ax=ax, c='orange')
