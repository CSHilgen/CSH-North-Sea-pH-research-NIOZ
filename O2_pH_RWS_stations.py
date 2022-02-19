import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from scipy.stats import linregress
import seaborn as sns

#%% # Import dataframes

resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn_final.csv")
RWSn = pd.read_csv("dataframes_made/RWSn_final.csv")

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
    ax.set_xlim(1700, 18500)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)

    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_O2_datetime/O2_" + fvar + ".png")
    plt.show()
            
print("I am almost done!")

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
    
    L1 = (resultsRWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none')

    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH$_{total}$')
    ax.grid(alpha=0.3)
    ax.set_ylim(6.5,9.5)
    ax.set_xlim(1700, 18500)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_" + fvar + ".png")
    plt.show()
            
print("I am almost done!")

#%% # RWSn pH per RWS station over time

x = resultsRWSn.datenum
y = resultsRWSn.pH_total_spectro_out

fvar = 'CALLOG4'

for fvar in ['WALCRN2', 'WALCRN20', 'WALCRN70', 'SCHOUWN10', 'GOERE2', 'GOERE6', 
'NOORDWK2', 'NOORDWK10', 'NOORDWK20', 'NOORDWK70', 'TERSLG10', 'TERSLG50', 
'TERSLG100', 'TERSLG135', 'TERSLG175', 'TERSLG235', 'ROTTMPT50', 'ROTTMPT70']:
    
    L1 = (RWSn.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:cobalt blue', edgecolor='none')
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH$_{total}$')
    ax.grid(alpha=0.3)
    ax.set_ylim(7,9)
    ax.set_xlim(17520, 19000)
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSn_stations_pH_datetime/pH_" + fvar + ".png")
    plt.show()
            
print("I am almost done!")

#%% # RWSo pH per RWS station over time + LR

resultsRWSo = resultsRWSo.dropna(axis='rows', how='all', subset=['pH_total'])

x = resultsRWSo.datenum
y = resultsRWSo.pH_total

P0 = (resultsRWSo.year <= 1985) 
P1 = (resultsRWSo.year >= 1985) & (resultsRWSo.year <= 2010) 
P2 = (resultsRWSo.year >= 2010) & (resultsRWSo.pH_total >= 7.5)

fvar = 'GOERE6'

for fvar in ['GOERE6','NOORDWK10','NOORDWK20','NOORDWK70',
'ROTTMPT50','ROTTMPT70','SCHOUWN10','TERSLG10','TERSLG50',
'WALCRN20','WALCRN70']:
    
    L1 = (resultsRWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none')
    
    slope, intercept, r, p, se = linregress(x[L1][P0], y[L1][P0])
    aslope, aintercept, ar, ap, ase = linregress(x[L1][P1], y[L1][P1])
    bslope, bintercept, br, bp, bse = linregress(x[L1][P2], y[L1][P2])    
    
    sns.regplot(x=x[L1][P0], y=y[L1][P0], data=resultsRWSo[P0], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',})
    sns.regplot(x=x[L1][P1], y=y[L1][P1], data=resultsRWSo[P1], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x=x[L1][P2], y=y[L1][P2], data=resultsRWSo[P2], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH$_{total}$')
    ax.grid(alpha=0.3)
    ax.set_ylim(6.5,9.5)
    ax.set_xlim(1700, 18500)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_line_" + fvar + ".png")
    plt.show()
            
#%% # RWSo pH per RWS station over time + LR

x = resultsRWSo.datenum
y = resultsRWSo.pH_total

P1 = (resultsRWSo.year <= 2010) 
P2 = (resultsRWSo.year >= 2010) & (resultsRWSo.pH_total >= 7.5)

fvar = 'TERSLG100'

for fvar in ['TERSLG100', 'TERSLG135', 'TERSLG175']:
    
    L1 = (resultsRWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none')
    
    aslope, aintercept, ar, ap, ase = linregress(x[L1][P1], y[L1][P1])
    bslope, bintercept, br, bp, bse = linregress(x[L1][P2], y[L1][P2])    
    
    sns.regplot(x=x[L1][P1], y=y[L1][P1], data=resultsRWSo[P1], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x=x[L1][P2], y=y[L1][P2], data=resultsRWSo[P2], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH$_{total}$')
    ax.grid(alpha=0.3)
    ax.set_ylim(6.5,9.5)
    ax.set_xlim(1700, 18500)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_line2_" + fvar + ".png")
    plt.show()
            
#%% # RWSo pH per RWS station over time + LR

x = resultsRWSo.datenum
y = resultsRWSo.pH_total

P0 = (resultsRWSo.year <= 1985) 

fvar = 'CALLOG4'

for fvar in ['CALLOG4', "CALLOG10", "CALLOG30",'CALLOG50','CALLOG70',
'EGMAZE4', 'EGMAZE10','EGMAZE20','EGMAZE30','EGMAZE50','EGMAZE70',
'GOERE10','GOERE20','GOERE30','GOERE50','GOERE70','TERHDE70',
'NOORDWK4','NOORDWK30','NOORDWK50','ROTTMPT20','ROTTMPT30','ROTTMPT100',
'SCHOUWN1','SCHOUWN4','SCHOUWN20','SCHOUWN30','SCHOUWN50','SCHOUWN70',
'TERSLG30','TERSLG70','WALCRN4','WALCRN10','WALCRN30','WALCRN50']:
    
    L1 = (resultsRWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none')
    
    slope, intercept, r, p, se = linregress(x[L1][P0], y[L1][P0])

    sns.regplot(x=x[L1][P0], y=y[L1][P0], data=resultsRWSo[P0], ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',})

    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH$_{total}$')
    ax.grid(alpha=0.3)
    ax.set_ylim(6.5,9.5)
    ax.set_xlim(1700, 18500)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_line3_" + fvar + ".png")
    plt.show()
            
print("I am finally done!")