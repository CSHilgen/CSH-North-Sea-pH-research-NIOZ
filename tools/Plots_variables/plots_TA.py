
def get_TA_plots(combinedmean, glodapnsmean, Cefasmean, D366mean, RWSnmean):
    
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    import matplotlib.dates as mdates
    from scipy.stats import linregress
    from scipy.optimize import least_squares
    from matplotlib.ticker import FuncFormatter
    from matplotlib.dates import MonthLocator, DateFormatter 
    
    #%% # TA - Time - Datasets - LINEAR REGRESSION LINE

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    combinedmeanTA = combinedmean.dropna(axis='rows', how='all', subset=['alkalinity'])
    slope, intercept, r, p, se = linregress(combinedmeanTA['datenum'], combinedmeanTA['alkalinity'])

    ax = ax
    ax.scatter('datenum', 'alkalinity', c='xkcd:velvet', data=combinedmean, label='Combined', s=20, alpha=0.4)
    sns.regplot(x='datenum', y='alkalinity', data=combinedmean, ax=ax,
                scatter_kws={"color": "xkcd:velvet"}, line_kws={"color": "blue", 'label': f'y = {slope:.2f}x + {intercept:.1f}'})

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Datasets North Sea')

    plt.tight_layout()
    plt.savefig("figures/TA_time_datasets_LR.png")
    plt.show()

    #%% # TA - Time - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter("datenum", "alkalinity", c="xkcd:violet", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
    ax.scatter('datenum', 'alkalinity', c='xkcd:orange', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
    ax.scatter('datenum', 'alkalinity', c='xkcd:neon pink', data=D366mean, label='D366', s=20, alpha=0.4)
    ax.scatter('datenum', 'alkalinity', c='xkcd:evergreen', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/TA_mean_time_datasets_combined.png")
    plt.show()

    #%% # TA - Time - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('datenum', 'alkalinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Seasons North Sea') 

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/TA_mean_time_seasons_combined.png")
    plt.show()

    #%% # TA - Time - Regions

    L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
    L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
    L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
    L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
    L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
    L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
    L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
    L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
    L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
    L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
    L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    x = combinedmean['datenum']
    y = combinedmean['alkalinity']

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

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Regions North Sea') 

    plt.tight_layout()
    plt.savefig("figures/TA_mean_time_regions_combined.png")
    plt.show()

    #%% # TA - Dayofyear - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter("dayofyear", "alkalinity", c="xkcd:violet", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
    ax.scatter('dayofyear', 'alkalinity', c='xkcd:orange', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
    ax.scatter('dayofyear', 'alkalinity', c='xkcd:neon pink', data=D366mean, label='D366', s=20, alpha=0.4)
    ax.scatter('dayofyear', 'alkalinity', c='xkcd:evergreen', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Months of year")
    month_fmt = DateFormatter('%b')
    def m_fmt(x, pos=None):
        return month_fmt(x)[0]

    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(m_fmt))
    ax.set_xlim(0, 365)
    ax.minorticks_on()
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/TA_mean_dayofyear_datasets_combined.png")
    plt.show()

    #%% # TA - Dayofyear - Regions

    L0 = (combinedmean['distance_to_shore'] > 0) & (combinedmean['distance_to_shore'] <=4)
    L1 = (combinedmean['distance_to_shore'] > 4) & (combinedmean['distance_to_shore'] <=10)
    L2 = (combinedmean['distance_to_shore'] > 10) & (combinedmean['distance_to_shore'] <=20)
    L3 = (combinedmean['distance_to_shore'] > 20) & (combinedmean['distance_to_shore'] <=30)
    L4 = (combinedmean['distance_to_shore'] > 30) & (combinedmean['distance_to_shore'] <=50)
    L5 = (combinedmean['distance_to_shore'] > 50) & (combinedmean['distance_to_shore'] <=70)
    L6 = (combinedmean['distance_to_shore'] > 70) & (combinedmean['distance_to_shore'] <=100)
    L7 = (combinedmean['distance_to_shore'] > 100) & (combinedmean['distance_to_shore'] <=150)
    L8 = (combinedmean['distance_to_shore'] > 150) & (combinedmean['distance_to_shore'] <=200)
    L9 = (combinedmean['distance_to_shore'] > 200) & (combinedmean['distance_to_shore'] <=250)
    L10 = (combinedmean['distance_to_shore'] > 250) & (combinedmean['distance_to_shore'] <=300)

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    x = combinedmean['dayofyear']
    y = combinedmean['alkalinity']

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

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
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
    ax.set_title('TA combined data - Regions North Sea') 

    plt.tight_layout()
    plt.savefig("figures/TA_mean_dayofyear_regions_combined.png")
    plt.show()

    #%% # TA - Dayofyear - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021

    ax = ax
    sc = ax.scatter('dayofyear', 'alkalinity', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
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
    ax.set_title('TA combined data - Year North Sea') 

    ticks = np.linspace(vmin, vmax, 5)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/TA_mean_dayofyear_year_combined.png")
    plt.show()

    #%% # TA - Regions - Datasets

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))

    ax = ax
    ax.scatter("distance_to_shore", "alkalinity", c="xkcd:violet", data=glodapnsmean, label='GLODAP', s=20, alpha=0.4)
    ax.scatter('distance_to_shore', 'alkalinity', c='xkcd:orange', data=Cefasmean, label='CEFAS', s=20, alpha=0.4)
    ax.scatter('distance_to_shore', 'alkalinity', c='xkcd:neon pink', data=D366mean, label='D366', s=20, alpha=0.4)
    ax.scatter('distance_to_shore', 'alkalinity', c='xkcd:evergreen', data=RWSnmean, label='RWSn', s=20, alpha=0.4)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/TA_mean_regions_datasets_combined.png")
    plt.show()

    #%% # TA - Regions - Seasons

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('twilight')

    ax = ax
    sc = ax.scatter('distance_to_shore', 'alkalinity', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=combinedmean, s=20)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Seasons North Sea') 

    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)

    plt.tight_layout()
    plt.savefig("figures/TA_mean_regions_seasons_combined.png")
    plt.show()

    #%% # TA - Regions - Year

    fig, ax = plt.subplots(dpi=300, figsize=(5.5,4))
    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021

    ax = ax
    sc = ax.scatter('distance_to_shore', 'alkalinity', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.set_ylabel("Total Alkalinity (µmol/kg)")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Distance to shore (km)")
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('TA combined data - Year North Sea') 

    ticks = np.linspace(vmin, vmax, 5)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/TA_mean_regions_year_combined.png")
    plt.show()

    #%% # Long Term Trend of TA combinedmean

    print('Long term trend of TA Combined')

    combinedmeanNTA = combinedmean.dropna(axis='rows', how='all', subset=['normalized_TA'])
    slope, intercept, r, p, se = linregress(combinedmeanNTA['datenum'], combinedmeanNTA['normalized_TA'])
    print("Linear regression Initial data")
    print(f"Slope: {slope:.6e}")
    print(f"Intercept: {intercept:.6e}")
    print(f"R-value: {r:.6e}")
    print(f"R-squared: {r**2:.6e}")
    print(f"P-value: {p:.6e}")
    print(f"Standard error: {se:.6e}")

    fig, ax = plt.subplots(dpi=300, figsize=(10,6))

    ax = ax
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean, ax=ax, ci=99.9,
                scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Normalized A$_T$ Combined')

    ax.set_title("Normalized TA combined data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Total Alkalinity (µmol/kg)')
    ax.set_ylim(2280, 2430)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/TA_fitting_Combined.png")    
    plt.show()

    # TA 2001-2021
    xbegin = 11565
    xend = 18808
    year = (xend-xbegin) / 365
    print(f"in {year:6f} years")
    ybegin = (slope * xbegin) + intercept
    yend = (slope * xend) + intercept
    changelongterm = yend - ybegin
    print(f"Change over 2001-2021: {changelongterm:6e}")
    changeperyear = changelongterm / (year)
    print(f"Change per year: {changeperyear:.6e}") 

    # Use the fit to predict fCO2 in console: SC_tools.seasonalcycle_fit(opt_result['x'], 1)
    # Last number is date (1 = 1 january 1970)

    #%% # Long Term Trend of TA combinedmean (splitting up)

    L0 = (combinedmean.year <= 2011)
    L1 = (combinedmean.year >= 2010)

    fig, axs = plt.subplots(nrows=2, dpi=300, figsize=(10,6), sharex=True)

    slope, intercept, r, p, se = linregress(combinedmean[L0]['datenum'], combinedmean[L0]['normalized_TA'])

    ax = axs[0]
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean[L0], ax=ax,
                scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Normalized A$_T$ Combined')

    ax.set_title("Normalized TA combined data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Total Alkalinity (µmol/kg)')
    ax.set_ylim(2280, 2430)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    slope, intercept, r, p, se = linregress(combinedmean[L1]['datenum'], combinedmean[L1]['normalized_TA'])

    ax = axs[1]
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean[L1], ax=ax,
                scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Normalized A$_T$ Combined')

    ax.grid(alpha=0.3)
    ax.set_xlabel(None)
    ax.set_ylabel('Total Alkalinity (µmol/kg)')
    ax.set_ylim(2280, 2430)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()

    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/TA_split_up_Combined.png")     
    plt.show()
    
    #%% # Long Term Trend of TA combinedmean (splitting LR up)
    
    L0 = (combinedmean.year <= 2011)
    L1 = (combinedmean.year >= 2010)
    
    fig, ax = plt.subplots(dpi=300, figsize=(10,6))
    
    aslope, aintercept, ar, ap, ase = linregress(combinedmean[L0]['datenum'], combinedmean[L0]['normalized_TA'])
    bslope, bintercept, br, bp, bse = linregress(combinedmean[L1]['datenum'], combinedmean[L1]['normalized_TA'])
    
    ax = ax
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean[L0], ax=ax,
                scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {aslope:.1e}x + {aintercept:.1f}'}, label='Normalized TA Combined')
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean[L1], ax=ax,
                scatter_kws={"color": "xkcd:red"}, line_kws={"color": "blue", 'label': f'y = {bslope:.1e}x + {bintercept:.1f}', 'linestyle': 'dotted'})
    
    ax.set_title("Normalized TA combined data - North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Total Alkalinity (µmol/kg)')
    ax.set_ylim(2280, 2430)
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Long_Term_Trends/TA_split_up_combinedmean2.png")     
    plt.show()

