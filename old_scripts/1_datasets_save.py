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

#%% # Import GLODAP data set

# glodapao = pd.read_csv("C:/Users/cecil/.spyder-py3/Python-nioz-2021/GLODAP/data/GLODAPv2.2021_Atlantic_Ocean.csv", na_values = -9999)
# glodapao.columns = glodapao.columns.str[2:]

# glodapns = glodapao[(glodapao["latitude"] >= 51.5) & (glodapao["latitude"] <= 56.5) 
#                     & (glodapao["longitude"] >= 2.5) & (glodapao["longitude"] <= 7)]
# glodapns.to_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/GLODAPv2.2021_North_Sea.csv", index=False)

glodapns = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/GLODAPv2.2021_North_Sea.csv")
glodapns = glodapns.rename(columns={'talk':'TA', 'tco2': 'DIC'})
glodapns['datetime'] = pd.to_datetime(glodapns[['year', 'month', 'day', 'hour', 'minute']], format='%Y%m%d %H%M')

#%% # Import DIC and TA datasets

Cefas = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/Cefas_SSB_data.xlsx", header=0, skiprows=[1])
D366 = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/D366UWCarbonateChemistrySynthesisData_140328_data.csv")
RWSn = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/RWS_NIOZ_North_Sea_data_v10_for_SDG14_3_1.xlsx", na_values=-999)

Cefas = Cefas.rename(columns={'Latitude':'latitude', 'Longitude':'longitude'})
D366 = D366.rename(columns={'Latitude [+ve = N]':'latitude', 'Longitude [+ve = E]':'longitude', 'DIC [umol/kg]':'DIC', 'TA [umol/kg]':'TA'})
RWSn = RWSn.rename(columns={'LATITUDE':'latitude', 'LONGITUDE': 'longitude', 'dic':'DIC', 'alkalinity':'TA'})

Cefas['datetime'] = pd.to_datetime(Cefas['Date+time (GMT)'])
D366['datetime'] = pd.to_datetime(D366['yyyy-mm-ddThh:mm'])
RWSn['datetime'] = pd.to_datetime(RWSn['DATE_UTC'])

Cefas = Cefas[(Cefas["latitude"] >= 51.5) & (Cefas["latitude"] <= 56.5) 
                    & (Cefas["longitude"] >= 2.5) & (Cefas["longitude"] <= 7)]
D366 = D366[(D366["latitude"] >= 51.5) & (D366["latitude"] <= 56.5) 
                    & (D366["longitude"] >= 2.5) & (D366["longitude"] <= 7)]
RWSn = RWSn[(RWSn["latitude"] >= 51.5) & (RWSn["latitude"] <= 56.5) 
                    & (RWSn["longitude"] >= 2.5) & (RWSn["longitude"] <= 7)]
    
#%% # Import RWSo data set

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
RWSo['datetime'] = RWSo['datetime'].dt.tz_localize(None)

#%% # Use vptree to calculate distance to shore

latrange = (50, 60)
lonrange = (0, 10) 
vpt = ks.maps.build_vptree(latrange, lonrange)

with open("distance_to_shore.pkl", "wb") as f:
      pickle.dump(vpt, f)

with open("distance_to_shore.pkl", "rb") as f:
     vpt = pickle.load(f)
    
#%% # Create distance_to_shore column in dataset (COMPLETE data)

def caldistance(row):
    print(row.name)
    distance_to_shore = vpt.get_nearest_neighbor((row.longitude, row.latitude))
    return distance_to_shore[0]

test = RWSnmean_out.apply(caldistance, axis=1)

with open("distance_apply.pkl", "wb") as f:
    pickle.dump(test, f)

with open("distance_apply.pkl", "rb") as f:
    RWSnmean_out['distance_to_shore'] = pickle.load(f)

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
    opt_k_bisulfate = 1  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultssocatnsair = pd.DataFrame.from_dict(results)
resultssocatnsair['datetime'] = socatns['datetime']
resultssocatnsair['longitude'] = socatns['longitude']
resultssocatnsair['latitude'] = socatns['latitude']
resultssocatnsair['distance_to_shore'] = socatns['distance_to_shore']

# Make dataset based on the mean 
socatnsairmean = resultssocatnsair.set_index('datetime').resample('M').mean()
socatnsairmean = socatnsairmean.reset_index()
socatnsairmean = socatnsairmean.dropna(axis='rows', how='all', subset=['xCO2'])

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
    opt_k_bisulfate = 1  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultssocatns = pd.DataFrame.from_dict(results)
