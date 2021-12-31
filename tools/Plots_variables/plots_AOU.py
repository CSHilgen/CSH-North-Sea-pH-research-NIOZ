
def get_AOU_plots(RWSomean):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    #%% # Oxygen - Time - Datasets - LINEAR REGRESSION
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    RWSomeanAOU = RWSomean.dropna(axis='rows', how='all', subset=['aou'])
    slope, intercept, r, p, se = linregress(RWSomeanAOU['datenum'], RWSomeanAOU['aou'])
    
    ax = ax
    ax.scatter('datenum', 'aou', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='aou', data=RWSomean, ax=ax,
                scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Datasets North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_time_datasets_LR.png")
    plt.show()
    
    #%% # Oxygen - Time - Datasets
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    ax = ax
    ax.scatter('datenum', 'aou', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Datasets North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_time_datasets.png")
    plt.show()
    
    #%% # Oxygen - Time - Seasons
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')
    
    ax = ax
    sc = ax.scatter('datenum', 'aou', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Seasons North Sea')
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_time_seasons.png")
    plt.show()
    
    #%% # Oxygen - Time - Regions
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    ax=ax
    x = RWSomean['datenum']
    y = RWSomean['aou']
    
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
    L10 = (RWSomean['distance_to_shore'] > 250) & (RWSomean['distance_to_shore'] <=300)
    
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
    
    ax.grid(alpha=0.3)
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('AOU RWS data - Regions North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_time_regions.png")
    plt.show()
    
    #%% # Oxygen - Dayofyear - Datasets
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    ax = ax
    ax.scatter('dayofyear', 'aou', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    
    ax.grid(alpha=0.3)
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Datasets North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_dayofyear_datasets.png")
    plt.show()
    
    #%% # Oxygen - Dayofyear - Regions
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    ax=ax
    x = RWSomean['dayofyear']
    y = RWSomean['aou']
    
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
    L10 = (RWSomean['distance_to_shore'] > 250) & (RWSomean['distance_to_shore'] <=300)
    
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
    
    ax.grid(alpha=0.3)
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('AOU RWS data - Regions North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_dayofyear_regions.png")
    plt.show()
    
    #%% Oxygen - Dayofyear - Year
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021
    
    ax=ax
    sc = ax.scatter('dayofyear', 'aou',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
    
    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
    
    ax.grid(alpha=0.3)
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Year North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_dayofyear_year.png")
    plt.show()
    
    #%% # Oxygen - Regions - Datasets
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    ax = ax
    ax.scatter('distance_to_shore', 'aou', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Datasets North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_regions_datasets.png")
    plt.show()
    
    #%% # Oxygen - Regions - Seasons
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')
    
    ax = ax
    sc = ax.scatter('distance_to_shore', 'aou', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Seasons North Sea')
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_regions_seasons.png")
    plt.show()
    
    #%% Oxygen - Regions - Year
    
    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    
    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021
    
    ax=ax
    sc = ax.scatter('distance_to_shore', 'aou',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
    
    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
    
    ax.grid(alpha=0.3)
    ax.set_xlabel('Distance to shore (km)')
    ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
    ax.set_ylim(-150, 100)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('AOU RWS data - Year North Sea')
    
    plt.tight_layout()
    plt.savefig("figures/AOU_mean_regions_year.png")
    plt.show()
    
    #%% # Long Term Trend of AOU RWSomean
    
    print('Long term trend of AOU RWSomean')
    
    slope, intercept, r, p, se = linregress(RWSomeanAOU['datenum'], RWSomeanAOU['aou'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    ax = ax
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial AOU RWS')
    
    ax.set_title("Apparent Oxygen Utilisation RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('AOU (µmol/kg)')
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/AOU_fitting_RWSomeanAOU.png")    
    plt.show()
    
    # AOU 1975-2018 
    xbegin = 2006
    xend = 17896
    slope, intercept, r, p, se = linregress(RWSomeanAOU['datenum'], RWSomeanAOU['aou'])
    
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-2018: {changelongterm:6e}")
    changeperyear = changelongterm / ((xend-xbegin)/365)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)
    
    #%% # Long Term Trend of AOU RWSomean (splitting up)
    
    L0 = (RWSomeanAOU.year <= 1985)
    L1 = (RWSomeanAOU.year >= 1985) & (RWSomeanAOU.year <= 2010)
    L2 = (RWSomeanAOU.year >= 2010)
    
    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)
    
    slope, intercept, r, p, se = linregress(RWSomeanAOU[L0]['datenum'], RWSomeanAOU[L0]['aou'])
    
    ax = axs[0]
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L0], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial AOU RWS')
    
    ax.set_title("Apparent Oxygen Utilisation RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('AOU (µmol/kg)')
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    slope, intercept, r, p, se = linregress(RWSomeanAOU[L1]['datenum'], RWSomeanAOU[L1]['aou'])
    
    ax = axs[1]
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L1], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial AOU RWS')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('AOU (µmol/kg)')
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    slope, intercept, r, p, se = linregress(RWSomeanAOU[L2]['datenum'], RWSomeanAOU[L2]['aou'])
    
    ax = axs[2]
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L2], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial AOU RWS')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('AOU (µmol/kg)')
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/AOU_split_up_RWSomeanAOU.png")     
    plt.show()
    
    #%% # Long Term Trend of AOU RWSomean (splitting LR up)
    
    L0 = (RWSomeanAOU.year <= 1985)
    L1 = (RWSomeanAOU.year >= 1985) & (RWSomeanAOU.year <= 2010)
    L2 = (RWSomeanAOU.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    slope, intercept, r, p, se = linregress(RWSomeanAOU[L0]['datenum'], RWSomeanAOU[L0]['aou'])
    aslope, aintercept, ar, ap, ase = linregress(RWSomeanAOU[L1]['datenum'], RWSomeanAOU[L1]['aou'])
    bslope, bintercept, br, bp, bse = linregress(RWSomeanAOU[L2]['datenum'], RWSomeanAOU[L2]['aou'])    
    
    ax = ax
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L0], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial AOU RWS')
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L1], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='aou', data=RWSomeanAOU[L2], ax=ax,
                scatter_kws={"color": "xkcd:spring green"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("Apparent Oxygen Utilisation RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('AOU (µmol/kg)')
    ax.set_ylim(-150, 100)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/AOU_split_up_RWSomeanAOU2.png")     
    plt.show()

