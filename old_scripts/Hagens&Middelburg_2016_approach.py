import PyCO2SYS as pyco2
from sklearn.cluster import MeanShift

#%% # Getting the means of the whole period (2000 - 2021)

LR = (resultsRWSo['year'] >= 2000)
LC = (resultscombined['year'] >= 2000)

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(),
    "Tmean": resultsRWSo[LR].temperature.mean(),
    "Smean": resultsRWSo[LR].salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSo[LR].total_borate.mean(),
    "TotFmean": resultsRWSo[LR].total_fluoride.mean(),
    "TotSO4mean": resultsRWSo[LR].total_sulfate.mean(),
    "TotNH3mean": resultsRWSo[LR].total_ammonia.mean(),
    "TotPhosmean": resultsRWSo[LR].total_phosphate.mean(),
    "TotSimean": resultsRWSo[LR].total_silicate.mean()}

print(overbarvalues['pHmean']) # 7.898909700381638

#%% # Getting the means of the year 2000-2005

LR = (resultsRWSo['year'] >= 2000) & (resultsRWSo['year'] <= 2005) 
LC = (resultscombined['year'] >= 2000) & (resultscombined['year'] <= 2005) 

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(),
    "Tmean": resultsRWSo[LR].temperature.mean(),
    "Smean": resultsRWSo[LR].salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSo[LR].total_borate.mean(),
    "TotFmean": resultsRWSo[LR].total_fluoride.mean(),
    "TotSO4mean": resultsRWSo[LR].total_sulfate.mean(),
    "TotNH3mean": resultsRWSo[LR].total_ammonia.mean(),
    "TotPhosmean": resultsRWSo[LR].total_phosphate.mean(),
    "TotSimean": resultsRWSo[LR].total_silicate.mean()}

print(overbarvalues['pHmean']) # 7.9378801529016005

#%% # Getting the means of the year 2005-2010

LR = (resultsRWSo['year'] >= 2005) & (resultsRWSo['year'] <= 2010) 
LC = (resultscombined['year'] >= 2005) & (resultscombined['year'] <= 2010) 

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(),
    "Tmean": resultsRWSo[LR].temperature.mean(),
    "Smean": resultsRWSo[LR].salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSo[LR].total_borate.mean(),
    "TotFmean": resultsRWSo[LR].total_fluoride.mean(),
    "TotSO4mean": resultsRWSo[LR].total_sulfate.mean(),
    "TotNH3mean": resultsRWSo[LR].total_ammonia.mean(),
    "TotPhosmean": resultsRWSo[LR].total_phosphate.mean(),
    "TotSimean": resultsRWSo[LR].total_silicate.mean()}

print(overbarvalues['pHmean']) # 7.903210290869563

#%% # Getting the means of the year 2010-2015

LR = (resultsRWSo['year'] >= 2010) & (resultsRWSo['year'] <= 2015) 
LC = (resultscombined['year'] >= 2010) & (resultscombined['year'] <= 2015) 

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(),
    "Tmean": resultsRWSo[LR].temperature.mean(),
    "Smean": resultsRWSo[LR].salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSo[LR].total_borate.mean(),
    "TotFmean": resultsRWSo[LR].total_fluoride.mean(),
    "TotSO4mean": resultsRWSo[LR].total_sulfate.mean(),
    "TotNH3mean": resultsRWSo[LR].total_ammonia.mean(),
    "TotPhosmean": resultsRWSo[LR].total_phosphate.mean(),
    "TotSimean": resultsRWSo[LR].total_silicate.mean()}

print(overbarvalues['pHmean']) # 7.853175226243286

#%% # Getting the means of the year 2015-2018

LR = (resultsRWSo['year'] >= 2015) & (resultsRWSo['year'] <= 2018) 
LC = (resultscombined['year'] >= 2015) & (resultscombined['year'] <= 2018) 

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(),
    "Tmean": resultsRWSo[LR].temperature.mean(),
    "Smean": resultsRWSo[LR].salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSo[LR].total_borate.mean(),
    "TotFmean": resultsRWSo[LR].total_fluoride.mean(),
    "TotSO4mean": resultsRWSo[LR].total_sulfate.mean(),
    "TotNH3mean": resultsRWSo[LR].total_ammonia.mean(),
    "TotPhosmean": resultsRWSo[LR].total_phosphate.mean(),
    "TotSimean": resultsRWSo[LR].total_silicate.mean()}

print(overbarvalues['pHmean']) # 7.8797986596957985

#%% # Getting the means of the RWSn only (2018-2021)

LR = (resultsRWSo['year'] >= 2018)
LC = (resultscombined['year'] >= 2018)

