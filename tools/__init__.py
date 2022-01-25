# Hagens & Middelburg 2016 tools

def get_pH_predicted(LR, LC, resultsRWSo, resultscombined):
    """Calculate the predicted pH based on T, DIC, TA, S, borate, fluoride, and nutrients
    following the same approach as Hagens & Middelburg 2016 (equation 2)"""
    import pandas as pd
    import PyCO2SYS as pyco2
    
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
    
    print(f"pH total mean value = {overbarvalues['pHmean']:6f}") 

    # Getting the derivatives of the mean values
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
    
    print(f"pH total overbar value = {results['pH_total']:6f}") 
    pH_total_overbar = results['pH_total']
    d_pH_total__d_dic = results['d_pH_total__d_par1']
    d_pH_total__d_alkalinity = results['d_pH_total__d_par2']
    
    # resultsRWSo - Overbar values H0 - data values
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
    
    # resultscombined - Overbar values H0 - data values
    parametersDA = pd.DataFrame(resultscombined[LC].normalized_DIC)
    parametersDA['DIC_overbar'] = overbarvalues['DICmean']
    parametersDA['DIC-DIC'] = parametersDA['normalized_DIC'] - parametersDA['DIC_overbar']
    parametersDA['normalized_TA'] = resultscombined[LC].normalized_TA
    parametersDA['TA_overbar'] = overbarvalues['TAmean']
    parametersDA['TA-TA'] = parametersDA['normalized_TA'] - parametersDA['TA_overbar']
    
    parametersDA['dayofyear'] = resultscombined[LC].dayofyear
    
    # Deleting the nans and combining datasets
    parametersNN = parameters.dropna()     
    parametersDANN = parametersDA.dropna()     
    allparameters = (pd.merge(parametersNN, parametersDANN, how='outer', on='dayofyear'))
    
    # Calculation (2) Hagens&Middelburg 2016
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
    
    # Determination of the principal drivers of pH seasonality (pH pred) - per each individual parameter
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

    return allparameters

def deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel):
    """Print the ΔpH winter-to-summer for each individual parameter"""
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    
    fvar = 'pHpredicted'
    
    for fvar in ['pHpredicted', 'pH_T', 'pH_DIC', 'pH_TA', 'pH_S', 'pH_TotB',
                 'pH_TotF', 'pH_TotSO4', 'pH_TotNH3', 'pH_TotPhos', 'pH_TotSi']:
        
        LpH = (allparametersdubbel[fvar] >= 7.5) & (allparametersdubbel[fvar] <= 8.5)
    
        x = allparametersdubbel['dayofyear'][LpH].to_numpy()
        y = allparametersdubbel[fvar][LpH].to_numpy()
        
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
        
        plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
        plotting['y_plotting'] = y_plotting
        Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
        Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
        meansummer = plotting.y_plotting[Lsummer].mean()
        meanwinter = plotting.y_plotting[Lwinter].mean()
        print(fvar + f" ΔpH winter-to-summer : {meansummer - meanwinter:4f}")
    
    LpHf = (resultsRWSodubbel.pH_total >= 7.5) & (resultsRWSodubbel.pH_total <= 8.5)
    x = resultsRWSodubbel['dayofyear'][LpHf].to_numpy()
    y = resultsRWSodubbel.pH_total[LpHf].to_numpy()
    
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
    
    plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
    plotting['y_plotting'] = y_plotting
    Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
    Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
    meansummer = plotting.y_plotting[Lsummer].mean()
    meanwinter = plotting.y_plotting[Lwinter].mean()
    print(f"pHfitted ΔpH winter-to-summer : {meansummer - meanwinter:4f}")
    
