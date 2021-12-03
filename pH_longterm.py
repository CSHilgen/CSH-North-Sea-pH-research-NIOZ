# pH fitting - long term trend

#%% # Interpolation of pH (RWSo)

L0 = (RWSomean.year >= 2000) & (RWSomean.year <= 2010)
L1 = (RWSomean.year >= 2010)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='pH_total', data=RWSomean[L0], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue"})

ax.set_title("pH - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

ax = axs[1]
sns.regplot(x='datenum', y='pH_total', data=RWSomean[L1], ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

ax = axs[2]
sns.regplot(x='datenum', y='pH_total_out', data=RWSnmean_out, ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/pH_longterm/pH_fitting.png")    
plt.show()

#%% # Outcomes linear regression

#slope, intercept, r, p, se = linregress(RWSomean['datenum'][L0], RWSomean['pH_total'][L0])

# RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
# slope, intercept, r, p, se = linregress(RWSomean['datenum'][L1], RWSomean['pH_total'][L1])

slope, intercept, r, p, se = linregress(RWSnmean_out['datenum'], RWSnmean_out['pH_total_out'])

result = linregress(RWSnmean_out['datenum'], RWSnmean_out['pH_total_out'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSnmean_out['datenum'], RWSnmean_out['pH_total_out'])
print(f"R-squared: {res.rvalue**2:.6f}")

#%%
# pH data (2000-2010)
# slope = -3.758720795412976e-05
# intercept = 8.38528690774876
# intercept_stderr = 0.12964944372811366
# r = -0.31861862891813325
# p = 0.00024695186103695666
# se = 9.961812451934047e-06
# R-squared = 0.101518

# pH data (2000-2010) LONG TERM CHANGE RWSo
xbegin = 10972.695934209332
xend = 14957.83805902066
ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -0.14979036577204585 umol/kg
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -0.013719330903257358 umol/kg

# # pH data (2010-2021)
# slope = 4.808697934329894e-05 (m)
# intercept = 7.059763473906516 (b)
# intercept_stderr = 0.3638023966505977
# r = 0.20639226669883123
# p = 0.03378286794493958
# se = 2.2354482708593162e-05
# R-squared = 0.042598

# pH data (2010-2021) LONG TERM CHANGE RWSo
xbegin = 14623.58725057
xend = 17876.53029662152
ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 0.15642420506040722
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 0.0175517474603041

# # pH data (2018-2021)
slope = -5.0278201535597545e-05  #(m)
intercept = 8.9940166143516 #(b) 
# intercept_stderr = 0.7187929140101699
# r = -0.22860787403202934
# p = 0.21609116299572192
# se = 3.9758848564196145e-05
# R-squared = 0.052262

# pH data (2018-2021) LONG TERM CHANGE RWSn
xbegin = 17562
xend = 18808
ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -0.06264663911335511
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -0.01835154356049327


#%% # Interpolation of pH_total RWSomean

L = RWSomean.year > 2000
RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['pH_total'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['pH_total']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])
combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue"})

ax.set_title("RWSo pH data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
# ax.set_ylim(200, 550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
RWSomean.plot.scatter("datenum", "pH_total", ax=ax, c='xkcd:water blue', label='RWSo pH')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
#ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['pH_total'] - RWSomean['seasoncycle']

ax = axs[2]
#RWSomean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('pH (total scale)')
#ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/pH_longterm/pH_season_fitting_RWSomean_2000.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)