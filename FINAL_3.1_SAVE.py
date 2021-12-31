import pandas as pd
import koolstof as ks
import PyCO2SYS as pyco2
import pickle
import matplotlib.dates as mdates

#%% # Import all datasets

# SOCAT dataset (area: 51.5-56.5 N & 2.5-7 E) from 1991-2021 (fCO2 air & sea)
socatns = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/SOCATv2.2021_North_Sea.csv", na_values=[-999, -1e+34], skiprows=64, delimiter=",")
socatns.columns = socatns.columns.str.lower()
socatns = socatns.rename(columns={'sal':'salinity', 'temp':'temperature'})
socatns['datetime'] = pd.to_datetime(socatns[['year', 'month', 'day', 'hour', 'minute']], format='%Y%m%d %H%M')

# Excluding SOCAT outliers (close to harbours)
socatnsrotterdam = socatns[(socatns['longitude'] < 4.5) & (socatns['longitude'] > 4.05) & (socatns['latitude'] > 51.8) & (socatns['latitude'] < 52)].index
socatns.drop(socatnsrotterdam, inplace=True)
socatnsantwerp = socatns[(socatns['longitude'] <= 3.09503) & (socatns['longitude'] >= 2.854) & (socatns['latitude'] >= 51.501) & (socatns['latitude'] <= 51.58153)].index
socatns.drop(socatnsantwerp, inplace=True)
socatnshighpeak = socatns[(socatns['longitude'] == 3.1121) & (socatns['latitude'] == 53.0816)].index
socatns.drop(socatnshighpeak, inplace=True)
socatnsfreshwater = socatns[(socatns['longitude'] == 6.5434) & (socatns['latitude'] == 53.0969)].index
socatns.drop(socatnsfreshwater, inplace=True)

# GLODAP dataset (area: 51.5-56.5 N & 2.5-7 E) from 2001-2011 (DIC & TA)
glodapns = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_North_Sea/GLODAPv2.2021_North_Sea.csv")
glodapns = glodapns.rename(columns={'talk':'TA', 'tco2': 'DIC'})
glodapns['datetime'] = pd.to_datetime(glodapns[['year', 'month', 'day', 'hour', 'minute']], format='%Y%m%d %H%M')

# CEFAS dataset from 2014-2015 (DIC & TA)
Cefas = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/Cefas_SSB_data.xlsx", header=0, skiprows=[1])
Cefas = Cefas.rename(columns={'Latitude':'latitude', 'Longitude':'longitude'})
Cefas['datetime'] = pd.to_datetime(Cefas['Date+time (GMT)'])
Cefas = Cefas[(Cefas["latitude"] >= 51.5) & (Cefas["latitude"] <= 56.5) & (Cefas["longitude"] >= 2.5) & (Cefas["longitude"] <= 7)]

# D366 dataset from juni-july 2011 (DIC & TA)
D366 = pd.read_csv("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/D366UWCarbonateChemistrySynthesisData_140328_data.csv")
D366 = D366.rename(columns={'Latitude [+ve = N]':'latitude', 'Longitude [+ve = E]':'longitude', 'DIC [umol/kg]':'DIC', 'TA [umol/kg]':'TA', 'SST [deg C]':'temperature', 'Salinity [dimensionless]':'salinity'})
D366['datetime'] = pd.to_datetime(D366['yyyy-mm-ddThh:mm'])
D366 = D366[(D366["latitude"] >= 51.5) & (D366["latitude"] <= 56.5) & (D366["longitude"] >= 2.5) & (D366["longitude"] <= 7)]

# RWS dataset from 2018-2021 (DIC & TA) - RWSnew
RWSn = pd.read_excel("C:/Users/cecil/Documenten/GitHub/CSH-North-Sea-pH-research-NIOZ/data_DIC_TA/RWS_NIOZ_North_Sea_data_v10_for_SDG14_3_1.xlsx", na_values=-999)
RWSn = RWSn.rename(columns={'LATITUDE':'latitude', 'LONGITUDE': 'longitude', 'dic':'DIC', 'alkalinity':'TA'})
RWSn['datetime'] = pd.to_datetime(RWSn['DATE_UTC'])
RWSn = RWSn[(RWSn["latitude"] >= 51.5) & (RWSn["latitude"] <= 56.5) & (RWSn["longitude"] >= 2.5) & (RWSn["longitude"] <= 7)]
 
