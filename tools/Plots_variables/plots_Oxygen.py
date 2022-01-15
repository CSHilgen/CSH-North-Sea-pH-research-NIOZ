
def get_oxygen_plots(RWSomean, RWSomeano2):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    import tools.seasonalfitting as SF_tools
    
    #%% # Oxygen - Time - Datasets - LINEAR REGRESSION

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg'])

    ax = ax
    ax.scatter('datenum', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomeano2, label='RWS', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2, ax=ax,
                scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_time_datasets_LR.png")
    plt.show()

    #%% # Oxygen - Time - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('datenum', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomeano2, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_time_datasets.png")
    plt.show()

    #%% # Oxygen - Time - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'oxygen umol/kg', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomeano2, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/O2_mean_time_seasons.png")
    plt.show()

    #%% # Oxygen - Time - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = RWSomeano2['datenum']
    y = RWSomeano2['oxygen umol/kg']

    L0 = (RWSomeano2['distance_to_shore'] > 0) & (RWSomeano2['distance_to_shore'] <=4)
    L1 = (RWSomeano2['distance_to_shore'] > 4) & (RWSomeano2['distance_to_shore'] <=10)
    L2 = (RWSomeano2['distance_to_shore'] > 10) & (RWSomeano2['distance_to_shore'] <=20)
    L3 = (RWSomeano2['distance_to_shore'] > 20) & (RWSomeano2['distance_to_shore'] <=30)
    L4 = (RWSomeano2['distance_to_shore'] > 30) & (RWSomeano2['distance_to_shore'] <=50)
    L5 = (RWSomeano2['distance_to_shore'] > 50) & (RWSomeano2['distance_to_shore'] <=70)
    L6 = (RWSomeano2['distance_to_shore'] > 70) & (RWSomeano2['distance_to_shore'] <=100)
    L7 = (RWSomeano2['distance_to_shore'] > 100) & (RWSomeano2['distance_to_shore'] <=150)
    L8 = (RWSomeano2['distance_to_shore'] > 150) & (RWSomeano2['distance_to_shore'] <=200)
    L9 = (RWSomeano2['distance_to_shore'] > 200) & (RWSomeano2['distance_to_shore'] <=250)
    L10 = (RWSomeano2['distance_to_shore'] > 250) & (RWSomeano2['distance_to_shore'] <=300)

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
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Oxygen RWSo data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_time_regions.png")
    plt.show()

    #%% # Oxygen - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('dayofyear', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomeano2, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
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
    ax.set_title('Oxygen RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_dayofyear_datasets.png")
    plt.show()

    #%% # Oxygen - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = RWSomeano2['dayofyear']
    y = RWSomeano2['oxygen umol/kg']

    L0 = (RWSomeano2['distance_to_shore'] > 0) & (RWSomeano2['distance_to_shore'] <=4)
    L1 = (RWSomeano2['distance_to_shore'] > 4) & (RWSomeano2['distance_to_shore'] <=10)
    L2 = (RWSomeano2['distance_to_shore'] > 10) & (RWSomeano2['distance_to_shore'] <=20)
    L3 = (RWSomeano2['distance_to_shore'] > 20) & (RWSomeano2['distance_to_shore'] <=30)
    L4 = (RWSomeano2['distance_to_shore'] > 30) & (RWSomeano2['distance_to_shore'] <=50)
    L5 = (RWSomeano2['distance_to_shore'] > 50) & (RWSomeano2['distance_to_shore'] <=70)
    L6 = (RWSomeano2['distance_to_shore'] > 70) & (RWSomeano2['distance_to_shore'] <=100)
    L7 = (RWSomeano2['distance_to_shore'] > 100) & (RWSomeano2['distance_to_shore'] <=150)
    L8 = (RWSomeano2['distance_to_shore'] > 150) & (RWSomeano2['distance_to_shore'] <=200)
    L9 = (RWSomeano2['distance_to_shore'] > 200) & (RWSomeano2['distance_to_shore'] <=250)
    L10 = (RWSomeano2['distance_to_shore'] > 250) & (RWSomeano2['distance_to_shore'] <=300)

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
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
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
    ax.set_title('Oxygen RWSo data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_dayofyear_regions.png")
    plt.show()

    #%% Oxygen - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax=ax
    sc = ax.scatter('dayofyear', 'oxygen umol/kg',  c="year", data=RWSomeano2, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    ax.grid(alpha=0.3)
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
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
    ax.set_title('Oxygen RWSo data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_dayofyear_year.png")
    plt.show()

    #%% # Oxygen - Regions - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('distance_to_shore', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomeano2, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_regions_datasets.png")
    plt.show()

    #%% # Oxygen - Regions - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'oxygen umol/kg', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomeano2, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Oxygen (µmol/kg)")
    ax.set_ylim(175, 425)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/O2_mean_regions_seasons.png")
    plt.show()

    #%% Oxygen - Regions - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax=ax
    sc = ax.scatter('distance_to_shore', 'oxygen umol/kg',  c="year", data=RWSomeano2, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    ax.grid(alpha=0.3)
    ax.set_xlabel('Distance to shore (km)')
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Oxygen RWSo data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/O2_mean_regions_year.png")
    plt.show()

    #%% # Long Term Trend of Oxygen RWSomeano2

    print('Long term trend of Oxygen RWSomeano2')

    opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                               args=(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg']))
    slope, intercept, sine_stretch, sine_shift = opt_result['x']
    
    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)
    
    slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")
    
    ax = axs[0]
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial O$_2$ RWS')

    ax.set_title("Oxygen RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['sc_oxygen umol/kg'])
    print("Linear regression Seasonality Curve")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[1]
    RWSomeano2.plot.scatter("datenum", "oxygen umol/kg", ax=ax, c='xkcd:green', label='Initial O$_2$ RWS')

    fx = np.linspace(RWSomeano2.datenum.min(), RWSomeano2.datenum.max(), 1000)
    fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
    fx_datetime = mdates.num2date(fx)
    ax.plot(fx, fy, 'g', label='Seasonal cycle') 

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['ms_oxygen umol/kg'])
    print("Linear regression Minus Seasonality")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[2]
    sns.regplot(x='datenum', y='ms_oxygen umol/kg', data=RWSomeano2, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1e}'}, label='Seasonal corrected O$_2$ RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Oxygen_season_fitting_RWSomeano2.png")    
    plt.show()

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of Oxygen RWSomeano2 (splitting up)

    L0 = (RWSomeano2.year <= 1985)
    L1 = (RWSomeano2.year >= 1985) & (RWSomeano2.year <= 2010)
    L2 = (RWSomeano2.year >= 2010)

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWSomeano2[L0]['datenum'], RWSomeano2[L0]['oxygen umol/kg'])

    ax = axs[0]
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L0], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial O$_2$ RWS')

    ax.set_title("Oxygen RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeano2[L1]['datenum'], RWSomeano2[L1]['oxygen umol/kg'])

    ax = axs[1]
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L1], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial O$_2$ RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeano2[L2]['datenum'], RWSomeano2[L2]['oxygen umol/kg'])

    ax = axs[2]
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L2], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.2f}'}, label='Initial O$_2$ RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Oxygen_split_up_RWSomeano2.png")     
    plt.show()

    #%% # Long Term Trend of Oxygen RWSomeano2 (splitting LR up)
    
    L0 = (RWSomeano2.year <= 1985)
    L1 = (RWSomeano2.year >= 1985) & (RWSomeano2.year <= 2010)
    L2 = (RWSomeano2.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    slope, intercept, r, p, se = linregress(RWSomeano2[L0]['datenum'], RWSomeano2[L0]['oxygen umol/kg'])
    aslope, aintercept, ar, ap, ase = linregress(RWSomeano2[L1]['datenum'], RWSomeano2[L1]['oxygen umol/kg'])
    bslope, bintercept, br, bp, bse = linregress(RWSomeano2[L2]['datenum'], RWSomeano2[L2]['oxygen umol/kg'])    
    
    ax = ax
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L0], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial O$_2$ RWS')
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L1], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='oxygen umol/kg', data=RWSomeano2[L2], ax=ax,
                scatter_kws={"color": "xkcd:green"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("Oxygen RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Oxygen_split_up_RWSomeano22.png")     
    plt.show()

#%% # Change per year and period
    
    P1 = (RWSomeano2.year <= 1985)
    P2 = (RWSomeano2.year >= 1985) & (RWSomeano2.year <= 2010)
    P3 = (RWSomeano2.year >= 2010)
    P4 = (RWSomeano2.year >= 2000)
    
    # Total 1975-2018 
    slope, intercept, r, p, se = linregress(RWSomeano2['datenum'], RWSomeano2['oxygen umol/kg']) 
    xbegin = RWSomeano2.datenum.min() 
    xend = RWSomeano2.datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Total 1975-1985
    slope, intercept, r, p, se = linregress(RWSomeano2[P1]['datenum'], RWSomeano2[P1]['oxygen umol/kg']) 
    xbegin = RWSomeano2[P1].datenum.min() 
    xend = RWSomeano2[P1].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-1985: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
    
    # Total 1985-2010 
    slope, intercept, r, p, se = linregress(RWSomeano2[P2]['datenum'], RWSomeano2[P2]['oxygen umol/kg']) 
    xbegin = RWSomeano2[P2].datenum.min() 
    xend = RWSomeano2[P2].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1985-2010: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2010-2018
    slope, intercept, r, p, se = linregress(RWSomeano2[P3]['datenum'], RWSomeano2[P3]['oxygen umol/kg']) 
    xbegin = RWSomeano2[P3].datenum.min() 
    xend = RWSomeano2[P3].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2010-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")

    # Total 2000-2018
    slope, intercept, r, p, se = linregress(RWSomeano2[P4]['datenum'], RWSomeano2[P4]['oxygen umol/kg']) 
    xbegin = RWSomeano2[P4].datenum.min() 
    xend = RWSomeano2[P4].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2000-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")