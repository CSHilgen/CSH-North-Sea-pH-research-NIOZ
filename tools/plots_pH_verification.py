
def plot_pH_verification(RWSomean, RWSnmean, results_TA_fCO2, results_TA_pCO2):
    from matplotlib import pyplot as plt
    import matplotlib.dates as mdates
    
    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('datenum', 'pH_total', c='xkcd:water blue', data=RWSomean, label='pH RWS$_{1975-2018}$', s=20, alpha=0.4)
    ax.scatter('datenum', 'pH_total_spectro_out', c='xkcd:cobalt blue', data=RWSnmean, label='pH$_{spectro}$ RWS$_{2018-2021}$', s=20, alpha=0.4)
    # pCO2 air
    ax.scatter('datenum', 'pH_total', c='xkcd:black', data=results_TA_pCO2, label='pH$_{pred}$ TA & pCO$_{2AIR}$', s=20, alpha=0.4)
    # fCO2 sea
    ax.scatter('datenum', 'pH_total', c='xkcd:goldenrod', data=results_TA_fCO2, label='pH$_{pred}$ TA & fCO$_{2SW}$', s=20, alpha=0.4)

    ax.grid(alpha=0.3)
    ax.set_ylabel("pH$_{total}$", fontsize=12)
    ax.set_xlabel("Time (yrs)", fontsize=12)
    #ax.set_xlim([9069, 19000])
    ax.set_xlim(10950, 19345)
    ax.set_ylim(7, 8.5)
    ax.legend()#bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH predicted - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_pH_mean_time_datasets.png")
    plt.show()
    
def plot_pH_predicted_vs_initial(RWSomean):
    from matplotlib import pyplot as plt
    import pandas as pd, numpy as np
    
    fig, ax = plt.subplots(dpi=300)
    x = np.linspace(7.5,8.5,100)
    y = np.linspace(7.5,8.5,100)
    
    ax = ax
    ax.scatter('pH_pred_TA_pCO2', 'pH_total', c='xkcd:water blue', data=RWSomean, label='pH$_{pred}$ based on TA & pCO$_{2AIR}$', s=20, alpha=0.4)
    ax.plot(x, y, color='xkcd:dark grey', label='y = x', alpha=0.3)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("pH$_{pred}$ TA & pCO$_{2AIR}$")
    ax.set_ylabel("pH$_{initial}$")
    ax.set_ylim(7.5, 8.5)
    ax.set_xlim(7.5, 8.5)
    ax.legend()
    ax.set_aspect(1)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH initial vs predicted - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_pH_vs_initial_pH_pCO2air.png")
    plt.show()
    
    fig, ax = plt.subplots(dpi=300)

    ax = ax
    ax.scatter('pH_pred_TA_fCO2', 'pH_total', c='xkcd:water blue', data=RWSomean, label='pH$_{pred}$ based on TA & fCO$_{2SW}$', s=20, alpha=0.4)
    ax.plot(x, y, color='xkcd:dark grey', label='y = x', alpha=0.3)
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("pH$_{pred}$ TA & fCO$_{2SW}$")
    ax.set_ylabel("pH$_{initial}$")
    ax.set_ylim(7.5, 8.5)
    ax.set_xlim(7.5, 8.5)
    ax.legend()
    ax.set_aspect(1)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    ax.set_title('pH initial vs predicted - Datasets North Sea') 

    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_pH_vs_initial_pH_fCO2sea.png")
    plt.show()
    
def predicted_fCO2_pCO2_alkalinity_RWSo(RWSomean):    
    from matplotlib import pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

    fig, ax = plt.subplots(dpi=300)
    
    ax=ax
    ax.scatter('datenum', 'predicted_alkalinity', c='xkcd:water blue', data=RWSomean, label='RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("nTA (μmol/kg)")
    ax.set_title("Predicted TA for RWSomean - North Sea")
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_alkalinity_RWSomean.png")
    plt.show()
    
    fig, ax = plt.subplots(dpi=300)
    
    ax=ax
    ax.scatter('datenum', 'predicted_pCO2_air', c='xkcd:water blue', data=RWSomean, label='RWS')

    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("pCO$_2$ (uatm)")
    ax.set_title("Predicted pCO$_2$ air for RWSomean - North Sea")
    ax.set_xlim([9069,19000])
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_pCO2_air_RWSomean.png")
    plt.show()
    
    fig, ax = plt.subplots(dpi=300)
    
    ax=ax
    ax.scatter('datenum', 'predicted_fCO2_sea', c='xkcd:water blue', data=RWSomean, label='RWS')
    
    ax.grid(alpha=0.3)
    ax.set_xlabel("Time (yrs)")
    ax.set_ylabel("fCO$_2$ (uatm)")
    ax.set_title("Predicted fCO$_2$ sea for RWSomean - North Sea")
    ax.legend()
    ax.set_xlim([9069,19000])
    ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    ax.get_legend().set_title("Dataset")
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.YearLocator())
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig("figures/pH_verification_model/Predicted_fCO2_sea_RWSomean.png")
    plt.show()