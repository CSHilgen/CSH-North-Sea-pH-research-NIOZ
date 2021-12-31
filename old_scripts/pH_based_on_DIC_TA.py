#%% # With TA and DIC

# TA and DIC values 
# TA combined (normalized)
# DIC combined (normalized & seasonal corrected)

TA = combinedmean['normalized_TA']
DIC = combinedmeandic2['dic_final2']
sal = combinedmean['salinity']
temp = combinedmean['temperature']
phos = combinedmean['total_phosphate']
sil = combinedmean['total_silicate']

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
NDICTA = pd.DataFrame.from_dict(results)
NDICTA['datetime'] =  combinedmean['datetime']
NDICTA['longitude'] =  combinedmean['longitude']
NDICTA['latitude'] =  combinedmean['latitude']
NDICTA['distance_to_shore'] =  combinedmean['distance_to_shore']
NDICTA['dayofyear'] =  combinedmean['dayofyear']
NDICTA['month'] =  combinedmean['month']
NDICTA['year'] =  combinedmean['year']
NDICTA['datenum'] =  combinedmean['datenum']

#%% # pH - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datenum', 'pH_total', c='xkcd:aqua', data=RWSomean, label='RWSo$_{initial}$', s=20, alpha=0.4)
ax.scatter('datenum', 'pH_total_out', c='xkcd:dark orange', data=RWSnmean_out, label='RWSn$_{spectro}$', s=20, alpha=0.4)
ax.scatter('datenum', 'pH_total', c='xkcd:velvet', data=NDICTA, label='Combined$_{DIC&TA}$', s=20, alpha=0.4)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_xlim(10950, 19000)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
# ax.set_title('pH RWSo data - Datasets North Sea') 
ax.set_title('pH data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_time_datasets_NDICTA.png")
plt.show()

#%% # pH - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('datetime', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
#sc = ax.scatter('datetime', 'pH_total_out', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSnmean_out, s=20)
#sc = ax.scatter('datenum', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=NDICTA, s=20)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_xlim(10950, 19000)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Seasons North Sea') 

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/pH_mean_time_seasons_NDICTA2.png")
plt.show()