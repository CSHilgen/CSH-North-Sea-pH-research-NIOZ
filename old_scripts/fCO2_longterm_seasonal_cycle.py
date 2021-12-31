# fCO2 SOCAT fitting long term trend
import statistics

#%% # Interpolation of gvco2 (air xCO2) & air fCO2 Socat data

# L = socatnsairmean.year > 2000
# socatnsairmean = socatnsairmean[L]

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
sns.regplot(x='datenum', y='fCO2', data=socatnsairmean, ax=ax,
   #         scatter_kws={"color": "black"}, line_kws={"color": "b", 'label': 'y = 0.006x + 297.5'}, label='Initial fCO$_2$ air')
          scatter_kws={"color": "black"}, line_kws={"color": "b", 'label': 'y = 0.006x + 301.7'}, label='Initial xCO$_2$ air')

ax.set_title("SOCAT xCO$_2$ air data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
socatnsairmean.plot.scatter("datenum", "xCO2", ax=ax, c='black', label='Initial xCO$_2$ air')
fx = np.linspace(socatnsairmean.datenum.min(), socatnsairmean.datenum.max(), 10000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
socatnsairmean['minusseasonality'] = socatnsairmean['xCO2'] - socatnsairmean['seasoncycle']

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=socatnsairmean, ax=ax, ci=99.9,
            scatter_kws={"color": "black"}, line_kws={"color": "b", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('xCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/fCO2_longterm/xCO2_air_season_fitting_no_xlim.png")    
plt.show()

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # xCO2 air LONG TERM CHANGE

slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['xCO2'])

# slope = 0.006045831312187939
# intercept = 301.57504350922835
# r = 0.9238917534966
# p = 1.9355429109473955e-33
# se = 0.00028723298617394866

xbegin = 9069 # 8003 # 11565 
xend = 18169

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 55.017064940910245 (1994) µmol/mol
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 2.206728428948598 (1994) µmol/mol

#%% # Uncertainties xCO2 air

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(socatnsairmean['datenum'], socatnsairmean['xCO2']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev) # [0.00718862 0.91977318 0.61589148 1.0210968 ]
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) # 0.01437724530519887

# From data
std_dev_data = statistics.stdev(socatnsairmean['xCO2'])
var_data = statistics.variance(socatnsairmean['xCO2'])
print(std_dev_data) # 14.479510981305197

# Residual std dev
socatnsairmean['yest'] = slope * socatnsairmean['datenum'] + intercept
socatnsairmean['residual'] = socatnsairmean['xCO2'] - socatnsairmean['yest']
socatnsairmean['residual_squared'] = socatnsairmean['residual']**2
sum_of_squared_residuals = socatnsairmean['residual_squared'].sum()
n_of_residuals = 78 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # 5.576974203776717

#%% # fCO2 air LONG TERM CHANGE

socatnsairmean = socatnsairmean.dropna(axis='rows', how='all', subset=['fCO2'])
slope, intercept, r, p, se = linregress(socatnsairmean['datenum'], socatnsairmean['fCO2'])

result = linregress(socatnsairmean['datenum'], socatnsairmean['fCO2'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(socatnsairmean['datenum'], socatnsairmean['fCO2'])
print(f"R-squared: {res.rvalue**2:.6f}")

# slope = 0.005851567849378946
# intercept = 297.4855205445053
# intercept_stderr = 5.403231682471172
# r = 0.8776633106117994
# p = 1.1534774113839719e-25
# se = 0.0003689783561107006 
# R-squared: 0.791664

xbegin = 9069 
xend = 18169

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 53.496869658949606 
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 2.1457535632435834 

#%% # Uncertainties fCO2 air

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(socatnsairmean['datenum'], socatnsairmean['fCO2']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev) # [0.00721568 0.91977319 0.61596975 0.92362447]
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) # 0.014431357603213355

# From data
std_dev_data = statistics.stdev(socatnsairmean['fCO2']) 
var_data = statistics.variance(socatnsairmean['fCO2'])
print(std_dev_data) # 14.619595880645836

# Residual std dev
socatnsairmean['yest'] = slope * socatnsairmean['datenum'] + intercept
socatnsairmean['residual'] = socatnsairmean['fCO2'] - socatnsairmean['yest']
socatnsairmean['residual_squared'] = socatnsairmean['residual']**2
sum_of_squared_residuals = socatnsairmean['residual_squared'].sum()
n_of_residuals = 78 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # 6.716695079672789

#%% # Interpolation of fco2_recommended (sea fCO2) Socat data 

# L = socatnsmean.year > 2000
# socatnsmean = socatnsmean[L]

# socatnsmean = pd.read_csv("dataframes_made/socatnsmean.csv")
slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fco2_sea'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 600, 162, 680], 
                         args=(socatnsmean['datenum'], socatnsmean['fco2_sea']))

socatnsmean['seasoncycle'] = fco2_fit(opt_result['x'], socatnsmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='fco2_sea', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue", 'label': 'y = 0.003x + 306.4'}, label='Initial fCO$_2$ sea')

ax.set_title("SOCAT fCO$_2$ sea data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
socatnsmean.plot.scatter("datenum", "fco2_sea", ax=ax, c='orange', label='Initial fCO$_2$ sea')
fx = np.linspace(socatnsmean.datenum.min(), socatnsmean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
socatnsmean['minusseasonality'] = socatnsmean['fco2_sea'] - socatnsmean['seasoncycle']

ax = axs[2]
#socatnsmean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsmean, ax=ax, ci=99.9,
            scatter_kws={"color": "orange"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('fCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
#plt.savefig("figures/fCO2_longterm/fCO2_sea_season_fitting_no_xlim.png")    

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
print(changelongterm) # 36.64053302952158 (1991) # 32.95330484020127 (1994) # 24.348138551968475 (2000) uatm
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 1.262512466324495 (1991) # 1.262512466324495 (1994) # 1.263983867368581 (2000) uatm

#%% # Uncertainties fCO2 sea

slope, intercept, r, p, se = linregress(socatnsmean['datenum'], socatnsmean['fCO2'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(socatnsmean['datenum'], socatnsmean['fCO2']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev) # [0.00652116 0.83167793 0.53924892 0.31760469]
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) # 0.01302677928501963

# From data
std_dev_data = statistics.stdev(socatnsmean['fCO2'])
var_data = statistics.variance(socatnsmean['fCO2'])
print(std_dev_data) # 62.0877960464136

# Residual std dev
socatnsmean['yest'] = slope * socatnsmean['datenum'] + intercept
socatnsmean['residual'] = socatnsmean['fCO2'] - socatnsmean['yest']
socatnsmean['residual_squared'] = socatnsmean['residual']**2
sum_of_squared_residuals = socatnsmean['residual_squared'].sum()
n_of_residuals = 118 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # 61.885772563423599

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
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': 'y = -0.001x + -2.4'}, label='Initial ΔfCO$_2$')

ax.set_title("SOCAT Δ fCO$_2$ (sea - air) data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('ΔfCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
socatnsmeandelta.plot.scatter("datenum", "deltafco2", ax=ax, c='xkcd:dark orange', label='Initial ΔfCO$_2$')
fx = np.linspace(socatnsmeandelta.datenum.min(), socatnsmeandelta.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('ΔfCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
socatnsmeandelta['minusseasonality'] = socatnsmeandelta['deltafco2'] - socatnsmeandelta['seasoncycle']

ax = axs[2]
#socatnsmeandelta.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=socatnsmeandelta, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('ΔfCO$_2$ (µatm)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/fCO2_longterm/fCO2_delta_season_fitting_no_xlim.png")    

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
print(changelongterm) # -14.884199081143215 (1991) # -9.574646402181596 (2000)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -0.5970035895183817 (1991) # -0.5291862411865963 (2000)

#%% # Uncertainties fCO2 delta

slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev) # [0.00719759 0.92337366 0.58281239 0.33421328]
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) # 0.014437710219828927

# From data
std_dev_data = statistics.stdev(socatnsmeandelta['deltafco2']) 
var_data = statistics.variance(socatnsmeandelta['deltafco2'])
print(std_dev_data) # # 72.79923097393318

# Residual std dev
socatnsmeandelta['yest'] = slope * socatnsmeandelta['datenum'] + intercept
socatnsmeandelta['residual'] = socatnsmeandelta['deltafco2'] - socatnsmeandelta['yest']
socatnsmeandelta['residual_squared'] = socatnsmeandelta['residual']**2
sum_of_squared_residuals = socatnsmeandelta['residual_squared'].sum()
n_of_residuals = 78 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # 73.18600220373993

#%% # Interpolation of fco2_recommended (sea fCO2) Socat data + COMBINED

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
