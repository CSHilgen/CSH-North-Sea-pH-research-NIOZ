
def plot_salinity_vs_DIC(combinedmean):
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns   
    from scipy.stats import linregress
    
    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('twilight')
    
    vmin = 1
    vmax = 365
    
    slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['dic'])
    
    ax=ax
    sns.regplot(x='salinity', y='dic', data=combinedmean, ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1f}'})
    
    #sc = ax.scatter('salinity', 'normalized_DIC', c='dayofyear', cmap=cm, data=combinedmean, label='Normalized DIC', vmin=vmin, vmax=vmax)
    sc = ax.scatter('salinity', 'dic', c='dayofyear', cmap=cm, data=combinedmean, label='Initial DIC', vmin=vmin, vmax=vmax)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Salinity")
    ax.set_ylabel("DIC (µmol/kg)")
    ax.set_title("DIC and S combined data - North Sea")
    ax.legend()
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2000, 2250])
    ax.set_xlim([31, 35.5])
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_S_mean_normalized_scatter_LR2.png")
    plt.show()
    
def plot_salinity_vs_TA(combinedmean):
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns   
    from scipy.stats import linregress
    
    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('twilight')
    
    vmin = 1
    vmax = 365
    
    slope, intercept, r, p, se = linregress(combinedmean['salinity'], combinedmean['alkalinity'])
    
    ax=ax
    sns.regplot(x='salinity', y='alkalinity', data=combinedmean, ax=ax,
                scatter_kws={"color": "none"}, line_kws={"color": "blue", 'label': f'y = {slope:.1f}x + {intercept:.1f}'})
    
    #sc = ax.scatter('salinity', 'normalized_TA', c='dayofyear', cmap=cm, data=combinedmean, label='Normalized A$_T$', vmin=vmin, vmax=vmax)
    sc = ax.scatter('salinity', 'alkalinity', c='dayofyear', cmap=cm, data=combinedmean, label='Initial A$_T$', vmin=vmin, vmax=vmax)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Salinity")
    ax.set_ylabel("A$_T$ (µmol/kg)")
    ax.set_title("TA and S combined data - North Sea")
    ax.legend()
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2280, 2430])
    ax.set_xlim([31, 35.5])
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/TA_S_mean_normalized_scatter_LR2.png")
    plt.show()

