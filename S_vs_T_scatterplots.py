# S vs T scatterplots

#%% # S vs T scatter plots based all points or mean - Glodap, D366, Socat, RWSn

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)

ax = axs[0,0]
resultsglodapns.plot.scatter('salinity', 'temperature',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor=None, alpha=0.3)
#glodapnsmean.plot.scatter('salinity', 'temperature',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultsglodapns.plot.scatter('salinity', 'temperature',  c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)

ax.set_title('Glodap')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[1,0]
resultssocatns.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor=None, alpha=0.3)
#socatnsmean.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultssocatns.plot.scatter('salinity', 'temperature', c='xkcd:goldenrod', ax=ax, label='Socat', s=20, alpha=0.4)

ax.set_title('Socat')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[0,1]
resultsD366.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor=None, alpha=0.3)
#D366mean.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultsD366.plot.scatter('salinity', 'temperature', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)

ax.set_title('D366')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[1,1]
resultsRWSn.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, s=35, edgecolor=None, alpha=0.3)
#RWSnmean.plot.scatter('salinity', 'temperature', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, s=35, edgecolor='black')
#resultsRWSn.plot.scatter('salinity', 'temperature', c='xkcd:dark orange', ax=ax, label='RWS', s=20, alpha=0.4)

ax.set_title('RWSn')
ax.grid(alpha=0.3)
ax.set_xlabel("Salinity")
ax.set_ylabel("Temperature (°C)")
ax.set_xlim([25, 36])
ax.set_ylim([0, 25])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
#plt.savefig("figures/Sal_Temp_plots_scatter_allpoints_dayofyear.png")
#plt.savefig("figures/Sal_Temp_plots_scatter_mean_dayofyear.png")
#plt.savefig("figures/Sal_Temp_plots_scatter_allpoints_datasets.png")
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
ax.set_xlim([26, 36])
ax.set_ylim([0, 25])
ax.set_title('RWSo S & T data - mean')

plt.tight_layout()
#plt.savefig("figures/Sal_Temp_plots_scatter_mean_dayofyear_RWSo.png")
plt.show()
