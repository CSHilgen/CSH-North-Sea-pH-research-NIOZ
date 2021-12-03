# Salinity box model - long term trend

#%% # TA difference

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])

print(f"TA of rivers at 0 salinity: {intercept:6f}")
x = 35.5
TAopenocean = slope * x + intercept
print(f"TA of open ocean at 35.5 salinity: {TAopenocean:6f}") # 2293.114461

# slope = -27.52694780454991
# intercept = 3270.321108328358
# r = -0.782156085790011
# p = 1.988832102804454e-11
# se = 3.1651157480927976

ax=ax
# sns.regplot(x='salinity', y='alkalinity', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='TA', vmin=vmin, vmax=vmax)
sc = ax.scatter('salinity', 'predicted_alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='x', label='predicted TA', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity (μmol/kg)")
ax.set_title("TA and S data - North Sea")
ax.legend()
# ax.set_ylim([2275,2425])
# ax.set_xlim([31,35.5])

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/S_longterm/TApredicted_S_mean_scatter.png")
plt.show()

#%% # DIC difference

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['dic'])

print(f"DIC of rivers at 0 salinity: {intercept:6f}")
x = 35.5
DICopenocean = slope * x + intercept
print(f"DIC of open ocean at 35.5 salinity: {DICopenocean:6f}")

# slope = -25.704629890056953
# intercept = 2995.9684418250117
# r = -0.5333481113901318
# p = 6.661485828319392e-05
# se = 5.884327961010647

ax=ax
# sns.regplot(x='salinity', y='dic', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

sc = ax.scatter('salinity', 'dic', c='dayofyear', cmap='twilight', data=combinedmean, marker='o', label='DIC', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("DIC (μmol/kg)")
ax.set_title("DIC and S data - North Sea")
ax.legend()
ax.set_ylim([2000,2250])
ax.set_xlim([31,35.5])

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
#plt.savefig("figures/S_longterm/DIC_S_mean_scatter.png")
plt.show()

#%% # S vs time

fig, ax = plt.subplots(dpi=300)

# Predict TA
TAintercept = 3270.321108328358
TAslope = -27.52694780454991
combinedmean['predicted_alkalinity'] = (TAslope * combinedmean['salinity']) + TAintercept
RWSomean['predicted_alkalinity'] = (TAslope * RWSomean['salinity']) + TAintercept

# Predict DIC
DICintercept = 2995.9684418250117
DICslope = -25.704629890056953
combinedmean['predicted_dic'] = (DICslope * combinedmean['salinity']) + DICintercept
RWSomean['predicted_dic'] = (DICslope * RWSomean['salinity']) + DICintercept

ax=ax
# sc = ax.scatter('datenum', 'alkalinity', c='xkcd:velvet', data=combinedmean, label='Initial', marker='x')
# sc = ax.scatter('datenum', 'predicted_alkalinity', c='xkcd:velvet', data=combinedmean, label='Predicted')
#sc = ax.scatter('datenum', 'predicted_alkalinity', c='xkcd:aqua', data=RWSomean, label='RWSo')

#sc = ax.scatter('datenum', 'dic', c='xkcd:velvet', data=combinedmean, label='Initial', marker='x')
#sc = ax.scatter('datenum', 'predicted_dic', c='xkcd:velvet', data=combinedmean, label='Predicted')
#sc = ax.scatter('datenum', 'predicted_dic', c='xkcd:aqua', data=RWSomean, label='RWSo')

#sc = ax.scatter('datenum', 'predicted_pCO2', c='xkcd:aqua', data=RWSomean, label='RWSo')
sc = ax.scatter('datenum', 'predicted_fCO2', c='xkcd:aqua', data=RWSomean, label='RWSo')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO2")
ax.set_title("fCO2 sea (salinity box model) - North Sea")
ax.legend()
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("RWSo")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

plt.tight_layout()
#plt.savefig("figures/S_longterm/TA_mean_time_scatter_combined.png")
#plt.savefig("figures/S_longterm/fCO2_mean_time_scatter_RWSo.png")
plt.show()

#%% # With TA and DIC

# TA and DIC values (not normalized) - based on equation with salinity
# TA combined
# DIC combined

# TA = combinedmean['alkalinity']
# DIC = combinedmean['dic']

TA = RWSomean['predicted_alkalinity']
DIC = RWSomean['predicted_dic']
sal = RWSomean['salinity']
temp = RWSomean['temperature']
phos = RWSomean['total_phosphate']
sil = RWSomean['total_silicate']

kwargs = dict(
    par1 = TA,
    par2 = DIC,
    par1_type = 1,
    par2_type = 2,
    salinity = sal,
    temperature = temp,
    total_phosphate = phos, 
    total_silicate = sil,
    opt_k_carbonic = 4,  
    opt_k_bisulfate = 1  
    )

results = pyco2.sys(**kwargs)
results_boxmodel = pd.DataFrame.from_dict(results)
results_boxmodel['datetime'] =  RWSomean['datetime']
results_boxmodel['longitude'] =  RWSomean['longitude']
results_boxmodel['latitude'] =  RWSomean['latitude']
results_boxmodel['distance_to_shore'] =  RWSomean['distance_to_shore']
results_boxmodel['dayofyear'] =  RWSomean['dayofyear']
results_boxmodel['month'] =  RWSomean['month']
results_boxmodel['year'] =  RWSomean['year']
results_boxmodel['datenum'] =  RWSomean['datenum']

#%% # With TA and air pCO2

# TA and pCO2 
# TA combined (not normalized) - based on equation with salinity
# pCO2 Socat - seasonal function

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [0.006, 386, 162, 680], 
                           args=(socatnsairmean['datenum'], socatnsairmean['pCO2']))

