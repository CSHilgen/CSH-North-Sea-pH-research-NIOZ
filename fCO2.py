# fCO2

#%% # pfxCO2 - Datasets

fig, axs = plt.subplots(dpi=300, nrows=3)

ax = axs[0]
glodapnsmean.plot.scatter("datetime", "pCO2", c="b", ax=ax, s=20, alpha=0.4, label='GLODAP')
#mssmean.plot.scatter('datetime', 'pCO2', c='xkcd:velvet', ax=ax alpha=0.4, label="MSS")
Cefasmean.plot.scatter('datetime', 'pCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4, label='Cefas')
D366mean.plot.scatter('datetime', 'pCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4, label='D366')
RWSnmean.plot.scatter('datetime', 'pCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4, label='RWSn')
socatnsmean.plot.scatter('datetime', 'pCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4, label='SOCAT')
socatnsairmean.plot.scatter('datetime', 'pCO2', c='black', ax=ax, s=20, alpha=0.4, label='Atmosphere')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("pCO$_2$ (ppm)")
ax.set_ylim([0, 700])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('pCO$_2$, fCO$_2$, and xCO$_2$ data - Datasets North Sea')

ax = axs[1]
glodapnsmean.plot.scatter("datetime", "fCO2", c="b", ax=ax, s=20, alpha=0.4)#, label='GLODAP')
#mssmean.plot.scatter('datetime', 'fCO2', c='xkcd:velvet', ax=ax, label="MSS")
Cefasmean.plot.scatter('datetime', 'fCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4)#, label='Cefas')
D366mean.plot.scatter('datetime', 'fCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4)#, label='D366')
RWSnmean.plot.scatter('datetime', 'fCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4)#, label='RWSn')
socatnsmean.plot.scatter('datetime', 'fCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4)#, label='SOCAT')
socatnsairmean.plot.scatter('datetime', 'fCO2', c='black', ax=ax, s=20, alpha=0.4)#, label='Atmosphere')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.set_ylim([0, 700])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

ax = axs[2]
glodapnsmean.plot.scatter("datetime", "xCO2", c="b", ax=ax, s=20, alpha=0.4)#, label='GLODAP')
#mssmean.plot.scatter('datetime', 'xCO2', c='xkcd:velvet', ax=ax, alpha=0.4)#label="MSS")
Cefasmean.plot.scatter('datetime', 'xCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4)#, label='Cefas')
D366mean.plot.scatter('datetime', 'xCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4)#, label='D366')
RWSnmean.plot.scatter('datetime', 'xCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4)#, label='RWSn')
socatnsmean.plot.scatter('datetime', 'xCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4)#, label='SOCAT')
socatnsairmean.plot.scatter('datetime', 'xCO2', c='black', ax=ax, s=20, alpha=0.4)#, label='Atmosphere')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("xCO$_2$ (uatm)")
ax.set_ylim([0, 700])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/pfxCO2_mean_datasets.png")
plt.show()

#%% # SOCAT pfxCO2 sea water and air - Dataset & seasons

fig, axs = plt.subplots(dpi=300, nrows=3)
cm = plt.cm.get_cmap('twilight')

ax = axs[0]
ax.scatter('datetime', 'fCO2', c='xkcd:aqua', data=socatnsmean, s=20, alpha=0.4, label='SOCAT')
ax.scatter('datetime', 'fCO2', c='black', data=socatnsairmean, s=20, alpha=0.4, label='Atmosphere')
ax.set_title("fCO$_2$ SOCAT data - North Sea")

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
#ax.set_ylim([100, 550])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title('Dataset')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

ax = axs[1]
seasonplotsea = ax.scatter('datetime', 'fCO2', c='dayofyear', 
                         cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)#, label='SOCAT')

cbar = plt.colorbar(seasonplotsea, ax=ax)
cbar.set_label('Day of year')
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ sea (uatm)")
#ax.set_ylim([100, 550])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

ax = axs[2]
seasonplotsea = ax.scatter('datetime', 'fCO2', c='dayofyear', 
                         cmap=cm, vmin=1, vmax=365, data=socatnsairmean, s=20)#, label='SOCAT')

cbar = plt.colorbar(seasonplotsea, ax=ax)
cbar.set_label('Day of year')
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ air (uatm)")
#ax.set_ylim([300, 450])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("figures/pfxCO2_mean_socat.png")
plt.show()

#%% # fCO2 - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
glodapnsmean.plot.scatter("datetime", "fCO2", c="b", ax=ax, s=20, alpha=0.4, label='GLODAP')
#mssmean.plot.scatter('datetime', 'fCO2', c='xkcd:velvet', ax=ax alpha=0.4, label="MSS")
Cefasmean.plot.scatter('datetime', 'fCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4, label='Cefas')
D366mean.plot.scatter('datetime', 'fCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4, label='D366')
RWSnmean.plot.scatter('datetime', 'fCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4, label='RWSn')
socatnsmean.plot.scatter('datetime', 'fCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4, label='SOCAT')
socatnsairmean.plot.scatter('datetime', 'fCO2', c='black', ax=ax, s=20, alpha=0.4, label='Atmosphere')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.set_ylim([0, 700])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_mean_datasets.png")
plt.show()

#%% # fCO2 sea - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
socatnsmean.plot.scatter('datetime', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)#, label='SOCAT')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ sea (uatm)")
#ax.set_ylim([100, 550])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('SOCAT fCO$_2$ sea data - Seasons North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_sea_mean_seasons.png")
plt.show()

#%% # fCO2 air - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
socatnsairmean.plot.scatter('datetime', 'fCO2', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)#, label='Atmosphere')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ air (uatm)")
#ax.set_ylim([300, 450])
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('SOCAT fCO$_2$ air data - Seasons North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_air_mean_seasons.png")
plt.show()

#%% # Socatnsmean fCO2 sea water data - Regions

x = socatnsmean['datetime']
y = socatnsmean['fCO2']

#Choose different method periods
L0 = (socatnsmean['distance_to_shore'] > 0) & (socatnsmean['distance_to_shore'] <=4)
L1 = (socatnsmean['distance_to_shore'] > 4) & (socatnsmean['distance_to_shore'] <=10)
L2 = (socatnsmean['distance_to_shore'] > 10) & (socatnsmean['distance_to_shore'] <=20)
L3 = (socatnsmean['distance_to_shore'] > 20) & (socatnsmean['distance_to_shore'] <=30)
L4 = (socatnsmean['distance_to_shore'] > 30) & (socatnsmean['distance_to_shore'] <=50)
L5 = (socatnsmean['distance_to_shore'] > 50) & (socatnsmean['distance_to_shore'] <=70)
L6 = (socatnsmean['distance_to_shore'] > 70) & (socatnsmean['distance_to_shore'] <=100)
L7 = (socatnsmean['distance_to_shore'] > 100) & (socatnsmean['distance_to_shore'] <=150)
L8 = (socatnsmean['distance_to_shore'] > 150) & (socatnsmean['distance_to_shore'] <=200)
L9 = (socatnsmean['distance_to_shore'] > 200) & (socatnsmean['distance_to_shore'] <=250)
L10 = (socatnsmean['distance_to_shore'] > 250) & (socatnsmean['distance_to_shore'] <=300)

fig, ax = plt.subplots(dpi=300)
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
ax.set_ylabel('fCO$_2$ (uatm)')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('SOCAT fCO$_2$ sea data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_sea_mean_regions.png")
plt.show()


#%% # Socatnsmean fCO2 air data - Regions

x = socatnsairmean['datetime']
y = socatnsairmean['fCO2']

#Choose different method periods
L0 = (socatnsairmean['distance_to_shore'] > 0) & (socatnsairmean['distance_to_shore'] <=4)
L1 = (socatnsairmean['distance_to_shore'] > 4) & (socatnsairmean['distance_to_shore'] <=10)
L2 = (socatnsairmean['distance_to_shore'] > 10) & (socatnsairmean['distance_to_shore'] <=20)
L3 = (socatnsairmean['distance_to_shore'] > 20) & (socatnsairmean['distance_to_shore'] <=30)
L4 = (socatnsairmean['distance_to_shore'] > 30) & (socatnsairmean['distance_to_shore'] <=50)
L5 = (socatnsairmean['distance_to_shore'] > 50) & (socatnsairmean['distance_to_shore'] <=70)
L6 = (socatnsairmean['distance_to_shore'] > 70) & (socatnsairmean['distance_to_shore'] <=100)
L7 = (socatnsairmean['distance_to_shore'] > 100) & (socatnsairmean['distance_to_shore'] <=150)
L8 = (socatnsairmean['distance_to_shore'] > 150) & (socatnsairmean['distance_to_shore'] <=200)
L9 = (socatnsairmean['distance_to_shore'] > 200) & (socatnsairmean['distance_to_shore'] <=250)
L10 = (socatnsairmean['distance_to_shore'] > 250) & (socatnsairmean['distance_to_shore'] <=300)

fig, ax = plt.subplots(dpi=300)
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
ax.set_ylabel('fCO$_2$ (uatm)')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('SOCAT fCO$_2$ air data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_air_mean_regions.png")
plt.show()

