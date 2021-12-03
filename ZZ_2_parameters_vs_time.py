# Same x axis different y axis - plots with different parameters

#%% # DIC & TA - Datasets & Seasons

fig, axs = plt.subplots(dpi=300, nrows=2)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
glodapnsmean.plot.scatter("datetime", "dic", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
#mssmean.plot.scatter('datetime', 'dic', c='xkcd:velvet', ax=ax, label="MSS", s=20, alpha=0.4)
Cefasmean.plot.scatter('datetime', 'dic', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
D366mean.plot.scatter('datetime', 'dic', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
RWSnmean.plot.scatter('datetime', 'dic', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
#sc = combinedmean.plot.scatter("datetime", "dic", c="dayofyear", cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("DIC")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.set_title('DIC and TA data - Datasets North Sea')
#ax.set_title('DIC and TA data - Seasons North Sea')

ax = axs[1]
glodapnsmean.plot.scatter("datetime", "alkalinity", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
#mssmean.plot.scatter('datetime', 'alkalinity', c='xkcd:velvet', ax=ax, label="MSS", s=20, alpha=0.4)
Cefasmean.plot.scatter('datetime', 'alkalinity', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
D366mean.plot.scatter('datetime', 'alkalinity', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
RWSnmean.plot.scatter('datetime', 'alkalinity', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
#scc = combinedmean.plot.scatter('datetime', 'alkalinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Total alkalinity")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
#plt.xticks(rotation=45)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("figures/DIC_TA_mean_datetime_datasets.png")
#plt.savefig("figures/DIC_TA_mean_datetime_seasons.png")
plt.show()

#%% # pH, salinity and temperature - Datasets & Seasons

fig, axs = plt.subplots(dpi=300, nrows=4, sharex=True)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
#RWSomean.plot.scatter('datetime', 'pH_total', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)
RWSomean.plot.scatter('datetime', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("pH - RWSo")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.set_title('pH, T, and sal data - Seasons')

ax = axs[1]
# glodapnsmean.plot.scatter("datetime", "pH_total", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
# #mssmean.plot.scatter('datetime', 'pH_total', c='xkcd:velvet', ax=ax, label="MSS")
# Cefasmean.plot.scatter('datetime', 'pH_total', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
# D366mean.plot.scatter('datetime', 'pH_total', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
# RWSnmean.plot.scatter('datetime', 'pH_total', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
sc = combinedmean.plot.scatter('datetime', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("pH")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)

ax = axs[2]
# glodapnsmean.plot.scatter("datetime", "temperature", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
# #mssmean.plot.scatter('datetime', 'temperature', c='xkcd:velvet', ax=ax, label="MSS")
# Cefasmean.plot.scatter('datetime', 'temperature', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
# D366mean.plot.scatter('datetime', 'temperature', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
# RWSnmean.plot.scatter('datetime', 'temperature', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
scc = combinedmean.plot.scatter('datetime', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Temperature (℃)")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)

ax = axs[3]
# glodapnsmean.plot.scatter("datetime", "salinity", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
# #mssmean.plot.scatter('datetime', 'salinity', c='xkcd:velvet', ax=ax, label="MSS")
# Cefasmean.plot.scatter('datetime', 'salinity', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
# D366mean.plot.scatter('datetime', 'salinity', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
# RWSnmean.plot.scatter('datetime', 'salinity', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
sccc = combinedmean.plot.scatter('datetime', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Salinity")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.set_axisbelow(True) # not working!!

plt.tight_layout()
#plt.savefig("figures/pHsaltemp_mean_datasets.png")
plt.savefig("figures/pHsaltemp_mean_seasons.png")
plt.show()

#%% # Salinity and temperature - Datasets & Seasons

fig, axs = plt.subplots(dpi=300, nrows=4, sharex=True)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
#RWSomean.plot.scatter('datetime', 'temperature', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)
RWSomean.plot.scatter('datetime', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("T (℃) - RWSo")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.set_title('T and sal data - Seasons')

ax = axs[1]
# glodapnsmean.plot.scatter("datetime", "temperature", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
# #mssmean.plot.scatter('datetime', 'temperature', c='xkcd:velvet', ax=ax, label="MSS")
# Cefasmean.plot.scatter('datetime', 'temperature', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
# D366mean.plot.scatter('datetime', 'temperature', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
# RWSnmean.plot.scatter('datetime', 'temperature', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
scc = combinedmean.plot.scatter('datetime', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("T (℃)")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)

ax = axs[2]
#RWSomean.plot.scatter('datetime', 'salinity', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)
RWSomean.plot.scatter('datetime', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("S - RWSo")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)

ax = axs[3]
# glodapnsmean.plot.scatter("datetime", "salinity", c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)
# #mssmean.plot.scatter('datetime', 'salinity', c='xkcd:velvet', ax=ax, label="MSS")
# Cefasmean.plot.scatter('datetime', 'salinity', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)
# D366mean.plot.scatter('datetime', 'salinity', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)
# RWSnmean.plot.scatter('datetime', 'salinity', c='xkcd:dark orange', ax=ax, label='RWSn', s=20, alpha=0.4)
sccc = combinedmean.plot.scatter('datetime', 'salinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Salinity")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)

plt.tight_layout()
#plt.savefig("figures/Saltemp_mean_datasets.png")
plt.savefig("figures/Saltemp_mean_seasons.png")
plt.show()

#%% # DIC & TA - Regions

x = combinedmean['datetime']
y = combinedmean['dic']
z = combinedmean['alkalinity']

#Choose different method periods
L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('DIC')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('DIC and TA data - Regions North Sea')

ax=axs[1]
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Total alkalinity')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.get_legend().set_title("Km distance to shore")
#ax.set_axisbelow(True)

# plt.tight_layout()
plt.savefig("figures/DIC_TA_regions_distance_to_shore.png")
plt.show()

#%% # Temperature & salinity - Regions

x = combinedmean['datetime']
y = combinedmean['temperature']
z = combinedmean['salinity']

#Choose different method periods
L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

fig, axs = plt.subplots(dpi=300, nrows=2)

ax=axs[0]
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Temperature (℃)')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=45)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('T and S data - Regions North Sea')

ax=axs[1]
ax.scatter(x[L0], z[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], z[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], z[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], z[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], z[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], z[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], z[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], z[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], z[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], z[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], z[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('Salinity')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.get_legend().set_title("Km distance to shore")
#ax.set_axisbelow(True)

# plt.tight_layout()
plt.savefig("figures/Saltemp_regions_distance_to_shore.png")
plt.show()
