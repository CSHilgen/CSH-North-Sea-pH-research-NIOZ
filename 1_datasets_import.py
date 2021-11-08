import pandas as pd, numpy as np, xarray as xr
from matplotlib import pyplot as plt
import koolstof as ks
import pickle
import PyCO2SYS as pyco2
import matplotlib.dates as mdates
from cartopy import crs as ccrs, feature as cfeature
import cmocean
import scipy.optimize
from scipy import interpolate 
from scipy.stats import linregress
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
from numpy import arange
import seaborn as sns
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#%% # Import dataframes

# Initial dataframes are in study area, the wrong data points are dropped
# datetime is created, and distance_to_shore is included
glodapns = pd.read_csv("dataframes_made/glodapns.csv")
socatns = pd.read_csv("dataframes_made/socatns.csv")
Cefas = pd.read_csv("dataframes_made/Cefas.csv")
D366 = pd.read_csv("dataframes_made/D366.csv")
RWSn = pd.read_csv("dataframes_made/RWSn.csv")
RWSo = pd.read_csv("dataframes_made/RWSo.csv")
combined = pd.read_csv("dataframes_made/combined.csv")

# Results are the dataframes of pyCO2sys (all data points)
resultsglodapns = pd.read_csv("dataframes_made/resultsglodapns.csv")
resultssocatnsair = pd.read_csv("dataframes_made/resultssocatnsair.csv")
resultssocatns = pd.read_csv("dataframes_made/resultssocatns.csv")
resultsCefas = pd.read_csv("dataframes_made/resultsCefas.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn.csv")
resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined.csv")

# Mean are the dataframes of pyCO2sys (mean per month)
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean.csv")
socatnsairmean = pd.read_csv("dataframes_made/socatnsairmean.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean.csv")
D366mean = pd.read_csv("dataframes_made/D366mean.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean.csv")

RWSnstation = pd.read_csv("dataframes_made/RWSnstation.csv")
RWSnstation = pd.read_csv("dataframes_made/RWSostation.csv")

#%% # Set datetime column

glodapns['datetime'] = pd.to_datetime(glodapns['datetime'])
socatns['datetime'] = pd.to_datetime(socatns['datetime'])
Cefas['datetime'] = pd.to_datetime(Cefas['datetime'])
D366['datetime'] = pd.to_datetime(D366['datetime'])
RWSn['datetime'] = pd.to_datetime(RWSn['datetime'])
RWSo['datetime'] = pd.to_datetime(RWSo['datetime'])
combined['datetime'] = pd.to_datetime(combined['datetime'])

resultsglodapns['datetime'] = pd.to_datetime(resultsglodapns['datetime'])
resultssocatns['datetime'] = pd.to_datetime(resultssocatns['datetime'])
resultssocatnsair['datetime'] = pd.to_datetime(resultssocatnsair['datetime'])
resultsCefas['datetime'] = pd.to_datetime(resultsCefas['datetime'])
resultsD366['datetime'] = pd.to_datetime(resultsD366['datetime'])
resultsRWSn['datetime'] = pd.to_datetime(resultsRWSn['datetime'])
resultsRWSo['datetime'] = pd.to_datetime(resultsRWSo['datetime'])
resultscombined['datetime'] = pd.to_datetime(resultscombined['datetime'])

glodapnsmean['datetime'] = pd.to_datetime(glodapnsmean['datetime'])
socatnsmean['datetime'] = pd.to_datetime(socatnsmean['datetime'])
socatnsairmean['datetime'] = pd.to_datetime(socatnsairmean['datetime'])
Cefasmean['datetime'] = pd.to_datetime(Cefasmean['datetime'])
D366mean['datetime'] = pd.to_datetime(D366mean['datetime'])
RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSomean['datetime'] = pd.to_datetime(RWSomean['datetime'])
combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])
