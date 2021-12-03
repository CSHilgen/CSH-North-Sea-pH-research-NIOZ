# fCO2 SOCAT fitting long term trend

#%% # Interpolation of gvco2 (air fCO2) Socat data

# L = socatnsairmean.year > 2000
# socatnsairmean = socatnsairmean[L]

slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['fCO2'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(socatnsairmean['datenum'], socatnsairmean['fCO2']))

socatnsairmean['seasoncycle'] = fco2_fit(opt_result['x'], socatnsairmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='fCO2', data=socatnsairmean, ax=ax,
            scatter_kws={"color": "black"}, line_kws={"color": "blue"})

ax.set_title("SOCAT fCO$_2$ air data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
socatnsairmean.plot.scatter("datenum", "fCO2", ax=ax, c='black')
fx = np.linspace(socatnsairmean.datenum.min(), socatnsairmean.datenum.max(), 10000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

# Minus the sin cycle trend and the long-term trend
socatnsairmean['minusseasonality'] = socatnsairmean['fCO2'] - socatnsairmean['seasoncycle']

ax = axs[2]
#socatnsairmean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsairmean, ax=ax, ci=99.9,
            scatter_kws={"color": "black"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/fCO2_longterm/fCO2_air_season_fitting_no_xlim.png")    
plt.show()

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # xCO2 air LONG TERM CHANGE

slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['xCO2'])

# slope = 0.006038368700883675
# intercept = 301.69608430133616
# r = 0.9154756271287411
# p = 2.2255073910421853e-31
# se = 0.00030645838103225773 

xbegin = 8003 # 9069 # 11565 
xend = 18169

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 59.61915149431877 (1991) # 53.36752691307305 (1994) # 38.729576674058706 (2000) µmol/mol
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 2.1405656399199637 (1991) # 2.1405656399199633 (1994) # 2.1405656399199615 (2000) µmol/mol

#%% # fCO2 air LONG TERM CHANGE

socatnsairmean = socatnsairmean.dropna(axis='rows', how='all', subset=['fCO2'])
slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['fCO2'])

# slope = 0.005851567849378946
# intercept = 297.4855205445053
# r = 0.8776633106117994
# p = 1.1534774113839719e-25
# se = 0.0003689783561107006 

xbegin = 9069 # 11565
xend = 18169

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 53.496869658949606 # 38.643754077298524
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 2.1457535632435834 # 2.135822265023313

#%% # Interpolation of fco2_recommended (sea fCO2) Socat data 

L = socatnsmean.year > 2000
socatnsmean = socatnsmean[L]

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

#opt_result = least_squares(lsq_fco2_fit, [0.006, 600, 162, 680], 
 #                          args=(socatnsmean['datenum'], socatnsmean['fCO2']))
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
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
#plt.savefig("figures/fCO2_longterm/fCO2_sea_season_fitting.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # fCO2 sea LONG TERM CHANGE

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])

# slope = 0.00346296949963995
# intercept = 306.42776836804853
# r = 0.11256724403466686
# p = 0.22894356533224247
# se = 0.0028629586103729268 

xbegin = 8003 # 9069 # 11565
xend = 18596

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 36.64053302952158 # 32.95330484020127 # 24.348138551968475 uatm
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 1.262512466324495 (1991) # 1.262512466324495 (1994) # 1.263983867368581 (2000) uatm

#%% # Interpolation of delta fco2 (sea fCO2 - air fco2) Socat data 

socatnsmeandelta = socatnsmean.dropna(axis='rows', how='all', subset=['deltafco2'])
# L = socatnsmeandelta.year > 2000
# socatnsmeandelta = socatnsmeandelta[L]

slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

#opt_result = least_squares(lsq_fco2_fit, [0.006, 600, 162, 680], 
 #                          args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))
 
socatnsmeandelta['seasoncycle'] = fco2_fit(opt_result['x'], socatnsmeandelta['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue"})

ax.set_title("SOCAT fCO$_2$ delta data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
socatnsmeandelta.plot.scatter("datenum", "deltafco2", ax=ax, c='xkcd:dark orange', legend=False)
fx = np.linspace(socatnsmeandelta.datenum.min(), socatnsmeandelta.datenum.max(), 1000)
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
socatnsmeandelta['minusseasonality'] = socatnsmeandelta['deltafco2'] - socatnsmeandelta['seasoncycle']

ax = axs[2]
#socatnsmeandelta.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsmeandelta, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (uatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
#plt.savefig("figures/fCO2_longterm/fCO2_delta_season_fitting.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Delta fCO2 LONG TERM CHANGE

slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])

# slope = -0.0014498253183194423
# intercept = -2.3626335256454247
# r = -0.041595729209856346
# p = 0.7194555976343038
# se = 0.004021242565964851

xbegin = 9069 # 11565
xend = 18169

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -14.884199081143215 # -9.574646402181596
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -0.5970035895183817 # -0.5291862411865963

#%% # Interpolation of fco2_recommended (sea fCO2) Socat data 

L = socatnsmean.year > 2000
socatnsmean = socatnsmean[L]

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
combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='fCO2', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue"})
ax.scatter('datenum', 'fCO2', data=combinedmean, c='xkcd:velvet')

ax.set_title("SOCAT fCO$_2$ sea data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO2 (uatm)')
ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
socatnsmean.plot.scatter("datenum", "fCO2", ax=ax, c='orange', label='Socat fCO2')
ax.scatter('datenum', 'fCO2', data=combinedmean, c='xkcd:velvet', label='Combined fCO2')
fx = np.linspace(socatnsmean.datenum.min(), socatnsmean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (uatm)')
ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
socatnsmean['minusseasonality'] = socatnsmean['fCO2'] - socatnsmean['seasoncycle']
combinedmean['minusseasonality'] = combinedmean['fCO2'] - combinedmean['seasoncycle']

ax = axs[2]
#socatnsmean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue"})
ax.scatter('datenum', 'minusseasonality', data=combinedmean, c='xkcd:velvet')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (uatm)')
ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/fCO2_longterm/fCO2_sea_season_fitting_combined.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)
