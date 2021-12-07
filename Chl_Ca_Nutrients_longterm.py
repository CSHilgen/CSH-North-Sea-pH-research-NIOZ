# Chlorophyll & Calcium & Nutrients - long term trend

#%% # Interpolation of Chlorophyll RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['chlorophyll'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['chlorophyll'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['chlorophyll']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='chlorophyll', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': 'y = -0.0002x + 5.9'}, label='Initial Chl')

ax.set_title("RWSo Chlorophyll data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Chlorophyll')
ax.set_ylim(0,26)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "chlorophyll", ax=ax, c='xkcd:brown', label='Initial Chl')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Chlorophyll')
ax.set_ylim(0,26)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['chlorophyll'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('chlorophyll')
ax.set_ylim(-16,26)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/Chl_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['chlorophyll'])

result = linregress(RWSomean['datenum'], RWSomean['chlorophyll'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['chlorophyll'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Chl data
# slope = -0.00017056781001596204
# intercept = 5.882480175450506
# result.intercept_stderr = 0.5618697689984392
# r = -0.1476464644631345
# p = 0.0009065566477092844
# se = 5.1097889692650114e-05
# R-squared = 0.021799

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected Chl data
# slope = 3.340727552511966e-12
# intercept = -4.0497388715553337e-08
# result.intercept_stderr = 0.5023359144697214
# r = 3.2703522192421023e-09
# p = 0.9999999416820236
# se = 4.568372701735738e-05
# R-squared = 0

#%% # Seasonal corrected Chl LONG TERM CHANGE

# Chl data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 2.1791565825035552e-08 
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 1.2193655566668674e-09

#%% # Uncertainties Chl

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [[3.10736002e-03 3.78248488e-01 3.81865778e-01 1.18320930e+04]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 4.733103747898233
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 4.681983799144775

#%% # Interpolation of Calcium RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_calcium'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_calcium'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['total_calcium']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_calcium', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': 'y = 0.01x + 165.6'}, label='Initial Ca')

ax.set_title("RWSo Calcium data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Calcium (µmol/kg)')
#ax.set_ylim(0,26)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_calcium", ax=ax, c='xkcd:grey', label='Initial Ca')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Calcium (µmol/kg)')
#ax.set_ylim(0,26)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['total_calcium'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': 'y = -1.6e-06x + 0.03'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Calcium (µmol/kg)')
#ax.set_ylim(-16,26)
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/Ca_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_calcium'])

result = linregress(RWSomean['datenum'], RWSomean['total_calcium'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['total_calcium'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Ca data
# slope = 0.0146621689734568
# intercept = 165.62949492225093
# result.intercept_stderr = 40.41867121444575
# r = 0.47723556755796026
# p = 4.657748233052171e-08
# se = 0.002506769002574807
# R-squared = 0.227754

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected Ca data
# slope = -9.495571604827571e-07
# intercept = 0.015343126067017283
# result.intercept_stderr = 40.310881043534664
# r =  -3.526448484038092e-05
# p = 0.9996976077741306
# se = 0.00250008384813743
# R-squared = 0

#%% # Seasonal corrected Ca LONG TERM CHANGE

# Ca data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -0.006193961357829026
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -0.0003465883635762064

#%% # Uncertainties Chl

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [[3.10736002e-03 3.78248488e-01 3.81865778e-01 1.18320930e+04]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 4.733103747898233
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 4.681983799144775

#%% # Interpolation of Phosphate RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_phosphate'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_phosphate'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['total_phosphate']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_phosphate', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:apricot"}, line_kws={"color": "blue", 'label': 'y = -9.6e-07x + 0.03'}, label='Initial P')

ax.set_title("RWSo Total phosphate data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_ylim(0,0.12)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_phosphate", ax=ax, c='xkcd:apricot', label='Initial P')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_ylim(0,0.12)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['total_phosphate'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:apricot"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Phosphate (µmol/kg)')
ax.set_ylim(-0.05,0.12)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/Phos_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_phosphate'])

result = linregress(RWSomean['datenum'], RWSomean['total_phosphate'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['total_phosphate'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Phos data
# slope = -9.597902004954136e-07
# intercept = 0.031206654495075786
# result.intercept_stderr = 0.0022619481732432025
# r = -0.2042616940104875
# p = 3.9521978201050196e-06
# se = 2.0570741588909666e-07
# R-squared = 0.041723

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected Phos data
# slope = 1.5009347634453512e-21
# intercept = -1.2759070509503142e-17
# result.intercept_stderr = 0.002061101200888499
# r = 3.581048470678294e-16
# p = 0.9999999416820236
# se = 1.8744187286695215e-07
# R-squared = 0

#%% # Seasonal corrected Phos LONG TERM CHANGE

# Phos data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 9.790597461954024e-18
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 5.47841188657553e-19

#%% # Uncertainties Phos

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [3.10634650e-03 3.72932429e-01 3.77338767e-01 6.13307035e+04]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 0.019420084325487592
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 0.01921033745147335

#%% # Interpolation of Silicate RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_silicate'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_silicate'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['total_silicate']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_silicate', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:navy"}, line_kws={"color": "blue", 'label': 'y = -1.4e-06x + 0.2'}, label='Initial Si')

ax.set_title("RWSo Total Silicate data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Silicate (µmol/kg)')
ax.set_ylim(0,0.75)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_silicate", ax=ax, c='xkcd:navy', label='Initial Si')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Silicate (µmol/kg)')
ax.set_ylim(0,0.75)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['total_silicate'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:navy"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Silicate (µmol/kg)')
ax.set_ylim(-0.2,0.4)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/Si_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_silicate'])

result = linregress(RWSomean['datenum'], RWSomean['total_silicate'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['total_silicate'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Si data
# slope = -1.3539498561104993e-06
# intercept = 0.16521443337310399
# result.intercept_stderr = 0.013135404536300879
# r = -0.05062320389243583
# p = 0.2575800352855422
# se = 1.1945676544596275e-06
# R-squared = 0.002563

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected Si data
# slope = -6.967719690585744e-20
# intercept = 6.019786973361401e-16
# result.intercept_stderr = 0.008334024915269389
# r = -4.111341722331309e-15
# p = 0.9999999999999267
# se = 7.579177761696161e-07
# R-squared = 0

#%% # Seasonal corrected Si LONG TERM CHANGE

# Si data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -4.54504355416908e-16
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -2.5432176870637957e-17

#%% # Uncertainties Si

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [3.11194617e-03 3.74095445e-01 3.80762146e-01 1.92999629e+05]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 0.07852475490067004
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 0.07767664726132606

#%% # Interpolation of Ammonia RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_ammonia'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_ammonia'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['total_ammonia']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_ammonia', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': 'y = -2.1e-06x + 0.5'}, label='Initial NH$_3$')

ax.set_title("RWSo Total Ammonia data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0,0.2)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_ammonia", ax=ax, c='xkcd:plum', label='Initial NH$_3$')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(0,0.2)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['total_ammonia'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:plum"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Ammonia (µmol/kg)')
ax.set_ylim(-0.1,0.1)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/NH3_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_ammonia'])

result = linregress(RWSomean['datenum'], RWSomean['total_ammonia'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['total_ammonia'])
print(f"R-squared: {res.rvalue**2:.6f}")

# NH3 data
# slope = -2.1069220670223276e-06
# intercept = 0.05021962367868045
# result.intercept_stderr = 0.0016771954787073492
# r = -0.5250193221280967
# p = 1.257368037247577e-36
# se = 1.5335854914900225e-07
# R-squared = 0.275645

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected NH3 data
# slope = 8.502488586699539e-22
# intercept = 1.7203720392976357e-17
# result.intercept_stderr = 0.0015238618284994666
# r = 2.7399038376547856e-16
# p = 0.9999999999999951
# se = 1.3933810464498711e-07
# R-squared = 0

#%% # Seasonal corrected NH3 LONG TERM CHANGE

# NH3 data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 5.54617330510411e-18
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 3.103408334145332e-19

#%% # Uncertainties NH3

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [3.11963097e-03 3.71679910e-01 3.75410530e-01 3.93350295e+01]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 0.014306327169812526
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 0.014095204023775367


#%% # Interpolation of Nitrate RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['total_nitrate'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_nitrate'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['total_nitrate']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='total_nitrate', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue", 'label': 'y = -6.9e-06x + 0.24'}, label='Initial N')

ax.set_title("RWSo Total Nitrate data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_ylim(0,0.75)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "total_nitrate", ax=ax, c='xkcd:light violet', label='Initial N')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_ylim(0,0.75)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['total_nitrate'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:light violet"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Nitrate (µmol/kg)')
ax.set_ylim(-0.25,0.5)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/Chl_Ca_nutrient_longterm/N_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['total_nitrate'])

result = linregress(RWSomean['datenum'], RWSomean['total_nitrate'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['total_nitrate'])
print(f"R-squared: {res.rvalue**2:.6f}")

# N data
# slope = -6.892241124935217e-06
# intercept =  0.24002766188026528
# result.intercept_stderr = 0.015201770222126534
# r = -0.21259651047717226
# p = 1.5735144175594635e-06
# se = 1.418113145485245e-06
# R-squared = 0.045197

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected N data
# slope = -2.0397935507599375e-19
# intercept = 2.053593457614443e-15
# result.intercept_stderr = 0.009602785899944823
# r = -1.0193468293398115e-14
# p = 0.9999999999998184
# se = 8.958059962102986e-07
# R-squared = 0

#%% # Seasonal corrected N LONG TERM CHANGE

# N data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -1.3305573331607075e-15
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -7.445246460273773e-17

#%% # Uncertainties N

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['minusseasonality']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) # [3.14586812e-03 3.75037461e-01 3.83601582e-01 2.54190559e+05]
print(std_dev)

# From data
std_dev_data = statistics.stdev(RWSomean['minusseasonality']) # 0.09054660205870221
var_data = statistics.variance(RWSomean['minusseasonality'])
print(std_dev_data)

# Residual std dev
RWSomean['yest'] = slope * RWSomean['datenum'] + intercept
RWSomean['residual'] = RWSomean['minusseasonality'] - RWSomean['yest']
RWSomean['residual_squared'] = RWSomean['residual']**2
sum_of_squared_residuals = RWSomean['residual_squared'].sum()
n_of_residuals = 514 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 0.08947921777949694