
def plot_DIC_combined_clustering(combinedmeandubbel):
    """ CLuster DIC and day of year profile with MeanShift and interpolate"""

    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
  
    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021
    
    x = combinedmeandubbel['dayofyear'].to_numpy()
    y = combinedmeandubbel.normalized_DIC.to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=5).fit(x_v)
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
  
    fig, ax = plt.subplots(dpi=300)

    sc = ax.scatter('dayofyear', 'normalized_DIC', data=combinedmeandubbel, c='year', s=50, cmap=cm, 
               vmin=vmin, vmax=vmax+1, edgecolors='grey', linewidth=0.5, label='Initial DIC Combined')
    ax.scatter(x_clusters, y_clusters, c='xkcd:green', s=10)
    ax.plot(x_plotting, y_plotting, c='xkcd:green', label='Seasonal cycle')
    
    ax.set_ylabel("DIC (μmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlim(0, 365)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_title('DIC combined - Seasonal cycle')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    ticks = np.linspace(vmin, vmax, 5)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/Temporal_variability/DIC_Combined_Clustering.png")
    plt.show()

def plot_DIC_and_Chl(combinedmeandubbel, RWSo):
    """ Plot DIC and Chlorophyll on day of year to observe algalbloom"""

    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    x = combinedmeandubbel['dayofyear'].to_numpy()
    y = combinedmeandubbel.normalized_DIC.to_numpy()
    
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
  
    fig, ax1 = plt.subplots(dpi=300)
    
    ax=ax1
    ax.scatter('dayofyear', 'chlorophyll',  c="xkcd:aqua", data=RWSo, label='RWSo')
    ax1.set_ylabel('Chlorophyll-a (μg/L)')
    ax.legend()
    
    ax2 = ax1.twinx()
    ax=ax2
    ax.scatter('dayofyear', 'dic', data=combinedmeandubbel, c='xkcd:purple', s=50,
                label='Initial DIC Combined')
    ax.scatter(x_clusters, y_clusters, c='xkcd:green', s=10)
    ax.plot(x_plotting, y_plotting, c='xkcd:green', label='Seasonal cycle')
    
    ax2.set_ylabel('DIC (μmol/kg)')
    ax.grid(alpha=0.3)
    ax.set_xlim(0, 365)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_title('Chl and DIC data - Day of Year North Sea')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
 
    plt.tight_layout()
    plt.savefig("figures/Temporal_variability/Chl_DIC_dayofyear.png")
    plt.show()

def plot_DIC_dayofyear_cycle_RWSn(RWSnmeandubbel):
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns  
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 

    yeardataa = [2018, 2019, 2020, 2021]
    yeardatatextt = ['2018', '2019', '2020', '2021']
    
    for yeardata, yeardatatext in zip(yeardataa, yeardatatextt):
    
        L = (RWSnmeandubbel['year'] == yeardata) 
        
        x = RWSnmeandubbel['dayofyear'][L].to_numpy()
        y = RWSnmeandubbel[L].dic.to_numpy()
        
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
                
        fig, ax = plt.subplots(dpi=300)
        
        ax.scatter('dayofyear', 'dic', data=RWSnmeandubbel[L], c='xkcd:evergreen', s=50, label='Initial DIC RWS')
        # ax.scatter(x_clusters, y_clusters, c='xkcd:green', s=10)
        ax.plot(x_plotting, y_plotting, c='xkcd:green', label='Seasonal cycle')
        
        ax.set_ylabel("DIC (μmol/kg)")
        ax.grid(alpha=0.3)
        ax.set_xlim(0, 365)
        ax.set_xlabel("Months of year")
        month_fmt = DateFormatter('%b')
        def m_fmt(x, pos=None):
            return month_fmt(x)[0]

        ax.xaxis.set_major_locator(MonthLocator())
        ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
        ax.minorticks_on()
        ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
        ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
        ax.set_title('DIC ' + yeardatatext + ' - Seasonal cycle')
        ax.legend()
          
        plt.tight_layout()
        plt.savefig("figures/Temporal_variability/DIC_Combined_" + yeardatatext + "Clustering.png")
        plt.show()