RWSomean['predicted_pCO2'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

TA = RWSomean['predicted_alkalinity']
pCO2 = RWSomean['predicted_pCO2']
sal = RWSomean['salinity']
temp = RWSomean['temperature']
phos = RWSomean['total_phosphate']
sil = RWSomean['total_silicate']

kwargs = dict(
    par1 = TA,
    par2 = pCO2,
    par1_type = 1,
    par2_type = 4,
    salinity = sal,
    temperature = temp,
    total_phosphate = phos, 
    total_silicate = sil,
    opt_k_carbonic = 4,  
    opt_k_bisulfate = 1  
    )

results = pyco2.sys(**kwargs)
results_boxmodel2 = pd.DataFrame.from_dict(results)
results_boxmodel2 = results_boxmodel2.dropna(axis='rows', how='all', subset=['salinity'])
results_boxmodel2['datetime'] = RWSomean['datetime']
results_boxmodel2['longitude'] = RWSomean['longitude']
results_boxmodel2['latitude'] = RWSomean['latitude']
results_boxmodel2['distance_to_shore'] = RWSomean['distance_to_shore']
results_boxmodel2['dayofyear'] = RWSomean['dayofyear']
results_boxmodel2['month'] = RWSomean['month']
results_boxmodel2['year'] = RWSomean['year']
results_boxmodel2['datenum'] = RWSomean['datenum']

#%% # With TA and sea fCO2

# TA and pCO2 
# TA combined (not normalized) - based on equation with salinity
# fCO2 Socat - seasonal function

opt_result = least_squares(lsq_fco2_fit, [0.006, 600, 162, 680], 
                           args=(socatnsmean['datenum'], socatnsmean['fCO2']))

RWSomean['predicted_fCO2'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

TA = RWSomean['predicted_alkalinity']
fCO2 = RWSomean['predicted_fCO2']
sal = RWSomean['salinity']
temp = RWSomean['temperature']
phos = RWSomean['total_phosphate']
sil = RWSomean['total_silicate']

kwargs = dict(
    par1 = TA,
    par2 = fCO2,
    par1_type = 1,
    par2_type = 5,
    salinity = sal,
    temperature = temp,
    total_phosphate = phos, 
    total_silicate = sil,
    opt_k_carbonic = 4,  
    opt_k_bisulfate = 1  
    )

results = pyco2.sys(**kwargs)
results_boxmodel3 = pd.DataFrame.from_dict(results)
results_boxmodel3 = results_boxmodel3.dropna(axis='rows', how='all', subset=['pH_total'])
results_boxmodel3['datetime'] = RWSomean['datetime']
results_boxmodel3['longitude'] = RWSomean['longitude']
results_boxmodel3['latitude'] = RWSomean['latitude']
results_boxmodel3['distance_to_shore'] = RWSomean['distance_to_shore']
results_boxmodel3['dayofyear'] = RWSomean['dayofyear']
results_boxmodel3['month'] = RWSomean['month']
results_boxmodel3['year'] = RWSomean['year']
results_boxmodel3['datenum'] = RWSomean['datenum']

#%% # pH based on TA & DIC - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datetime', 'pH_total', c='xkcd:aqua', data=RWSomean, label='pH$_{initial RWSo}$', s=20, alpha=0.4)
ax.scatter('datetime', 'pH_total_out', c='xkcd:dark orange', data=RWSnmean_out, label='pH$_{spectro RWSn}$', s=20, alpha=0.4)
# TA & DIC RWSo
ax.scatter('datetime', 'pH_total', c='xkcd:dark aqua', data=results_boxmodel, label='TA&DIC$_{predicted RWSo}$', s=20, alpha=0.4)
# pCO2 air RWSo
ax.scatter('datetime', 'pH_total', c='xkcd:black', data=results_boxmodel2, label='TA&pCO2air$_{predicted RWSo}$', s=20, alpha=0.4)
# fCO2 sea RWSo
ax.scatter('datetime', 'pH_total', c='xkcd:goldenrod', data=results_boxmodel3, label='TA&fCO2sea$_{predicted RWSo}$', s=20, alpha=0.4)

# Combined
# ax.scatter('datetime', 'pH_total', c='xkcd:velvet', data=results_boxmodel, label='TA&DIC$_{initial}$', s=20, alpha=0.4)
# #ax.scatter('datetime', 'pH_total', c='xkcd:velvet', data=results_boxmodel, label='TA&DIC$_{pred}$', s=20, alpha=0.4)
# ax.scatter('datetime', 'pH_total', c='xkcd:black', data=results_boxmodel2, label='TA&pCO2air$_{pred}$', s=20, alpha=0.4)
# ax.scatter('datetime', 'pH_total', c='xkcd:goldenrod', data=results_boxmodel3, label='TA&fCO2sea$_{pred}$', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_ylabel("pH (total scale)")
ax.set_ylim([7.25, 8.5])
ax.set_xlabel("Time (yrs)")
ax.set_xlim([10950,19000])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('RWSo pH data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/S_longterm/pH_mean_time_datasets_RWSo&RWSnspectro&RWSopred3_zoomin.png")
plt.show()


#%% # Interpolation of Salinity RWSomean

# L = RWSomean.year > 2000
# RWSomean = RWSomean[L]
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['salinity'])
slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['salinity'])

def fco2_fit(coeffs, datenum):
    slope, intercept, sine_stretch, sine_shift = coeffs
    fco2 = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    return fco2

def lsq_fco2_fit(coeffs, datenum, fco2):
    return fco2_fit(coeffs, datenum) - fco2

opt_result = least_squares(lsq_fco2_fit, [slope, intercept, sine_stretch, sine_shift], 
                           args=(RWSomean['datenum'], RWSomean['salinity']))

RWSomean['seasoncycle'] = fco2_fit(opt_result['x'], RWSomean['datenum'])

# Fitted values:
slope, intercept, sine_stretch, sine_shift = opt_result['x']

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='salinity', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:golden"}, line_kws={"color": "blue"})

ax.set_title("RWSo Salinity data - North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Salinity')
# ax.set_ylim(200, 550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

ax = axs[1]
RWSomean.plot.scatter("datenum", "salinity", ax=ax, c='xkcd:golden', label='RWSo S')

fx = np.linspace(RWSomean.datenum.min(), RWSomean.datenum.max(), 1000)
fy = fco2_fit(opt_result['x'], fx)
fx_datetime = mdates.num2date(fx)
ax.plot(fx, fy, 'g') # fy + 55.61 is the difference between the orange line and blue line (start point -> date 1991-11-30)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Salinity')
#ax.set_ylim(200,550)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)
ax.legend()

# Minus the sin cycle trend and the long-term trend
RWSomean['minusseasonality'] = RWSomean['salinity'] - RWSomean['seasoncycle']

ax = axs[2]
#RWSomean.plot.scatter("datetime", "minusseasonality", ax=ax)
sns.regplot(x='datenum', y='minusseasonality', data=RWSomean, ax=ax, ci=99.9,
            scatter_kws={"color": "xkcd:golden"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Salinity')
#ax.set_ylim(-200,200)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
# ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("figures/S_longterm/S_season_fitting_RWSomean.png")    

# Use the fit to predict fCO2 in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)


#%% # Outcome linear regression

#slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['salinity'])

slope, intercept, r, p, se = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])

result = linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(result.intercept, result.intercept_stderr)

res = stats.linregress(RWSomean['datenum'], RWSomean['minusseasonality'])
print(f"R-squared: {res.rvalue**2:.6f}")

# Seasonal corrected DIC data
# slope = -2.455358405858721e-12
# intercept = 3.654470315155289e-08
# result.intercept_stderr = 0.3754383349050931
# r = -6.6915564314539875e-09
# p = 0.9999999230910491
# se = 2.5442283187118627e-05
# R-squared = 0

#%% # Seasonal corrected S LONG TERM CHANGE

# S data (2001-2021) LONG TERM CHANGE RWSo
xbegin = 11353
xend = 17876

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # -1.601630288141644e-08 (μmol/kg)
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # -8.962058181384332e-10 (μmol/kg)
