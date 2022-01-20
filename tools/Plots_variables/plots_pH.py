
def get_pH_plots(RWSomean, RWSnmean):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    RWSomeanpH = RWSomean.dropna(axis='rows', how='all', subset=['pH_total'])
    RWSnmeanpH = RWSnmean.dropna(axis='rows', how='all', subset=['pH_total_spectro_out'])
    
    #%% # pH - Time - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('datenum', 'pH_total', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    ax.scatter('datenum', 'pH_total_spectro_out', c='xkcd:dark aqua', data=RWSnmean, label='RWS$_{spectro}$', s=20, alpha=0.4)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_mean_time_datasets_RWS.png")
    plt.show()

    #%% # pH - Time - Seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
    sc = ax.scatter('datenum', 'pH_total_spectro_out', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSnmean, s=20)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Seasons North Sea') 

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/pH_mean_time_seasons_RWS.png")
    plt.show()

    #%% # pH - Time - Regions

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    x = RWSomean['datenum']
    y = RWSomean['pH_total']

    L0 = (RWSomean['distance_to_shore'] > 0) & (RWSomean['distance_to_shore'] <=4)
    L1 = (RWSomean['distance_to_shore'] > 4) & (RWSomean['distance_to_shore'] <=10)
    L2 = (RWSomean['distance_to_shore'] > 10) & (RWSomean['distance_to_shore'] <=20)
    L3 = (RWSomean['distance_to_shore'] > 20) & (RWSomean['distance_to_shore'] <=30)
    L4 = (RWSomean['distance_to_shore'] > 30) & (RWSomean['distance_to_shore'] <=50)
    L5 = (RWSomean['distance_to_shore'] > 50) & (RWSomean['distance_to_shore'] <=70)
    L6 = (RWSomean['distance_to_shore'] > 70) & (RWSomean['distance_to_shore'] <=100)
    L7 = (RWSomean['distance_to_shore'] > 100) & (RWSomean['distance_to_shore'] <=150)
    L8 = (RWSomean['distance_to_shore'] > 150) & (RWSomean['distance_to_shore'] <=200)
    L9 = (RWSomean['distance_to_shore'] > 200) & (RWSomean['distance_to_shore'] <=250)
    L10 = (RWSomean['distance_to_shore'] > 250) & (RWSnmean['distance_to_shore'] <=300)

    ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")

    x = RWSnmean['datenum']
    y = RWSnmean['pH_total_spectro_out']

    L0 = (RWSnmean['distance_to_shore'] > 0) & (RWSnmean['distance_to_shore'] <=4)
    L1 = (RWSnmean['distance_to_shore'] > 4) & (RWSnmean['distance_to_shore'] <=10)
    L2 = (RWSnmean['distance_to_shore'] > 10) & (RWSnmean['distance_to_shore'] <=20)
    L3 = (RWSnmean['distance_to_shore'] > 20) & (RWSnmean['distance_to_shore'] <=30)
    L4 = (RWSnmean['distance_to_shore'] > 30) & (RWSnmean['distance_to_shore'] <=50)
    L5 = (RWSnmean['distance_to_shore'] > 50) & (RWSnmean['distance_to_shore'] <=70)
    L6 = (RWSnmean['distance_to_shore'] > 70) & (RWSnmean['distance_to_shore'] <=100)
    L7 = (RWSnmean['distance_to_shore'] > 100) & (RWSnmean['distance_to_shore'] <=150)
    L8 = (RWSnmean['distance_to_shore'] > 150) & (RWSnmean['distance_to_shore'] <=200)
    L9 = (RWSnmean['distance_to_shore'] > 200) & (RWSnmean['distance_to_shore'] <=250)
    L10 = (RWSnmean['distance_to_shore'] > 250) & (RWSnmean['distance_to_shore'] <=300)

    ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Regions North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_mean_time_regions_RWS.png")
    plt.show()

    #%% # pH - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter("dayofyear", "pH_total", c="xkcd:aqua", data=RWSomean, label='RWS', s=20, alpha=0.4)
    ax.scatter('dayofyear', 'pH_total_spectro_out', c='xkcd:dark aqua', data=RWSnmean, label='RWS$_{spectro}$', s=20, alpha=0.4)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)

    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_mean_dayofyear_datasets_RWS.png")
    plt.show()

    #%% # pH - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    x = RWSomean['dayofyear']
    y = RWSomean['pH_total']

    L0 = (RWSomean['distance_to_shore'] > 0) & (RWSomean['distance_to_shore'] <=4)
    L1 = (RWSomean['distance_to_shore'] > 4) & (RWSomean['distance_to_shore'] <=10)
    L2 = (RWSomean['distance_to_shore'] > 10) & (RWSomean['distance_to_shore'] <=20)
    L3 = (RWSomean['distance_to_shore'] > 20) & (RWSomean['distance_to_shore'] <=30)
    L4 = (RWSomean['distance_to_shore'] > 30) & (RWSomean['distance_to_shore'] <=50)
    L5 = (RWSomean['distance_to_shore'] > 50) & (RWSomean['distance_to_shore'] <=70)
    L6 = (RWSomean['distance_to_shore'] > 70) & (RWSomean['distance_to_shore'] <=100)
    L7 = (RWSomean['distance_to_shore'] > 100) & (RWSomean['distance_to_shore'] <=150)
    L8 = (RWSomean['distance_to_shore'] > 150) & (RWSomean['distance_to_shore'] <=200)
    L9 = (RWSomean['distance_to_shore'] > 200) & (RWSomean['distance_to_shore'] <=250)
    L10 = (RWSomean['distance_to_shore'] > 250) & (RWSnmean['distance_to_shore'] <=300)

    ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")

    x = RWSnmean['dayofyear']
    y = RWSnmean['pH_total_spectro_out']

    L0 = (RWSnmean['distance_to_shore'] > 0) & (RWSnmean['distance_to_shore'] <=4)
    L1 = (RWSnmean['distance_to_shore'] > 4) & (RWSnmean['distance_to_shore'] <=10)
    L2 = (RWSnmean['distance_to_shore'] > 10) & (RWSnmean['distance_to_shore'] <=20)
    L3 = (RWSnmean['distance_to_shore'] > 20) & (RWSnmean['distance_to_shore'] <=30)
    L4 = (RWSnmean['distance_to_shore'] > 30) & (RWSnmean['distance_to_shore'] <=50)
    L5 = (RWSnmean['distance_to_shore'] > 50) & (RWSnmean['distance_to_shore'] <=70)
    L6 = (RWSnmean['distance_to_shore'] > 70) & (RWSnmean['distance_to_shore'] <=100)
    L7 = (RWSnmean['distance_to_shore'] > 100) & (RWSnmean['distance_to_shore'] <=150)
    L8 = (RWSnmean['distance_to_shore'] > 150) & (RWSnmean['distance_to_shore'] <=200)
    L9 = (RWSnmean['distance_to_shore'] > 200) & (RWSnmean['distance_to_shore'] <=250)
    L10 = (RWSnmean['distance_to_shore'] > 250) & (RWSnmean['distance_to_shore'] <=300)

    ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
    ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
    ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
    ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
    ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
    ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
    ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
    ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
    ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
    ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
    ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Regions North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_mean_dayofyear_regions_RWS.png")
    plt.show()

    #%% # pH - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300)

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax = ax
    sc = ax.scatter('dayofyear', 'pH_total', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
    sc = ax.scatter('dayofyear', 'pH_total_spectro_out', c='year', data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Year North Sea') 

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/pH_mean_dayofyear_year_RWS.png")
    plt.show()

    #%% # pH - Regions - Datasets

    fig, ax = plt.subplots(dpi=300)

    slope, intercept, r, p, se = linregress(RWSomeanpH['distance_to_shore'], RWSomeanpH['pH_total'])
    ax = ax
    #ax.scatter("distance_to_shore", "pH_total", c="xkcd:aqua", data=RWSomean, label='RWS', s=20, alpha=0.4)
    #ax.scatter('distance_to_shore', 'pH_total_spectro_out', c='xkcd:dark aqua', data=RWSnmean, label='RWS$_{spectro}$', s=20, alpha=0.4)
    sns.regplot(x='distance_to_shore', y='pH_total', data=RWSomean, ax=ax,
            scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial pH RWS')
   
    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Datasets North Sea') 

    plt.tight_layout()
    #plt.savefig("figures/pH_mean_regions_datasets_RWS.png")
    plt.show()

    #%% # pH - Regions - Seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
    sc = ax.scatter('distance_to_shore', 'pH_total_spectro_out', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSnmean, s=20)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Seasons North Sea') 

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/pH_mean_regions_seasons_RWSn.png")
    plt.show()

    #%% # pH - Regions - Year

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax = ax
    sc = ax.scatter('distance_to_shore', 'pH_total', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
    sc = ax.scatter('distance_to_shore', 'pH_total_spectro_out', c='year', data=RWSnmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.set_ylabel("pH")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH RWS data - Year North Sea') 

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/pH_mean_regions_year_RWS.png")
    plt.show()

    #%% # Long Term Trend of pH RWSomean

    print('Long term trend of pH RWSomean')

    L0 = (RWSomean.year <= 1985)
    L1 = (RWSomean.year >= 1985) & (RWSomean.year <= 2010)
    L2 = (RWSomean.year >= 2010)
            
    slope, intercept, r, p, se = linregress(RWSomeanpH['datenum'], RWSomeanpH['pH_total'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])
    print("Linear regression Initial Spectro data")
    print(f"Slope: {nslope:.6e}")
    print(f"Intercept: {nintercept:.6e}")
    print(f"R-value: {nr:.6e}")
    print(f"R-squared: {nr**2:.6e}")
    print(f"P-value: {np:.6e}")
    print(f"Standard error: {nse:.6e}")
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))

    ax = ax
    sns.regplot(x='datenum', y='pH_total', data=RWSomean, ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial pH RWS')
    sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
                scatter_kws={"color": "xkcd:cobalt blue"}, line_kws={"color": "xkcd:cobalt blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.2f}'}, label='Initial pH$_{spectro}$ RWS')
    
    ax.set_title("pH RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('pH')
    ax.set_ylim(7.15, 9.10)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/pH_fitting_RWSomean.png")    
    plt.show()

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of pH RWSomean (splitting up)

    L0 = (RWSomean.year <= 1985)
    L1 = (RWSomean.year >= 1985) & (RWSomean.year <= 2010)
    L2 = (RWSomean.year >= 2010)

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWSomean[L0]['datenum'], RWSomean[L0]['pH_total'])

    ax = axs[0]
    sns.regplot(x='datenum', y='pH_total', data=RWSomean[L0], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial pH RWS')

    ax.set_title("pH RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('pH')
    ax.set_ylim(7.15, 9.10)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomean[L1]['datenum'], RWSomean[L1]['pH_total'])

    ax = axs[1]
    sns.regplot(x='datenum', y='pH_total', data=RWSomean[L1], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial pH RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('pH')
    ax.set_ylim(7.15, 9.10)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomean[L2]['datenum'], RWSomean[L2]['pH_total'])
    nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

    ax = axs[2]
    sns.regplot(x='datenum', y='pH_total', data=RWSomean[L2], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial pH RWS')
    sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
                scatter_kws={"color": "xkcd:cobalt blue"}, line_kws={"color": "xkcd:cobalt blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.1f}'}, label='Initial pH$_{spectro}$ RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('pH')
    ax.set_ylim(7.15, 9.10)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/pH_split_up_RWSomean.png")     
    plt.show()
    
    #%% # Long Term Trend of pH RWSomean (splitting LR up)
    
    L0 = (RWSomeanpH.year <= 1985)
    L1 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
    L2 = (RWSomeanpH.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    slope, intercept, r, p, se = linregress(RWSomeanpH[L0]['datenum'], RWSomeanpH[L0]['pH_total'])
    aslope, aintercept, ar, ap, ase = linregress(RWSomeanpH[L1]['datenum'], RWSomeanpH[L1]['pH_total'])
    bslope, bintercept, br, bp, bse = linregress(RWSomeanpH[L2]['datenum'], RWSomeanpH[L2]['pH_total'])    
    nslope, nintercept, nr, np, nse = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out'])

    ax = ax
    sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L0], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial pH RWS')
    sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L1], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='pH_total', data=RWSomeanpH[L2], ax=ax,
                scatter_kws={"color": "xkcd:water blue"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    sns.regplot(x='datenum', y='pH_total_spectro_out', data=RWSnmean, ax=ax,
                scatter_kws={"color": "xkcd:cobalt blue"}, line_kws={"color": "xkcd:cobalt blue", 'linestyle': 'dashdot', 'label': f'y = {nslope:.1e}x + {nintercept:.1f}'}, label='Initial pH$_{spectro}$ RWS')
    
    ax.set_title("pH RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('pH')
    ax.set_ylim(7.15, 9.10)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())

    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/pH_split_up_RWSomeanpH2.png")     
    plt.show()
    
#%% # Change per year and period
    
    P1 = (RWSomeanpH.year <= 1985)
    P2 = (RWSomeanpH.year >= 1985) & (RWSomeanpH.year <= 2010)
    P3 = (RWSomeanpH.year >= 2010)
    P4 = (RWSomeanpH.year >= 2000)
    
    # Total 1975-2018 
    slope, intercept, r, p, se = linregress(RWSomeanpH['datenum'], RWSomeanpH['pH_total']) 
    xbegin = RWSomeanpH.datenum.min() 
    xend = RWSomeanpH.datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Total 1975-1985
    slope, intercept, r, p, se = linregress(RWSomeanpH[P1]['datenum'], RWSomeanpH[P1]['pH_total']) 
    xbegin = RWSomeanpH[P1].datenum.min() 
    xend = RWSomeanpH[P1].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-1985: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Total 1985-2010 
    slope, intercept, r, p, se = linregress(RWSomeanpH[P2]['datenum'], RWSomeanpH[P2]['pH_total']) 
    xbegin = RWSomeanpH[P2].datenum.min() 
    xend = RWSomeanpH[P2].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1985-2010: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2010-2018
    slope, intercept, r, p, se = linregress(RWSomeanpH[P3]['datenum'], RWSomeanpH[P3]['pH_total']) 
    xbegin = RWSomeanpH[P3].datenum.min() 
    xend = RWSomeanpH[P3].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2010-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2018-2021
    slope, intercept, r, p, se = linregress(RWSnmeanpH['datenum'], RWSnmeanpH['pH_total_spectro_out']) 
    xbegin = RWSnmeanpH.datenum.min() 
    xend = RWSnmeanpH.datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2018-2021: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")

    # Total 2000-2018
    slope, intercept, r, p, se = linregress(RWSomeanpH[P4]['datenum'], RWSomeanpH[P4]['pH_total']) 
    xbegin = RWSomeanpH[P4].datenum.min() 
    xend = RWSomeanpH[P4].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2000-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")