# The parameters with overbars represent the annual means = H0
overbarvalues = {
    "pHmean": resultsRWSo[LR].pH_total.mean(), 
    "pHmean_out": results_out.pH_total_out.mean(),
    "Tmean": resultsRWSn.temperature.mean(),
    "Smean": resultsRWSn.salinity.mean(),
    "DICmean": resultscombined[LC].normalized_DIC.mean(),
    "TAmean": resultscombined[LC].normalized_TA.mean(),
    "TotBmean": resultsRWSn.total_borate.mean(),
    "TotFmean": resultsRWSn.total_fluoride.mean(),
    "TotSO4mean": resultsRWSn.total_sulfate.mean(),
    "TotNH3mean": resultsRWSn.total_ammonia.mean(),
    "TotPhosmean": resultsRWSn.total_phosphate.mean(),
    "TotSimean": resultsRWSn.total_silicate.mean()}

print(overbarvalues['pHmean']) # 8.019276848246173
print(overbarvalues['pHmean_out']) # 7.735306945494023

#%% # Getting the derivatives of the mean values

# Arguments (splatting)
kwargs = {
    "par1": overbarvalues['DICmean'], # DIC
    "par2": overbarvalues['TAmean'], # TA
    "par1_type": 2,
    "par2_type": 1,
    "temperature": overbarvalues['Tmean'],
    "salinity": overbarvalues['Smean'],
    "total_borate": overbarvalues['TotBmean'], 
    "total_fluoride": overbarvalues['TotFmean'],
    "total_sulfate": overbarvalues['TotSO4mean'],
    "total_ammonia": overbarvalues['TotNH3mean'],
    "total_phosphate": overbarvalues['TotPhosmean'], 
    "total_silicate": overbarvalues['TotSimean']}

results = pyco2.sys(
    **kwargs,
    grads_of=["pH_total"],
    grads_wrt=["temperature", "salinity", "par1", "par2", "total_borate", 
               "total_fluoride", "total_sulfate", "total_ammonia", 
               "total_phosphate", "total_silicate"])

print(results['pH_total']) 
pH_total_overbar = results['pH_total']
d_pH_total__d_dic = results['d_pH_total__d_par1']
d_pH_total__d_alkalinity = results['d_pH_total__d_par2']

#%% # resultsRWSo - Overbar values H0 - data values

parameters = pd.DataFrame(resultsRWSo[LR].temperature)
parameters['T_overbar'] = overbarvalues['Tmean']
parameters['T-T'] = parameters['temperature'] - parameters['T_overbar']
parameters['salinity'] = resultsRWSo[LR].salinity
parameters['S_overbar'] = overbarvalues['Smean']
parameters['S-S'] = parameters['salinity'] - parameters['S_overbar']
parameters['borate'] = resultsRWSo[LR].total_borate
parameters['TotB_overbar'] = overbarvalues['TotBmean']
parameters['TotB-TotB'] = parameters['borate'] - parameters['TotB_overbar']
parameters['fluoride'] = resultsRWSo[LR].total_fluoride
parameters['TotF_overbar'] = overbarvalues['TotFmean']
parameters['TotF-TotF'] = parameters['fluoride'] - parameters['TotF_overbar']
parameters['sulfate'] = resultsRWSo[LR].total_sulfate
parameters['TotSO4_overbar'] = overbarvalues['TotSO4mean']
parameters['TotSO4-TotSO4'] =  parameters['sulfate'] - parameters['TotSO4_overbar']
parameters['ammonia'] = resultsRWSo[LR].total_ammonia
parameters['TotNH3_overbar'] = overbarvalues['TotNH3mean']
parameters['TotNH3-TotNH3'] = parameters['ammonia'] - parameters['TotNH3_overbar']
parameters['phosphate'] = resultsRWSo[LR].total_phosphate
parameters['TotPhos_overbar'] = overbarvalues['TotPhosmean'] 
parameters['TotPhos-TotPhos'] = parameters['phosphate'] - parameters['TotPhos_overbar']
parameters['silicate'] = resultsRWSo[LR].total_silicate
parameters['TotSi_overbar'] = overbarvalues['TotSimean']
parameters['TotSi-TotSi'] = parameters['silicate'] - parameters['TotSi_overbar'] 

parameters['dayofyear'] = resultsRWSo[LR].dayofyear

#%% # resultsRWSn - Overbar values H0 - data values

