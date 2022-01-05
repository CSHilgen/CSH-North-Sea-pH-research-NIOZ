# Hagens & Middelburg 2016 tools

def get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod):
       
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    fvar = 'dayofyear'
    LpHp = (allparametersdubbel.pHpredicted >= 7.5) & (allparametersdubbel.pHpredicted <= 8.5)
    LpHf = (resultsRWSodubbel.pH_total >= 7.5) & (resultsRWSodubbel.pH_total <= 8.5)
    LpHT = (allparametersdubbel.pH_T >= 7.5) & (allparametersdubbel.pH_T <= 8.5)
    LpHDIC = (allparametersdubbel.pH_DIC >= 7.5) & (allparametersdubbel.pH_DIC <= 8.5)
    LpHTA = (allparametersdubbel.pH_TA >= 7.5) & (allparametersdubbel.pH_TA <= 8.5)
    
    label=[80, 172, 264, 355] # start days of seasons
    
    fig, ax = plt.subplots(dpi=300)
    
    x = allparametersdubbel[fvar][LpHp].to_numpy()
    y = allparametersdubbel.pHpredicted[LpHp].to_numpy()
    
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:dark blue', label='pH$_{pred}$')
    #ax.scatter(fvar, 'pHpredicted', data=allparameters, c='xkcd:water blue', s=50, alpha=0.3, label='pH$_{pred}$')
    ax.legend()
    
    x = resultsRWSodubbel[fvar][LpHf].to_numpy()
    y = resultsRWSodubbel.pH_total[LpHf].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=14).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:black', label='pH$_{fit}$')
    #ax.scatter(fvar, 'pH_total', data=resultsRWSoNN, c='xkcd:black', s=50, alpha=0.3, label='pH$_{fit}$')
    ax.legend()
    
    x = allparametersdubbel[fvar][LpHT].to_numpy()
    y = allparametersdubbel.pH_T[LpHT].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:pink', label='pH$_{T}$')
    #ax.scatter(fvar, 'pH_T',  c="xkcd:pink", data=allparameters, s=20, label='pH due to T')
    ax.legend()
      
    x = allparametersdubbel[fvar][LpHDIC].to_numpy()
    y = allparametersdubbel.pH_DIC[LpHDIC].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:purple', label='pH$_{DIC}$')
    #ax.scatter(fvar, 'pH_DIC',  c="xkcd:purple", data=allparameters, s=20, label='pH due to DIC')
    ax.legend()
    
    x = allparametersdubbel[fvar][LpHTA].to_numpy()
    y = allparametersdubbel.pH_TA[LpHTA].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:red', label='pH$_{AT}$')
    #ax.scatter(fvar, 'pH_TA',  c="xkcd:red", data=allparameters, s=20, label='pH due to TA')
    ax.legend()
      
    ax.set_xlim(0, 365)
    # ax.set_ylim(7.9, 8.4) 
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_title('pH '+ timeperiod + ' - North Sea')
    ax.legend(loc='lower center')
    
    plt.tight_layout()
    plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_" + timeperiod + "_all.png")  
    plt.show()
    
