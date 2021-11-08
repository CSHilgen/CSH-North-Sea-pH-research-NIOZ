# fCO2 SOCAT fitting

#%% # Interpolation of gvco2 (air xCO2) Socat data

slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['xCO2'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(socatnsairmean['datenum'], socatnsairmean['xCO2']))

socatnsairmean['seasoncycle'] = fco2_fit(opt_result['x'], socatnsairmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='xCO2', data=socatnsairmean, ax=ax,
            scatter_kws={"color": "black"}, line_kws={"color": "blue"})

ax.set_title("SOCAT xCO$_2$ air data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (umol/mol)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

# ax = axs[1]
# socatnsairmean.plot("datenum", "xCO2", ax=ax, c='black', legend=False)
# fx = np.array([socatnsairmean.datenum.min(), socatnsairmean.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy)

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('xCO$_2$ (umol/mol)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
# plt.xticks(rotation=30)

ax = axs[1]
socatnsairmean.plot.scatter("datenum", "xCO2", ax=ax, c='black')
fx = np.linspace(socatnsairmean.datenum.min(), socatnsairmean.datenum.max(), 10000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (umol/mol)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

# Minus the sin cycle trend and the long-term trend
socatnsairmean['minusseasonality'] = socatnsairmean['xCO2'] - socatnsairmean['seasoncycle']

ax = axs[2]
#socatnsairmean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsairmean, ax=ax, ci=99.9,
            scatter_kws={"color": "black"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (umol/mol)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/xCO2_air_season_fitting.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Interpolation of fco2_recommended (sea fCO2) Socat data 

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fCO2']))

socatnsmean['seasoncycle'] = fco2_fit(opt_result['x'], socatnsmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='fCO2', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue"})

ax.set_title("SOCAT fCO$_2$ sea data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

# ax = axs[1]
# socatnsmean.plot("datenum", "fCO2", ax=ax, legend=False)
# fx = np.array([socatnsmean.datenum.min(), socatnsmean.datenum.max()])
# fy = fx * slope + intercept # * 1.5
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy) 

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('fCO$_2$ (uatm)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
# plt.xticks(rotation=30)

ax = axs[1]
socatnsmean.plot.scatter("datenum", "fCO2", ax=ax, c='orange', legend=False)
fx = np.linspace(socatnsmean.datenum.min(), socatnsmean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

# Minus the sin cycle trend and the long-term trend
socatnsmean['minusseasonality'] = socatnsmean['fCO2'] - socatnsmean['seasoncycle']

ax = axs[2]
#socatnsmean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/fCO2_sea_season_fitting.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Interpolation of deltafco2 (fco2 sea - fco2 air) Socat data

# socatns['datetime'] = pd.to_datetime(socatns['datetime'])
# # Make dataset based on the mean 
# i = socatns.set_index('datetime').resample('M').mean()
# ri = i.reset_index()
# # Drop all rows where fCO2 is nan
# si = ri.dropna(axis='rows', how='all', subset=['fco2_recommended'])
# socatnsmean['deltafco2'] = si['deltafco2']

# slope, intercept, r, p, se = linregress(si['datenum'], si['deltafco2'])

# def fco2_fit(coeffs, datenum):
#     slope, intercept, sine_stretch, sine_shift = coeffs
#     fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
#     return fco2

# def lsq_fco2_fit(coeffs, datenum, fco2):
#     return fco2_fit(coeffs, datenum) - fco2

# opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
#                             args=(si['datenum'], si['deltafco2']))

# si['seasoncycle'] = fco2_fit(opt_result['x'], si['datenum'])

# # Fitted values:
# slope, intercept, sine_stretch, sine_shift = opt_result['x']

# fig, axs = plt.subplots(nrows=4, dpi=300, figsize=(10,6))
# ax = axs[0]
# sns.regplot(x='datenum', y='deltafco2', data=si, ax=ax, ci=99.9)

# ax.set_title("SOCAT deltafco2 North Sea interpolation")
# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('fCO2 (uatm)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# plt.xticks(rotation=30)

# ax = axs[1]
# si.plot("datetime", "deltafco2", ax=ax)
# fx = np.array([si.datenum.min(), si.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy) 

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('CO2 (uatm)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# plt.xticks(rotation=30)

# ax = axs[2]
# si.plot("datetime", "deltafco2", ax=ax)
# fx = np.linspace(si.datenum.min(), si.datenum.max(), 1000)
# fy = fco2_fit(opt_result['x'], fx)
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx, fy) # 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('CO2 (uatm)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# plt.xticks(rotation=30)

# si['minusseasonality'] = si['deltafco2'] - si['seasoncycle']

# ax = axs[3]
# # si.plot.scatter("datetime", "minusseasonality", ax=ax)
# sns.regplot(x='datenum', y='minusseasonality', data=si, ax=ax, ci=99.9)

# ax.grid(alpha=0.3)
# ax.set_xlabel("Time (yrs)")
# ax.set_ylabel('CO2 (uatm)')
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# plt.xticks(rotation=30)

# plt.tight_layout()
# plt.savefig("figures/NS_fitting_delta_fCO2_seasoncycle.png")    

# # Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# # Last number is date (1 = 1 january 1970)