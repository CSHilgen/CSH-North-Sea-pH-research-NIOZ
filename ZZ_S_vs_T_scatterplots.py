# S vs T scatterplots

#%% # S vs T scatter plots based all points or mean - Glodap, D366, Socat, RWSn

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)

ax = axs[0,0]
#sc = ax.scatter('salinity', 'temperature',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsglodapns, edgecolor=None, alpha=0.3)
#sc = ax.scatter('salinity', 'temperature',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=glodapnsmean, edgecolor='black')
sc = ax.scatter('salinity', 'temperature',  c="b", data=resultsglodapns, label='GLODAP', s=20, alpha=0.4)

ax.set_title('Glodap')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Sp', 'Su', 'A', 'W'])

ax = axs[1,0]
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultssocatns, edgecolor=None, alpha=0.3)
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=socatnsmean, edgecolor='black')
sc = ax.scatter('salinity', 'temperature', c='xkcd:goldenrod', data=resultssocatns, label='Socat', s=20, alpha=0.4)

ax.set_title('Socat')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Sp', 'Su', 'A', 'W'])

ax = axs[0,1]
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsD366, edgecolor=None, alpha=0.3)
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=D366mean, edgecolor='black')
sc = ax.scatter('salinity', 'temperature', c='xkcd:pink', data=resultsD366, label='D366', s=20, alpha=0.4)

ax.set_title('D366')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Sp', 'Su', 'A', 'W'])

ax = axs[1,1]
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsRWSn, s=35, edgecolor=None, alpha=0.3)
#sc = ax.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=RWSnmean, s=35, edgecolor='black')
sc = ax.scatter('salinity', 'temperature', c='xkcd:dark orange', data=resultsRWSn, label='RWS', s=20, alpha=0.4)

ax.set_title('RWSn')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature (°C)")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Sp', 'Su', 'A', 'W'])

plt.tight_layout()
#plt.savefig("figures/Sal_Temp_plots_scatter_allpoints_dayofyear.png")
#plt.savefig("figures/Sal_Temp_plots_scatter_mean_dayofyear.png")
plt.savefig("figures/Sal_Temp_plots_scatter_allpoints_datasets.png")
plt.show()

#%% # S vs T scatter plots based all points or mean - Glodap, D366, Socat, RWSn

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

sc= ax.scatter(RWSomean['salinity'], RWSomean['temperature'], c=RWSomean['dayofyear'], vmin=0, vmax=365, s=35, cmap=cm, edgecolor="None")

cbar=fig.colorbar(sc,ax=ax, orientation='horizontal')

cbar.set_label('Seasons')
# cbar.outline.set_edgecolor('Grey')
label=[79,173,265,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['', '', '', ''])

spx=108
y=135
cbar.ax.text(spx,y, 'spring')
sux=200
y=135
cbar.ax.text(sux,y, 'summer')
sx=290
y=135
cbar.ax.text(sx,y, 'autumn')
sx=10
y=135
cbar.ax.text(sx,y, 'winter')

ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature (°C)")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])
ax.set_title('RWSo S & T data - mean')

plt.tight_layout()
plt.savefig("figures/Sal_Temp_plots_scatter_mean_dayofyear_RWSo.png")
plt.show()
