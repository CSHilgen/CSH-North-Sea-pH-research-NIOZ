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

#%% # Import GLODAP data set

# glodapao = pd.read_csv("C:/Users/cecil/.spyder-py3/Python-nioz-2021/GLODAP/data/GLODAPv2.2021_Atlantic_Ocean.csv", na_values = -9999)
# glodapao.columns = glodapao.columns.str[2:]

# glodapns = glodapao[(glodapao["latitude"] >= 51.5) & (glodapao["latitude"] <= 56.5) 
#                     & (glodapao["longitude"] >= 2.5) & (glodapao["longitude"] <= 7)]
# glodapns.to_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/GLODAPv2.2021_North_Sea.csv", index=False)

glodapns = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/GLODAPv2.2021_North_Sea.csv")
glodapns = glodapns.rename(columns={'talk':'TA', 'tco2': 'DIC'})
glodapns['datetime'] = pd.to_datetime(glodapns[['year', 'month', 'day', 'hour', 'minute']], format='%Y%m%d %H%M')

#%% # Use vptree to calculate distance to shore

latrange = (50, 60)
lonrange = (0, 10) 
vpt = ks.maps.build_vptree(latrange, lonrange)

with open("distance_to_shore.pkl", "wb") as f:
      pickle.dump(vpt, f)

with open("distance_to_shore.pkl", "rb") as f:
     vpt = pickle.load(f)
    
#%% # Create distance_to_shore column in dataset

def caldistance(row):
    print(row.name)
    distance_to_shore = vpt.get_nearest_neighbor((row.longitude, row.latitude))
    return distance_to_shore[0]

test = resultssocatnsair.apply(caldistance, axis=1)

with open("distance_apply.pkl", "wb") as f:
    pickle.dump(test, f)

with open("distance_apply.pkl", "rb") as f:
    resultssocatnsair['distance_to_shore'] = pickle.load(f)

#%% # Import SOCAT data set

socatns = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/SOCATv2.2021_North_Sea.csv", na_values=[-999,-1e+34], skiprows=64, delimiter=",")
socatns.columns = socatns.columns.str.lower()
socatns['datetime'] = pd.to_datetime(socatns[['year', 'month', 'day', 'hour', 'minute']], format='%Y%m%d %H%M')

socatnsrotterdam = socatns[(socatns['longitude'] < 4.5) & (socatns['longitude'] > 4.05) & (socatns['latitude'] > 51.8) & (socatns['latitude'] < 52)].index
socatns.drop(socatnsrotterdam, inplace=True)
socatnsantwerp = socatns[(socatns['longitude'] <= 3.09503) & (socatns['longitude'] >= 2.854) & (socatns['latitude'] >= 51.501) & (socatns['latitude'] <= 51.58153)].index
socatns.drop(socatnsantwerp, inplace=True)
socatnshighpeak = socatns[(socatns['longitude'] == 3.1121) & (socatns['latitude'] == 53.0816)].index
socatns.drop(socatnshighpeak, inplace=True)

#%% # Import DIC and TA datasets

mss = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/MSS_DIC_TA_v1_0_ctd_data.csv")
Cefas = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/Cefas_SSB_data.xlsx", header=0, skiprows=[1])
D366 = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/D366UWCarbonateChemistrySynthesisData_140328_data.csv")
RWSn = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/RWS_NIOZ_North_Sea_data_v10_for_SDG14_3_1.xlsx", na_values=-999)

mss = mss.rename(columns={'Latitude[deg+veN]':'latitude', 'Longitude[deg+veE]':'longitude'})
Cefas = Cefas.rename(columns={'Latitude':'latitude', 'Longitude':'longitude'})
D366 = D366.rename(columns={'Latitude [+ve = N]':'latitude', 'Longitude [+ve = E]':'longitude', 'DIC [umol/kg]':'DIC', 'TA [umol/kg]':'TA'})
RWSn = RWSn.rename(columns={'LATITUDE':'latitude', 'LONGITUDE': 'longitude', 'dic':'DIC', 'alkalinity':'TA'})

