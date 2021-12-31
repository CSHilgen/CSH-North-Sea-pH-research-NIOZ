# Oxygen - long term trend

#%% # Interpolation of oxygen umol/kg RWSo

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['oxygen umol/kg'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['oxygen umol/kg'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(RWSomean['datenum'], RWSomean['oxygen umol/kg']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "green"}, line_kws={"color": "blue", 'label': 'y = 0.0004x + 270.7'}, label='Initial O$_2$')

ax.set_title("RWSo Oyxgen data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oyxgen (µmol/kg)')
# ax.set_ylim(200, 550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "oxygen umol/kg", ax=ax, c='green', label='Initial O$_2$')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oyxgen (µmol/kg)')
#ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['oxygen umol/kg'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
#RWSomean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "green"}, line_kws={"color": "blue", 'label': 'y = 0 + 0.0009'}, label='Seasonal correction')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oyxgen (µmol/kg)')
#ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/O2_longterm/O2_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)


#%% # Interpolation of AOU umol/kg RWSo

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['aou'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['aou'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(RWSomean['datenum'], RWSomean['aou']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='aou', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': 'y = -0.0007x + 5.9'}, label='Initial AOU')

ax.set_title("RWSo Oyxgen data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
# ax.set_ylim(200, 550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
RWSomean.plot.scatter("datenum", "aou", ax=ax, c='xkcd:spring green', label='Initial AOU')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g', label='Seasonal cycle') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
#ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['aou'] - RWSomean['seasoncycle']

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

ax = axs[2]
#RWSomean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': 'y = 0'}, label='Initial AOU')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
#ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

plt.tight_layout()
plt.savefig("figures/O2_longterm/AOU_season_fitting_RWSomean.png")    
plt.show()

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Interpolation of O2 (RWSo)

L0 = (RWSomean.year <= 1986)
L1 = (RWSomean.year >= 1986) & (RWSomean.year <= 2010)
L2 = (RWSomean.year >= 2010)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomean[L0], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': 'y = 0.007x + 240.1'}, label='AOU')

ax.set_title("O2 - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oxygen (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

ax = axs[1]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomean[L1], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': 'y = 0.002x + 264.6'}, label='AOU')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oxygen (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

ax = axs[2]
sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomean[L2], ax=ax,
            scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': 'y = -0.03x + 714.8'}, label='AOU')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Oxygen (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

plt.tight_layout()
plt.savefig("figures/O2_longterm/O2_fitting2.png")    
plt.show()

#%%

RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['oxygen umol/kg'])

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L0], RWSomean['oxygen umol/kg'][L0])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L0], RWSomean['oxygen umol/kg'][L0]))

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L1], RWSomean['oxygen umol/kg'][L1])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L1], RWSomean['oxygen umol/kg'][L1]))

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L2], RWSomean['oxygen umol/kg'][L2])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L2], RWSomean['oxygen umol/kg'][L2]))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev)
# [0.00835913 0.58947309 0.53237824 0.38723629] # L0
# [0.00470019 0.51217995 0.43603866 0.32690981] # L1
# [0.01017448 1.29644832 0.56706046 0.43320212] # L2
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) 
# 0.0167182610062491 L0
# 0.009400389006086097 L1
# 0.02034896704571519 L2

#%% # Interpolation of AOU (RWSo)

L0 = (RWSomean.year <= 1986)
L1 = (RWSomean.year >= 1986) & (RWSomean.year <= 2010)
L2 = (RWSomean.year >= 2010)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='aou', data=RWSomean[L0], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': 'y = -0.006x + 29.0'}, label='AOU')

ax.set_title("O2 - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

ax = axs[1]
sns.regplot(x='datenum', y='aou', data=RWSomean[L1], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': 'y = -0.002x + 16.8'}, label='AOU')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

ax = axs[2]
sns.regplot(x='datenum', y='aou', data=RWSomean[L2], ax=ax,
            scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': 'y = 0.02x + -365.8'}, label='AOU')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('AOU (µmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.legend()

plt.tight_layout()
plt.savefig("figures/O2_longterm/AOU_fitting2.png")    
plt.show()

#%%

RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['aou'])

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L0], RWSomean['aou'][L0])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L0], RWSomean['aou'][L0]))

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L1], RWSomean['aou'][L1])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L1], RWSomean['aou'][L1]))

slope, intercept, r, p, se = linregress(RWSomean['datenum'][L2], RWSomean['aou'][L2])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(RWSomean['datenum'][L2], RWSomean['aou'][L2]))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev)
# [0.00836083 0.58695434 0.52493577 0.57747371] # L0
# [0.0046985  0.51440069 0.43671708 0.49390462] # L1
# [0.01019322 1.30552889 0.56039872 0.7331359 ] # L2
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) 
# 0.016721661981920072 L0
# 0.009397006460117286 L1
# 0.02038644217393357 L2