parameters = pd.DataFrame(resultsRWSn.temperature)
parameters['T_overbar'] = overbarvalues['Tmean']
parameters['T-T'] = parameters['temperature'] - parameters['T_overbar']
parameters['salinity'] = resultsRWSn.salinity
parameters['S_overbar'] = overbarvalues['Smean']
parameters['S-S'] = parameters['salinity'] - parameters['S_overbar']
parameters['borate'] = resultsRWSn.total_borate
parameters['TotB_overbar'] = overbarvalues['TotBmean']
parameters['TotB-TotB'] =  parameters['borate'] - parameters['TotB_overbar']
parameters['fluoride'] = resultsRWSn.total_fluoride
parameters['TotF_overbar'] = overbarvalues['TotFmean']
parameters['TotF-TotF'] = parameters['fluoride'] - parameters['TotF_overbar']
parameters['sulfate'] = resultsRWSn.total_sulfate
parameters['TotSO4_overbar'] = overbarvalues['TotSO4mean']
parameters['TotSO4-TotSO4'] = parameters['sulfate'] - parameters['TotSO4_overbar']
parameters['ammonia'] = resultsRWSn.total_ammonia
parameters['TotNH3_overbar'] = overbarvalues['TotNH3mean']
parameters['TotNH3-TotNH3'] = parameters['ammonia'] - parameters['TotNH3_overbar']
parameters['phosphate'] = resultsRWSn.total_phosphate
parameters['TotPhos_overbar'] = overbarvalues['TotPhosmean'] 
parameters['TotPhos-TotPhos'] = parameters['phosphate'] - parameters['TotPhos_overbar']
parameters['silicate'] = resultsRWSn.total_silicate
parameters['TotSi_overbar'] = overbarvalues['TotSimean']
parameters['TotSi-TotSi'] = parameters['silicate'] - parameters['TotSi_overbar']

parameters['dayofyear'] = resultsRWSn.dayofyear

#%% # Resultscombined - Overbar values H0 - data values

parametersDA = pd.DataFrame(resultscombined[LC].normalized_DIC)
parametersDA['DIC_overbar'] = overbarvalues['DICmean']
parametersDA['DIC-DIC'] = parametersDA['normalized_DIC'] - parametersDA['DIC_overbar']
parametersDA['normalized_TA'] = resultscombined[LC].normalized_TA
parametersDA['TA_overbar'] = overbarvalues['TAmean']
parametersDA['TA-TA'] = parametersDA['normalized_TA'] - parametersDA['TA_overbar']

parametersDA['dayofyear'] = resultscombined[LC].dayofyear

#%% # Deleting the nans 

parametersNN = parameters.dropna()     
parametersDANN = parametersDA.dropna()     

allparameters = (pd.merge(parametersNN, parametersDANN, how='outer', on='dayofyear'))

#%% # Calculation (2) 

allparameters['pHpredicted'] = (pH_total_overbar + 
(results['d_pH_total__d_temperature']*(allparameters['T-T'])) +
(results['d_pH_total__d_salinity']*(allparameters['S-S'])) +
(d_pH_total__d_dic*(allparameters['DIC-DIC'])) +
(d_pH_total__d_alkalinity*(allparameters['TA-TA'])) +
(results['d_pH_total__d_total_borate']*(allparameters['TotB-TotB'])) +
(results['d_pH_total__d_total_fluoride']*(allparameters['TotF-TotF'])) +
(results['d_pH_total__d_total_sulfate']*(allparameters['TotSO4-TotSO4'])) +
((results['d_pH_total__d_total_ammonia']*(allparameters['TotNH3-TotNH3'])) +
(results['d_pH_total__d_total_phosphate']*(allparameters['TotPhos-TotPhos'])) +
(results['d_pH_total__d_total_silicate']*(allparameters['TotSi-TotSi']))))

#%% # Get the pH predicted for each individual parameter

# Determination of the principal drivers of pH seasonality - per each parameter
allparameters['pH_T'] = pH_total_overbar + (results['d_pH_total__d_temperature']*(allparameters['T-T'])) 
allparameters['pH_S'] = pH_total_overbar + (results['d_pH_total__d_salinity']*(allparameters['S-S']))  
allparameters['pH_DIC'] = pH_total_overbar + ((d_pH_total__d_dic)*(allparameters['DIC-DIC']))  
allparameters['pH_TA'] = pH_total_overbar + ((d_pH_total__d_alkalinity)*(allparameters['TA-TA']))  
allparameters['pH_TotB'] = pH_total_overbar + (results['d_pH_total__d_total_borate']*(allparameters['TotB-TotB']))  
allparameters['pH_TotF'] = pH_total_overbar + (results['d_pH_total__d_total_fluoride']*(allparameters['TotF-TotF'])) 
allparameters['pH_TotSO4'] = pH_total_overbar + (results['d_pH_total__d_total_sulfate']*(allparameters['TotSO4-TotSO4']))  
allparameters['pH_TotNH3'] = pH_total_overbar + (results['d_pH_total__d_total_ammonia']*(allparameters['TotNH3-TotNH3'])) 
allparameters['pH_TotPhos'] = pH_total_overbar + (results['d_pH_total__d_total_phosphate']*(allparameters['TotPhos-TotPhos'])) 
allparameters['pH_TotSi'] = pH_total_overbar + (results['d_pH_total__d_total_silicate']*(allparameters['TotSi-TotSi'])) 