def cycliccurve_2000_2021(allparameters, resultsRWSo, LR):
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
    
    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2000_2005(allparameters, resultsRWSo, LR):
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

    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2005_2010(allparameters, resultsRWSo, LR):
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

    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2010_2015(allparameters, resultsRWSo, LR):
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

    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2015_2018(allparameters, resultsRWSo, LR):
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

    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2018_2021(allparameters, resultsRWSo, LR, resultsRWSn):
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
    resultsRWSndubbel = resultsRWSn.append(resultsRWSn.loc[[564] *1].assign(**{'dayofyear':376}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[560:562].assign(**{'dayofyear':378}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[83] *1].assign(**{'dayofyear':-19}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[95] *1].assign(**{'dayofyear':-19}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[107] *1].assign(**{'dayofyear':-19}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[131] *1].assign(**{'dayofyear':-19}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[143] *1].assign(**{'dayofyear':-19}), ignore_index=True)
    resultsRWSndubbel = resultsRWSndubbel.append(resultsRWSndubbel.loc[[154] *1].assign(**{'dayofyear':-19}), ignore_index=True)

    return resultsRWSodubbel, allparametersdubbel, resultsRWSndubbel

def get_pH_predicted_RWSn(LR, LC, resultsRWSo, resultscombined, resultsRWSn):
    """Calculate the predicted pH based on T, DIC, TA, S, borate, fluoride, and nutrients
    following the same approach as Hagens & Middelburg 2016 (equation 2) period 2018-2021"""
    import pandas as pd
    import PyCO2SYS as pyco2
    
    overbarvalues = {
       "pHmean": resultsRWSo[LR].pH_total.mean(), 
       "pHmean_out": resultsRWSn.pH_total_spectro_out.mean(),
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

    print(f"pH total mean value = {overbarvalues['pHmean']:6f}") 
    print(f"pH total mean spectro value = {overbarvalues['pHmean']:6f}") 
    
    # Getting the derivatives of the mean values
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
    
    print(f"pH total overbar value = {results['pH_total']:6f}") 
    pH_total_overbar = results['pH_total']
    d_pH_total__d_dic = results['d_pH_total__d_par1']
    d_pH_total__d_alkalinity = results['d_pH_total__d_par2']
    
    # resultsRWSn - Overbar values H0 - data values

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
    
    # resultscombined - Overbar values H0 - data values
    parametersDA = pd.DataFrame(resultscombined[LC].normalized_DIC)
    parametersDA['DIC_overbar'] = overbarvalues['DICmean']
    parametersDA['DIC-DIC'] = parametersDA['normalized_DIC'] - parametersDA['DIC_overbar']
    parametersDA['normalized_TA'] = resultscombined[LC].normalized_TA
    parametersDA['TA_overbar'] = overbarvalues['TAmean']
    parametersDA['TA-TA'] = parametersDA['normalized_TA'] - parametersDA['TA_overbar']
    
    parametersDA['dayofyear'] = resultscombined[LC].dayofyear
    
    # Deleting the nans and combining datasets
    parametersNN = parameters.dropna()     
    parametersDANN = parametersDA.dropna()     
    allparameters = (pd.merge(parametersNN, parametersDANN, how='outer', on='dayofyear'))
    
    # Calculation (2) Hagens&Middelburg 2016
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
    
    # Determination of the principal drivers of pH seasonality (pH pred) - per each individual parameter
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

    return allparameters

def deltapH_winter_summer_RWSn(allparametersdubbel, resultsRWSodubbel, resultsRWSndubbel):
    """Print the ΔpH winter-to-summer for each individual parameter"""
    import numpy as np
    from sklearn.cluster import MeanShift
    from scipy import interpolate 
    import pandas as pd
    
    fvar = 'pHpredicted'
    
    for fvar in ['pHpredicted', 'pH_T', 'pH_DIC', 'pH_TA', 'pH_S', 'pH_TotB',
                 'pH_TotF', 'pH_TotSO4', 'pH_TotNH3', 'pH_TotPhos', 'pH_TotSi']:
        
        LpH = (allparametersdubbel[fvar] >= 7.5) & (allparametersdubbel[fvar] <= 8.5)
    
        x = allparametersdubbel['dayofyear'][LpH].to_numpy()
        y = allparametersdubbel[fvar][LpH].to_numpy()
        
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
       
        plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
        plotting['y_plotting'] = y_plotting
        Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
        Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
        meansummer = plotting.y_plotting[Lsummer].mean()
        meanwinter = plotting.y_plotting[Lwinter].mean()
        print(fvar + f" ΔpH winter-to-summer : {meansummer - meanwinter:4f}")
    
    LpHout = (resultsRWSndubbel.pH_total_spectro_out >= 7.5) & (resultsRWSndubbel.pH_total_spectro_out <= 8.5)

    x = resultsRWSndubbel['dayofyear'][LpHout].to_numpy()
    y = resultsRWSndubbel.pH_total_spectro_out[LpHout].to_numpy()
    
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
    
    plotting = pd.DataFrame(x_plotting, columns=['x_plotting'])
    plotting['y_plotting'] = y_plotting
    Lwinter = ((plotting.x_plotting >= 355) & (plotting.x_plotting <= 365)) | ((plotting.x_plotting >= 1) & (plotting.x_plotting < 80)) # 21 dec - 21 march
    Lsummer = (plotting.x_plotting >= 172) & (plotting.x_plotting < 264) # 21 juni - 21 sep
    meansummer = plotting.y_plotting[Lsummer].mean()
    meanwinter = plotting.y_plotting[Lwinter].mean()
    print(f"pHfitted ΔpH winter-to-summer : {meansummer - meanwinter:4f}")

def cycliccurve_2000_2011(allparameters, resultsRWSo, LR):
    # Get a cyclic curve
    allparametersdubbel = allparameters.append(allparameters.loc[4078 : 4097].assign(**{'dayofyear':407}), ignore_index=True)
    allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[4607 : 4613].assign(**{'dayofyear':-35}), ignore_index=True)
    allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[4555 : 4599].assign(**{'dayofyear':-36}), ignore_index=True)
    # Drop na for fitted pH values
    resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
    resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[1607] *1].assign(**{'dayofyear':367}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[710] *1].assign(**{'dayofyear':368}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[986] *1].assign(**{'dayofyear':368}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[2068] *1].assign(**{'dayofyear':368}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[189] *1].assign(**{'dayofyear':-2}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[460] *1].assign(**{'dayofyear':-2}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1117] *1].assign(**{'dayofyear':-2}), ignore_index=True)
    
    return resultsRWSodubbel, allparametersdubbel

def cycliccurve_2010_2018(allparameters, resultsRWSo, LR):
    # Get a cyclic curve
    allparametersdubbel = allparameters.append(allparameters.loc[2001 : 2012].assign(**{'dayofyear':387}), ignore_index=True)
    allparametersdubbel = allparametersdubbel.append(allparametersdubbel.loc[1472 : 1506].assign(**{'dayofyear':-19}), ignore_index=True)
    # Drop na for fitted pH values
    resultsRWSoNN = resultsRWSo[LR].dropna(axis='rows', how='all', subset=['pH_total'])
    resultsRWSodubbel = resultsRWSoNN.append(resultsRWSoNN.loc[[3899] *1].assign(**{'dayofyear':371}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[345] *1].assign(**{'dayofyear':371}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[877] *1].assign(**{'dayofyear':371}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[674] *1].assign(**{'dayofyear':-10}), ignore_index=True)
    resultsRWSodubbel = resultsRWSodubbel.append(resultsRWSodubbel.loc[[1203] *1].assign(**{'dayofyear':-10}), ignore_index=True)
    
    return resultsRWSodubbel, allparametersdubbel