# RWS dataset from 1975-2018 (pH) - RWSold
RWSo = pd.read_parquet("C:/Users/cecil/Documenten/GitHub/rws-the-olden-days/data/old_rws_data/rws_compilation.parquet")
RWSo = RWSo[['bod', 'calcium', 'chlorophyll', 'doc', 'poc', 'ammonia', 'nitrite', 'nitrate', 'pn', 'oxygen', 'toc', 'pH', 'phosphate', 'pp', 'dp', 'tp', 'salinity', 'silicate', 'spm', 'temperature', 'dn', 'tn', 'longitude', 'latitude', 'datenum', 'datetime']]
RWSo_surface = RWSo.xs("surface", level="vertical_pos") 
RWSo = RWSo_surface[(RWSo_surface["latitude"] >= 51.5) & (RWSo_surface["latitude"] <= 56.5) & (RWSo_surface["longitude"] >= 2.5) & (RWSo_surface["longitude"] <= 7)]

# Select only North Sea stations
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

#%% # Use pyCO2sys to convert SOCAT atmosphere xCO2 to fCO2 to compute ΔfCO2

socatns = socatns.reset_index()

xco2 = socatns['gvco2'] 
temp = socatns['temperature']
sal = socatns['salinity']

# Define input conditions
kwargs = dict(
    par1 = xco2,  # Value of the first parameter
    par1_type = 9,  # The first parameter supplied is of type "9", which is "xCO2"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature of the sample
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultssocatns = pd.DataFrame.from_dict(results)
resultssocatns['datetime'] = socatns['datetime']
resultssocatns['longitude'] = socatns['longitude']
resultssocatns['latitude'] = socatns['latitude']
resultssocatns['fco2_air'] = resultssocatns['fCO2']
resultssocatns['fco2_sea'] = socatns['fco2_recommended'] 
resultssocatns['deltafco2'] = resultssocatns['fco2_sea'] - resultssocatns['fco2_air']

# Make dataset based on the mean per month
socatnsmean = resultssocatns.set_index('datetime').resample('M').mean()
socatnsmean = socatnsmean.reset_index()
socatnsmean = socatnsmean.dropna(axis='rows', how='all', subset=['fco2_sea'])

#%% # Use pyCO2sys to predict pH with GLODAP DIC and TA 

glodapns = glodapns.reset_index()

TA = glodapns['TA'] 
DIC = glodapns['DIC']
phos = glodapns['phosphate']
sil = glodapns['silicate']
temp = glodapns['temperature']
sal = glodapns['salinity']

# Define input conditions
kwargs = dict(
    par1 = TA,  # Value of the first parameter
    par2 = DIC,  # Value of the second parameter
    par1_type = 1,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 2,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature of the sample
    total_silicate = sil,  # Concentration of silicate  in the sample (in µmol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in µmol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultsglodapns = pd.DataFrame.from_dict(results)
resultsglodapns['datetime'] = glodapns['datetime']
resultsglodapns['longitude'] = glodapns['longitude']
resultsglodapns['latitude'] = glodapns['latitude']
resultsglodapns['oxygen'] = glodapns['oxygen']
resultsglodapns['total_nitrate'] = glodapns['nitrate']

# Make dataset based on the mean per month
glodapnsmean = resultsglodapns.set_index('datetime').resample('M').mean()
glodapnsmean = glodapnsmean.reset_index()
glodapnsmean = glodapnsmean.dropna(axis='rows', how='all', subset=['par1'])

#%% # Use pyCO2sys to predict pH with CEFAS DIC and TA 

Cefas = Cefas.reset_index()

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
    temperature = temp,  # Temperature of the sample
    total_silicate = sil,  # Concentration of silicate  in the sample (in µmol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in µmol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultsCefas = pd.DataFrame.from_dict(results)
resultsCefas['datetime'] = Cefas['datetime']
resultsCefas['longitude'] = Cefas['longitude']
resultsCefas['latitude'] = Cefas['latitude']
resultsCefas['total_nitrate'] = Cefas['Nitrate']

# Make dataset based on the mean per month
Cefasmean = resultsCefas.set_index('datetime').resample('M').mean()
Cefasmean = Cefasmean.reset_index()
Cefasmean = Cefasmean.dropna(axis='rows', how='all', subset=['par1'])

#%% # Use pyCO2sys to predict pH with D366 DIC and TA 

D366 = D366.reset_index()

TA = D366['TA'] 
DIC = D366['DIC']
#pH = D366['pH [dimensionless]']
phos = D366['Phosphate [umol/kg]'] 
sil = D366['Si [umol/kg]']
temp = D366['temperature']
sal = D366['salinity']

# Define input conditions
kwargs = dict(
    par1 = DIC,  # Value of the first parameter
    par2 = TA,  # Value of the second parameter, which is a long vector of different DIC's!
    par1_type = 2,  # The first parameter supplied is of type "1", which is "alkalinity"
    par2_type = 1,  # The second parameter supplied is of type "2", which is "DIC"
    salinity = sal,  # Salinity of the sample
    temperature = temp,  # Temperature of the sample
    total_silicate = sil,  # Concentration of silicate  in the sample (in µmol/kg)
    total_phosphate = phos,# Concentration of phosphate in the sample (in µmol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultsD366 = pd.DataFrame.from_dict(results)
resultsD366['datetime'] = D366['datetime']
resultsD366['longitude'] = D366['longitude']
resultsD366['latitude'] = D366['latitude']
resultsD366['total_nitrate'] = D366['Nitrate [umol/kg]']

# Make dataset based on the mean per month
D366mean = resultsD366.set_index('datetime').resample('M').mean()
D366mean = D366mean.reset_index()
D366mean = D366mean.dropna(axis='rows', how='all', subset=['par1'])

#%% # Use pyCO2sys to predict pH with RWS DIC and TA 

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
    temperature = temp,  # Temperature of the sample
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos,  # Concentration of phosphate in the sample (in umol/kg)
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultsRWSn = pd.DataFrame.from_dict(results)
resultsRWSn['datetime'] = RWSn['datetime']
resultsRWSn['longitude'] = RWSn['longitude']
resultsRWSn['latitude'] = RWSn['latitude']
resultsRWSn['station'] = RWSn['station']
resultsRWSn['total_nitrate'] = RWSn['nitrate']

# Make dataset based on the mean per month
RWSnmean = resultsRWSn.set_index('datetime').resample('M').mean()
RWSnmean = RWSnmean.reset_index()
RWSnmean = RWSnmean.dropna(axis='rows', how='all', subset=['par1'])

#%% # Get the pH of the RWSn (spectro measurements)

results = pyco2.sys(
    par1=RWSn['pH_spectro_total_lab'],
    par2=RWSn['DIC'],
    par1_type=3,
    par2_type=2,
    salinity=RWSn['salinity'],
    temperature=RWSn['pH_spectro_temperature'],
    total_phosphate=RWSn['phosphate'], 
    total_silicate=RWSn['silicate'],
    temperature_out=RWSn['temperature'])

print(results['pH_total_out']) 
results_out = pd.DataFrame.from_dict(results)
results_out['datetime'] = resultsRWSn['datetime']
resultsRWSn['pH_total_spectro_out'] = results_out['pH_total_out']
RWSnmean_out = results_out.set_index('datetime').resample('M').mean()
RWSnmean_out = RWSnmean_out.reset_index()
RWSnmean['pH_total_spectro_out'] = RWSnmean_out['pH_total_out']

#%% # Use pyCO2sys to convert RWS pH in NBS scale to total scale and
# calculate the apparent oxygen utilisation (Garcia & Gordon, 1992)

# Convert oxygen mg/l to umol/kg
densitysw = 1.0248 # Density of seawater at ... degrees celcius
convertfactor = ((0.001/(15.9994*2))*1000000)/densitysw
RWSo['oxygen umol/kg'] = RWSo['oxygen'] * convertfactor

aou = ks.parameterisations.aou_GG92(oxygen=RWSo['oxygen umol/kg'], temperature=RWSo['temperature'], salinity=RWSo['salinity'])
RWSo['aou'] = aou[0]
RWSo['%_aou_from_oxygen'] = aou[1]
RWSo['oxygen_saturation'] = aou[2]

# Convert calcium mg/l to umol/kg
densitysw = 1.0248 # Density of seawater at ... degrees celcius
molarmass = 40.078
convertfactor = ((0.001 / molarmass) * 1000000) / densitysw
RWSo['calcium umol/kg'] = RWSo['calcium'] * convertfactor

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
    temperature = temp,  # Temperature of the sample
    total_silicate = sil,  # Concentration of silicate  in the sample (in umol/kg)
    total_phosphate = phos, # Concentration of phosphate in the sample (in umol/kg)
    opt_pH_scale = 4, # NBS scale has been  used in par1
    opt_k_carbonic = 4,  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    opt_k_bisulfate = 1)  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

results = pyco2.sys(**kwargs)
resultsRWSo = pd.DataFrame.from_dict(results)
resultsRWSo['datetime'] = RWSo['datetime']
resultsRWSo['longitude'] = RWSo['longitude']
resultsRWSo['latitude'] = RWSo['latitude']
resultsRWSo['station'] = RWSo['station']
resultsRWSo['oxygen umol/kg'] = RWSo['oxygen umol/kg']
resultsRWSo['aou'] = RWSo['aou']
resultsRWSo['%_aou_from_oxygen'] = RWSo['%_aou_from_oxygen']
resultsRWSo['oxygen_saturation'] = RWSo['oxygen_saturation']
resultsRWSo['total_ammonia'] = RWSo['ammonia']
resultsRWSo['total_nitrate'] = RWSo['nitrate']
resultsRWSo['chlorophyll'] = RWSo['chlorophyll']
resultsRWSo['calcium umol/kg'] = RWSo['calcium umol/kg']

# Make dataset based on the mean per month
RWSomean = resultsRWSo.set_index('datetime').resample('M').mean()
RWSomean = RWSomean.reset_index()
RWSomean = RWSomean.dropna(axis='rows', how='all', subset=['par1'])

#%% # Use vptree to calculate distance to shore

latrange = (50, 60)
lonrange = (0, 10) 
vpt = ks.maps.build_vptree(latrange, lonrange)

with open("distance_to_shore.pkl", "wb") as f:
      pickle.dump(vpt, f)

with open("distance_to_shore.pkl", "rb") as f:
     vpt = pickle.load(f)
    
#%% # Create distance_to_shore, datenum, dayofyear, month, and year column in every dataset 
# (initial dataset, resultsdataset, datasetmean), set datetime and save dataset

dataset = socatns

for dataset in [socatns, resultssocatns, socatnsmean, glodapns, resultsglodapns, glodapnsmean, 
                D366, resultsD366, D366mean, Cefas, resultsCefas, Cefasmean, RWSn, 
                resultsRWSn, RWSnmean, RWSo, resultsRWSo, RWSomean]:
    
    def caldistance(row):
        print(row.name)
        distance_to_shore = vpt.get_nearest_neighbor((row.longitude, row.latitude))
        return distance_to_shore[0]
    
    test = dataset.apply(caldistance, axis=1)
    
    with open("distance_apply.pkl", "wb") as f:
        pickle.dump(test, f)
    
    with open("distance_apply.pkl", "rb") as f:
        dataset['distance_to_shore'] = pickle.load(f)

    dataset['datenum'] = mdates.date2num(dataset.datetime)
    dataset['dayofyear'] = dataset.datetime.dt.dayofyear
    dataset['month'] = dataset.datetime.dt.month
    dataset['year'] = dataset.datetime.dt.year
    dataset['datetime'] = pd.to_datetime(dataset['datetime'])
    
print('All dataframes are ready for further analysis.')
    
#%% # Make combined datasets of DIC and TA data, and RWS data

# Combined dataset includes GLODAP, D366, CEFAS, RWSn (all DIC and TA data)
combined = pd.concat(objs=(Cefas, D366, RWSn, glodapns), keys=['Cefas', 'D366', 'RWSn', 'glodapns'])
resultscombined = pd.concat(objs=(resultsCefas, resultsD366, resultsRWSn, resultsglodapns), keys=['resultsCefas', 'resultsD366', 'resultsRWSn', 'resultsglodapns'])
combinedmean = pd.concat(objs=(Cefasmean, D366mean, RWSnmean, glodapnsmean), keys=['Cefasmean', 'D366mean', 'RWSnmean', 'glodapnsmean'])

# RWS dataset includes RWSn and RWSo (both RWS dataset)
RWStotal = pd.concat(objs=(RWSn, RWSo), keys=['RWSn', 'RWSo'])
resultsRWStotal = pd.concat(objs=(resultsRWSn, resultsRWSo), keys=['resultsRWSn', 'resultsRWSo'])
RWStotalmean = pd.concat(objs=(RWSnmean, RWSomean), keys=['RWSnmean', 'RWSomean'])            

#%% # Save all datasets

socatns.to_csv("dataframes_made/socatns_final.csv")
glodapns.to_csv("dataframes_made/glodapns_final.csv")
D366.to_csv("dataframes_made/D366_final.csv")
Cefas.to_csv("dataframes_made/Cefas_final.csv")
RWSn.to_csv("dataframes_made/RWSn_final.csv")
RWSo.to_csv("dataframes_made/RWSo_final.csv")
combined.to_csv("dataframes_made/combined_final.csv")
RWStotal.to_csv("dataframes_made/RWStotal_final.csv")

resultssocatns.to_csv("dataframes_made/resultssocatns_final.csv")
resultsglodapns.to_csv("dataframes_made/resultsglodapns_final.csv")
resultsD366.to_csv("dataframes_made/resultsD366_final.csv")
resultsCefas.to_csv("dataframes_made/resultsCefas_final.csv")
resultsRWSn.to_csv("dataframes_made/resultsRWSn_final.csv")
resultsRWSo.to_csv("dataframes_made/resultsRWSo_final.csv")
resultscombined.to_csv("dataframes_made/resultscombined_final.csv")
resultsRWStotal.to_csv("dataframes_made/resultsRWStotal_final.csv")

socatnsmean.to_csv("dataframes_made/socatnsmean_final.csv")
glodapnsmean.to_csv("dataframes_made/glodapnsmean_final.csv")
D366mean.to_csv("dataframes_made/D366mean_final.csv")
Cefasmean.to_csv("dataframes_made/Cefasmean_final.csv")
RWSnmean.to_csv("dataframes_made/RWSnmean_final.csv")
RWSomean.to_csv("dataframes_made/RWSomean_final.csv")
combinedmean.to_csv("dataframes_made/combinedmean_final.csv")
RWStotalmean.to_csv("dataframes_made/RWStotalmean_final.csv")

#%% # Import dataframes

# socatns = pd.read_csv("dataframes_made/socatns_final.csv")
# glodapns = pd.read_csv("dataframes_made/glodapns_final.csv")
# D366 = pd.read_csv("dataframes_made/D366_final.csv")
# Cefas = pd.read_csv("dataframes_made/Cefas_final.csv")
# RWSn = pd.read_csv("dataframes_made/RWSn_final.csv")
# RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
# combined = pd.read_csv("dataframes_made/combined_final.csv")
# RWStotal = pd.read_csv("dataframes_made/RWStotal_final.csv")

# resultssocatns = pd.read_csv("dataframes_made/resultssocatns_final.csv")
# resultsglodapns = pd.read_csv("dataframes_made/resultsglodapns_final.csv")
# resultsD366 = pd.read_csv("dataframes_made/resultsD366_final.csv")
# resultsCefas = pd.read_csv("dataframes_made/resultsCefas_final.csv")
# resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn_final.csv")
# resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
# resultscombined = pd.read_csv("dataframes_made/resultscombined_final.csv")
# resultsRWStotal = pd.read_csv("dataframes_made/resultsRWStotal_final.csv")

# socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
# glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean_final.csv")
# D366mean = pd.read_csv("dataframes_made/D366mean_final.csv")
# Cefasmean = pd.read_csv("dataframes_made/Cefasmean_final.csv")
# RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
# RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
# combinedmean = pd.read_csv("dataframes_made/combinedmean_final.csv")
# RWStotalmean = pd.read_csv("dataframes_made/RWStotalmean_final.csv")