resultssocatns['datetime'] = socatns['datetime']
resultssocatns['longitude'] = socatns['longitude']
resultssocatns['latitude'] = socatns['latitude']
resultssocatns['fco2_air'] = resultssocatnsair['fCO2']
resultssocatns['deltafco2'] = resultssocatns['fCO2'] - resultssocatns['fco2_air']
resultssocatns['distance_to_shore'] = socatns['distance_to_shore']

# Make dataset based on the mean 
# socatnsmean['fco2_air'] = socatnsairmean['fCO2']
# socatnsmean['deltafco2'] = socatnsmean['fCO2'] - socatnsmean['fco2_air']
socatnsmean = resultssocatns.set_index('datetime').resample('M').mean()
socatnsmean = socatnsmean.reset_index()
socatnsmean = socatnsmean.dropna(axis='rows', how='all', subset=['par1'])

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
resultsglodapns['longitude'] = glodapns['longitude']
resultsglodapns['latitude'] = glodapns['latitude']
resultsglodapns['oxygen'] = glodapns['oxygen']
resultsglodapns['total_nitrate'] = glodapns['nitrate']

# Make dataset based on the mean 
glodapnsmean = resultsglodapns.set_index('datetime').resample('M').mean()
glodapnsmean = glodapnsmean.reset_index()
glodapnsmean = glodapnsmean.dropna(axis='rows', how='all', subset=['par1'])

#%% # PyCO2sys Cefas

TA = Cefas['TA'] 
DIC = Cefas['DIC']
phos = Cefas['Phosphate'] 
sil = Cefas['Silicate']
temp = Cefas['Temperature']
sal = Cefas['Salinity (practical)']

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
resultsCefas = pd.DataFrame.from_dict(results)

Cefas = Cefas.reset_index()
resultsCefas['datetime'] = Cefas['datetime']
resultsCefas['longitude'] = Cefas['longitude']
resultsCefas['latitude'] = Cefas['latitude']
resultsCefas['total_nitrate'] = Cefas['Nitrate']

# Make dataset based on the mean 
Cefasmean = resultsCefas.set_index('datetime').resample('M').mean()
Cefasmean = Cefasmean.reset_index()
Cefasmean = Cefasmean.dropna(axis='rows', how='all', subset=['par1'])

#%% # PyCO2sys D366

TA = D366['TA'] 
DIC = D366['DIC']
#pH = D366['pH [dimensionless]']
phos = D366['Phosphate [umol/kg]'] 
sil = D366['Si [umol/kg]']
temp = D366['SST [deg C]']
sal = D366['Salinity [dimensionless]']

# Define input conditions
kwargs = dict(
    par1 = DIC,  # Value of the first parameter
    par2 = TA,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 2,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 1,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature at input conditions
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,# Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsD366 = pd.DataFrame.from_dict(results)
# D366 = D366.reset_index()
resultsD366['datetime'] = D366['datetime']
resultsD366['longitude'] = D366['longitude']
resultsD366['latitude'] = D366['latitude']
resultsD366['total_nitrate'] = D366['Nitrate [umol/kg]']

# Make dataset based on the mean 
D366mean = resultsD366.set_index('datetime').resample('M').mean()
D366mean = D366mean.reset_index()
D366mean = D366mean.dropna(axis='rows', how='all', subset=['par1'])
#D366mean['datenum'] = mdates.date2num(D366mean.datetime)

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
resultsRWSn['longitude'] = RWSn['longitude']
resultsRWSn['latitude'] = RWSn['latitude']
resultsRWSn['station'] = RWSn['station']
resultsRWSn['total_nitrate'] = RWSn['nitrate']

# Make dataset based on the mean 
RWSnmean = resultsRWSn.set_index('datetime').resample('M').mean()
RWSnmean = RWSnmean.reset_index()
RWSnmean = RWSnmean.dropna(axis='rows', how='all', subset=['par1'])

RWSnstation = resultsRWSn.groupby(by=['dayofyear', 'month', 'year', 'station']).mean()

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
    total_phosphate = phos, # Concentration of phosphate in the sample (in umol/kg)
    opt_pH_scale = 4, # NBS scale has been  used in par1
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1,  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
)

results = pyco2.sys(**kwargs)
resultsRWSo = pd.DataFrame.from_dict(results)
resultsRWSo['datetime'] = RWSo['datetime']
resultsRWSo['longitude'] = RWSo['longitude']
resultsRWSo['latitude'] = RWSo['latitude']
resultsRWSo['station'] = RWSo['station']
resultsRWSo['oxygen'] = RWSo['oxygen']
resultsRWSo['total_ammonia'] = RWSo['ammonia']
resultsRWSo['total_nitrate'] = RWSo['nitrate']
resultsRWSo['chlorophyll'] = RWSo['chlorophyll']
resultsRWSo['total_calcium'] = RWSo['calcium']