def get_curve_parameters_2018_2021(allparametersdubbel, resultsRWSodubbel, resultsRWSndubbel):
       
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    fvar = 'dayofyear'
    LpHp = (allparametersdubbel.pHpredicted >= 7.5) & (allparametersdubbel.pHpredicted <= 8.5)
    LpHf = (resultsRWSodubbel.pH_total >= 7.5) & (resultsRWSodubbel.pH_total <= 8.5)
    LpHT = (allparametersdubbel.pH_T >= 7.5) & (allparametersdubbel.pH_T <= 8.5)
    LpHDIC = (allparametersdubbel.pH_DIC >= 7.5) & (allparametersdubbel.pH_DIC <= 8.5)
    LpHTA = (allparametersdubbel.pH_TA >= 7.5) & (allparametersdubbel.pH_TA <= 8.5)
    LpHout = (resultsRWSndubbel.pH_total_spectro_out >= 7.5) & (resultsRWSndubbel.pH_total_spectro_out <= 8.5)
    
    label=[80, 172, 264, 355] # start days of seasons
    
    fig, ax = plt.subplots(dpi=300)
    
    x = allparametersdubbel[fvar][LpHp].to_numpy()
    y = allparametersdubbel.pHpredicted[LpHp].to_numpy()
    
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:dark blue', label='pH$_{pred}$')
    #ax.scatter(fvar, 'pHpredicted', data=allparameters, c='xkcd:water blue', s=50, alpha=0.3, label='pH$_{pred}$')
    ax.legend()
    
    x = resultsRWSndubbel[fvar][LpHout].to_numpy()
    y = resultsRWSndubbel.pH_total_spectro_out[LpHout].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=14).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:black', label='pH$_{fit}$')
    #ax.scatter(fvar, 'pH_total_spectro_out', data=resultsRWSn, c='xkcd:black', s=50, alpha=0.3, label='pH$_{fit}$')
    ax.legend()   
    
    x = allparametersdubbel[fvar][LpHT].to_numpy()
    y = allparametersdubbel.pH_T[LpHT].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:pink', label='pH$_{T}$')
    #ax.scatter(fvar, 'pH_T',  c="xkcd:pink", data=allparameters, s=20, label='pH due to T')
    ax.legend()
      
    x = allparametersdubbel[fvar][LpHDIC].to_numpy()
    y = allparametersdubbel.pH_DIC[LpHDIC].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:purple', label='pH$_{DIC}$')
    #ax.scatter(fvar, 'pH_DIC',  c="xkcd:purple", data=allparameters, s=20, label='pH due to DIC')
    ax.legend()
    
    x = allparametersdubbel[fvar][LpHTA].to_numpy()
    y = allparametersdubbel.pH_TA[LpHTA].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=12).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:red', label='pH$_{AT}$')
    #ax.scatter(fvar, 'pH_TA',  c="xkcd:red", data=allparameters, s=20, label='pH due to TA')
    ax.legend()
      
    ax.set_xlim(0, 365)
    # ax.set_ylim(7.9, 8.4) 
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_title('pH 2018_2021 - North Sea')
    ax.legend(loc='lower center')
    
    plt.tight_layout()
    plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_2018_2021_all.png")  
    plt.show()

def get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod):
 
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    fvarr = ['temperature', 'normalized_DIC', 'normalized_TA']
    colourr = ['xkcd:pink', 'xkcd:purple', 'xkcd:red']
    label_yy = ['Temperature (°C)', 'DIC (µmol/kg)', 'A$_T$ (µmol/kg)']
    Tdata = pd.DataFrame(columns=['dayofyear', 'temperature'])
    DICdata = pd.DataFrame(columns=['dayofyear', 'normalized_DIC'])
    TAdata = pd.DataFrame(columns=['dayofyear', 'normalized_TA'])
    dff = [Tdata, DICdata, TAdata]
    # if timeperiod == str(2000_2021):
    yrangee = [[2.5, 23], [1900, 2400], [2200, 2500]] # period 2000-2021
    # yrangee = [[2.5, 23], [2075, 2225], [2320, 2400]] # period 2000-2005
    # yrangee = [[2.5, 21], [2100, 2200], [2340, 2410]] # period 2010-2015
    # yrangee = [[2.5, 21], [1700, 2400], [2250, 2450]] # period 2015-2018
    # yrangee = [[2.5, 23], [1700, 2400], [2100, 2500]] # period 2018-2021
    
    for fvar, colour, label_y, yrange, df in zip(fvarr, colourr, label_yy, yrangee, dff):
       
        Ldic = (allparametersdubbel.normalized_DIC >= 1900) & (allparametersdubbel.normalized_DIC <= 2400)
        
        fig, ax = plt.subplots(dpi=300)
        allparametersdubbelx = allparametersdubbel.dropna(axis='rows', how='all', subset=[fvar])
        x = allparametersdubbelx['dayofyear'][Ldic].to_numpy()
        y = allparametersdubbelx[fvar][Ldic].to_numpy()
        
        x_v = np.vstack(x)
        clustering = MeanShift(bandwidth=12).fit(x_v)
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
        
        ax.plot(x_plotting, y_plotting, c=colour)
        ax.scatter('dayofyear', fvar,  c=colour, data=allparameters, s=15, alpha=0.1)
        
        ax.set_xlim(0, 365)
        ax.set_xlabel("Months of year")
        ax.set_ylim(yrange)
        month_fmt = DateFormatter('%b')
        def m_fmt(x, pos=None):
            return month_fmt(x)[0]
    
        ax.xaxis.set_major_locator(MonthLocator())
        ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
        ax.set_ylabel(label_y)
        ax.grid(alpha=0.3)
        ax.set_title(fvar + ' ' + timeperiod + ' - North Sea')

        df['dayofyear'] = x_plotting
        df[fvar] = y_plotting
        
        plt.tight_layout()
        plt.savefig("figures/pH_Hagens&Middelburg_2016/Data_" + timeperiod + "_" + fvar + ".png") 
        plt.show()
               
    return Tdata, DICdata, TAdata
        
