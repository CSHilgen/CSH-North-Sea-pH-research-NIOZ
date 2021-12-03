# Temperature - long term trend

#%% # Interpolation of Temperature RWSomean

L = RWSomean.year > 2000
RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['temperature'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['temperature'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + (sine_stretch*3) * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25)) 
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['temperature']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='temperature', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue"})

ax.set_title("RWSo Temperature data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
# ax.set_ylim(200, 550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
RWSomean.plot.scatter("datenum", "temperature", ax=ax, c='xkcd:pink', label='RWSo T')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx) + 1.5
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
#ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['temperature'] - RWSomean['seasoncycle']

ax = axs[2]
#RWSomean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Temperature (°C)')
#ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/T_longterm/T_season_fitting_RWSomean2_2000.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

#slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['temperature'])

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected DIC data
# slope = 5.260647022614757e-12
# intercept = -7.827835077421452e-08
# result.intercept_stderr = 0.797994200041035
# r = 6.745129515459824e-09
# p = 0.9999999224753104
# se = 5.407757421536226e-05
# R-squared = 0

#%% # Seasonal corrected T LONG TERM CHANGE

# T data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 3.431520052851605e-08 (μmol/kg)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 1.9201361632543856e-09 (μmol/kg)