# Make dataset based on the mean 
RWSomean = resultsRWSo.set_index('datetime').resample('M').mean()
RWSomean = RWSomean.reset_index()
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['par1'])

RWSostation = resultsRWSo.groupby(by=['dayofyear', 'month', 'year', 'station']).mean()
RWSostation['distance_to_shore'] = RWSo['distance_to_shore']

#%% # Create distance_to_shore column in dataset (MEAN & RESULTS data)

def caldistance(row):
    print(row.name)
    distance_to_shore = vpt.get_nearest_neighbor((row.longitude, row.latitude))
    return distance_to_shore[0]

test = RWSnstation.apply(caldistance, axis=1)

with open("distance_apply.pkl", "wb") as f:
    pickle.dump(test, f)

with open("distance_apply.pkl", "rb") as f:
    RWSnstation['distance_to_shore'] = pickle.load(f)


#%% # Make datenum, dayofyear, month, year column

resultssocatnsair['datenum'] = mdates.date2num(resultssocatnsair.datetime)
resultssocatnsair['dayofyear'] = resultssocatnsair.datetime.dt.dayofyear
resultssocatnsair['month'] = resultssocatnsair.datetime.dt.month
resultssocatnsair['year'] = resultssocatnsair.datetime.dt.year
socatnsairmean['datenum'] = mdates.date2num(socatnsairmean.datetime)
socatnsairmean['dayofyear'] = socatnsairmean.datetime.dt.dayofyear
socatnsairmean['month'] = socatnsairmean.datetime.dt.month
socatnsairmean['year'] = socatnsairmean.datetime.dt.year

socatns['datenum'] = mdates.date2num(socatns.datetime)
socatns['dayofyear'] = socatns.datetime.dt.dayofyear
socatns['month'] = socatns.datetime.dt.month
socatns['year'] = socatns.datetime.dt.year
resultssocatns['datenum'] = mdates.date2num(resultssocatns.datetime)
resultssocatns['dayofyear'] = resultssocatns.datetime.dt.dayofyear
resultssocatns['month'] = resultssocatns.datetime.dt.month
resultssocatns['year'] = resultssocatns.datetime.dt.year
socatnsmean['datenum'] = mdates.date2num(socatnsmean.datetime)
socatnsmean['dayofyear'] = socatnsmean.datetime.dt.dayofyear
socatnsmean['month'] = socatnsmean.datetime.dt.month
socatnsmean['year'] = socatnsmean.datetime.dt.year

glodapns['datenum'] = mdates.date2num(glodapns.datetime)
glodapns['dayofyear'] = glodapns.datetime.dt.dayofyear
glodapns['month'] = glodapns.datetime.dt.month
glodapns['year'] = glodapns.datetime.dt.year
resultsglodapns['datenum'] = mdates.date2num(resultsglodapns.datetime)
resultsglodapns['dayofyear'] = resultsglodapns.datetime.dt.dayofyear
resultsglodapns['month'] = resultsglodapns.datetime.dt.month
resultsglodapns['year'] = resultsglodapns.datetime.dt.year
glodapnsmean['datenum'] = mdates.date2num(glodapnsmean.datetime)
glodapnsmean['dayofyear'] = glodapnsmean.datetime.dt.dayofyear
glodapnsmean['month'] = glodapnsmean.datetime.dt.month
glodapnsmean['year'] = glodapnsmean.datetime.dt.year

Cefas['datenum'] = mdates.date2num(Cefas.datetime)
Cefas['dayofyear'] = Cefas.datetime.dt.dayofyear
Cefas['month'] = Cefas.datetime.dt.month
Cefas['year'] = Cefas.datetime.dt.year
resultsCefas['datenum'] = mdates.date2num(resultsCefas.datetime)
resultsCefas['dayofyear'] = resultsCefas.datetime.dt.dayofyear
resultsCefas['month'] = resultsCefas.datetime.dt.month
resultsCefas['year'] = resultsCefas.datetime.dt.year
Cefasmean['datenum'] = mdates.date2num(Cefasmean.datetime)
Cefasmean['dayofyear'] = Cefasmean.datetime.dt.dayofyear
Cefasmean['month'] = Cefasmean.datetime.dt.month
Cefasmean['year'] = Cefasmean.datetime.dt.year

D366['datenum'] = mdates.date2num(D366.datetime)
D366['dayofyear'] = D366.datetime.dt.dayofyear
D366['month'] = D366.datetime.dt.month
D366['year'] = D366.datetime.dt.year
resultsD366['datenum'] = mdates.date2num(resultsD366.datetime)
resultsD366['dayofyear'] = resultsD366.datetime.dt.dayofyear
resultsD366['month'] = resultsD366.datetime.dt.month
resultsD366['year'] = resultsD366.datetime.dt.year
D366mean['datenum'] = mdates.date2num(D366mean.datetime)
D366mean['dayofyear'] = D366mean.datetime.dt.dayofyear
D366mean['month'] = D366mean.datetime.dt.month
D366mean['year'] = D366mean.datetime.dt.year

