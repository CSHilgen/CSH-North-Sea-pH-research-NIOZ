
def get_temperature_plots(RWStotalmean, RWStotalmeanT, RWSomean, RWSnmean):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    import tools.seasonalfitting as SF_tools

    #%% # Temperature - Time - Datasets - LINEAR REGRESSION

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])

    ax = ax
    ax.scatter('datenum', 'temperature', c='xkcd:aqua', data=RWStotalmean, label='RWS', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='temperature', data=RWStotalmean, ax=ax,
                scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.4f}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_time_datasets_LR.png")
    plt.show()

    #%% # Temperature - Time - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('datenum', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    ax.scatter('datenum', 'temperature', c='xkcd:dark aqua', data=RWSnmean, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_time_datasets.png")
    plt.show()

    #%% # Temperature - Time - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWStotalmean, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Temperature (°C)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Seasons North Sea')

    fig.subplots_adjust(right=1.2)
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/T_mean_time_seasons.png")
    plt.show()

    #%% # Temperature - Time - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = RWStotalmean['datenum']
    y = RWStotalmean['temperature']

    L0 = (RWStotalmean['distance_to_shore'] > 0) & (RWStotalmean['distance_to_shore'] <=4)
    L1 = (RWStotalmean['distance_to_shore'] > 4) & (RWStotalmean['distance_to_shore'] <=10)
    L2 = (RWStotalmean['distance_to_shore'] > 10) & (RWStotalmean['distance_to_shore'] <=20)
    L3 = (RWStotalmean['distance_to_shore'] > 20) & (RWStotalmean['distance_to_shore'] <=30)
    L4 = (RWStotalmean['distance_to_shore'] > 30) & (RWStotalmean['distance_to_shore'] <=50)
    L5 = (RWStotalmean['distance_to_shore'] > 50) & (RWStotalmean['distance_to_shore'] <=70)
    L6 = (RWStotalmean['distance_to_shore'] > 70) & (RWStotalmean['distance_to_shore'] <=100)
    L7 = (RWStotalmean['distance_to_shore'] > 100) & (RWStotalmean['distance_to_shore'] <=150)
    L8 = (RWStotalmean['distance_to_shore'] > 150) & (RWStotalmean['distance_to_shore'] <=200)
    L9 = (RWStotalmean['distance_to_shore'] > 200) & (RWStotalmean['distance_to_shore'] <=250)
    L10 = (RWStotalmean['distance_to_shore'] > 250) & (RWStotalmean['distance_to_shore'] <=300)

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
    ax.set_ylabel('Temperature (°C)')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Temperature RWS data - Regions North Sea')

    #plt.tight_layout()
    plt.savefig("figures/T_mean_time_regions.png")
    plt.show()

    #%% # Temperature - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('dayofyear', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    ax.scatter('dayofyear', 'temperature', c='xkcd:dark aqua', data=RWSnmean, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.set_ylabel("Temperature (°C)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_dayofyear_datasets.png")
    plt.show()

    #%% # Temperature - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = RWStotalmean['dayofyear']
    y = RWStotalmean['temperature']

    L0 = (RWStotalmean['distance_to_shore'] > 0) & (RWStotalmean['distance_to_shore'] <=4)
    L1 = (RWStotalmean['distance_to_shore'] > 4) & (RWStotalmean['distance_to_shore'] <=10)
    L2 = (RWStotalmean['distance_to_shore'] > 10) & (RWStotalmean['distance_to_shore'] <=20)
    L3 = (RWStotalmean['distance_to_shore'] > 20) & (RWStotalmean['distance_to_shore'] <=30)
    L4 = (RWStotalmean['distance_to_shore'] > 30) & (RWStotalmean['distance_to_shore'] <=50)
    L5 = (RWStotalmean['distance_to_shore'] > 50) & (RWStotalmean['distance_to_shore'] <=70)
    L6 = (RWStotalmean['distance_to_shore'] > 70) & (RWStotalmean['distance_to_shore'] <=100)
    L7 = (RWStotalmean['distance_to_shore'] > 100) & (RWStotalmean['distance_to_shore'] <=150)
    L8 = (RWStotalmean['distance_to_shore'] > 150) & (RWStotalmean['distance_to_shore'] <=200)
    L9 = (RWStotalmean['distance_to_shore'] > 200) & (RWStotalmean['distance_to_shore'] <=250)
    L10 = (RWStotalmean['distance_to_shore'] > 250) & (RWStotalmean['distance_to_shore'] <=300)

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
    ax.set_ylabel('Temperature (°C)')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Temperature RWS data - Regions North Sea')

    # plt.tight_layout()
    plt.savefig("figures/T_mean_dayofyear_regions.png")
    plt.show()

    #%% Temperature - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1970
    vmax = 2021

    ax=ax
    sc = ax.scatter('dayofyear', 'temperature',  c="year", data=RWStotalmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 6)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1970, 1980, 1990, 2000, 2010, 2020])

    ax.grid(alpha=0.3)
    ax.set_ylabel('Temperature (°C)')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.set_title('Temperature RWS data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_dayofyear_year.png")
    plt.show()

    #%% # Temperature - Regions - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('distance_to_shore', 'temperature', c='xkcd:aqua', data=RWSomean, label='RWS', s=20, alpha=0.4)
    ax.scatter('distance_to_shore', 'temperature', c='xkcd:dark aqua', data=RWSnmean, label='RWS', s=20, alpha=0.4)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_regions_datasets.png")
    plt.show()

    #%% # Temperature - Regions - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'temperature', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWStotalmean, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Temperature (°C)")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Seasons North Sea')

    fig.subplots_adjust(right=1.2)
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/T_mean_regions_seasons.png")
    plt.show()

    #%% Temperature - Regions - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1970
    vmax = 2021

    ax=ax
    sc = ax.scatter('distance_to_shore', 'temperature',  c="year", data=RWStotalmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 6)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1970, 1980, 1990, 2000, 2010, 2020])

    ax.grid(alpha=0.3)
    ax.set_xlabel('Day of Year')
    ax.set_ylabel('Temperature (°C)')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim(0, 22)
    ax.set_title('Temperature RWS data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/T_mean_regions_year.png")
    plt.show()

    #%% # Long Term Trend of Temperature RWStotalmean

    print('Long term trend of Temperature RWStotalmean')

    opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_T, [0.006, 386, 162, 680], 
                               args=(RWStotalmeanT['datenum'], RWStotalmeanT['temperature']))
    slope, intercept, sine_stretch, sine_shift = opt_result['x']
        
    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)
   
    slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")
    
    ax = axs[0]
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial T RWS')

    ax.set_title("Temperature RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    # slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['sc_temperature'])
    print("Linear regression Seasonality Curve")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[1]
    RWStotalmeanT.plot.scatter("datenum", "temperature", ax=ax, c='xkcd:pink', label='Initial T RWS')

    fx = np.linspace(RWStotalmeanT.datenum.min(), RWStotalmeanT.datenum.max(), 1000)
    fy = SF_tools.seasonalcycle_fit_T(opt_result['x'], fx)
    fx_datetime = mdates.num2date(fx)
    ax.plot(fx, fy, 'g', label='Seasonal cycle') 

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    # slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['ms_temperature'])
    print("Linear regression Minus Seasonality")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[2]
    sns.regplot(x='datenum', y='ms_temperature', data=RWStotalmeanT, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1f}'}, label='Seasonal corrected T RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Temperature (°C)')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Temperature_season_fitting_RWStotalmeanT.png")    
    plt.show()

    # Temperature 1975-2021 
    xbegin = 1976
    xend = 18808
    slope, intercept, r, p, se = linregress(RWStotalmeanT['datenum'], RWStotalmeanT['temperature'])
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-2021: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of Temperature RWStotalmeanT (splitting up)

    L0 = (RWStotalmeanT.year <= 1985)
    L1 = (RWStotalmeanT.year >= 1985) & (RWStotalmeanT.year <= 2010)
    L2 = (RWStotalmeanT.year >= 2010)

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWStotalmeanT[L0]['datenum'], RWStotalmeanT[L0]['temperature'])

    ax = axs[0]
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L0], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial T RWS')

    ax.set_title("Temperature RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWStotalmeanT[L1]['datenum'], RWStotalmeanT[L1]['temperature'])

    ax = axs[1]
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L1], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial T RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWStotalmeanT[L2]['datenum'], RWStotalmeanT[L2]['temperature'])

    ax = axs[2]
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L2], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial T RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Temperature_split_up_RWStotalmeanT.png")     
    plt.show()

    #%% # Long Term Trend of temperature RWStotalmeanT (splitting LR up)
    
    L0 = (RWStotalmeanT.year <= 1985)
    L1 = (RWStotalmeanT.year >= 1985) & (RWStotalmeanT.year <= 2010)
    L2 = (RWStotalmeanT.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    slope, intercept, r, p, se = linregress(RWStotalmeanT[L0]['datenum'], RWStotalmeanT[L0]['temperature'])
    aslope, aintercept, ar, ap, ase = linregress(RWStotalmeanT[L1]['datenum'], RWStotalmeanT[L1]['temperature'])
    bslope, bintercept, br, bp, bse = linregress(RWStotalmeanT[L2]['datenum'], RWStotalmeanT[L2]['temperature'])    
    
    ax = ax
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L0], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial T RWS')
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L1], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='temperature', data=RWStotalmeanT[L2], ax=ax,
                scatter_kws={"color": "xkcd:pink"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("Temperature RWS data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Temperature (°C)')
    ax.set_ylim(0, 22)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Temperature_split_up_RWStotalmeanT2.png")     
    plt.show()