import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from sklearn.cluster import MeanShift
from scipy import interpolate 

#%% # Import dataframes

RWSomeano2 = pd.read_csv("dataframes_made/RWSomeano2_final.csv")
resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")

#%% # Relationships between pH and oxygen

fig, ax1 = plt.subplots(dpi=300)

RWSomeano2['datetime'] = pd.to_datetime(RWSomeano2['datetime'])
RWSomeano2year = RWSomeano2.set_index('datetime').resample('Y').mean()
RWSomeano2year = RWSomeano2year.reset_index()

LpH = (RWSomeano2year.pH_total >= 7.5) & (RWSomeano2year.pH_total <= 8.5)

x = RWSomeano2year['datenum'][LpH].to_numpy()
y = RWSomeano2year['pH_total'][LpH].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=1000).fit(x_v)
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

ax=ax1
ax.plot(x_plotting, y_plotting, c='xkcd:dark aqua', label='pH')
ax.scatter('datenum', 'pH_total', c="xkcd:aqua", data=RWSomeano2year, label='pH$_{mean year}$')
ax1.set_ylabel('pH')
ax.legend(bbox_to_anchor=(1.1, 1.0), loc='upper left')

x = RWSomeano2year['datenum'].to_numpy()
y = RWSomeano2year['oxygen umol/kg'].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=1000).fit(x_v)
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

ax2 = ax1.twinx()
ax=ax2
ax.plot(x_plotting, y_plotting, c='xkcd:dark green', label='O$_2$')
ax.scatter('datenum', 'oxygen umol/kg',  c="xkcd:green", data=RWSomeano2year, label='O$_{2 mean year}$', alpha=0.6, marker='x')
ax2.set_ylabel('Oxygen (µmol/kg)')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax.legend(bbox_to_anchor=(1.1, 1.2), loc='upper left')
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax1.minorticks_on()
ax1.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax1.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax1.set_title('Oxygen and pH RWS data - North Sea')

plt.tight_layout()
plt.savefig("figures/Relationships_Oxygen_pH_lines.png")
plt.show()

#%% # Relationships between pH and AOU

fig, ax1 = plt.subplots(dpi=300)

LpH = (RWSomeano2year.pH_total >= 7.5) & (RWSomeano2year.pH_total <= 8.5)

x = RWSomeano2year['datenum'][LpH].to_numpy()
y = RWSomeano2year['pH_total'][LpH].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=1000).fit(x_v)
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

ax=ax1
ax.plot(x_plotting, y_plotting, c='xkcd:dark aqua', label='pH')
ax.scatter('datenum', 'pH_total', c="xkcd:aqua", data=RWSomeano2year, label='pH$_{mean year}$')
ax1.set_ylabel('pH')
ax.legend(bbox_to_anchor=(1.1, 1.0), loc='upper left')

x = RWSomeano2year['datenum'].to_numpy()
y = RWSomeano2year['aou'].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=1000).fit(x_v)
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

ax2 = ax1.twinx()
ax=ax2
ax.plot(x_plotting, y_plotting, c='xkcd:green', label='AOU')
ax.scatter('datenum', 'aou',  c="xkcd:spring green", data=RWSomeano2year, label='AOU$_{mean year}$', alpha=0.6, marker='x')
ax2.set_ylabel('AOU (µmol/kg)')

ax1.grid(alpha=0.3)
ax1.set_xlabel("Time (yrs)")
ax.legend(bbox_to_anchor=(1.1, 1.2), loc='upper left')
ax1.xaxis.set_major_locator(mdates.YearLocator(5))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator())
ax1.minorticks_on()
ax1.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax1.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax1.set_title('AOU and pH RWS data - North Sea')

plt.tight_layout()
plt.savefig("figures/Relationships_AOU_pH_lines.png")
plt.show()

#%% # RWSo O2 per RWS station over time

x = resultsRWSo['datenum']
y = resultsRWSo['oxygen umol/kg']

fvar = 'CALLOG4'

