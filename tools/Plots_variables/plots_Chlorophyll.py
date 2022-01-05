
def get_chlorophyll_plots(RWSomean, RWSomeanChl):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    import tools.seasonalfitting as SF_tools

    #%% # Chlorophyll - Time - Datasets - LINEAR REGRESSION

    fig, ax = plt.subplots(dpi=300)

    slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])

    ax = ax
    ax.scatter('datenum', 'chlorophyll', c='xkcd:aqua', data=RWSomeanChl, label='RWS', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl, ax=ax,
                scatter_kws={"color": "xkcd:aqua"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_time_datasets_LR.png")
    plt.show()

    #%% # Chlorophyll - Time - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('datenum', 'chlorophyll', c='xkcd:aqua', data=RWSomeanChl, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_time_datasets.png")
    plt.show()

    #%% # Chlorophyll - Time - Seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'chlorophyll', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomeanChl, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_time_seasons.png")
    plt.show()

    #%% # Chlorophyll - Time - Regions

    fig, ax = plt.subplots(dpi=300)

    ax=ax
    x = RWSomeanChl['datenum']
    y = RWSomeanChl['chlorophyll']

    L0 = (RWSomeanChl['distance_to_shore'] > 0) & (RWSomeanChl['distance_to_shore'] <=4)
    L1 = (RWSomeanChl['distance_to_shore'] > 4) & (RWSomeanChl['distance_to_shore'] <=10)
    L2 = (RWSomeanChl['distance_to_shore'] > 10) & (RWSomeanChl['distance_to_shore'] <=20)
    L3 = (RWSomeanChl['distance_to_shore'] > 20) & (RWSomeanChl['distance_to_shore'] <=30)
    L4 = (RWSomeanChl['distance_to_shore'] > 30) & (RWSomeanChl['distance_to_shore'] <=50)
    L5 = (RWSomeanChl['distance_to_shore'] > 50) & (RWSomeanChl['distance_to_shore'] <=70)
    L6 = (RWSomeanChl['distance_to_shore'] > 70) & (RWSomeanChl['distance_to_shore'] <=100)
    L7 = (RWSomeanChl['distance_to_shore'] > 100) & (RWSomeanChl['distance_to_shore'] <=150)
    L8 = (RWSomeanChl['distance_to_shore'] > 150) & (RWSomeanChl['distance_to_shore'] <=200)
    L9 = (RWSomeanChl['distance_to_shore'] > 200) & (RWSomeanChl['distance_to_shore'] <=250)
    L10 = (RWSomeanChl['distance_to_shore'] > 250) & (RWSomeanChl['distance_to_shore'] <=300)

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
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('Chlorophyll RWSo data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_time_regions.png")
    plt.show()

    #%% # Chlorophyll - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('dayofyear', 'chlorophyll', c='xkcd:aqua', data=RWSomeanChl, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
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
    ax.set_title('Chlorophyll RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_dayofyear_datasets.png")
    plt.show()

    #%% # Chlorophyll - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300)

    ax=ax
    x = RWSomeanChl['dayofyear']
    y = RWSomeanChl['chlorophyll']

    L0 = (RWSomeanChl['distance_to_shore'] > 0) & (RWSomeanChl['distance_to_shore'] <=4)
    L1 = (RWSomeanChl['distance_to_shore'] > 4) & (RWSomeanChl['distance_to_shore'] <=10)
    L2 = (RWSomeanChl['distance_to_shore'] > 10) & (RWSomeanChl['distance_to_shore'] <=20)
    L3 = (RWSomeanChl['distance_to_shore'] > 20) & (RWSomeanChl['distance_to_shore'] <=30)
    L4 = (RWSomeanChl['distance_to_shore'] > 30) & (RWSomeanChl['distance_to_shore'] <=50)
    L5 = (RWSomeanChl['distance_to_shore'] > 50) & (RWSomeanChl['distance_to_shore'] <=70)
    L6 = (RWSomeanChl['distance_to_shore'] > 70) & (RWSomeanChl['distance_to_shore'] <=100)
    L7 = (RWSomeanChl['distance_to_shore'] > 100) & (RWSomeanChl['distance_to_shore'] <=150)
    L8 = (RWSomeanChl['distance_to_shore'] > 150) & (RWSomeanChl['distance_to_shore'] <=200)
    L9 = (RWSomeanChl['distance_to_shore'] > 200) & (RWSomeanChl['distance_to_shore'] <=250)
    L10 = (RWSomeanChl['distance_to_shore'] > 250) & (RWSomeanChl['distance_to_shore'] <=300)

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
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
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
    ax.set_title('Chlorophyll RWSo data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_dayofyear_regions.png")
    plt.show()

    #%% Chlorophyll - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300)

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax=ax
    sc = ax.scatter('dayofyear', 'chlorophyll',  c="year", data=RWSomeanChl, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    ax.grid(alpha=0.3)
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
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
    ax.set_title('Chlorophyll RWSo data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_dayofyear_year.png")
    plt.show()

    #%% # Chlorophyll - Regions - Datasets

    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('distance_to_shore', 'chlorophyll', c='xkcd:aqua', data=RWSomeanChl, label='RWS', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_regions_datasets.png")
    plt.show()

    #%% # Chlorophyll - Regions - Seasons

    fig, ax = plt.subplots(dpi=300)
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'chlorophyll', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomeanChl, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_regions_seasons.png")
    plt.show()

    #%% Chlorophyll - Regions - Year

    fig, ax = plt.subplots(dpi=300)

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1975
    vmax = 2021

    ax=ax
    sc = ax.scatter('distance_to_shore', 'chlorophyll',  c="year", data=RWSomeanChl, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 10)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

    ax.grid(alpha=0.3)
    ax.set_xlabel('Distance to shore (km)')
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Chlorophyll RWSo data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/Chl_mean_regions_year.png")
    plt.show()

    #%% # Long Term Trend of Chlorophyll RWSomeanChl

    print('Long term trend of Chlorophyll RWSomeanChl')

    opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit, [0.006, 386, 162, 680], 
                               args=(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll']))
    slope, intercept, sine_stretch, sine_shift = opt_result['x']

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")
        
    ax = axs[0]
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

    ax.set_title("Chlorophyll RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['sc_chlorophyll'])
    print("Linear regression Seasonality Curve")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[1]
    RWSomeanChl.plot.scatter("datenum", "chlorophyll", ax=ax, c='xkcd:brown', label='Initial Chl RWS')

    fx = np.linspace(RWSomeanChl.datenum.min(), RWSomeanChl.datenum.max(), 1000)
    fy = SF_tools.seasonalcycle_fit(opt_result['x'], fx)
    fx_datetime = mdates.num2date(fx)
    ax.plot(fx, fy, 'g', label='Seasonal cycle') 

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['ms_chlorophyll'])
    print("Linear regression Minus Seasonality")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[2]
    sns.regplot(x='datenum', y='ms_chlorophyll', data=RWSomeanChl, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1e}'}, label='Seasonal corrected Chl RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(-10, 20)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Chlorophyll_season_fitting_RWSomeanChl.png")    
    plt.show()

    # Chlorophyll 1975-2018
    xbegin = 1976
    xend = 17896
    slope, intercept, r, p, se = linregress(RWSomeanChl['datenum'], RWSomeanChl['chlorophyll'])
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1975-2018: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of Chlorophyll RWSomeanChl (splitting up)

    L0 = (RWSomeanChl.year <= 1985)
    L1 = (RWSomeanChl.year >= 1985) & (RWSomeanChl.year <= 2010)
    L2 = (RWSomeanChl.year >= 2010)

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(RWSomeanChl[L0]['datenum'], RWSomeanChl[L0]['chlorophyll'])

    ax = axs[0]
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L0], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

    ax.set_title("Chlorophyll RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeanChl[L1]['datenum'], RWSomeanChl[L1]['chlorophyll'])

    ax = axs[1]
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L1], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(RWSomeanChl[L2]['datenum'], RWSomeanChl[L2]['chlorophyll'])

    ax = axs[2]
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L2], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial Chl RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Chlorophyll_split_up_RWSomeanChl.png")     
    plt.show()

    #%% # Long Term Trend of Chlorophyll RWSomean (splitting LR up)
    
    # Set range of Chl linear regression line below value 15
    L0 = (RWSomeanChl.year <= 1985) & (RWSomeanChl.chlorophyll <= 15)
    L1 = (RWSomeanChl.year >= 1985) & (RWSomeanChl.year <= 2010) & (RWSomeanChl.chlorophyll <= 15)
    L2 = (RWSomeanChl.year >= 2010) & (RWSomeanChl.chlorophyll <= 15)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    slope, intercept, r, p, se = linregress(RWSomeanChl[L0]['datenum'], RWSomeanChl[L0]['chlorophyll'])
    aslope, aintercept, ar, ap, ase = linregress(RWSomeanChl[L1]['datenum'], RWSomeanChl[L1]['chlorophyll'])
    bslope, bintercept, br, bp, bse = linregress(RWSomeanChl[L2]['datenum'], RWSomeanChl[L2]['chlorophyll'])    
    
    ax = ax
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L0], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}', 'linestyle': '--',}, label='Initial Chl RWS')
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L1], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'})
    sns.regplot(x='datenum', y='chlorophyll', data=RWSomeanChl[L2], ax=ax,
                scatter_kws={"color": "xkcd:brown"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    ax.scatter('datenum', 'chlorophyll', c='xkcd:brown', data=RWSomeanChl, label=None)
    
    ax.set_title("Chlorophyll RWSo data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Chlorophyll-a (µg/L)")
    ax.set_ylim(0, 30)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/Chlorophyll_split_up_RWSomeanChl2.png")     
    plt.show()
