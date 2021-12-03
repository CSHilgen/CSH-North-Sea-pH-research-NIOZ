# TA normalization - long term trend

#%% # Equation (2) of paper Friis et al. 2003

# # Take the salinity mean of combined dataset
# csalinitymean = combinedmean['salinity'].mean()
# print(csalinitymean) # Result is 33.31298717967724 

# Take the salinity mean of only the RWSo dataset
salinitymean = RWSomean['salinity'].mean()
print(salinitymean) # Result is 32.86875624846805 

# Salinity endmember (intercept) is 3261.75288288982 (for TA - derived below)
salendmember = 3270.321108328358 # Previous value was 3261.75288288982
resultscombined['normalized_TA'] = (((resultscombined['alkalinity'] - salendmember) / 
                                 resultscombined['salinity']) * salinitymean) + salendmember

resultscombined['salinityeffect_TA'] = resultscombined['alkalinity'] - resultscombined['normalized_TA']

combinedmean['normalized_TA'] = (((combinedmean['alkalinity'] - salendmember) / 
                                 combinedmean['salinity']) * salinitymean) + salendmember

combinedmean['salinityeffect_TA'] = combinedmean['alkalinity'] - combinedmean['normalized_TA']

#%% # TA normalized to salinity

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

ax=ax
#sc = ax.scatter('datetime','normalized_TA', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)
#sc = ax.scatter('datetime','alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)
sc = ax.scatter('datetime','salinityeffect_TA', c='dayofyear', cmap='twilight', data=combinedmean, vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
#ax.set_title("TA data - Normalized to salinity North Sea")
#ax.set_title("TA data - Seasons North Sea")
ax.set_title("TA data minus normalized to salinity North Sea")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
#ax.set_ylim([2275,2425])
ax.set_ylim([-100,100])
ax.yaxis.set_minor_locator(MultipleLocator(10))
plt.grid(b=True, which='minor', axis='both', color='grey', linestyle='-', alpha=0.1)
plt.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
#plt.savefig("figures/TA_longterm/TA_mean_normalized.png")
#plt.savefig("figures/TA_longterm/TA_mean_seasons.png")
plt.savefig("figures/TA_longterm/TA_mean_salinityeffect.png")
plt.show()

#%% # (Normalized) TA vs salinity

fig, ax = plt.subplots(dpi=300)

vmin = 1
vmax = 365

ax=ax
#sns.regplot(x='salinity', y='alkalinity', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])
print(intercept) # 3270.321108328358
nslope, nintercept, nr, np, nse = linregress(combinedmean['salinity'], combinedmean['normalized_TA'])
print(nintercept) # 2360.0596984702515
#plt.plot(0, intercept, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

sc = ax.scatter('salinity', 'normalized_TA', c='dayofyear', cmap='twilight', data=combinedmean, marker='X', label='TA normalized', vmin=vmin, vmax=vmax)
sc = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='TA', vmin=vmin, vmax=vmax)

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA and S data - Normalization to salinity North Sea")
ax.legend()
# ax.set_ylim([2300,3300])
# ax.set_xlim([-10,35])
ax.set_ylim([2275,2425])
ax.set_xlim([31,35.5])

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
#plt.savefig("figures/TA_longterm/TA_S_mean_normalized_scatter.png")
plt.show()

#%% # Interpolation of TA (combined = D366, Cefas, RWSn, Glodap)

fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

ax = axs[0]
sns.regplot(x='datenum', y='alkalinity', data=combinedmean, ax=ax,
            scatter_kws={"color": "red"}, line_kws={"color": "blue"})

ax.set_title("TA - Fitting North Sea")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Alkalinity')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2275,2425])

ax = axs[1]
combinedmean.plot.scatter("datenum", "alkalinity", ax=ax, c='red', label='TA data')
combinedmean.plot.scatter('datenum', 'normalized_TA', ax=ax, c='g', label='Normalized TA data')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Alkalinity')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2275,2425])

ax = axs[2]
sns.regplot(x='datenum', y='normalized_TA', data=combinedmean, ax=ax, ci=99.9,
            scatter_kws={"color": "g"}, line_kws={"color": "blue"})

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel('Normalized TA')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xticks(rotation=0)
ax.set_ylim([2275,2425])

plt.tight_layout()
plt.savefig("figures/TA_longterm/TA_normalization_fitting.png")    
plt.show()

#%% # Outcomes linear regression

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['alkalinity'])
nslope, nintercept, nr, np, nse = linregress(combinedmean['datenum'], combinedmean['normalized_TA'])

# result = linregress(combinedmean['datenum'], combinedmean['normalized_TA'])
# print(result.intercept, result.intercept_stderr)

# res = stats.linregress(combinedmean['datenum'], combinedmean['normalized_TA'])
# print(f"R-squared: {res.rvalue**2:.6f}")

# TA data
# slope = 0.010172145030777145
# intercept = 2181.8098149428274
# intercept_stderr = 26.405629560215093
# r = 0.6870900774656917
# p = 3.5824949535774576e-08
# se = 0.0015525909530880388
# R-squared = 0.472093

# TA LONG TERM CHANGE
xbegin = 11565
xend = 18808

ybegin = (slope * xbegin) + intercept
yend = (slope * xend) + intercept
changelongterm = yend - ybegin
print(changelongterm) # 73.6768464579186 umol/kg
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 3.712832936233645 umol/kg

# # Normalized TA data
# nslope = 0.0022295609566250975 (m)
# nintercept = 2327.9489285374557 (b)
# nintercept_stderr = 21.96225661286377
# nr = 0.2418118823823207
# np = 0.0906782590781297
# nse = 0.001291330731152334
# R-squared = 0.058473

# Normalized TA LONG TERM CHANGE
xbegin = 11565
xend = 18808

ybegin = (nslope * xbegin) + nintercept
yend = (nslope * xend) + nintercept
changelongterm = yend - ybegin
print(changelongterm) # 16.14871000883568 umol/kg
changeperyear = changelongterm / ((xend-xbegin)/365)
print(changeperyear) # 0.8137897491681655 umol/kg