#%% # 2000-2021

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[1438 : 1537].assign(**{'dayofyear':-19}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[8318 : 8353].assign(**{'dayofyear':378}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[3612] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[23] *1].assign(**{'dayofyear':367}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[352] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[665] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1761] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1121] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1520] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[3216] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1131] *1].assign(**{'dayofyear':-8}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1528] *1].assign(**{'dayofyear':-8}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[3224] *1].assign(**{'dayofyear':-8}), ignore_index=True)

#%% # 2000-2005

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[1731:1750].assign(**{'dayofyear':407}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[2074 : 2080].assign(**{'dayofyear':-35}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1998 : 2042].assign(**{'dayofyear':-36}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[1607] *1].assign(**{'dayofyear':367}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[23] *1].assign(**{'dayofyear':367}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[97] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[249] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[572] *1].assign(**{'dayofyear':-2}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[361] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[512] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1055] *1].assign(**{'dayofyear':368}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[371] *1].assign(**{'dayofyear':-8}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[520] *1].assign(**{'dayofyear':-8}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1063] *1].assign(**{'dayofyear':-8}), ignore_index=True)

#%% # 2005-2010

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[171:174].assign(**{'dayofyear':370}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[548:554].assign(**{'dayofyear':-35}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[214:225].assign(**{'dayofyear':-36}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[13971] *1].assign(**{'dayofyear':372}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[12] *1].assign(**{'dayofyear':367}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[363] *1].assign(**{'dayofyear':370}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[500] *1].assign(**{'dayofyear':370}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1061] *1].assign(**{'dayofyear':370}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[22] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[133] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[257] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[373] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[409] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[509] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[593] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[783] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[811] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[901] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[989] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1069] *1].assign(**{'dayofyear':-11}), ignore_index=True)

#%% # 2010-2015

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[832:834].assign(**{'dayofyear':371}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1050:1051].assign(**{'dayofyear':372}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[294:297].assign(**{'dayofyear':-13}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[801:803].assign(**{'dayofyear':373}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1022:1023].assign(**{'dayofyear':374}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1018:1021].assign(**{'dayofyear':-14}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[961:964].assign(**{'dayofyear':-135}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[15367] *1].assign(**{'dayofyear':-13}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[169] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[261] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[613] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[796] *1].assign(**{'dayofyear':372}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[438] *1].assign(**{'dayofyear':372}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[45] *1].assign(**{'dayofyear':-13}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[327] *1].assign(**{'dayofyear':-13}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[500] *1].assign(**{'dayofyear':-13}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1020] *1].assign(**{'dayofyear':-13}), ignore_index=True)

#%% # 2015-2018

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[884:886].assign(**{'dayofyear':371}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[967:968].assign(**{'dayofyear':372}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1099:1102].assign(**{'dayofyear':-12}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[154:157].assign(**{'dayofyear':-16}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[953:955].assign(**{'dayofyear':373}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1103:1104].assign(**{'dayofyear':374}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[777:788].assign(**{'dayofyear':387}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[282:301].assign(**{'dayofyear':-19}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[3899] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[92] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[115] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[361] *1].assign(**{'dayofyear':371}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[231] *1].assign(**{'dayofyear':372}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[466] *1].assign(**{'dayofyear':372}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[298] *1].assign(**{'dayofyear':-10}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[533] *1].assign(**{'dayofyear':-10}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[414] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[183] *1].assign(**{'dayofyear':-11}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[114] *1].assign(**{'dayofyear':-11}), ignore_index=True)

#%% # 2018-2021

# Get a cyclic curve
allparametersdubbel = allparameters.append(allparameters.loc[3838:3842].assign(**{'dayofyear':-14}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[3847:3882].assign(**{'dayofyear':378}), ignore_index=True)
allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1506:1535].assign(**{'dayofyear':-8}), ignore_index=True)
# Drop na for fitted pH values
resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[3918] *1].assign(**{'dayofyear':373}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[20] *1].assign(**{'dayofyear':373}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[24] *1].assign(**{'dayofyear':373}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[49] *1].assign(**{'dayofyear':374}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[86] *1].assign(**{'dayofyear':-20}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[122] *1].assign(**{'dayofyear':-20}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[132] *1].assign(**{'dayofyear':-20}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[146] *1].assign(**{'dayofyear':-20}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[76] *1].assign(**{'dayofyear':373}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[99] *1].assign(**{'dayofyear':374}), ignore_index=True)
resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[48] *1].assign(**{'dayofyear':-21}), ignore_index=True)
# Get a cyclic curve 
results_outdubbel = results_out.append(results_out.loc[[564] *1].assign(**{'dayofyear':376}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[560:562].assign(**{'dayofyear':378}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[83] *1].assign(**{'dayofyear':-19}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[95] *1].assign(**{'dayofyear':-19}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[107] *1].assign(**{'dayofyear':-19}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[131] *1].assign(**{'dayofyear':-19}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[143] *1].assign(**{'dayofyear':-19}), ignore_index=True)
results_outdubbel = results_outdubbel.append(results_outdubbel.loc[[154] *1].assign(**{'dayofyear':-19}), ignore_index=True)

#%% # CURVE FITTING - pHpred, pHfit, T, DIC, TA

fvar = 'dayofyear'
LpHp = (allparametersdubbel.pHpredicted >= 7.5) & (allparametersdubbel.pHpredicted <= 8.5)
LpHf = (resultsRWSodubbel.pH_total >= 7.5) & (resultsRWSodubbel.pH_total <= 8.5)
LpHT = (allparametersdubbel.pH_T >= 7.5) & (allparametersdubbel.pH_T <= 8.5)
LpHDIC = (allparametersdubbel.pH_DIC >= 7.5) & (allparametersdubbel.pH_DIC <= 8.5)
LpHTA = (allparametersdubbel.pH_TA >= 7.5) & (allparametersdubbel.pH_TA <= 8.5)
LpHout = (results_outdubbel.pH_total_out >= 7.5) & (results_outdubbel.pH_total_out <= 8.5)

label=[80, 172, 264, 355] # start days of seasons

fig, ax = plt.subplots(dpi=300)

x = allparametersdubbel[fvar][LpHp].to_numpy()
y = allparametersdubbel.pHpredicted[LpHp].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=28).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