RWSn['datenum'] = mdates.date2num(RWSn.datetime)
RWSn['dayofyear'] = RWSn.datetime.dt.dayofyear
RWSn['month'] = RWSn.datetime.dt.month
RWSn['year'] = RWSn.datetime.dt.year
resultsRWSn['datenum'] = mdates.date2num(resultsRWSn.datetime)
resultsRWSn['dayofyear'] = resultsRWSn.datetime.dt.dayofyear
resultsRWSn['month'] = resultsRWSn.datetime.dt.month
resultsRWSn['year'] = resultsRWSn.datetime.dt.year
RWSnmean['datenum'] = mdates.date2num(RWSnmean.datetime)
RWSnmean['dayofyear'] = RWSnmean.datetime.dt.dayofyear
RWSnmean['month'] = RWSnmean.datetime.dt.month
RWSnmean['year'] = RWSnmean.datetime.dt.year

RWSo['datenum'] = mdates.date2num(RWSo.datetime)
RWSo['dayofyear'] = RWSo.datetime.dt.dayofyear
RWSo['month'] = RWSo.datetime.dt.month
RWSo['year'] = RWSo.datetime.dt.year
resultsRWSo['datenum'] = mdates.date2num(resultsRWSo.datetime)
resultsRWSo['dayofyear'] = resultsRWSo.datetime.dt.dayofyear
resultsRWSo['month'] = resultsRWSo.datetime.dt.month
resultsRWSo['year'] = resultsRWSo.datetime.dt.year
RWSomean['datenum'] = mdates.date2num(RWSomean.datetime)
RWSomean['dayofyear'] = RWSomean.datetime.dt.dayofyear
RWSomean['month'] = RWSomean.datetime.dt.month
RWSomean['year'] = RWSomean.datetime.dt.year

#%% # Make combined dataset

combined = pd.concat(objs=(Cefas, D366, RWSn, glodapns), keys=['Cefas', 'D366', 'RWSn', 'glodapns'])
resultscombined = pd.concat(objs=(resultsCefas, resultsD366, resultsRWSn, resultsglodapns), keys=['resultsCefas', 'resultsD366', 'resultsRWSn', 'resultsglodapns'])
combinedmean = pd.concat(objs=(Cefasmean, D366mean, RWSnmean, glodapnsmean), keys=['Cefasmean', 'D366mean', 'RWSnmean', 'glodapnsmean'])

#resultscombined = resultscombined.dropna(axis='rows', how='all', subset=['par1'])
combinedmean['datenum'] = mdates.date2num(combinedmean.datetime)

#%% # Save datasets

socatns.to_csv("dataframes_made/socatns2.csv")
glodapns.to_csv("dataframes_made/glodapns2.csv")
Cefas.to_csv("dataframes_made/Cefas2.csv")
D366.to_csv("dataframes_made/D3662.csv")
RWSn.to_csv("dataframes_made/RWSn2.csv")
RWSo.to_csv("dataframes_made/RWSo2.csv")
combined.to_csv("dataframes_made/combined2.csv")

resultsglodapns.to_csv("dataframes_made/resultsglodapns2.csv")
resultssocatnsair.to_csv("dataframes_made/resultssocatnsair2.csv")
resultssocatns.to_csv("dataframes_made/resultssocatns2.csv")
resultsCefas.to_csv("dataframes_made/resultsCefas2.csv")
resultsD366.to_csv("dataframes_made/resultsD3662.csv")
resultsRWSn.to_csv("dataframes_made/resultsRWSn2.csv")
resultsRWSo.to_csv("dataframes_made/resultsRWSo2.csv")
resultscombined.to_csv("dataframes_made/resultscombined2.csv")

glodapnsmean.to_csv("dataframes_made/glodapnsmean2.csv")
socatnsairmean.to_csv("dataframes_made/socatnsairmean2.csv")
socatnsmean.to_csv("dataframes_made/socatnsmean2.csv")
Cefasmean.to_csv("dataframes_made/Cefasmean2.csv")
D366mean.to_csv("dataframes_made/D366mean2.csv")
RWSnmean.to_csv("dataframes_made/RWSnmean2.csv")
RWSomean.to_csv("dataframes_made/RWSomean2.csv")
combinedmean.to_csv("dataframes_made/combinedmean2.csv")

RWSnstation.to_csv("dataframes_made/RWSnstation.csv")
RWSostation.to_csv("dataframes_made/RWSostation.csv")
