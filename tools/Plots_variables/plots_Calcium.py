
def get_calcium_plots(RWSo, RWSoCa):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 

    #%% # Corrected Calcium data based on the methods (Method 1 - 720)
    
    RWSoCa = RWSo.dropna(axis='rows', how='all', subset=['calcium umol/kg'])

    L0 = (RWSoCa.year <= 2014)
    L1 = (RWSoCa.year >= 2015) & (RWSoCa.datenum <= 16996.3)
    L2 = (RWSoCa.datenum >= 17014.4)  
    
    #%% # Corrected Calcium data based on the methods (Method 1 - 720) - Time - Methods

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('datenum', 'calcium_corrected', edgecolors='yellow', facecolors='yellow', data=RWSoCa[L0], s=20, label='Method1$_{corr}$')
    ax.scatter('datenum', 'calcium_corrected', edgecolors='orange', facecolors='orange', data=RWSoCa[L1], s=20, label='Method 2')
    ax.scatter('datenum', 'calcium_corrected', edgecolors='green', facecolors='green', data=RWSoCa[L2], s=20, label='Method 3')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.legend()
    ax.set_ylim(0, 7500)
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium Method 1 corrected - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_time_datasets_c.png")
    plt.show()

    #%% # Salinity vs Calcium seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    vmin = 1
    vmax = 365

    ax=ax
    sns.regplot(x='salinity', y='calcium_corrected', data=RWSoCa, ax=ax,
                scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

    sc = ax.scatter('salinity', 'calcium_corrected', c='dayofyear', cmap=cm, data=RWSoCa, label='RWS Ca', vmin=vmin, vmax=vmax)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Salinity")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_title("Ca and S RWS data - North Sea")
    ax.set_ylim(0, 7500)

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/Ca_S_scatter_seasonsc.png")
    plt.show()

    #%% # Salinity vs Calcium year

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('rainbow')

    vmin = 2009
    vmax = 2021

    ax=ax
    sns.regplot(x='salinity', y='calcium_corrected', data=RWSoCa, ax=ax,
                scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

    sc = ax.scatter('salinity', 'calcium_corrected', c='year', cmap=cm, data=RWSoCa, label='RWS Ca', vmin=vmin, vmax=vmax)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Salinity")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_title("Ca and S RWS data - North Sea")
    ax.set_ylim(0, 7500)

    ticks = np.linspace(vmin, vmax, 7)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2009, 2011, 2013, 2015, 2017, 2019, 2021])

    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/Ca_S_scatter_year_c.png")
    plt.show()

    #%% # Salinity vs Calcium methods

    fig, ax = plt.subplots(dpi=300)

    ax=ax
    sns.regplot(x='salinity', y='calcium_corrected', data=RWSoCa, ax=ax,
                scatter_kws={"color": "aqua"}, line_kws={"color": "blue"})

    sc = ax.scatter('salinity', 'calcium_corrected', c='yellow', data=RWSoCa[L0],  label='Method 1$_{corr}$')
    sc = ax.scatter('salinity', 'calcium_corrected', c='orange', data=RWSoCa[L1], label='Method 2')
    sc = ax.scatter('salinity', 'calcium_corrected', c='green', data=RWSoCa[L2], label='Method 3')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Salinity")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_title("Ca and S RWS data - North Sea")
    ax.set_ylim(0, 7500)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/Ca_S_scatter_c.png")
    plt.show()

    #%% # Calcium - Time - Datasets - LINEAR REGRESSION LINE

    fig, ax = plt.subplots(dpi=300)

    slope, intercept, r, p, se = linregress(RWSoCa['datenum'], RWSoCa['calcium_corrected'])

    ax = ax
    ax.scatter('datenum', 'calcium_corrected', c='xkcd:aqua', data=RWSoCa, label='RWS$_{corr}$', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa, ax=ax,
                scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.legend()#bbox_to_anchor=(1.0, 1.0), loc='upper left')
    # ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_time_datasets_LRc.png")
    plt.show()

    #%% # Calcium - Time - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('datenum', 'calcium_corrected', c='xkcd:aqua', data=RWSoCa, label='RWS$_{corr}$', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.legend()
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_time_datasetsc.png")
    plt.show()
    
    #%% # Calcium - Time - Seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'calcium_corrected', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSoCa, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/Ca_time_seasonsc.png")
    plt.show()   
  
    #%% # Calcium - Time - Regions
    
    fig, ax = plt.subplots(dpi=300)
    
    ax=ax
    x = RWSoCa['datenum']
    y = RWSoCa['calcium_corrected']
    
    R0 = (RWSoCa['distance_to_shore'] > 0) & (RWSoCa['distance_to_shore'] <=4)
    R1 = (RWSoCa['distance_to_shore'] > 4) & (RWSoCa['distance_to_shore'] <=10)
    R2 = (RWSoCa['distance_to_shore'] > 10) & (RWSoCa['distance_to_shore'] <=20)
    R3 = (RWSoCa['distance_to_shore'] > 20) & (RWSoCa['distance_to_shore'] <=30)
    R4 = (RWSoCa['distance_to_shore'] > 30) & (RWSoCa['distance_to_shore'] <=50)
    R5 = (RWSoCa['distance_to_shore'] > 50) & (RWSoCa['distance_to_shore'] <=70)
    R6 = (RWSoCa['distance_to_shore'] > 70) & (RWSoCa['distance_to_shore'] <=100)
    R7 = (RWSoCa['distance_to_shore'] > 100) & (RWSoCa['distance_to_shore'] <=150)
    R8 = (RWSoCa['distance_to_shore'] > 150) & (RWSoCa['distance_to_shore'] <=200)
    R9 = (RWSoCa['distance_to_shore'] > 200) & (RWSoCa['distance_to_shore'] <=250)
    R10 = (RWSoCa['distance_to_shore'] > 250) & (RWSoCa['distance_to_shore'] <=300)
    
    ax.scatter(x[R0], y[R0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[R1], y[R1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[R2], y[R2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[R3], y[R3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[R4], y[R4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[R5], y[R5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[R6], y[R6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[R7], y[R7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[R8], y[R8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[R9], y[R9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[R10], y[R10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('Relative Calcium (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.set_ylim(0, 7500)
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Calcium RWSo data - Regions North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/Ca_time_regionsc.png")
    plt.show()
    
    #%% # Calcium - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('dayofyear', 'calcium_corrected', edgecolors='yellow', facecolors='yellow', data=RWSoCa[L0], s=20, label='Method 1$_{corr}$')
    ax.scatter('dayofyear', 'calcium_corrected', edgecolors='orange', facecolors='orange', data=RWSoCa[L1], s=20, label='Method 2')
    ax.scatter('dayofyear', 'calcium_corrected', edgecolors='green', facecolors='green', data=RWSoCa[L2], s=20, label ='Method 3')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.legend()
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_dayofyear_datasetsc.png")
    plt.show()
    
    #%% # Calcium - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300)

    ax=ax
    x = RWSoCa['dayofyear']
    y = RWSoCa['calcium_corrected']

    R0 = (RWSoCa['distance_to_shore'] > 0) & (RWSoCa['distance_to_shore'] <=4)
    R1 = (RWSoCa['distance_to_shore'] > 4) & (RWSoCa['distance_to_shore'] <=10)
    R2 = (RWSoCa['distance_to_shore'] > 10) & (RWSoCa['distance_to_shore'] <=20)
    R3 = (RWSoCa['distance_to_shore'] > 20) & (RWSoCa['distance_to_shore'] <=30)
    R4 = (RWSoCa['distance_to_shore'] > 30) & (RWSoCa['distance_to_shore'] <=50)
    R5 = (RWSoCa['distance_to_shore'] > 50) & (RWSoCa['distance_to_shore'] <=70)
    R6 = (RWSoCa['distance_to_shore'] > 70) & (RWSoCa['distance_to_shore'] <=100)
    R7 = (RWSoCa['distance_to_shore'] > 100) & (RWSoCa['distance_to_shore'] <=150)
    R8 = (RWSoCa['distance_to_shore'] > 150) & (RWSoCa['distance_to_shore'] <=200)
    R9 = (RWSoCa['distance_to_shore'] > 200) & (RWSoCa['distance_to_shore'] <=250)
    R10 = (RWSoCa['distance_to_shore'] > 250) & (RWSoCa['distance_to_shore'] <=300)
    
    ax.scatter(x[R0], y[R0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[R1], y[R1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[R2], y[R2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[R3], y[R3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[R4], y[R4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[R5], y[R5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[R6], y[R6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[R7], y[R7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[R8], y[R8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[R9], y[R9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[R10], y[R10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel('Relative Calcium (μmol/kg)')
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Calcium RWSo data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_dayofyear_regionsc.png")
    plt.show()

    #%% Calcium - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300)

    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021

    ax=ax
    sc = ax.scatter('dayofyear', 'calcium_corrected',  c="year", data=RWSoCa, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 4)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2008, 2012, 2016, 2020])

    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_ylabel('Relative Calcium (μmol/kg)')
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium RWSo data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_dayofyear_yearc.png")
    plt.show()
    
    #%% # Calcium - Regions - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('distance_to_shore', 'calcium_corrected', edgecolors='yellow', facecolors='yellow', data=RWSoCa[L0], s=20, label='Method 1$_{corr}$')
    ax.scatter('distance_to_shore', 'calcium_corrected', edgecolors='orange', facecolors='orange', data=RWSoCa[L1], s=20, label='Method 2')
    ax.scatter('distance_to_shore', 'calcium_corrected', edgecolors='green', facecolors='green', data=RWSoCa[L2], s=20, label ='Method 3')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.legend()
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Ca_regions_datasetsc.png")
    plt.show()

    #%% # Calcium - Regions - Seasons
    
    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')
    
    ax = ax
    sc = ax.scatter('distance_to_shore', 'calcium_corrected', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSoCa, s=20)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel('Relative Calcium (μmol/kg)')
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium RWSo data - Seasons North Sea')
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    plt.tight_layout()
    plt.savefig("figures/Ca_regions_seasonsc.png")
    plt.show()
    
    #%% Calcium - Regions - Year
    
    fig, ax = plt.subplots(dpi=300)
    
    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021
    
    ax=ax
    sc = ax.scatter('distance_to_shore', 'calcium_corrected',  c="year", data=RWSoCa, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
    
    ticks = np.linspace(vmin, vmax, 4)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2008, 2012, 2016, 2020])
    
    ax.grid(alpha=0.3)
    ax.set_xlabel('Distance to shore (km)')
    ax.set_ylabel('Relative Calcium (μmol/kg)')
    ax.set_ylim(0, 7500)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Calcium RWSo data - Year North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/Ca_regions_yearc.png")
    plt.show()
    
    #%% # Long Term Trend of Calcium RWSoCa

    print('Long term trend of Calcium RWSo')

    slope, intercept, r, p, se = linregress(RWSoCa['datenum'], RWSoCa['calcium_corrected'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    fig, ax = plt.subplots(dpi=300, figsize=(10,6))

    ax = ax
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Ca RWS')

    ax.set_title("RWSo Calcium data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Calcium_fitting_RWSoCac.png")    
    plt.show()

    # Calcium 2009-2018 
    xbegin = 14252.4
    xend = 17877.5
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2009-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 

    #%% # Long Term Trend of Calcium RWSo (splitting up per method)

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWSoCa[L0]['datenum'], RWSoCa[L0]['calcium_corrected'])

    ax = axs[0]
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L0], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Corrected Ca RWS')

    ax.set_title("Calcium RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylim(0, 7500)
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSoCa[L1]['datenum'], RWSoCa[L1]['calcium_corrected'])

    ax = axs[1]
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L1], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Ca RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSoCa[L2]['datenum'], RWSoCa[L2]['calcium'])

    ax = axs[2]
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L2], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Ca RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Calcium_split_up_RWSoCac.png")     
    plt.show()
    
    #%% # Long Term Trend of Calcium RWSo (splitting LR up)

    fig, ax = plt.subplots(dpi=300, figsize=(10,6))

    L0 = (RWSoCa.year <= 2014)
    L1 = (RWSoCa.year >= 2015) & (RWSoCa.datenum <= 17315.6)
    L2 = (RWSoCa.datenum >= 17315.6)  

    slope, intercept, r, p, se = linregress(RWSoCa[L0]['datenum'], RWSoCa[L0]['calcium_corrected'])
    aslope, aintercept, ar, ap, ase = linregress(RWSoCa[L1]['datenum'], RWSoCa[L1]['calcium_corrected'])
    bslope, bintercept, br, bp, bse = linregress(RWSoCa[L2]['datenum'], RWSoCa[L2]['calcium_corrected'])    
    
    ax = ax
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L0], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Corrected Ca RWS')
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L1], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='calcium_corrected', data=RWSoCa[L2], ax=ax,
                scatter_kws={"color": "xkcd:grey"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("Calcium RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Relative Calcium (μmol/kg)")
    ax.set_ylim(0, 7500)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Calcium_split_up_RWSoCa2c.png")     
    plt.show()

#%% # Change per year and period
    
    P2 = (RWSoCa.year <= 2010)
    P3 = (RWSoCa.year >= 2010)
    
    # Total 2009-2021
    slope, intercept, r, p, se = linregress(RWSoCa['datenum'], RWSoCa['calcium_corrected']) 
    xbegin = RWSoCa.datenum.min() 
    xend = RWSoCa.datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2009-2021: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Total 2009-2010 
    slope, intercept, r, p, se = linregress(RWSoCa[P2]['datenum'], RWSoCa[P2]['calcium_corrected']) 
    xbegin = RWSoCa[P2].datenum.min() 
    xend = RWSoCa[P2].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2009-2010 : {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2010-2021
    slope, intercept, r, p, se = linregress(RWSoCa[P3]['datenum'], RWSoCa[P3]['calcium_corrected']) 
    xbegin = RWSoCa[P3].datenum.min() 
    xend = RWSoCa[P3].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2010-2021: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2009-2015
    slope, intercept, r, p, se = linregress(RWSoCa[L0]['datenum'], RWSoCa[L0]['calcium_corrected']) 
    xbegin = RWSoCa[L0].datenum.min() 
    xend = RWSoCa[L0].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2009-2015: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2015-2017
    slope, intercept, r, p, se = linregress(RWSoCa[L1]['datenum'], RWSoCa[L1]['calcium_corrected']) 
    xbegin = RWSoCa[L1].datenum.min() 
    xend = RWSoCa[L1].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2015-2017: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2017-2018
    slope, intercept, r, p, se = linregress(RWSoCa[L2]['datenum'], RWSoCa[L2]['calcium_corrected']) 
    xbegin = RWSoCa[L2].datenum.min() 
    xend = RWSoCa[L2].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2017-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    