# DIC normalization & seasonal correction

#%% # Equation (2) of paper Friis et al. 2003

# # Take the salinity mean of combined dataset
# csalinitymean = combinedmean['salinity'].mean()
# print(csalinitymean) # Result is 33.31298717967724 

# Take the salinity mean of only the RWSo dataset
salinitymean = RWSomean['salinity'].mean()
print(salinitymean) # Result is 32.86875624846805 

# Salinity endmember (intercept) is 2995.9684418250117 (for DIC - derived below)
salendmember = 2995.9684418250117
resultscombined['normalized_DIC'] = (((resultscombined['dic'] - salendmember) / 
                                 resultscombined['salinity']) * salinitymean) + salendmember

resultscombined['salinityeffect_DIC'] = resultscombined['dic'] - resultscombined['normalized_DIC']

combinedmean['normalized_DIC'] = (((combinedmean['dic'] - salendmember) / 
                                 combinedmean['salinity']) * salinitymean) + salendmember

combinedmean['salinityeffect_DIC'] = combinedmean['dic'] - combinedmean['normalized_DIC']

#%% # DIC normalized to salinity

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

ax=ax
sc = ax.scatter('datetime','normalized_DIC', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)
#sc = ax.scatter('datetime','dic', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)
#sc = ax.scatter('datetime','salinityeffect_DIC', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("DIC (μmol/kg)")
ax.set_title("DIC data - Normalized to salinity North Sea")
#ax.set_title("DIC data - Seasons North Sea")
#ax.set_title("DIC data minus normalized to salinity North Sea")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_ylim([2000,2250])
#ax.set_ylim([-100,100])
ax.yaxis.set_minor_locator(MultipleLocator(10))
plt.grid(b=True, which='minor', axis='both', color='grey', linestyle='-', alpha=0.1)
plt.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-')

cbar.set_label("Day of year")
cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/DIC_longterm/DIC_mean_normalized.png")
#plt.savefig("figures/DIC_longterm/DIC_mean_seasons.png")
#plt.savefig("figures/DIC_longterm/DIC_mean_salinityeffect.png")
plt.show()

#%% # (Normalized) DIC vs salinity

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

ax=ax
# ax = sns.regplot(x='salinity', y='dic', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['dic'])
print(intercept) # 2995.9684418250117
nslope, nintercept, nr, np, nse = linregress(combinedmean['salinity'], combinedmean['normalized_DIC'])
print(nintercept) # 2151.204410436687
# plt.plot(0, intercept, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

sc = ax.scatter('salinity', 'normalized_DIC', c='dayofyear', cmap='twilight', data=combinedmean, marker='X', label='DIC normalized', vmin=vmin, vmax=vmax)
sc = ax.scatter('salinity', 'dic', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='DIC', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("DIC (μmol/kg)")
ax.set_title("DIC and S data - Normalization to salinity North Sea")
ax.legend()
ax.set_ylim([2000,2250])
ax.set_xlim([31,35.5])

cbar.set_label("Day of year")
cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/DIC_longterm/DIC_S_mean_normalized_scatter.png")
plt.show()

#%% # Interpolation of DIC (combined = D366, Cefas, RWSn, Glodap)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='dic', data=combinedmean, ax=ax,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': 'y = 0.009x + 1994.8'}, label='Initial DIC', marker='x')

ax.set_title("DIC - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2000,2250])
ax.legend()

ax = axs[1]
combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple', label='Initial DIC', marker='x')
combinedmean.plot.scatter('datenum', 'normalized_DIC', ax=ax, c='purple', label='Normalized DIC')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2000,2250])
ax.legend()

ax = axs[2]
sns.regplot(x='datenum', y='normalized_DIC', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': 'y = 0.001x + 2131.4'}, label='Normalized DIC')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2000,2250])
ax.legend()

plt.tight_layout()
plt.savefig("figures/DIC_longterm/DIC_normalization_fitting.png")    

#%% # Outcomes linear regression

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['dic'])
nslope, nintercept, nr, np, nse = linregress(combinedmean['datenum'], combinedmean['normalized_DIC'])

# result = linregress(combinedmean['datenum'], combinedmean['dic'])
# print(result.intercept, result.intercept_stderr)

# res = stats.linregress(combinedmean['datenum'], combinedmean['dic'])
# print(f"R-squared: {res.rvalue**2:.6f}")

# # DIC data
# slope = 0.008591780875809623
# intercept = 1994.8095735606953
# result.intercept_stderr = 45.07830353419786
# r = 0.4237877146294286
# p = 0.0021637364609371217
# se = 0.002650501707908609
# R-squared = 0.179596

# # Normalized DIC data
# nslope = 0.001226061444022521 (m)
# nintercept = 2130.41743254563 (b)
# nintercept_stderr = 42.360420522060245
# nr = 0.07087243775153242
# np = 0.6247820643035529
# nse = 0.002490696369180599
# R-squared = 0.005023