def plot_normalized_DIC(combinedmean):
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    from scipy.stats import linregress
    import matplotlib.dates as mdates

    # Plot DIC and normalized DIC (combined dataset = D366, Cefas, RWSn, Glodap)
    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)
    
    slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['dic'])
    
    ax = axs[0]
    sns.regplot(x='datenum', y='dic', data=combinedmean, ax=ax,
                scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial DIC', marker='x')
    
    ax.set_title("DIC - Fitting North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('DIC (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2000, 2250])
    ax.legend()
    
    ax = axs[1]
    combinedmean.plot.scatter("datenum", "dic", ax=ax, c='purple', label='Initial DIC', marker='x')
    combinedmean.plot.scatter('datenum', 'normalized_DIC', ax=ax, c='purple', label='Normalized DIC')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('DIC (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2000, 2250])
    ax.legend()
    
    slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['normalized_DIC'])
    
    ax = axs[2]
    sns.regplot(x='datenum', y='normalized_DIC', data=combinedmean, ax=ax, ci=99.9,
                scatter_kws={"color": "purple"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Normalized DIC')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('DIC (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2000, 2250])
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_normalization_fitting.png")
    plt.show()

def plot_normalized_TA(combinedmean):
    import pandas as pd, numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    from scipy.stats import linregress
    import matplotlib.dates as mdates
    
    # Plot TA and normalized TA (combined dataset = D366, Cefas, RWSn, Glodap)
    fig, axs = plt.subplots(nrows=3, dpi=300, figsize=(10,6), sharex=True)
    
    slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['alkalinity'])
    
    ax = axs[0]
    sns.regplot(x='datenum', y='alkalinity', data=combinedmean, ax=ax,
                scatter_kws={"color": "red"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Initial A$_T$', marker='x')
    
    ax.set_title("A$_T$ - Fitting North Sea")
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('A$_T$ (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2280, 2420])
    ax.legend()
    
    ax = axs[1]
    combinedmean.plot.scatter("datenum", "alkalinity", ax=ax, c='red', label='Initial TA', marker='x')
    combinedmean.plot.scatter('datenum', 'normalized_TA', ax=ax, c='red', label='Normalized A$_T$')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('Total alkalinity (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2280, 2420])
    ax.legend()
    
    slope, intercept, r, p, se = linregress(combinedmean['datenum'], combinedmean['normalized_TA'])
    
    ax = axs[2]
    sns.regplot(x='datenum', y='normalized_TA', data=combinedmean, ax=ax, ci=99.9,
                scatter_kws={"color": "red"}, line_kws={"color": "blue", 'label': f'y = {slope:.1e}x + {intercept:.1f}'}, label='Normalized A$_T$')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel('A$_T$ (μmol/kg)')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_ylim([2280, 2420])
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/TA_normalization_fitting.png")    
    plt.show()
    
def plot_DIC_TA(combinedmean):
    from matplotlib import pyplot as plt

    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('twilight')
    
    sc = ax.scatter(combinedmean['dic'], combinedmean['alkalinity'], c=combinedmean['dayofyear'], vmin=0, vmax=365, s=35, cmap=cm, edgecolor="None")
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("DIC (μmol/kg)")
    ax.set_ylabel("A$_T$ (μmol/kg)")
    ax.set_xlim([2000, 2250])
    ax.set_ylim([2280, 2420])
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('DIC & TA combined data - mean')
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_TA_plot_scatter_mean_dayofyear_combined.png")
    plt.show()
    
def plot_DIC_TA_year(combinedmean):
    
    from matplotlib import pyplot as plt
    import numpy as np
    
    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021

    ax = ax
    sc = ax.scatter('dic', 'alkalinity', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("DIC (μmol/kg)")
    ax.set_ylabel("A$_T$ (μmol/kg)")
    ax.set_xlim([2000, 2250])
    ax.set_ylim([2280, 2420])
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('DIC & TA combined data - mean')

    ticks = np.linspace(vmin, vmax, 5)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_TA_plot_scatter_mean_year_combined.png")
    plt.show()

def plot_NDIC_NTA(combinedmean):
    from matplotlib import pyplot as plt
    
    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('twilight')
    
    sc = ax.scatter(combinedmean['normalized_DIC'], combinedmean['normalized_TA'], c=combinedmean['dayofyear'], vmin=0, vmax=365, s=35, cmap=cm, edgecolor="None")
    
    cbar=fig.colorbar(sc, ax=ax, orientation='vertical', location='right')
    label=[80,172,264,355]
    cbar.set_ticks(label)
    cbar.set_ticklabels(['Winter    ', 'Spring    ', 'Summer    ', 'Autumn    '])
    cbar.ax.tick_params(rotation=90)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("nDIC (μmol/kg)")
    ax.set_ylabel("nA$_T$ (μmol/kg)")
    ax.set_xlim([2000, 2250])
    ax.set_ylim([2280, 2420])
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Normalized DIC & TA combined data - mean')
    
    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_TA_plot_scatter_mean_dayofyear_combined_normalized.png")
    plt.show()

def plot_NDIC_NTA_year(combinedmean):
    
    from matplotlib import pyplot as plt
    import numpy as np
    
    fig, ax = plt.subplots(dpi=300, figsize=(6,4))
    cm = plt.cm.get_cmap('rainbow')
    vmin = 2000
    vmax = 2021

    ax = ax
    sc = ax.scatter('normalized_DIC', 'normalized_TA', c='year', data=combinedmean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

    ax.grid(alpha=0.3)
    ax.set_xlabel("nDIC (μmol/kg)")
    ax.set_ylabel("nA$_T$ (μmol/kg)")
    ax.set_xlim([2000, 2250])
    ax.set_ylim([2280, 2420])
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('Normalized DIC & TA combined data - mean')

    ticks = np.linspace(vmin, vmax, 5)
    cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
    cbar.set_label('Time (yrs)')
    cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

    plt.tight_layout()
    plt.savefig("figures/Spatial_variability/DIC_TA_plot_scatter_mean_year_combined_normalized.png")
    plt.show()