for fvar in ['CALLOG4', "CALLOG10", "CALLOG30",'CALLOG50','CALLOG70',
'EGMAZE4', 'EGMAZE10','EGMAZE20','EGMAZE30','EGMAZE50','EGMAZE70',
'GOERE6','GOERE10','GOERE20','GOERE30','GOERE50','GOERE70',
'NOORDWK4','NOORDWK10','NOORDWK20','NOORDWK30','NOORDWK50','NOORDWK70',
'ROTTMPT20','ROTTMPT30','ROTTMPT50','ROTTMPT70','ROTTMPT100',
'SCHOUWN1','SCHOUWN4','SCHOUWN10','SCHOUWN20','SCHOUWN30','SCHOUWN50','SCHOUWN70',
'TERSLG10','TERSLG30','TERSLG50','TERSLG70','TERSLG100','TERSLG135','TERSLG175',
'WALCRN4','WALCRN10','WALCRN20','WALCRN30','WALCRN50','WALCRN70',
'TERHDE70']:
    
    L1 = (RWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:green', edgecolor='none')
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.grid(alpha=0.3)
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_O2_datetime/O2_" + fvar + ".png")
    plt.show()
            
print("I am done!")

#%% # RWSo pH per RWS station over time

x = resultsRWSo.datenum
y = resultsRWSo.pH_total

fvar = 'CALLOG4'

for fvar in ['CALLOG4', "CALLOG10", "CALLOG30",'CALLOG50','CALLOG70',
'EGMAZE4', 'EGMAZE10','EGMAZE20','EGMAZE30','EGMAZE50','EGMAZE70',
'GOERE6','GOERE10','GOERE20','GOERE30','GOERE50','GOERE70',
'NOORDWK4','NOORDWK10','NOORDWK20','NOORDWK30','NOORDWK50','NOORDWK70',
'ROTTMPT20','ROTTMPT30','ROTTMPT50','ROTTMPT70','ROTTMPT100',
'SCHOUWN1','SCHOUWN4','SCHOUWN10','SCHOUWN20','SCHOUWN30','SCHOUWN50','SCHOUWN70',
'TERSLG10','TERSLG30','TERSLG50','TERSLG70','TERSLG100','TERSLG135','TERSLG175',
'WALCRN4','WALCRN10','WALCRN20','WALCRN30','WALCRN50','WALCRN70',
'TERHDE70']:
    
    L1 = (RWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none')
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH')
    ax.grid(alpha=0.3)
    ax.set_ylim(5,10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_" + fvar + ".png")
    plt.show()
            
print("I am done!")

#%% # RWSo pH all stations over time

x = resultsRWSo.datenum
y = resultsRWSo.pH_total

L2 = (resultsRWSo.station == 'GOERE6')
L3 = (resultsRWSo.station == 'NOORDWK10')
L4 = (resultsRWSo.station == 'NOORDWK20')
L5 = (resultsRWSo.station == 'NOORDWK70')
L6 = (resultsRWSo.station == 'ROTTMPT50')
L7 = (resultsRWSo.station == 'ROTTMPT70')
L8 = (resultsRWSo.station == 'SCHOUWN10')
L9 = (resultsRWSo.station == 'TERSLG10')
L10 = (resultsRWSo.station == 'TERSLG50')
L11 = (resultsRWSo.station == 'TERSLG100')
L12 = (resultsRWSo.station == 'TERSLG135')
L13 = (resultsRWSo.station == 'TERSLG175')
L14 = (resultsRWSo.station == 'WALCRN20')
L15 = (resultsRWSo.station == 'WALCRN70')

fig, ax = plt.subplots(dpi=300, figsize=(8,3))
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:banana', edgecolor='none', label='GOERE6')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='NOORDWK10')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:light orange', edgecolor='none', label='NOORDWK20')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:teal', edgecolor='none', label='NOORDWK70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='ROTTMPT50')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:purple', edgecolor='none', label='ROTTMPT70')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:light pink', edgecolor='none', label='SCHOUWN10')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:light orange', edgecolor='none', label='TERSLG10')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:light red', edgecolor='none', label='TERSLG50')
ax.scatter(x[L11], y[L11], alpha=0.5, s=40, c='xkcd:royal blue', edgecolor='none', label='TERSLG100')
ax.scatter(x[L12], y[L12], alpha=0.5, s=40, c='xkcd:dark blue', edgecolor='none', label='TERSLG135')
ax.scatter(x[L13], y[L13], alpha=0.5, s=40, c='xkcd:dark green', edgecolor='none', label='TERSLG175')
ax.scatter(x[L14], y[L14], alpha=0.5, s=40, c='xkcd:dark pink', edgecolor='none', label='WALCRN20')
ax.scatter(x[L15], y[L15], alpha=0.5, s=40, c='xkcd:violet', edgecolor='none', label='WALCRN70')

ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('pH')
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("RWS station")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.set_axisbelow(True)
ax.grid(alpha=0.3)

ax.set_title('pH RWSo - Stations North Sea')
# plt.tight_layout()
plt.savefig("figures/RWSo_stations_pH_datetime/allstationsfrom_1975_2020.png")
plt.show()