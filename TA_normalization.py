from scipy import stats
# TA normalization

#%% # Equation (2) of paper Friis et al. 2003

csalinitymean = combinedmean['salinity'].mean()
print(csalinitymean)

combinedmean['normalized_TA'] = (((combinedmean['alkalinity'] - 3261.75288288982) / 
                                 combinedmean['salinity']) * csalinitymean) + 3261.75288288982

combinedmean['salinityeffect_TA'] = combinedmean['alkalinity'] - combinedmean['normalized_TA']

#%% # TA normalized to salinity

fig, ax = plt.subplots(dpi=300)

ax=ax
# At = ax.scatter('datetime','normalized_TA', c='dayofyear', cmap='twilight', data=combinedmean)
# At = ax.scatter('datetime','alkalinity', c='dayofyear', cmap='twilight', data=combinedmean)
At = ax.scatter('datetime','salinityeffect_TA', c='dayofyear', cmap='twilight', data=combinedmean)

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
# ax.set_title("TA data - Normalized to salinity North Sea")
# ax.set_title("TA data - Seasons North Sea")
ax.set_title("TA data minus normalized to salinity North Sea")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
#ax.set_ylim([2280,2420])
ax.set_ylim([-100,100])

plt.tight_layout()
# plt.savefig("figures/DIC_TA_fitting/TA_mean_normalized.png")
# plt.savefig("figures/DIC_TA_fitting/TA_mean_seasons.png")
plt.savefig("figures/DIC_TA_fitting/TA_mean_salinityeffect.png")
plt.show()

#%% # (Normalized) TA vs salinity

fig, ax = plt.subplots(dpi=300)

ax=ax
# ax = sns.regplot(x='salinity', y='alkalinity', data=combinedmean, ax=ax,
#             scatter_kws={"color": "purple"}, line_kws={"color": "blue"})

# c = 0
# w = 3261.752
# slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])
# plt.plot(c, w, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

At = ax.scatter('salinity', 'normalized_TA', c='dayofyear', cmap='twilight', data=combinedmean, marker='X', label='TA normalized')
At = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='TA')

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA and S data - Normalization to salinity North Sea")
ax.legend()
ax.set_ylim([2280,2420])

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_S_mean_normalized_scatter.png")
plt.show()

#%% # Equation (1) of paper Friis et al. 2003: TRADITIONALLY

combinedmean['normalized_TA_t'] = ((combinedmean['alkalinity'] / 
                                 combinedmean['salinity']) * csalinitymean)

combinedmean['salinityeffect_TA_t'] = combinedmean['alkalinity'] - combinedmean['normalized_TA_t']

#%% # TA normalized to salinity TRADITIONALLY

fig, ax = plt.subplots(dpi=300)

ax=ax
At = ax.scatter('datetime','normalized_TA_t', c='dayofyear', cmap='twilight', data=combinedmean)
#At = ax.scatter('datetime','alkalinity', c='dayofyear', cmap='twilight', data=combinedmean)
#At = ax.scatter('datetime','salinityeffect_TA_t', c='dayofyear', cmap='twilight', data=combinedmean)

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA data - Normalized to salinity (traditionally) North Sea")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_mean_normalized_t.png")
plt.show()

#%% # (Normalized) TA vs salinity TRADITIONALLY

fig, ax = plt.subplots(dpi=300)

ax=ax
At = ax.scatter('salinity', 'normalized_TA_t', c='dayofyear', cmap='twilight', data=combinedmean, marker='X', label='TA normalized')
At = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap='twilight', data=combinedmean, marker='v', label='TA')

cbar = plt.colorbar(At)
cbar.set_label("Day of year")
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Total alkalinity")
ax.set_title("TA and S data - Normalization to salinity (traditionally) North Sea")
ax.legend()

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_S_mean_normalized_t_scatter.png")
plt.show()

#%% # Interpolation of TA (combined = D366, Cefas, RWSn, Glodap)

slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['alkalinity'])

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
# ax.get_legend().remove()

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

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_normalization_fitting.png")    

# Use the fit to predict DIC in console: fco2_fit(opt_result['x'], 1)
# Last number is date (1 = 1 january 1970)