mss['datetime'] = pd.to_datetime(mss['yyyy-mm-ddThh24:mi[GMT/UT]'])
mss['datetime'] = mss['datetime'].dt.tz_localize(None)
Cefas['datetime'] = pd.to_datetime(Cefas['Date+time (GMT)'])
D366['datetime'] = pd.to_datetime(D366['yyyy-mm-ddThh:mm'])
RWSn['datetime'] = pd.to_datetime(RWSn['DATE_UTC'])

#%% # Select study area

mss = mss[(mss["latitude"] >= 51.5) & (mss["latitude"] <= 56.5) 
                    & (mss["longitude"] >= 2.5) & (mss["longitude"] <= 7)]
Cefas = Cefas[(Cefas["latitude"] >= 51.5) & (Cefas["latitude"] <= 56.5) 
                    & (Cefas["longitude"] >= 2.5) & (Cefas["longitude"] <= 7)]
D366 = D366[(D366["latitude"] >= 51.5) & (D366["latitude"] <= 56.5) 
                    & (D366["longitude"] >= 2.5) & (D366["longitude"] <= 7)]
RWSn = RWSn[(RWSn["latitude"] >= 51.5) & (RWSn["latitude"] <= 56.5) 
                    & (RWSn["longitude"] >= 2.5) & (RWSn["longitude"] <= 7)]
    
#%% # Import RWS old data set

rwss = pd.read_parquet("C:/Users/cecil/Documenten/GitHub/rws-the-olden-days/data/old_rws_data/rws_compilation.parquet")
rwss = rwss[['bod', 'calcium', 'chlorophyll', 'doc', 'poc', 'ammonia', 'nitrite', 'nitrate', 'pn', 'oxygen', 'toc', 'pH', 'phosphate', 'pp', 'dp', 'tp', 'salinity', 'silicate', 'spm', 'temperature', 'dn', 'tn', 'longitude', 'latitude', 'datenum', 'datetime']]
rwssurface = rwss.xs("surface", level="vertical_pos") 

RWSo = rwssurface[(rwssurface["latitude"] >= 51.5) & (rwssurface["latitude"] <= 56.5) 
                    & (rwssurface["longitude"] >= 2.5) & (rwssurface["longitude"] <= 7)]

RWSo = RWSo.loc[["CALLOG4", "CALLOG10", "CALLOG30", "EGMAZE4", "EGMAZE10", "EGMAZE20", 
                    "EGMAZE30", "GOERE6", "GOERE10", "GOERE20", "GOERE30", "NOORDWK4", "NOORDWK10", 
                    "NOORDWK20", "NOORDWK30", "ROTTMPT20", "ROTTMPT30", "SCHOUWN1", "SCHOUWN4", 
                    "SCHOUWN10", "SCHOUWN20", "SCHOUWN30", "TERSLG10", "TERSLG30", "WALCRN4", 
                    "WALCRN10", "WALCRN20", "WALCRN30", "CALLOG50", "CALLOG70", "EGMAZE50", 
                    "EGMAZE70", "GOERE50", "GOERE70", "NOORDWK50", "NOORDWK70", "ROTTMPT50", 
                    "ROTTMPT70", "ROTTMPT100", "SCHOUWN50", "SCHOUWN70", "TERHDE70", "TERSLG50", 
                    "TERSLG70", "TERSLG100", "TERSLG135", "TERSLG175", "WALCRN50", "WALCRN70"]]

RWSo = RWSo.reset_index()

#%% # PyCO2sys mss

TA = mss['TA'] 
DIC = mss['DIC']
# phos = mss['phosphate'] 
# sil = mss['silicate']
# temp = mss['temperature']
# sal = mss['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    #salinity = sal,  # Salinity of the sample
    #temperature = temp,  # Temperature at input conditions
    #total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    #total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsmss = pd.DataFrame.from_dict(results)
resultsmss['datetime'] = mss['datetime']
resultsmss['datetime'] = pd.to_datetime(resultsmss['datetime'])
resultsmss['distance_to_shore'] = mss['distance_to_shore']
resultsmss['longitude'] = mss['longitude']
resultsmss['latitude'] = mss['latitude']