ax.plot(x_plotting, y_plotting, c='xkcd:dark blue', label='pH$_{pred}$')
#ax.scatter(fvar, 'pHpredicted', data=allparameters, c='xkcd:water blue', s=50, alpha=0.3, label='pH$_{pred}$')
ax.legend()

plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
plotting['y_plotting'] = y_plotting
Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
meansummer = plotting.y_plotting[Lsummer].mean()
meanwinter = plotting.y_plotting[Lwinter].mean()
print(f"Delta pH winter-to-summer (pHpred): {meansummer - meanwinter:4f}")

# x = resultsRWSodubbel[fvar][LpHf].to_numpy()
# y = resultsRWSodubbel.pH_total[LpHf].to_numpy()
x = results_outdubbel[fvar][LpHout].to_numpy()
y = results_outdubbel.pH_total_out[LpHout].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=14).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

#ax.scatter(fvar, 'pH_total_out', data=results_out, c='xkcd:black', s=50, alpha=0.3, label='pH$_{fit}$')

ax.plot(x_plotting, y_plotting, c='xkcd:black', label='pH$_{fit}$')
#ax.scatter(fvar, 'pH_total', data=resultsRWSoNN, c='xkcd:black', s=50, alpha=0.3, label='pH$_{fit}$')
ax.legend()

plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
plotting['y_plotting'] = y_plotting
Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
meansummer = plotting.y_plotting[Lsummer].mean()
meanwinter = plotting.y_plotting[Lwinter].mean()
print(f"Delta pH winter-to-summer (pHfit): {meansummer - meanwinter:4f}")

x = allparametersdubbel[fvar][LpHT].to_numpy()
y = allparametersdubbel.pH_T[LpHT].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

ax.plot(x_plotting, y_plotting, c='xkcd:pink', label='pH due to T')
#ax.scatter(fvar, 'pH_T',  c="xkcd:pink", data=allparameters, s=20, label='pH due to T')
ax.legend()

plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
plotting['y_plotting'] = y_plotting
Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
meansummer = plotting.y_plotting[Lsummer].mean()
meanwinter = plotting.y_plotting[Lwinter].mean()
print(f"Delta pH winter-to-summer (pH due to T): {meansummer - meanwinter:4f}")

x = allparametersdubbel[fvar][LpHDIC].to_numpy()
y = allparametersdubbel.pH_DIC[LpHDIC].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

ax.plot(x_plotting, y_plotting, c='xkcd:purple', label='pH due to DIC')
#ax.scatter(fvar, 'pH_DIC',  c="xkcd:purple", data=allparameters, s=20, label='pH due to DIC')
ax.legend()

plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
plotting['y_plotting'] = y_plotting
Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
meansummer = plotting.y_plotting[Lsummer].mean()
meanwinter = plotting.y_plotting[Lwinter].mean()
print(f"Delta pH winter-to-summer (pH due to DIC): {meansummer - meanwinter:4f}")

x = allparametersdubbel[fvar][LpHTA].to_numpy()
y = allparametersdubbel.pH_TA[LpHTA].to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

ax.plot(x_plotting, y_plotting, c='xkcd:red', label='pH due to TA')
#ax.scatter(fvar, 'pH_TA',  c="xkcd:red", data=allparameters, s=20, label='pH due to TA')
ax.legend()

plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
plotting['y_plotting'] = y_plotting
Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
meansummer = plotting.y_plotting[Lsummer].mean()
meanwinter = plotting.y_plotting[Lwinter].mean()
print(f"Delta pH winter-to-summer (pH due to TA): {meansummer - meanwinter:4f}")

ax.set_xlim(0, 365)
# ax.set_ylim(7.9, 8.4) 
ax.set_xlabel("Day of Year")
ax.set_ylabel("pH")
ax.grid(alpha=0.3)
ax.set_title('pH 2000-2021 - North Sea')

plt.tight_layout()
#plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_line_2018-2021_notfit.png") 
#plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_line_2010-2015_pH_fitted&predicted.png") 
plt.show()

#%% # CURVE FITTING - T, DIC, TA

fvar = 'dayofyear'

fig, ax = plt.subplots(dpi=300)

allparametersdubbelT = allparametersdubbel.dropna(axis='rows', how='all', subset=['temperature'])
x = allparametersdubbelT[fvar].to_numpy()
y = allparametersdubbelT.temperature.to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

# ax.plot(x_plotting, y_plotting, c='xkcd:pink')
# ax.scatter(fvar, 'temperature',  c="xkcd:pink", data=allparameters, s=20)

allparametersdubbelD = allparametersdubbel.dropna(axis='rows', how='all', subset=['normalized_DIC'])
x = allparametersdubbelD[fvar].to_numpy()
y = allparametersdubbelD.normalized_DIC.to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

# ax.plot(x_plotting, y_plotting, c='xkcd:purple')
# ax.scatter(fvar, 'normalized_DIC',  c="xkcd:purple", data=allparameters, s=20)

allparametersdubbelT = allparametersdubbel.dropna(axis='rows', how='all', subset=['normalized_TA'])
x = allparametersdubbelT[fvar].to_numpy()
y = allparametersdubbelT.normalized_TA.to_numpy()

x_v = np.vstack(x)
clustering = MeanShift(bandwidth=12).fit(x_v)
cluster_labels = clustering.labels_
x_clusters = clustering.cluster_centers_.ravel()
y_clusters = np.full_like(x_clusters, np.nan)
for i in range(len(x_clusters)):
    y_clusters[i] = np.mean(y[cluster_labels == i])  
x_index = np.argsort(x_clusters)
y_clusters = y_clusters[x_index]
x_clusters = x_clusters[x_index]
interpolator = interpolate.PchipInterpolator(x_clusters, y_clusters)
x_plotting = np.linspace(np.min(x), np.max(x), num=1000)
y_plotting = interpolator(x_plotting)

ax.plot(x_plotting, y_plotting, c='xkcd:red')
ax.scatter(fvar, 'normalized_TA',  c="xkcd:red", data=allparameters, s=20)

ax.set_xlim(0, 365)
ax.set_xlabel("Day of Year")
# ax.set_ylabel("Temperature (°C)")
# ax.set_ylabel("DIC (µmol/kg)")
ax.set_ylabel("Total alkalinity (µmol/kg)")
ax.grid(alpha=0.3)
ax.set_title('TA 2018-2021 - North Sea')

plt.tight_layout()
# plt.savefig("figures/pH_Hagens&Middelburg_2016/Data_2018-2021_TA.png") 
plt.show()

#%% # pH predicted and fitted

fig, ax = plt.subplots(dpi=300)

#ax.scatter('dayofyear', 'pHpredicted',  c="xkcd:water blue", data=allparameters, label='pH$_{pred}$', s=20)

#ax.scatter('dayofyear', 'pH_total',  c="xkcd:black", data=resultsRWSo[LR], label='pH$_{fit}$ RWSo', s=20, alpha=0.4)

#ax.scatter('dayofyear', 'pH_total_out',  c="xkcd:black", data=results_out, label='pH$_{fit}$ RWSn', s=20, alpha=0.4)

