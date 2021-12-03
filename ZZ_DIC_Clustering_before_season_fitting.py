# Clustering before fitting seasonal cycle
from sklearn.cluster import MeanShift
from datetime import datetime

#%% # Make new dateframe with the datapoint of 365 located at 0.

combinedmeandubbel = combinedmean.append(combinedmean.loc[[7] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[19] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[36] *1].assign(**{'dayofyear':396}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[35] *1].assign(**{'dayofyear':-30}), ignore_index=True)
combinedmeandubbel = combinedmeandubbel.append(combinedmeandubbel.loc[[18] *1].assign(**{'dayofyear':0}), ignore_index=True)

#%% # Make new dateframe with the datapoint of 365 located at 0.

RWSnmeandubbel = RWSnmean.append(RWSnmean.loc[[11] *1].assign(**{'dayofyear':0, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[10] *1].assign(**{'dayofyear':-31, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[28] *1].assign(**{'dayofyear':-30, 'year':2021}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[0] *1].assign(**{'dayofyear':396, 'year':2019}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[12] *1].assign(**{'dayofyear':396, 'year':2020}), ignore_index=True)
RWSnmeandubbel = RWSnmeandubbel.append(RWSnmeandubbel.loc[[29] *1].assign(**{'dayofyear':396, 'year':2021}), ignore_index=True)

#%% # CURVE FITTING only RWSn !!! PART 3

fvar = 'dayofyear'

# L0 = (RWSnmeandubbel['year'] == 2018) 
# L1 = (RWSnmeandubbel['year'] == 2019)
# L2 = (RWSnmeandubbel['year'] == 2020) 
# L3 = (RWSnmeandubbel['year'] == 2021) 

# x = RWSnmeandubbel[fvar].to_numpy()
# y = RWSnmeandubbel.dic.to_numpy()
x = combinedmeandubbel[fvar].to_numpy()
y = combinedmeandubbel.normalized_DIC.to_numpy()

# def cluster_profile(x, y, bandwidth=15): 
#     """ CLuster DIC and day of year profile with MeanShift and interpolate"""
    
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
#ax.scatter(fvar, 'dic', data=RWSnmeandubbel, c='xkcd:blue', s=50)
ax.scatter(fvar, 'dic', data=combinedmeandubbel, c='xkcd:blue', s=50)
#RWSnmean.plot(fvar, 'dic', ax=ax, legend=False)
#ax.scatter(x_unique, y_unique, c='xkcd:raspberry', s=10)
ax.scatter(x_clusters, y_clusters, c='xkcd:raspberry', s=10)
#ax.plot(x_clusters, y_clusters, c='xkcd:raspberry')
ax.plot(x_plotting, y_plotting, c='xkcd:raspberry')
ax.set_xlim([0,400])
#ax.set_ylim([2100,2275])
ax.set_xlabel("Day of Year")
ax.set_ylabel("DIC")
ax.grid(alpha=0.3)
plt.xlim(0,365)
#ax.grid(axis='both', which='major', linestyle=':', linewidth='2')

#plt.savefig("figures/DIC_season_fitting/DIC_RWSn_Clustering3.png")    
#plt.savefig("figures/DIC_season_fitting/DIC_Combinedmean_Clustering_normalized_DIC.png")    


#%% # Making a dateframe to plot the seasonal cycle for every year

combinedmeandic = pd.DataFrame()
combinedmeandic['datenum'] = np.arange(10957, 18993)
combinedmeandic['datetime'] = mdates.num2date(combinedmeandic.datenum)
combinedmeandic['dayofyear'] = combinedmeandic.datetime.dt.dayofyear
combinedmeandic['interpolator_dic'] = interpolator(combinedmeandic['dayofyear'])

#%% # Making a dateframe for subtracting seasonal cycle from the datapoints

combinedmeandic2 = pd.DataFrame(combinedmean['datetime'])
combinedmeandic2['dayofyear'] = combinedmean['dayofyear']
combinedmeandic2['datenum'] = combinedmean['datenum']
#combinedmeandic2['dic'] = combinedmean['dic']
combinedmeandic2['normalized_DIC'] = combinedmean['normalized_DIC']
combinedmeandic2['interpolator_dic'] = interpolator(combinedmeandic2['dayofyear'])

# plt.scatter(combinedmeandic2['datetime'], combinedmeandic2['interpolator_dic'], c='r')
# plt.scatter(combinedmean['datetime'], combinedmean['dic'], c='b')

combinedmeandic2['dicminusseason'] = (combinedmeandic2['normalized_DIC'] - combinedmeandic2['interpolator_dic'])
