# ERROR on making a plot . year is one line in color.


#%% DIC and TA vs day of year (color is year) allpoints, mean, 2mean

fig, ax = plt.subplots(dpi=300)
x = RWSnmean['month']
y = RWSnmean['dic']

L0 = (RWSnmean['year'] == 2018)
L1 = (RWSnmean['year'] == 2019)
L2 = (RWSnmean['year'] == 2020)
L3 = (RWSnmean['year'] == 2021)
RWSnmean.plot.scatter(x[L0], y[L0], c='b', ax=ax)
RWSnmean.plot(x[L1], y[L1], c='r', ax=ax)
RWSnmean.plot(x[L2], y[L2], c='white', ax=ax)
RWSnmean.plot(x[L3], y[L3], c='xkcd:banana', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Month")
ax.set_ylabel("DIC")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

# ax=axs[1]
# RWSnmean.plot.scatter('month', 'alkalinity', c='year', cmap='magma', ax=ax)


# ax.grid(alpha=0.3)
# ax.set_xlabel("Month")
# ax.set_ylabel("Total alkalinity")
# # ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

plt.tight_layout()

plt.show()