#%% # DIC LONG TERM CHANGE

xbegin = 11565
xend = 18808

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 62.23026888348886 (μmol/kg)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 3.1360000196705005 (μmol/kg)

#%% # Normalized DIC LONG TERM CHANGE

xbegin = 11565
xend = 18808

ybegin = (nslope * xbegin) + nintercept
yend = (nslope * xend) + nintercept
changelongterm = yend - ybegin
print(changelongterm) # 8.880363039055283 (μmol/kg)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 0.4475124270682284 (μmol/kg)

#%% # Make new dateframe with the datapoint of 365 located at 0.

combinedmeandubbel = combinedmean.append(combinedmean.loc[[7] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[19] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[36] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[35] *1].assign(**{'dayofyear':-30}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[18] *1].assign(**{'dayofyear':0}), ignore_index=True)

#%% # Seasonal cycle - combined data

fvar = 'dayofyear'

x = combinedmeandubbel[fvar].to_numpy()
y = combinedmeandubbel.normalized_DIC.to_numpy()

# def cluster_profile(x, y, bandwidth=15): 
#     """ CLuster DIC and day of year profile with MeanShift and interpolate"""
    
x_v = np.vstack(x)
clustering = MeanShift(bandwidth=28).fit(x_v)
cluster_labels = clustering.labels_

x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])
    
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
    
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)
 
    # return x_clusters, y_clusters, x_plotting, y_plotting

# x_unique = np.unique(x)
# y_unique = np.full_like(x_unique, np.nan)
# for i in range(len(x_unique)):
#     y_unique[i] = np.mean(y[x == x_unique[i]])
    
# interpolator = interpolate.PchipInterpolator(x_unique, y_unique)
# x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
# y_plotting = interpolator(x_plotting)

fig, ax = plt.subplots(dpi=300)
#ax.scatter(fvar, 'dic', data=RWSnmeandubbel, c='xkcd:blue', s=50)
ax.scatter(fvar, 'dic', data=combinedmeandubbel, c='xkcd:blue', s=50)
#RWSnmean.plot(fvar, 'dic', ax=ax, legend=False)
#ax.scatter(x_unique, y_unique, c='xkcd:raspberry', s=10)
ax.scatter(x_clusters, y_clusters, c='xkcd:raspberry', s=10)
#ax.plot(x_clusters, y_clusters, c='xkcd:raspberry')
ax.plot(x_plotting, y_plotting, c='xkcd:raspberry')
ax.set_xlim([0,400])
#ax.set_ylim([2100,2275])
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC (μmol/kg)")
ax.grid(alpha=0.3)
plt.xlim(0,365)
#ax.grid(axis='both', which='major', linestyle=':', linewidth='2')
ax.set_title('DIC combined - Seasonal cycle')

#plt.savefig("figures/DIC_longterm/DIC_Combined_Clustering.png")    
#plt.savefig("figures/DIC_season_fitting/DIC_Combinedmean_Clustering_normalized_DIC.png")    

#%% # Making a dateframe to plot the seasonal cycle for every year

combinedmeandic = pd.DataFrame()
combinedmeandic['datenum'] = np.arange(11330, 18993)
combinedmeandic['datetime'] = mdates.num2date(combinedmeandic.datenum)
combinedmeandic['dayofyear'] = combinedmeandic.datetime.dt.dayofyear
combinedmeandic['interpolator_dic'] = interpolator(combinedmeandic['dayofyear'])

#%% # Making a dateframe for subtracting seasonal cycle from the datapoints

combinedmeandic2 = pd.DataFrame(combinedmean['datetime'])
combinedmeandic2['dayofyear'] = combinedmean['dayofyear']
combinedmeandic2['datenum'] = combinedmean['datenum']
combinedmeandic2['normalized_DIC'] = combinedmean['normalized_DIC']
combinedmeandic2['interpolator_dic'] = interpolator(combinedmeandic2['dayofyear'])

# plt.scatter(combinedmeandic2['datetime'], combinedmeandic2['interpolator_dic'], c='r')
# plt.scatter(combinedmean['datetime'], combinedmean['normalized_DIC'], c='b')

combinedmeandic2['dicminusseason'] = (combinedmeandic2['normalized_DIC'] - combinedmeandic2['interpolator_dic'])

#%% # Interpolation of sea DIC (combined = D366, Cefas, RWSn, Glodap)

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['normalized_DIC'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], args=(combinedmean['datenum'], combinedmean['normalized_DIC']))

