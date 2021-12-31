# Clustering all parameters
from sklearn.cluster import MeanShift
from datetime import datetime

#%% # CURVE FITTING only RWSn & combined !!!
from scipy.interpolate import splev, splrep
combinedmeandubbel = combinedmean.append(combinedmeandubbel.loc[[7] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[19] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[36] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[35] *1].assign(**{'dayofyear':-30}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[18] *1].assign(**{'dayofyear':0}), ignore_index=True)

fvar = 'dayofyear'

# x = RWSnmeandubbel[fvar].to_numpy()
# y = RWSnmeandubbel.dic.to_numpy()
x = combinedmeandubbel[fvar].to_numpy()
y = combinedmeandubbel.salinity.to_numpy()

# def cluster_profile(x, y, bandwidth=15): 
#     """ CLuster alkalinity and day of year profile with MeanShift and interpolate"""
    
x_v = np.vstack(x)
clustering = MeanShift(bandwidth=28).fit(x_v)
cluster_labels = clustering.labels_

x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])
    
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
    
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)
 
    # return x_clusters, y_clusters, x_plotting, y_plotting

# x_unique = np.unique(x)
# y_unique = np.full_like(x_unique, np.nan)
# for i in range(len(x_unique)):
#     y_unique[i] = np.mean(y[x == x_unique[i]])
    
# interpolator = interpolate.PchipInterpolator(x_unique, y_unique)
# x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
# y_plotting = interpolator(x_plotting)

fig, ax = plt.subplots(dpi=300)
ax.scatter(fvar, 'salinity', data=combinedmeandubbel, c='xkcd:blue', s=50)
#RWSnmean.plot(fvar, 'alkalinity', ax=ax, legend=False)
#ax.scatter(x_unique, y_unique, c='xkcd:raspberry', s=10)
ax.scatter(x_clusters, y_clusters, c='xkcd:raspberry', s=10)
#ax.plot(x_clusters, y_clusters, c='xkcd:raspberry')
ax.plot(x_plotting, y_plotting, c='xkcd:raspberry')
ax.set_xlim([0,400])
#ax.set_ylim([2100,2275])
ax.set_xlabel("Day of Year")
ax.set_ylabel("Salinity")
ax.grid(alpha=0.3)
plt.xlim(0,365)
#ax.grid(axis='both', which='major', linestyle=':', linewidth='2')
ax.set_title('Salinity clustering')

plt.savefig("figures/Sal_RWSn_all2_Clustering.png") 

#%% # CURVE FITTING only RWSo 

RWSomeandubbel = RWSomean
# RWSomeandubbel = RWSomeandubbel.dropna(axis='rows', how='all', subset=['pH_total'])

RWSomeandubbel = RWSomean.groupby(by='dayofyear').mean()
RWSomeandubbel = RWSomeandubbel.reset_index()

RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[0] *1].assign(**{'dayofyear':396}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[1] *1].assign(**{'dayofyear':424}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[2] *1].assign(**{'dayofyear':425}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[19] *1].assign(**{'dayofyear':-31}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[20] *1].assign(**{'dayofyear':-30}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[21] *1].assign(**{'dayofyear':0}), ignore_index=True)
RWSomeandubbel = RWSomeandubbel.append(RWSomeandubbel.loc[[22] *1].assign(**{'dayofyear':-1}), ignore_index=True)

fvar = 'dayofyear'

x = RWSomeandubbel[fvar].to_numpy()
y = RWSomeandubbel['pH_total'].to_numpy()
# x = RWSomean[fvar].to_numpy()
# y = RWSomean.pH_total.to_numpy()

# def cluster_profile(x, y, bandwidth=15): 
#     """ CLuster pH_total and day of year profile with MeanShift and interpolate"""
    
x_v = np.vstack(x)
clustering = MeanShift(bandwidth=28).fit(x_v)
cluster_labels = clustering.labels_

x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])
    
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
    
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)
 
    # return x_clusters, y_clusters, x_plotting, y_plotting

# x_unique = np.unique(x)
# y_unique = np.full_like(x_unique, np.nan)
# for i in range(len(x_unique)):
#     y_unique[i] = np.mean(y[x == x_unique[i]])
    
# interpolator = interpolate.PchipInterpolator(x_unique, y_unique)
# x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
# y_plotting = interpolator(x_plotting)

fig, ax = plt.subplots(dpi=300)
ax.scatter(fvar, 'pH_total', data=RWSomeandubbel, c='xkcd:blue', s=50)
#RWSnmean.plot(fvar, 'pH_total', ax=ax, legend=False)
#ax.scatter(x_unique, y_unique, c='xkcd:raspberry', s=10)
ax.scatter(x_clusters, y_clusters, c='xkcd:raspberry', s=10)
#ax.plot(x_clusters, y_clusters, c='xkcd:raspberry')
ax.plot(x_plotting, y_plotting, c='xkcd:raspberry')
ax.set_xlim([0,400])
#ax.set_ylim([2100,2275])
ax.set_xlabel("Day of Year")
ax.set_ylabel("pH total")
ax.grid(alpha=0.3)
plt.xlim(0,365)
#ax.grid(axis='both', which='major', linestyle=':', linewidth='2')
ax.set_title('pH total clustering')

plt.savefig("figures/pH_RWSo_mean_Clustering.png") 