#ax.scatter('dayofyear', 'pH_T',  c="xkcd:pink", data=allparameters, s=20) #label='pHpred due to T', )
#ax.scatter('dayofyear', 'pH_DIC',  c="xkcd:purple", data=allparameters, s=20) #label='pHpred due to DIC')
#ax.scatter('dayofyear', 'pH_TA',  c="xkcd:red", data=allparameters, s=20) #label='pHpred due to TA')
#ax.scatter('dayofyear', 'pH_S',  c="xkcd:golden", data=allparameters, s=20) #label='pHpred due to S')
#ax.scatter('dayofyear', 'pH_TotB',  c="xkcd:yellow", data=allparameters, s=20) #label='pHpred due to TotB')
#ax.scatter('dayofyear', 'pH_TotF',  c="xkcd:velvet", data=allparameters, s=20) #label='pHpred due to TotF')
#ax.scatter('dayofyear', 'pH_TotSO4',  c="xkcd:brown", data=allparameters, s=20) #label='pHpred due to TotSO4')
#ax.scatter('dayofyear', 'pH_TotNH3',  c="xkcd:orangered", data=allparameters, s=20) #label='pHpred due to TotNH3')
#ax.scatter('dayofyear', 'pH_TotPhos',  c="xkcd:green", data=allparameters, s=20) #label='pHpred due to TotPhos')
#ax.scatter('dayofyear', 'pH_TotSi',  c="xkcd:grey", data=allparameters, s=20) #label='pHpred due to TotSi')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("pH (total scale)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.set_title('pH 2000-2021 North Sea')
ax.set_xlim(0, 365)

plt.tight_layout()
#plt.savefig("figures/pH_Hagens&Middelburg_2016/pH_2000-2021.png")
plt.show()

#%% # pH due to ... (Quantitative contribution)

import matplotlib.pyplot as plt

labels = ['2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021', '2000-2021']
pH_pred_means = [-0.060721, 0, -0.080048, -0.009379, -0.008139, -0.029972]
pH_fit_means = [0.041342, 0, 0.094465, 0.084005, -0.008046, 0.074431]
T_means = [-0.184349, 0, -0.178607, -0.187769, -0.182871, -0.177877]
DIC_means = [0.060889, 0, 0.036618, 0.113375, 0.109561, 0.105024]
TA_means = [0.045974, 0, 0.000309, 0.045092, 0.055686, 0.049881]

labels_line = ['2000-2005', '2010-2015', '2015-2018', '2018-2021']#, '2000-2021']
pH_pred_means_line = [-0.060721, -0.080048, -0.009379, -0.008139]#, -0.029972]
pH_fit_means_line = [0.041342, 0.094465, 0.084005, -0.008046]#, 0.074431]

labels_scatter = [5]#, '2000-2005', '2010-2015', '2015-2018', '2018-2021']
pH_pred_means_scatter = [-0.029972]#, 0, 0, 0, 0]

# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
width = 0.5 # the width of the bars: can also be len(x) sequence

df = pd.DataFrame(labels, columns=['periods'])
df['pH_pred_means'] = pH_pred_means
df['pH_fit_means'] = pH_fit_means
df['DIC_means'] = DIC_means
df['TA_means'] = TA_means
df['T_means'] = T_means

fig, ax = plt.subplots(dpi=300, figsize=(7,5))