# Make dataset based on the mean 
mssmean = resultsmss.set_index('datetime').resample('M').mean()
mssmean = mssmean.reset_index()

mssmean = mssmean.dropna(axis='rows', how='all', subset=['par1'])
mssmean["datenum"] = mdates.date2num(mssmean.datetime)

#%% # PyCO2sys Cefas

TA = Cefas['TA'] 
DIC = Cefas['DIC']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    #salinity = sal,  # Salinity of the sample
    #temperature = temp,  # Temperature at input conditions
    #total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    #total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsCefas = pd.DataFrame.from_dict(results)
resultsCefas['datetime'] = Cefas['datetime']
resultsCefas['datetime'] = pd.to_datetime(resultsCefas['datetime'])
resultsCefas['distance_to_shore'] = Cefas['distance_to_shore']
resultsCefas['longitude'] = Cefas['longitude']
resultsCefas['latitude'] = Cefas['latitude']

# Make dataset based on the mean 
Cefasmean = resultsCefas.set_index('datetime').resample('M').mean()
Cefasmean = Cefasmean.reset_index()

Cefasmean = Cefasmean.dropna(axis='rows', how='all', subset=['par1'])
Cefasmean["datenum"] = mdates.date2num(Cefasmean.datetime)

#%% # PyCO2sys D366

TA = D366['TA'] 
DIC = D366['DIC']
pH = D366['pH [dimensionless]']
phos = D366['Phosphate [umol/kg]'] 
sil = D366['Si [umol/kg]']
temp = D366['SST [deg C]']
sal = D366['Salinity [dimensionless]']