combinedmean['seasoncycle'] = fco2_fit(opt_result['x'], combinedmean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='normalized_DIC', data=combinedmean, ax=ax,
            scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': 'y = 0.001x + 2130.4'}, label='Normalized DIC')
combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple', label='Initial DIC', marker='x')
# combinedmeandic2.plot.scatter("datenum", "dic_final2", ax=ax, label='Final DIC', marker='s', facecolors='none', edgecolors='yellow')

ax.set_title("Normalized DIC - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

ax = axs[1]
combinedmean.plot.scatter("datenum", "normalized_DIC", ax=ax, c='purple', label="Normalized DIC")
combinedmeandic.plot('datenum', 'interpolator_dic', ax=ax, c='g', label='Seasonal cycle')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

combinedmeandic2['dic_final'] = 0.0005 * combinedmeandic2['datenum'] + 2130.4
combinedmeandic2['dic_final2'] = combinedmeandic2['dicminusseason'] + 2139.3

ax = axs[2]
# sns.regplot(x='datenum', y='dicminusseason', data=combinedmeandic2, ax=ax, ci=99.9,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': 'y = 0.0005x + -8.9'}, label='Seasonal corrected')
sns.regplot(x='datenum', y='dic_final2', data=combinedmeandic2, ax=ax, ci=99.9,
             scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': 'y = 0.0005x + 2130.4'}, label='Seasonal corrected')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('DIC (μmol/kg)')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.set_ylim(1980,2240)
ax.legend()

plt.tight_layout()
#plt.savefig("figures/DIC_longterm/DIC_normalized_season_fitting_final2.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)

#%% # Outcome linear regression

slope, intercept, r, p, se = linregress(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason'])

result = linregress(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected DIC data
# slope = 0.0005020699607318944
# intercept = -8.86601700545702
# result.intercept_stderr = 28.686465709385093
# r = 0.04292453345268265
# p = 0.7672440003664052
# se = 0.0016866989304268171
# R-squared = 0.001843

#%% # Seasonal corrected DIC LONG TERM CHANGE

xbegin = 11565
xend = 18808

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 3.6613627882205613 (μmol/kg)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 0.18450882475500552 (μmol/kg)

#%% # Uncertainties DIC
slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['dic'])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(combinedmean['datenum'], combinedmean['dic']))

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['normalized_DIC'])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(combinedmean['datenum'], combinedmean['normalized_DIC']))

slope, intercept, r, p, se = linregress(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason'])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(combinedmeandic2['datenum'], combinedmeandic2['dicminusseason']))

slope, intercept, r, p, se = linregress(combinedmeandic2['datenum'], combinedmeandic2['dic_final2'])
opt_result = least_squares(lsq_fco2_fit, [-0.055, 1182, 166, 686], 
                           args=(combinedmeandic2['datenum'], combinedmeandic2['dic_final2']))

# From linear regression
J = opt_result.jac
cov = np.linalg.inv(J.T.dot(J))
var = np.sqrt(np.diagonal(cov))
std_dev = np.sqrt(var) 
print(std_dev)
# [0.00797924 1.08199306 0.72505228 0.51856887] # Initial data
# 0.00797924, 1.08199, 0.729208, 0.557956 # Normalized data
# 0.00797924, 1.08199, 0.720852, 2.4578 # Corrected data
# [0.00797924 1.08199283 0.72085103 2.45782298] # Final data
doublestd_dev = std_dev[0] * 2
print(doublestd_dev) # 0.01595848261385133 # Final data

# From data
std_dev_data = statistics.stdev(combinedmean['dic']) # 45.70502319214557
var_data = statistics.variance(combinedmean['dic'])
std_dev_data = statistics.stdev(combinedmean['normalized_DIC']) # 38.999942632900634
var_data = statistics.variance(combinedmean['normalized_DIC'])
std_dev_data = statistics.stdev(combinedmeandic2['dicminusseason']) # 26.368641663508285
var_data = statistics.variance(combinedmeandic2['dicminusseason'])

# Residual std dev
combinedmean['yest'] = slope * combinedmean['datenum'] + intercept
combinedmean['residual'] = combinedmean['dic'] - combinedmean['yest']
combinedmean['residual_squared'] = combinedmean['residual']**2
sum_of_squared_residuals = combinedmean['residual_squared'].sum()
n_of_residuals = 50 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 41.82685707976837

combinedmean['yest'] = slope * combinedmean['datenum'] + intercept
combinedmean['residual'] = combinedmean['normalized_DIC'] - combinedmean['yest']
combinedmean['residual_squared'] = combinedmean['residual']**2
sum_of_squared_residuals = combinedmean['residual_squared'].sum()
n_of_residuals = 50 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 39.30501185944042

combinedmeandic2['yest'] = slope * combinedmeandic2['datenum'] + intercept
combinedmeandic2['residual'] = combinedmeandic2['dicminusseason'] - combinedmeandic2['yest']
combinedmeandic2['residual_squared'] = combinedmeandic2['residual']**2
sum_of_squared_residuals = combinedmeandic2['residual_squared'].sum()
n_of_residuals = 50 - 2 # Datapoints in dataframe - 2 
residual_std_dev = np.sqrt((sum_of_squared_residuals / n_of_residuals))
print(residual_std_dev) # Outcome is 26.61734376139221
