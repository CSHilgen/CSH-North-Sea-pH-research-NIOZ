import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import linregress
from scipy.optimize import least_squares
import tools.Plots_variables as tplotsAm
import tools.Plots_variables.plots_Nitrate as tplotsNi
import tools.Plots_variables.plots_Phosphate as tplotsPh
import tools.Plots_variables.plots_Silicate as tplotsSi
import tools.Plots_variables.plots_Temperature as tplotsTemp
import tools.Plots_variables.plots_Salinity as tplotsSal
import tools.Plots_variables.plots_Oxygen as tplotso2
import tools.Plots_variables.plots_AOU as tplotsAOU
import tools.Plots_variables.plots_Chlorophyll as tplotsChl
import tools.Plots_variables.plots_fCO2air as tplotsfCO2air
import tools.Plots_variables.plots_fCO2sea as tplotsfCO2sea
import tools.Plots_variables.plots_deltafCO2 as tplotsdeltafCO2
import tools.Plots_variables.plots_DIC as tplotsDIC
import tools.Plots_variables.plots_TA as tplotsTA
import tools.Plots_variables.plots_pH as tplotspH
import tools.Plots_variables.plots_Calcium as tplotsCa

#%% # Import datasets

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSomeanN = pd.read_csv("dataframes_made/RWSomeanN_final.csv")
RWSomeanP = pd.read_csv("dataframes_made/RWSomeanP_final.csv")
RWSomeanS = pd.read_csv("dataframes_made/RWSomeanS_final.csv")
RWStotalmeanT = pd.read_csv("dataframes_made/RWStotalmeanT_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
combinedmeansc_dic = pd.read_csv("dataframes_made/combinedmeansc_dic_final.csv")
socatnsmeandelta = pd.read_csv("dataframes_made/socatnsmeandelta_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
socatnsmeanair = pd.read_csv("dataframes_made/socatnsmeanair_final.csv")
RWSomeanChl = pd.read_csv("dataframes_made/RWSomeanChl_final.csv")
RWSomeano2 = pd.read_csv("dataframes_made/RWSomeano2_final.csv")
RWStotalmean = pd.read_csv("dataframes_made/RWStotalmean_final.csv")
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean_final.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean_final.csv")
D366mean = pd.read_csv("dataframes_made/D366mean_final.csv")

#%% # Get plots for datasets, day of year, regions, long term trends

# tplotsAm.get_ammonia_plots(RWSomean)
# tplotsAOU.get_AOU_plots(RWSomean)
# tplotsChl.get_chlorophyll_plots(RWSomean, RWSomeanChl)
# tplotsdeltafCO2.get_deltafCO2_plots(socatnsmean, socatnsmeandelta)
tplotsDIC.get_DIC_plots(combinedmean, glodapnsmean, Cefasmean, D366mean, RWSnmean, combinedmeansc_dic)
# tplotsfCO2air.get_fCO2air_plots(socatnsmean, socatnsmeanair)
# tplotsfCO2sea.get_fCO2sea_plots(socatnsmean)
# tplotsNi.get_nitrate_plots(RWSomean, RWSomeanN)
# tplotso2.get_oxygen_plots(RWSomean, RWSomeano2)
# tplotspH.get_pH_plots(RWSomean, RWSnmean)
# tplotsPh.get_phosphate_plots(RWSomean, RWSomeanP)
# tplotsSal.get_salinity_plots(RWStotalmean, RWSomean, RWSnmean)
# tplotsSi.get_silicate_plots(RWSomean, RWSomeanS)
tplotsTA.get_TA_plots(combinedmean, glodapnsmean, Cefasmean, D366mean, RWSnmean)
# tplotsTemp.get_temperature_plots(RWStotalmean, RWStotalmeanT, RWSomean, RWSnmean)
# tplotsCa.get_calcium_plots(RWSo, RWSomean)