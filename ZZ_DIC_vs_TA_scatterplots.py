# DIC vs TA scatterplots

#%% # DIC vs TA scatter plots based all points or mean

fig, axs = plt.subplots(dpi=300, nrows=2, ncols=2)

ax = axs[0,0]
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsglodapns, edgecolor='black')
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=glodapnsmean, edgecolor='black')
ax.scatter('dic', 'alkalinity',  c="b", data=resultsglodapns, label='GLODAP', s=20, alpha=0.4)

ax.set_title('Glodap')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

ax = axs[1,0]
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsCefas, edgecolor='black')
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=Cefasmean, edgecolor='black')
ax.scatter('dic', 'alkalinity',  c="xkcd:greenish", data=resultsCefas, label='Cefas', s=20, alpha=0.4)

ax.set_title('Cefas')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

ax = axs[0,1]
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsD366, edgecolor='black')
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=D366mean, edgecolor='black')
ax.scatter('dic', 'alkalinity',  c="xkcd:pink", data=resultsD366, label='D366', s=20, alpha=0.4)

ax.set_title('D366')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([2000,2300])
ax.set_ylim([2200,2450])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

ax = axs[1,1]
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=resultsRWSn, edgecolor='black')
#sc = ax.scatter('dic', 'alkalinity',  c="dayofyear", cmap='twilight', vmin=1, vmax=365, data=RWSnmean, edgecolor='black')
ax.scatter('dic', 'alkalinity',  c="xkcd:dark orange", data=resultsRWSn, label='RWSn', s=20, alpha=0.4)

ax.set_title('RWSn')
ax.grid(alpha=0.3)
ax.set_xlabel("DIC")
ax.set_ylabel("Total alkalinity")
ax.set_xlim([1800,2400])
ax.set_ylim([2200,2600])

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Seasons')
# label=[80,172,264,355]
# cbar.set_ticks(label)
# cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/DIC_TA_plots_scatter_allpoints_datasets.png")
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