def get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod):
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    pH_preddata = pd.DataFrame(columns=['dayofyear', 'pHpredicted'])
    pH_fitdata = pd.DataFrame(columns=['dayofyear', 'pH_total'])
    LpHp = (allparametersdubbel.pHpredicted >= 7.5) & (allparametersdubbel.pHpredicted <= 8.5)
    LpHf = (resultsRWSodubbel.pH_total >= 7.5) & (resultsRWSodubbel.pH_total <= 8.5)

    label=[80, 172, 264, 355] # start days of seasons
    
    fig, ax = plt.subplots(dpi=300)
    
    x = allparametersdubbel['dayofyear'][LpHp].to_numpy()
    y = allparametersdubbel.pHpredicted[LpHp].to_numpy()
    
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:dark blue', label='pH$_{pred}$')
    ax.scatter('dayofyear', 'pHpredicted', data=allparameters, c='xkcd:water blue', s=15, alpha=0.4, label='pH$_{pred}$')
    ax.legend()
    
    pH_preddata['dayofyear'] = x_plotting
    pH_preddata['pHpredicted'] = y_plotting
    
    x = resultsRWSodubbel['dayofyear'][LpHf].to_numpy()
    y = resultsRWSodubbel.pH_total[LpHf].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=14).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:black', label='pH$_{fit}$')
    ax.scatter('dayofyear', 'pH_total', data=resultsRWSo[LR], c='xkcd:black', s=15, alpha=0.4, label='pH$_{fit}$')
    ax.legend() 
    
    pH_fitdata['dayofyear'] = x_plotting
    pH_fitdata['pH_total'] = y_plotting
     
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel("pH")
    ax.legend(loc='lower center')
    ax.set_title('pH ' + timeperiod + ' - North Sea')
    ax.set_xlim(0, 365)
    ax.set_ylim(7, 8.65)
    
    plt.tight_layout()
    plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_" + timeperiod + ".png")
    plt.show()  
    
    return pH_preddata, pH_fitdata
    
def get_pHpred_pHfit_2018_2021(allparametersdubbel, resultsRWSndubbel, allparameters, resultsRWSn, timeperiod):
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
       
    pH_preddata = pd.DataFrame(columns=['dayofyear', 'pHpredicted'])
    pH_fitdata = pd.DataFrame(columns=['dayofyear', 'pH_total_spectro_out'])
    LpHp = (allparametersdubbel.pHpredicted >= 7.5) & (allparametersdubbel.pHpredicted <= 8.5)
    LpHout = (resultsRWSndubbel.pH_total_spectro_out >= 7.5) & (resultsRWSndubbel.pH_total_spectro_out <= 8.5)

    label=[80, 172, 264, 355] # start days of seasons
    
    fig, ax = plt.subplots(dpi=300)
    
    x = allparametersdubbel['dayofyear'][LpHp].to_numpy()
    y = allparametersdubbel.pHpredicted[LpHp].to_numpy()
    
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:dark blue', label='pH$_{pred}$')
    ax.scatter('dayofyear', 'pHpredicted', data=allparameters, c='xkcd:water blue', s=50, alpha=0.3, label='pH$_{pred}$')
    ax.legend()
    
    pH_preddata['dayofyear'] = x_plotting
    pH_preddata['pHpredicted'] = y_plotting
    
    x = resultsRWSndubbel['dayofyear'][LpHout].to_numpy()
    y = resultsRWSndubbel.pH_total_spectro_out[LpHout].to_numpy()
    
    x_v = np.vstack(x)
    clustering = MeanShift(bandwidth=14).fit(x_v)
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
    
    ax.plot(x_plotting, y_plotting, c='xkcd:black', label='pH$_{fit}$')
    ax.scatter('dayofyear', 'pH_total_spectro_out', data=resultsRWSn, c='xkcd:black', s=50, alpha=0.3, label='pH$_{fit}$')
    ax.legend() 
     
    pH_fitdata['dayofyear'] = x_plotting
    pH_fitdata['pH_total_spectro_out'] = y_plotting
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel("pH")
    ax.legend(loc='lower center')
    ax.set_title('pH ' + timeperiod + ' - North Sea')
    ax.set_xlim(0, 365)
    ax.set_ylim(7, 8.65)
    
    plt.tight_layout()
    plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_" + timeperiod + ".png")
    plt.show()
    
    return pH_preddata, pH_fitdata

