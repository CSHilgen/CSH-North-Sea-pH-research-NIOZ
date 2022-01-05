#%% # RWSo Chl - Dayofyear

fig, ax1 = plt.subplots(dpi=300)

# ax=ax1
ax.scatter('dayofyear', 'chlorophyll',  c="xkcd:aqua", data=RWSo, label='RWSo')
ax1.set_ylabel('Chlorophyll')
ax.legend()

# ax2 = ax1.twinx()
# ax=ax2
# ax.scatter('dayofyear', 'dic',  c="xkcd:dark orange", data=RWSnmean, label='RWSn')
# ax.plot(x_plotting, y_plotting, c='xkcd:dark orange')
# ax2.set_ylabel('DIC (umol/kg)')

ax.grid(alpha=0.3)
ax1.set_xlabel("Day of Year")
ax.legend()
ax.set_title('Chl and DIC data - Day of Year North Sea')

plt.tight_layout()
#plt.savefig("figures/Chl&DIC_dayofyear_datasets.png")
plt.show()
