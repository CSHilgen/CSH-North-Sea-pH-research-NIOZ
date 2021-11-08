# TA fitting

#%% # Dubbel mean on combined dataset - mean by day of year

combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])
combined2mean = combinedmean.groupby(by=combinedmean['dayofyear']).mean()
combined2mean = combined2mean.reset_index()

#%% TA - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultscombined.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#combinedmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
combined2mean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
combined2mean.plot('dayofyear','alkalinity', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
#ax.set_title("TA data - allpoints - Dayofyear")
#ax.set_title("TA data - mean - Dayofyear")
#ax.set_title("TA data - 2mean - Dayofyear")
ax.set_title("TA data - 2mean - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_2mean_scatter_dayofyear.png")
plt.savefig("figures/DIC_TA_fitting/TA_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the alkalinity mean, line as alkanitity winter mean and alkalinity - winter mean

resultscombinedwinter = resultscombined[(resultscombined["dayofyear"] >= 355) | (resultscombined["dayofyear"] <= 78)]
winteralkalinitymean = resultscombinedwinter['alkalinity'].mean() # Result is 2336.949
print("The mean of the TA in the winter =")
print(winteralkalinitymean)
resultscombined['alkalinity-winteralkalinitymean'] = resultscombined['alkalinity'] - winteralkalinitymean

# combinedmeanwinter = combinedmean[(combinedmean["dayofyear"] >= 355) | (combinedmean["dayofyear"] <= 78)]
# winteralkalinity2mean = combinedmeanwinter['alkalinity'].mean() # Result is 2355.875
# combinedmean['alkalinity-winteralkalinitymean'] = combinedmean['alkalinity'] - winteralkalinity2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
#resultscombined.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
resultscombined.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
#plt.axhline(y=winteralkalinitymean, color='r', linestyle='-')

# combinedmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
# combinedmean.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winteralkalinity2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("TA data - allpoints - Dayofyear")

plt.tight_layout()
#plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear_wintermean.png")
plt.savefig("figures/DIC_TA_fitting/TA_mean_dayofyear_minuswintermean.png")
plt.show()

#%% # Dubbel mean on RWSn dataset - mean by day of year

RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSn2mean = RWSnmean.groupby(by=RWSnmean['dayofyear']).mean()
RWSn2mean = RWSn2mean.reset_index()

#%% # RWSn TA - allpoints, mean, 2mean - Dayofyear

fig, ax = plt.subplots(dpi=300)

ax=ax
resultsRWSn.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSnmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#RWSn2mean.plot('dayofyear','alkalinity', c='r', ax=ax)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("Total alkalinity")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - allpoints - Dayofyear")
#ax.set_title("RWSn TA data - mean - Dayofyear")
#ax.set_title("RWSn TA data - 2mean - Dayofyear")
#ax.set_title("RWSn TA data - 2mean - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_mean_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_2mean_scatter_dayofyear.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_2mean_plot_dayofyear.png")
plt.show()

#%% # Plotting the RWSn alkalinity mean, line as alkalinity winter mean and alkalinity - winter mean

resultsRWSnwinter = resultsRWSn[(resultsRWSn["dayofyear"] >= 355) | (resultsRWSn["dayofyear"] <= 78)]
winteralkalinitymean = resultsRWSnwinter['alkalinity'].mean() # Result is 2360.320
print("The mean of the TA in the winter =")
print(winteralkalinitymean)
resultsRWSn['alkalinity-winteralkalinitymean'] = resultsRWSn['alkalinity'] - winteralkalinitymean

# RWSnmeanwinter = RWSnmean[(RWSnmean["dayofyear"] >= 355) | (RWSnmean["dayofyear"] <= 78)]
# winteralkalinity2mean = RWSnmeanwinter['alkalinity'].mean() # Result is 2204.358
# print("The mean of the TA mean in the winter =")
# print(winteralkalinity2mean)
# RWSnmean['alkalinity-winteralkalinitymean'] = RWSnmean['alkalinity'] - winteralkalinity2mean

fig, ax = plt.subplots(dpi=300)

ax=ax
resultsRWSn.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
#resultsRWSn.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
plt.axhline(y=winteralkalinitymean, color='r', linestyle='-')

# RWSnmean.plot.scatter('dayofyear','alkalinity', c='year', cmap='magma', ax=ax)
# RWSnmean.plot.scatter('dayofyear','alkalinity-winteralkalinitymean', c='year', cmap='magma', ax=ax)
# plt.axhline(y=winteralkalinity2mean, color='r', linestyle='-')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA - TA winter mean")
# ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - allpoints - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear_wintermean.png")
#plt.savefig("figures/DIC_TA_fitting/TA_RWSn_allpoints_dayofyear_minuswintermean.png")
plt.show()

#%% # CURVE FITTING only RWSn !!! PART 1

fig, ax = plt.subplots(dpi=300)

x = RWSn2mean['dayofyear']
y = RWSn2mean['alkalinity']

# define the true objective function
def objective(x, a, b , c):
 	return (a * x**3) - (b * x**2) + c
 
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c = popt
# plot input vs output
ax.scatter(x, y, c='purple')
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b, c)
# create a line plot for the mapping function
ax.plot(x_line, y_line, '--', color='red')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn TA data - curve fit - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_Interpolation_1.png")
plt.show()

#%% # CURVE FITTING only RWSn !!! PART 2

fig, ax = plt.subplots(dpi=300)

x = RWSn2mean['dayofyear']
y = RWSn2mean['alkalinity']

interp_spline = interpolate.UnivariateSpline(x, y)
x_interp = np.linspace(np.min(x), np.max(x), num=15)
y_spline = interp_spline(x_interp)
ax.plot(x_interp, y_spline, label='Spline', c='b')

interp_cubic = interpolate.interp1d(x, y, kind='cubic')
x_interp = np.linspace(np.min(x), np.max(x), num=15)
y_cubic = interp_cubic(x_interp)
ax.plot(x_interp, y_cubic, label='Cubic', c='red')

interp_nearest = interpolate.interp1d(x, y, kind='nearest')
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_nearest = interp_nearest(x_interp)
ax.plot(x_interp, y_nearest, label='Nearest', c='black')

interp_linear = interpolate.interp1d(x, y, kind='linear')
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_linear = interp_linear(x_interp)
ax.plot(x_interp, y_linear, label='Linear', c='orange')

interp_pchip = interpolate.PchipInterpolator(x, y)
x_interp = np.linspace(np.min(x), np.max(x), num=19)
y_pchip = interp_pchip(x_interp)
ax.plot(x_interp, y_pchip, label='Pchip', c='pink')

ax.scatter(x, y)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Interpolation")
# ax.plot(x, y)

# # define the true objective function
# def objective(x, a, b , c):
#  	return (a * x**3) - (b * x**2) + c
# # summarize the parameter values
# a, b, c = popt
# # plot input vs output
# plt.scatter(x, y)
# # define a sequence of inputs between the smallest and largest known inputs
# x_line = arange(min(x), max(x), 1)
# # calculate the output for the range
# y_line = objective(x_line, a, b, c)
# # create a line plot for the mapping function
# plt.plot(x_line, y_line, '--', color='red')
# plt.show() 

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("TA")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_title("RWSn - TA data - mean - Dayofyear")

plt.tight_layout()
plt.savefig("figures/DIC_TA_fitting/TA_RWSn_Interpolation_2.png")
plt.show()


