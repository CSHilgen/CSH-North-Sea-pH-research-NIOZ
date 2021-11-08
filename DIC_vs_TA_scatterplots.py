# DIC vs TA scatterplots

#%% # DIC vs TA scatter plots based all points or mean

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)

ax = axs[0,0]
#resultsglodapns.plot.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
glodapnsmean.plot.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultsglodapns.plot.scatter('dic', 'alkalinity',  c="b", ax=ax, label='GLODAP', s=20, alpha=0.4)

ax.set_title('Glodap')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[1,0]
#resultsCefas.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
Cefasmean.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultsCefas.plot.scatter('dic', 'alkalinity', c='xkcd:greenish', ax=ax, label='Cefas', s=20, alpha=0.4)

ax.set_title('Cefas')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[0,1]
#resultsD366.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
D366mean.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, edgecolor='black')
#resultsD366.plot.scatter('dic', 'alkalinity', c='xkcd:pink', ax=ax, label='D366', s=20, alpha=0.4)

ax.set_title('D366')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

ax = axs[1,1]
#resultsRWSn.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, s=35, edgecolor='black')
RWSnmean.plot.scatter('dic', 'alkalinity', c="dayofyear", cmap='twilight', vmin=1, vmax=365, ax=ax, s=35, edgecolor='black')
#resultsRWSn.plot.scatter('dic', 'alkalinity', c='xkcd:dark orange', ax=ax, label='RWS', s=20, alpha=0.4)

ax.set_title('RWSn')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([1800,2400])
ax.set_ylim([2200,2600])
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()
plt.savefig("figures/DIC_TA_plots_scatter_mean_dayofyear.png")
plt.show()

#%% # One plot

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

sc= ax.scatter(combinedmean['dic'], combinedmean['alkalinity'], c=combinedmean['dayofyear'], vmin=0, vmax=365, s=35, cmap=cm, edgecolor="None")

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
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])
ax.set_title('All combined DIC & TA data - mean')

plt.tight_layout()
plt.savefig("figures/DIC_TA_plots_scatter_mean_dayofyear_combined.png")
plt.show()