ax.bar(df['periods'], df['TA_means'], width, color='xkcd:red', label='∆pH$_{∆TA}$') #, yerr=women_std )
ax.bar(df['periods'], df['DIC_means'], width, bottom=TA_means, color='xkcd:purple', label='∆pH$_{∆DIC}$') #, yerr=women_std )
ax.bar(df['periods'], df['T_means'], width, color='xkcd:pink', label='∆pH$_{∆T}$') #, yerr=men_std )
ax.plot(labels_line, pH_pred_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:water blue', label='∆pH$_{predicted}$') #, yerr=men_std )
ax.plot(labels_line, pH_fit_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:black', label='∆pH$_{fitted}$') #, yerr=men_std )
ax.scatter(labels_scatter, pH_pred_means_scatter, color='black', s=100, zorder=10)

# ax.bar(df['periods'], df['TA_means'], width, color='xkcd:magenta', label='∆pH due to ∆TA') #, yerr=women_std )
# ax.bar(df['periods'], df['DIC_means'], width, bottom=TA_means, color='xkcd:goldenrod', label='∆pH due to ∆DIC') #, yerr=women_std )
# ax.bar(df['periods'], df['T_means'], width, color='xkcd:strong pink', label='∆pH due to ∆T') #, yerr=men_std )
# ax.plot(labels_try, pH_means_try, 'o-', markerfacecolor='none', color='xkcd:black', label='∆pH$_{predicted}$') #, yerr=men_std )

ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)# x ticks
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_ylabel('winter-to-summer ∆pH')
ax.set_title('Quantitative contribution')
ax.set_ylim(-0.2, 0.2)
ax.yaxis.set_major_locator(MultipleLocator(0.05))

# plt.tight_layout()
#plt.savefig("figures/pH_Hagens&Middelburg_2016/Quantitative_contribution_all.png")
plt.show()

#%% # Results

pH_due_to_T&DIC&TA = T + DIC + TA
['2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021', '2000-2021']
[-0.077486, 0, -0.14168, -0.029302, -0.017624, -0.022972]

pH_due_to_salinity&nutrients = pH_pred - (T + DIC + TA) 
['2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021', '2000-2021']
[0.016765, 0, 0.061632, 0.019923, 0.009485, -0.00699]

pHchange_not_explained = pH_fit - pH_pred # Not due to biogeochemical processes (measured pH - pH based on biogeochemical processes)
['2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021', '2000-2021']
[0.102063, 0, 0.174513, 0.093384, 9.30e-05, 0.104403]


#%% # FINAL 3.4 DRIVERS PLOT 2
#pH due to ... (Quantitative contribution)

import matplotlib.pyplot as plt

labels = ['2000-2021', '2000-2005', '2005-2010', '2010-2015', '2015-2018', '2018-2021']
pH_pred_means = [-0.030193, -0.060910, 0, -0.080080,  -0.009600, -0.008515]
pH_fit_means = [0.074431, 0.041342, 0, 0.094465, 0.084005, -0.008046]
T_means = [-0.176867, -0.179434, 0, -0.179426, -0.167912, -0.185910]
DIC_means = [0.120855, 0.072869, 0, 0.030189, 0.122911, 0.109603]
TA_means = [0.028111, 0.041195, 0, 0.021010, 0.026947, 0.067784]
S_means = [-0.002945, 0.000372, 0, -0.001663, -0.000054, -0.005808]
TotB_means = [-0.001412, 0.000177, 0, -0.000804, -0.000026, -0.002775]
TotF_means = [0.000001, 0, 0, 0, 0, 0.000002]
TotSO4_means = [0, 0, 0, 0, 0, 0] 
Totnutrients_means = [0.000075, 0.000042, 0, 0.000039, 0.000043, 0.001409]

labels_line = ['2000-2005', '2010-2015', '2015-2018', '2018-2021']
pH_pred_means_line = [-0.060721, -0.080048, -0.009379, -0.008139]
pH_fit_means_line = [0.041342, 0.094465, 0.084005, -0.008046]

labels_scatter = [0]
pH_pred_means_scatter = [-0.030193]
pH_fit_means_scatter = [0.074431]

# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
width = 0.5 # the width of the bars: can also be len(x) sequence

df = pd.DataFrame(labels, columns=['periods'])
df['pH_pred_means'] = pH_pred_means
df['pH_fit_means'] = pH_fit_means
df['T_means'] = T_means
df['DIC_means'] = DIC_means
df['TA_means'] = TA_means
df['S_means'] = S_means
df['TotB_means'] = TotB_means
df['TotF_means'] = TotF_means
df['TotSO4_means'] = TotSO4_means 
df['Totnutrients_means'] = Totnutrients_means

fig, ax = plt.subplots(dpi=300, figsize=(7,5))

ax.bar(df['periods'], df['Totnutrients_means'], width, color='xkcd:brown', label='∆pH$_{∆Totnutrients}$') #, yerr=men_std )
ax.bar(df['periods'], df['TA_means'], width, bottom=Totnutrients_means, color='xkcd:red', label='∆pH$_{∆TA}$') #, yerr=women_std )
ax.bar(df['periods'], df['DIC_means'], width, bottom=TA_means, color='xkcd:purple', label='∆pH$_{∆DIC}$') #, yerr=women_std )
ax.bar(df['periods'], df['T_means'], width, bottom=S_means, color='xkcd:pink', label='∆pH$_{∆T}$') #, yerr=men_std )
ax.bar(df['periods'], df['S_means'], width, bottom=TotB_means, color='xkcd:golden', label='∆pH$_{∆S}$') #, yerr=men_std )
ax.bar(df['periods'], df['TotB_means'], width, color='xkcd:light green', label='∆pH$_{∆TotB}$') #, yerr=men_std )
#ax.bar(df['periods'], df['TotF_means'], width, color='xkcd:royal', label='∆pH$_{∆T}$') #, yerr=men_std )
#ax.bar(df['periods'], df['TotSO4_means'], width, color='xkcd:dark grey', label='∆pH$_{∆T}$') #, yerr=men_std )

ax.plot(labels_line, pH_pred_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:water blue', label='∆pH$_{predicted}$') #, yerr=men_std )
ax.plot(labels_line, pH_fit_means_line, '-o', markerfacecolor='none', linestyle='dashed', color='xkcd:black', label='∆pH$_{fitted}$') #, yerr=men_std )
ax.scatter(labels_scatter, pH_pred_means_scatter, color='xkcd:water blue', facecolor='none', zorder=10)
ax.scatter(labels_scatter, pH_fit_means_scatter, color='black', facecolor='none', zorder=10)

ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)# x ticks
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.set_ylabel('winter-to-summer ∆pH')
ax.set_title('Quantitative contribution')
ax.set_ylim(-0.2, 0.2)
ax.yaxis.set_major_locator(MultipleLocator(0.05))

# plt.tight_layout()
plt.savefig("figures/pH_Hagens&Middelburg_2016/Quantitative_contribution_all_FINALALL.png")
plt.show()