def get_quantitative_contribution():
    
    import matplotlib.pyplot as plt
    import pandas as pd
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    
    labels = ['2000-2021', '2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021']
    pH_pred_means = [-0.030193, -0.060910, 0, -0.080080,  -0.009600, -0.008515]
    pH_fit_means = [0.074431, 0.041342, 0, 0.094465, 0.084005, -0.008046]
    T_means = [-0.176867, -0.179434, 0, -0.179426, -0.167912, -0.185910]
    DIC_means = [0.120855, 0.072869, 0, 0.030189, 0.122911, 0.109603]
    TA_means = [0.028111, 0.041195, 0, 0.021010, 0.026947, 0.067784]
    S_means = [-0.002945, 0.000372, 0, -0.001663, -0.000054, -0.005808]
    TotB_means = [-0.001412, 0.000177, 0, -0.000804, -0.000026, -0.002775]
    TotF_means = [0.000001, 0, 0, 0, 0, 0.000002]
    TotSO4_means = [0, 0, 0, 0, 0, 0] 
    Totnutrients_means = [0.000075, 0.000042, 0, 0.000039, 0.000043, 0.001409]
    
    labels_line = ['2000-2005', '2010-2015', '2015-2018', '2018-2021']
    pH_pred_means_line = [-0.060721, -0.080048, -0.009379, -0.008139]
    pH_fit_means_line = [0.041342, 0.094465, 0.084005, -0.008046]
    
    labels_scatter = [0]
    pH_pred_means_scatter = [-0.030193]
    pH_fit_means_scatter = [0.074431]
    
    # men_std = [2, 3, 4, 1, 2]
    # women_std = [3, 5, 2, 3, 3]
    width = 0.5 # the width of the bars: can also be len(x) sequence
    
    df = pd.DataFrame(labels, columns=['periods'])
    df['pH_pred_means'] = pH_pred_means
    df['pH_fit_means'] = pH_fit_means
    df['T_means'] = T_means
    df['DIC_means'] = DIC_means
    df['TA_means'] = TA_means
    df['S_means'] = S_means
    df['TotB_means'] = TotB_means
    df['TotF_means'] = TotF_means
    df['TotSO4_means'] = TotSO4_means 
    df['Totnutrients_means'] = Totnutrients_means
    
    fig, ax = plt.subplots(dpi=300, figsize=(7,5))
    
    ax.bar(df['periods'], df['Totnutrients_means'], width, color='xkcd:brown', label='∆pH$_{∆Totnutrients}$') #, yerr=men_std )
    ax.bar(df['periods'], df['TA_means'], width, bottom=Totnutrients_means, color='xkcd:red', label='∆pH$_{∆TA}$') #, yerr=women_std )
    ax.bar(df['periods'], df['DIC_means'], width, bottom=TA_means, color='xkcd:purple', label='∆pH$_{∆DIC}$') #, yerr=women_std )
    ax.bar(df['periods'], df['T_means'], width, bottom=S_means, color='xkcd:pink', label='∆pH$_{∆T}$') #, yerr=men_std )
    ax.bar(df['periods'], df['S_means'], width, bottom=TotB_means, color='xkcd:golden', label='∆pH$_{∆S}$') #, yerr=men_std )
    ax.bar(df['periods'], df['TotB_means'], width, color='xkcd:light green', label='∆pH$_{∆TotB}$') #, yerr=men_std )
    #ax.bar(df['periods'], df['TotF_means'], width, color='xkcd:royal', label='∆pH$_{∆T}$') #, yerr=men_std )
    #ax.bar(df['periods'], df['TotSO4_means'], width, color='xkcd:dark grey', label='∆pH$_{∆T}$') #, yerr=men_std )
    
    ax.plot(labels_line, pH_pred_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:water blue', label='∆pH$_{predicted}$') #, yerr=men_std )
    ax.plot(labels_line, pH_fit_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:black', label='∆pH$_{fitted}$') #, yerr=men_std )
    ax.scatter(labels_scatter, pH_pred_means_scatter, color='xkcd:water blue', facecolor='none', zorder=10)
    ax.scatter(labels_scatter, pH_fit_means_scatter, color='black', facecolor='none', zorder=10)
    
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)# x ticks
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.set_ylabel('winter-to-summer ∆pH')
    ax.set_xlabel('Periods (yrs)')
    ax.set_title('Quantitative contribution')
    ax.set_ylim(-0.2, 0.2)
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    
    # plt.tight_layout()
    plt.savefig("figures/pH_Hagens&Middelburg_2016/Quantitative_contribution_FINAL.png")
    plt.show()
