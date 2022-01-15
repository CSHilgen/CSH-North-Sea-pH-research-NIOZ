
def get_deltafCO2_plots(socatnsmean, socatnsmeandelta):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    import tools.seasonalfitting as SF_tools

    #%% # fCO2 - Time - Datasets - LINEAR REGRESSION

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])

    ax = ax
    ax.scatter('datenum', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='SOCAT', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmean, ax=ax,
                scatter_kws={"color": "xkcd:goldenrod"}, line_kws={"color": "blue", 'label': f'y = {slope:.4f}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_time_datasets_LR.png")
    plt.show()

    #%% # fCO2 - Time - Datasets 

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('datenum', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='SOCAT', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_time_datasets.png")
    plt.show()

    #%% # fCO2 - Time - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'deltafco2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_time_seasons.png")
    plt.show()

    #%% # fCO2 - Time - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = socatnsmean['datenum']
    y = socatnsmean['deltafco2']

    L0 = (socatnsmean['distance_to_shore'] > 0) & (socatnsmean['distance_to_shore'] <=4)
    L1 = (socatnsmean['distance_to_shore'] > 4) & (socatnsmean['distance_to_shore'] <=10)
    L2 = (socatnsmean['distance_to_shore'] > 10) & (socatnsmean['distance_to_shore'] <=20)
    L3 = (socatnsmean['distance_to_shore'] > 20) & (socatnsmean['distance_to_shore'] <=30)
    L4 = (socatnsmean['distance_to_shore'] > 30) & (socatnsmean['distance_to_shore'] <=50)
    L5 = (socatnsmean['distance_to_shore'] > 50) & (socatnsmean['distance_to_shore'] <=70)
    L6 = (socatnsmean['distance_to_shore'] > 70) & (socatnsmean['distance_to_shore'] <=100)
    L7 = (socatnsmean['distance_to_shore'] > 100) & (socatnsmean['distance_to_shore'] <=150)
    L8 = (socatnsmean['distance_to_shore'] > 150) & (socatnsmean['distance_to_shore'] <=200)
    L9 = (socatnsmean['distance_to_shore'] > 200) & (socatnsmean['distance_to_shore'] <=250)
    L10 = (socatnsmean['distance_to_shore'] > 250) & (socatnsmean['distance_to_shore'] <=300)

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
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Km to shore")
    ax.set_title('ΔfCO$_2$ SOCAT data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_time_regions.png")
    plt.show()

    #%% # fCO2 - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('dayofyear', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='SOCAT', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
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
    ax.set_title('ΔfCO$_2$ SOCAT data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_dayofyear_datasets.png")
    plt.show()

    #%% # fCO2 - Dayofyear - Regions

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax=ax
    x = socatnsmean['dayofyear']
    y = socatnsmean['deltafco2']

    L0 = (socatnsmean['distance_to_shore'] > 0) & (socatnsmean['distance_to_shore'] <=4)
    L1 = (socatnsmean['distance_to_shore'] > 4) & (socatnsmean['distance_to_shore'] <=10)
    L2 = (socatnsmean['distance_to_shore'] > 10) & (socatnsmean['distance_to_shore'] <=20)
    L3 = (socatnsmean['distance_to_shore'] > 20) & (socatnsmean['distance_to_shore'] <=30)
    L4 = (socatnsmean['distance_to_shore'] > 30) & (socatnsmean['distance_to_shore'] <=50)
    L5 = (socatnsmean['distance_to_shore'] > 50) & (socatnsmean['distance_to_shore'] <=70)
    L6 = (socatnsmean['distance_to_shore'] > 70) & (socatnsmean['distance_to_shore'] <=100)
    L7 = (socatnsmean['distance_to_shore'] > 100) & (socatnsmean['distance_to_shore'] <=150)
    L8 = (socatnsmean['distance_to_shore'] > 150) & (socatnsmean['distance_to_shore'] <=200)
    L9 = (socatnsmean['distance_to_shore'] > 200) & (socatnsmean['distance_to_shore'] <=250)
    L10 = (socatnsmean['distance_to_shore'] > 250) & (socatnsmean['distance_to_shore'] <=300)

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
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
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
    ax.set_title('ΔfCO$_2$ SOCAT data - Regions North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_dayofyear_regions.png")
    plt.show()

    #%% fCO2 - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1990
    vmax = 2021

    ax=ax
    sc = ax.scatter('dayofyear', 'deltafco2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 4)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1990, 2000, 2010, 2020])

    ax.grid(alpha=0.3)
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
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
    ax.set_title('ΔfCO$_2$ SOCAT data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_dayofyear_year.png")
    plt.show()

    #%% # fCO2 - Regions - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter('distance_to_shore', 'deltafco2', c='xkcd:goldenrod', data=socatnsmean, label='SOCAT', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_regions_datasets.png")
    plt.show()

    #%% # fCO2 - Regions - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'deltafco2', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=socatnsmean, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.set_ylabel("ΔfCO$_2$ (uatm)")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Seasons North Sea')

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_regions_seasons.png")
    plt.show()

    #%% fCO2 - Regions - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 1990
    vmax = 2021

    ax=ax
    sc = ax.scatter('distance_to_shore', 'deltafco2',  c="year", data=socatnsmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ticks = np.linspace(vmin, vmax, 4)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([1990, 2000, 2010, 2020])

    ax.grid(alpha=0.3)
    ax.set_xlabel('Distance to shore (km)')
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('ΔfCO$_2$ SOCAT data - Year North Sea')

    plt.tight_layout()
    plt.savefig("figures/DeltafCO2_mean_regions_year.png")
    plt.show()

    #%% # Long Term Trend of Delta fCO2 socatnsmean

    print('Long term trend of ΔfCO$_2$ SOCAT')

    opt_result = least_squares(SF_tools.lsq_seasonalcycle_fit_fco2_sea, [0.006, 386, 162, 680], 
                               args=(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']))
    slope, intercept, sine_stretch, sine_shift = opt_result['x']

    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[0]
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial ΔfCO$_2$ SOCAT')

    ax.set_title("ΔfCO$_2$ SOCAT data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.set_ylim(-240, 130)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['sc_deltafco2'])
    print("Linear regression Seasonality Curve")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[1]
    socatnsmeandelta.plot.scatter("datenum", "deltafco2", ax=ax, c='xkcd:dark orange', label='Initial ΔfCO$_2$ SOCAT')

    fx = np.linspace(socatnsmeandelta.datenum.min(), socatnsmeandelta.datenum.max(), 1000)
    fy = SF_tools.seasonalcycle_fit_fco2_sea(opt_result['x'], fx)
    fx_datetime = mdates.num2date(fx) 
    ax.plot(fx, fy, 'g', label='Seasonal cycle') 

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.set_ylim(-240, 130)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['ms_deltafco2'])
    print("Linear regression Minus Seasonality")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    ax = axs[2]
    sns.regplot(x='datenum', y='ms_deltafco2', data=socatnsmeandelta, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1e}'}, label='Seasonal corrected ΔfCO$_2$ SOCAT')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/DeltafCO2_season_fitting_SOCAT.png")    
    plt.show()

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of Delta fCO2 socatnsmeandelta (splitting up)

    L1 = (socatnsmeandelta.year <= 2010)
    L2 = (socatnsmeandelta.year >= 2010)

    fig, axs = plt.subplots(nrows=2, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(socatnsmeandelta[L1]['datenum'], socatnsmeandelta[L1]['deltafco2'])

    ax = axs[0]
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L1], ax=ax,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial ΔfCO$_2$ SOCAT')

    ax.set_title("ΔfCO$_2$ SOCAT data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.set_ylim(-240, 130)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(socatnsmeandelta[L2]['datenum'], socatnsmeandelta[L2]['deltafco2'])

    ax = axs[1]
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L2], ax=ax,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial ΔfCO$_2$ SOCAT')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.set_ylim(-240, 130)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/DeltafCO2_split_up_SOCAT.png")     
    plt.show()
    
    #%% # Long Term Trend of Delta fCO2 socatnsmeandelta (splitting LR up)
    
    L1 = (socatnsmeandelta.year <= 2010)
    L2 = (socatnsmeandelta.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    aslope, aintercept, ar, ap, ase = linregress(socatnsmeandelta[L1]['datenum'], socatnsmeandelta[L1]['deltafco2'])
    bslope, bintercept, br, bp, bse = linregress(socatnsmeandelta[L2]['datenum'], socatnsmeandelta[L2]['deltafco2'])    
    
    ax = ax
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L1], ax=ax,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Initial ΔfCO$_2$ SOCAT')
    sns.regplot(x='datenum', y='deltafco2', data=socatnsmeandelta[L2], ax=ax,
                scatter_kws={"color": "xkcd:dark orange"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("ΔfCO$_2$ SOCAT data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('ΔfCO$_2$ (uatm)')
    ax.set_ylim(-240, 130)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/DeltafCO2_split_up_SOCAT2.png")     
    plt.show()

#%% # Change per year and period
    
    P2 = (socatnsmeandelta.year <= 2010)
    P3 = (socatnsmeandelta.year >= 2010)
    P4 = (socatnsmeandelta.year >= 2000)
    
    # Total 1994-2019 
    slope, intercept, r, p, se = linregress(socatnsmeandelta['datenum'], socatnsmeandelta['deltafco2']) 
    xbegin = socatnsmeandelta.datenum.min() 
    xend = socatnsmeandelta.datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1994-2019: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 
       
    # Total 1994-2010 
    slope, intercept, r, p, se = linregress(socatnsmeandelta[P2]['datenum'], socatnsmeandelta[P2]['deltafco2']) 
    xbegin = socatnsmeandelta[P2].datenum.min() 
    xend = socatnsmeandelta[P2].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 1994-2010: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")
    
    # Total 2010-2019
    slope, intercept, r, p, se = linregress(socatnsmeandelta[P3]['datenum'], socatnsmeandelta[P3]['deltafco2']) 
    xbegin = socatnsmeandelta[P3].datenum.min() 
    xend = socatnsmeandelta[P3].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2010-2019: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")

    # Total 2000-2019
    slope, intercept, r, p, se = linregress(socatnsmeandelta[P4]['datenum'], socatnsmeandelta[P4]['deltafco2']) 
    xbegin = socatnsmeandelta[P4].datenum.min() 
    xend = socatnsmeandelta[P4].datenum.max() 
    
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2000-2019: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}")