# Define input conditions
kwargs = dict(
    par1 = DIC,  # Value of the first parameter
    par2 = pH,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 2,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 3,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,# Concentration of phosphate in the sample (in umol/kg)
    opt_pH_scale = 1, # Total scale has been  used in par2
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsD366 = pd.DataFrame.from_dict(results)
resultsD366['datetime'] = D366['datetime']
resultsD366['datetime'] = pd.to_datetime(resultsD366['datetime'])
resultsD366['distance_to_shore'] = D366['distance_to_shore']
resultsD366['longitude'] = D366['longitude']
resultsD366['latitude'] = D366['latitude']

# Make dataset based on the mean 
D366mean = resultsD366.set_index('datetime').resample('M').mean()
D366mean = D366mean.reset_index()

D366mean = D366mean.dropna(axis='rows', how='all', subset=['par1'])
D366mean["datenum"] = mdates.date2num(D366mean.datetime)

#%% # PyCO2sys RWSn

TA = RWSn['TA'] 
DIC = RWSn['DIC']
phos = RWSn['phosphate'] 
sil = RWSn['silicate']
temp = RWSn['temperature']
sal = RWSn['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsRWSn = pd.DataFrame.from_dict(results)
resultsRWSn['datetime'] = RWSn['datetime']
resultsRWSn['datetime'] = pd.to_datetime(resultsRWSn['datetime'])
resultsRWSn['distance_to_shore'] = RWSn['distance_to_shore']
resultsRWSn['longitude'] = RWSn['longitude']
resultsRWSn['latitude'] = RWSn['latitude']

# Make dataset based on the mean 
RWSnmean = resultsRWSn.set_index('datetime').resample('M').mean()
RWSnmean = RWSnmean.reset_index()

RWSnmean = RWSnmean.dropna(axis='rows', how='all', subset=['par1'])
RWSnmean["datenum"] = mdates.date2num(RWSnmean.datetime)

#%% # PyCO2sys glodapns

TA = glodapns['TA'] 
DIC = glodapns['DIC']
phos = glodapns['phosphate'] 
sil = glodapns['silicate']
temp = glodapns['temperature']
sal = glodapns['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsglodapns = pd.DataFrame.from_dict(results)
resultsglodapns['datetime'] = glodapns['datetime']
resultsglodapns['datetime'] = pd.to_datetime(resultsglodapns['datetime'])
resultsglodapns['distance_to_shore'] = glodapns['distance_to_shore']
resultsglodapns['longitude'] = glodapns['longitude']
resultsglodapns['latitude'] = glodapns['latitude']

# Make dataset based on the mean 
glodapnsmean = resultsglodapns.set_index('datetime').resample('M').mean()
glodapnsmean = glodapnsmean.reset_index()

glodapnsmean = glodapnsmean.dropna(axis='rows', how='all', subset=['par1'])
glodapnsmean["datenum"] = mdates.date2num(glodapnsmean.datetime)

#%% # Use pyCO2sys SOCAT atmosphere GVCO2 is xCO2

xco2 = socatns['gvco2'] 
temp = socatns['temp']
sal = socatns['sal']

# Define input conditions
kwargs = dict(
    par1 = xco2,  # Value of the first parameter
    par1_type = 9,  # The first parameter supplied is of type "9", which is "xCO2"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultssocatnsair = pd.DataFrame.from_dict(results)
resultssocatnsair['datetime'] = socatns['datetime']
resultssocatnsair['datetime'] = pd.to_datetime(resultssocatnsair['datetime'])
resultssocatnsair['distance_to_shore'] = socatns['distance_to_shore']
resultssocatnsair['longitude'] = socatns['longitude']
resultssocatnsair['latitude'] = socatns['latitude']

# Make dataset based on the mean 
socatnsairmean = resultssocatnsair.set_index('datetime').resample('M').mean()
socatnsairmean = socatnsairmean.reset_index()

socatnsairmean = socatnsairmean.dropna(axis='rows', how='all', subset=['par1'])
socatnsairmean["datenum"] = mdates.date2num(socatnsairmean.datetime)

socatns['fco2_air'] = resultssocatnsair['fCO2']
socatns['deltafco2'] = socatns['fco2_recommended'] - socatns['fco2_air']

#%% # Use pyCO2sys SOCAT seawater fCO2

fco2 = socatns['fco2_recommended'] 
temp = socatns['temp']
sal = socatns['sal']

# Define input conditions
kwargs = dict(
    par1 = fco2,  # Value of the first parameter
    par1_type = 5,  # The first parameter supplied is of type "5", which is "fCO2"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultssocatns = pd.DataFrame.from_dict(results)
resultssocatns['datetime'] = socatns['datetime']
resultssocatns['datetime'] = pd.to_datetime(resultssocatns['datetime'])
resultssocatns['distance_to_shore'] = socatns['distance_to_shore']
resultssocatns['longitude'] = socatns['longitude']
resultssocatns['latitude'] = socatns['latitude']

# Make dataset based on the mean 
socatnsmean = resultssocatns.set_index('datetime').resample('M').mean()
socatnsmean = socatnsmean.reset_index()

socatnsmean = socatnsmean.dropna(axis='rows', how='all', subset=['par1'])
socatnsmean["datenum"] = mdates.date2num(socatnsmean.datetime)

#%% # PyCO2sys RWSo

pH = RWSo['pH']
phos = RWSo['phosphate'] 
sil = RWSo['silicate']
temp = RWSo['temperature']
sal = RWSo['salinity']

# Define input conditions
kwargs = dict(
    par1 = pH,  # Value of the first parameter
    par1_type = 3,  # The second parameter supplied is of type "3", which is "pH"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_pH_scale = 4, # NBS scale has been  used in par1
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsRWSo = pd.DataFrame.from_dict(results)
resultsRWSo['datetime'] = RWSo['datetime']
resultsRWSo['datetime'] = pd.to_datetime(resultsRWSo['datetime'])
resultsRWSo['distance_to_shore'] = RWSo['distance_to_shore']
resultsRWSo['longitude'] = RWSo['longitude']
resultsRWSo['latitude'] = RWSo['latitude']
resultsRWSo['station'] = RWSo['station']
# Make dataset based on the mean 
#RWSomean = resultsRWSo.set_index('datetime').resample('M')
resultsRWSo['month'] = resultsRWSo.datetime.dt.month
groupedstation = resultsRWSo.groupby(by=['month', 'station']).mean()
RWSomean = RWSomean.reset_index()

RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['par1'])
RWSomean["datenum"] = mdates.date2num(RWSomean.datetime)

#%% # Set datetime column

glodapns['datetime'] = pd.to_datetime(glodapns['datetime'])
socatns['datetime'] = pd.to_datetime(socatns['datetime'])
#mss['datetime'] = pd.to_datetime(mss['datetime'])
Cefas['datetime'] = pd.to_datetime(Cefas['datetime'])
D366['datetime'] = pd.to_datetime(D366['datetime'])
RWSn['datetime'] = pd.to_datetime(RWSn['datetime'])
RWSo['datetime'] = pd.to_datetime(RWSo['datetime'])
combined['datetime'] = pd.to_datetime(combined['datetime'])

resultsglodapns['datetime'] = pd.to_datetime(resultsglodapns['datetime'])
resultssocatns['datetime'] = pd.to_datetime(resultssocatns['datetime'])
resultssocatnsair['datetime'] = pd.to_datetime(resultssocatnsair['datetime'])
#resultsmss['datetime'] = pd.to_datetime(resultsmss['datetime'])
resultsCefas['datetime'] = pd.to_datetime(resultsCefas['datetime'])
resultsD366['datetime'] = pd.to_datetime(resultsD366['datetime'])
resultsRWSn['datetime'] = pd.to_datetime(resultsRWSn['datetime'])
resultsRWSo['datetime'] = pd.to_datetime(resultsRWSo['datetime'])
resultscombined['datetime'] = pd.to_datetime(resultscombined['datetime'])

glodapnsmean['datetime'] = pd.to_datetime(glodapnsmean['datetime'])
socatnsmean['datetime'] = pd.to_datetime(socatnsmean['datetime'])
socatnsairmean['datetime'] = pd.to_datetime(socatnsairmean['datetime'])
#mssmean['datetime'] = pd.to_datetime(mssmean['datetime'])
Cefasmean['datetime'] = pd.to_datetime(Cefasmean['datetime'])
D366mean['datetime'] = pd.to_datetime(D366mean['datetime'])
RWSnmean['datetime'] = pd.to_datetime(RWSnmean['datetime'])
RWSomean['datetime'] = pd.to_datetime(RWSomean['datetime'])
combinedmean['datetime'] = pd.to_datetime(combinedmean['datetime'])

#%% # Make day of year column

glodapns['dayofyear'] = glodapns.datetime.dt.dayofyear
socatns['dayofyear'] = socatns.datetime.dt.dayofyear
#mss['dayofyear'] = mss.datetime.dt.dayofyear
Cefas['dayofyear'] = Cefas.datetime.dt.dayofyear
D366['dayofyear'] = D366.datetime.dt.dayofyear
RWSn['dayofyear'] = RWSn.datetime.dt.dayofyear
RWSo['dayofyear'] = RWSo.datetime.dt.dayofyear
combined['dayofyear'] = combined.datetime.dt.dayofyear

resultsglodapns['dayofyear'] = resultsglodapns.datetime.dt.dayofyear
resultssocatns['dayofyear'] = resultssocatns.datetime.dt.dayofyear
resultssocatnsair['dayofyear'] = resultssocatnsair.datetime.dt.dayofyear
#resultsmss['dayofyear'] = resultsmss.datetime.dt.dayofyear
resultsCefas['dayofyear'] = resultsCefas.datetime.dt.dayofyear
resultsD366['dayofyear'] = resultsD366.datetime.dt.dayofyear
resultsRWSn['dayofyear'] = resultsRWSn.datetime.dt.dayofyear
resultsRWSo['dayofyear'] = resultsRWSo.datetime.dt.dayofyear
resultscombined['dayofyear'] = resultscombined.datetime.dt.dayofyear

glodapnsmean['dayofyear'] = glodapnsmean.datetime.dt.dayofyear
socatnsmean['dayofyear'] = socatnsmean.datetime.dt.dayofyear
socatnsairmean['dayofyear'] = socatnsairmean.datetime.dt.dayofyear
#mssmean['dayofyear'] = mssmean.datetime.dt.dayofyear
Cefasmean['dayofyear'] = Cefasmean.datetime.dt.dayofyear
D366mean['dayofyear'] = D366mean.datetime.dt.dayofyear
RWSnmean['dayofyear'] = RWSnmean.datetime.dt.dayofyear
RWSomean['dayofyear'] = RWSomean.datetime.dt.dayofyear
combinedmean['dayofyear'] = combinedmean.datetime.dt.dayofyear

#%% # Make month column 

glodapns['month'] = glodapns.datetime.dt.month
socatns['month'] = socatns.datetime.dt.month
#mss['month'] = mss.datetime.dt.month
Cefas['month'] = Cefas.datetime.dt.month
D366['month'] = D366.datetime.dt.month
RWSn['month'] = RWSn.datetime.dt.month
RWSo['month'] = RWSo.datetime.dt.month
combined['month'] = combined.datetime.dt.month

resultsglodapns['month'] = resultsglodapns.datetime.dt.month
resultssocatns['month'] = resultssocatns.datetime.dt.month
resultssocatnsair['month'] = resultssocatnsair.datetime.dt.month
#resultsmss['month'] = resultsmss.datetime.dt.month
resultsCefas['month'] = resultsCefas.datetime.dt.month
resultsD366['month'] = resultsD366.datetime.dt.month
resultsRWSn['month'] = resultsRWSn.datetime.dt.month
resultsRWSo['month'] = resultsRWSo.datetime.dt.month
resultscombined['month'] = resultscombined.datetime.dt.month

glodapnsmean['month'] = glodapnsmean.datetime.dt.month
socatnsmean['month'] = socatnsmean.datetime.dt.month
socatnsairmean['month'] = socatnsairmean.datetime.dt.month
#mssmean['month'] = mssmean.datetime.dt.month
Cefasmean['month'] = Cefasmean.datetime.dt.month
D366mean['month'] = D366mean.datetime.dt.month
RWSnmean['month'] = RWSnmean.datetime.dt.month
RWSomean['month'] = RWSomean.datetime.dt.month
combinedmean['month'] = combinedmean.datetime.dt.month

#%% # Make year column

glodapns['year'] = glodapns.datetime.dt.year
socatns['year'] = socatns.datetime.dt.year
#mss['year'] = mss.datetime.dt.year
Cefas['year'] = Cefas.datetime.dt.year
D366['year'] = D366.datetime.dt.year
RWSn['year'] = RWSn.datetime.dt.year
RWSo['year'] = RWSo.datetime.dt.year
combined['year'] = combined.datetime.dt.year

resultsglodapns['year'] = resultsglodapns.datetime.dt.year
resultssocatns['year'] = resultssocatns.datetime.dt.year
resultssocatnsair['year'] = resultssocatnsair.datetime.dt.year
#resultsmss['year'] = resultsmss.datetime.dt.year
resultsCefas['year'] = resultsCefas.datetime.dt.year
resultsD366['year'] = resultsD366.datetime.dt.year
resultsRWSn['year'] = resultsRWSn.datetime.dt.year
resultsRWSo['year'] = resultsRWSo.datetime.dt.year
resultscombined['year'] = resultscombined.datetime.dt.year

glodapnsmean['year'] = glodapnsmean.datetime.dt.year
socatnsmean['year'] = socatnsmean.datetime.dt.year
socatnsairmean['year'] = socatnsairmean.datetime.dt.year
#mssmean['year'] = mssmean.datetime.dt.year
Cefasmean['year'] = Cefasmean.datetime.dt.year
D366mean['year'] = D366mean.datetime.dt.year
RWSnmean['year'] = RWSnmean.datetime.dt.year
RWSomean['year'] = RWSomean.datetime.dt.year
combinedmean['year'] = combinedmean.datetime.dt.year

#%% # Save datasets

glodapns.to_csv("dataframes_made/glodapns.csv")
socatns.to_csv("dataframes_made/socatns.csv")
mss.to_csv("dataframes_made/mss.csv")
Cefas.to_csv("dataframes_made/Cefas.csv")
D366.to_csv("dataframes_made/D366.csv")
RWSn.to_csv("dataframes_made/RWSn.csv")
RWSo.to_csv("dataframes_made/RWSo.csv")

resultsglodapns.to_csv("dataframes_made/resultsglodapns.csv")
resultssocatnsair.to_csv("dataframes_made/resultssocatnsair.csv")
resultssocatns.to_csv("dataframes_made/resultssocatns.csv")
#resultsmss.to_csv("dataframes_made/resultsmss.csv")
resultsCefas.to_csv("dataframes_made/resultsCefas.csv")
resultsD366.to_csv("dataframes_made/resultsD366.csv")
resultsRWSn.to_csv("dataframes_made/resultsRWSn.csv")
resultsRWSo.to_csv("dataframes_made/resultsRWSo.csv")

glodapnsmean.to_csv("dataframes_made/glodapnsmean.csv")
socatnsairmean.to_csv("dataframes_made/socatnsairmean.csv")
socatnsmean.to_csv("dataframes_made/socatnsmean.csv")
#mssmean.to_csv("dataframes_made/mssmean.csv")
Cefasmean.to_csv("dataframes_made/Cefasmean.csv")
D366mean.to_csv("dataframes_made/D366mean.csv")
RWSnmean.to_csv("dataframes_made/RWSnmean.csv")
RWSomean.to_csv("dataframes_made/RWSomean.csv")

combined = pd.concat(objs=(Cefas, D366, RWSn, glodapns), keys=['Cefas', 'D366', 'RWSn', 'glodapns'])
combined.to_csv("dataframes_made/combined.csv")
resultscombined = pd.concat(objs=(resultsCefas, resultsD366, resultsRWSn, resultsglodapns), keys=['resultsCefas', 'resultsD366', 'resultsRWSn', 'resultsglodapns'])
resultscombined.to_csv("dataframes_made/resultscombined.csv")
combinedmean = pd.concat(objs=(Cefasmean, D366mean, RWSnmean, glodapnsmean), keys=['Cefasmean', 'D366mean', 'RWSnmean', 'glodapnsmean'])
combinedmean.to_csv("dataframes_made/combinedmean.csv")

#%% # Import dataframs

# Initial dataframes are in study area, the wrong data points are dropped
# datetime is created, and distance_to_shore is included
glodapns = pd.read_csv("dataframes_made/glodapns.csv")
socatns = pd.read_csv("dataframes_made/socatns.csv")
mss = pd.read_csv("dataframes_made/mss.csv")
Cefas = pd.read_csv("dataframes_made/Cefas.csv")
D366 = pd.read_csv("dataframes_made/D366.csv")
RWSn = pd.read_csv("dataframes_made/RWSn.csv")
RWSo = pd.read_csv("dataframes_made/RWSo.csv")

# Results are the dataframes of pyCO2sys (all data points)
resultsglodapns = pd.read_csv("dataframes_made/resultsglodapns.csv")
resultssocatnsair = pd.read_csv("dataframes_made/resultssocatnsair.csv")
resultssocatns = pd.read_csv("dataframes_made/resultssocatns.csv")
#resultsmss = pd.read_csv("dataframes_made/resultsmss.csv")
resultsCefas = pd.read_csv("dataframes_made/resultsCefas.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn.csv")
resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo.csv")

# Mean are the dataframes of pyCO2sys (mean per month)
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean.csv")
socatnsairmean = pd.read_csv("dataframes_made/socatnsairmean.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean.csv")
#mssmean = pd.read_csv("dataframes_made/mssmean.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean.csv")
D366mean = pd.read_csv("dataframes_made/D366mean.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean.csv")

combined = pd.read_csv("dataframes_made/combined.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean.csv")
