import PyCO2SYS as pyco2

resultsRWSowinter = resultsRWSo[(resultsRWSo["dayofyear"] >= 355) | (resultsRWSo["dayofyear"] <= 78)]
winterphosmean = resultsRWSowinter['total_phosphate'].mean() 
wintersilmean = resultsRWSowinter['total_silicate'].mean() 
wintertempmean = resultsRWSowinter['temperature'].mean() 
wintersalmean = resultsRWSowinter['salinity'].mean() 
print(winterphosmean)
print(wintersilmean)
print(wintertempmean)
print(wintersalmean)

# 0.03396524157108097
# 0.32666417213964744
# 5.671317796381054
# 32.623349640290385

resultsRWSosummer = resultsRWSo[(resultsRWSo["dayofyear"] > 78) & (resultsRWSo["dayofyear"] < 355)]
summerphosmean = resultsRWSosummer['total_phosphate'].mean() 
summersilmean = resultsRWSosummer['total_silicate'].mean() 
summertempmean = resultsRWSosummer['temperature'].mean() 
summersalmean = resultsRWSosummer['salinity'].mean() 
print(summerphosmean)
print(summersilmean)
print(summertempmean)
print(summersalmean)

# 0.019615144688962045
# 0.0894885689277899
# 13.472875475393025
# 32.88283909162645

resultsRWSoclose = resultsRWSo[(resultsRWSo["distance_to_shore"] >= 0) & (resultsRWSo["distance_to_shore"] <= 50)]
closephosmean = resultsRWSoclose['total_phosphate'].mean() 
closesilmean = resultsRWSoclose['total_silicate'].mean() 
closetempmean = resultsRWSoclose['temperature'].mean() 
closesalmean = resultsRWSoclose['salinity'].mean() 
print(closephosmean) 
print(closesilmean)
print(closetempmean)
print(closesalmean)

# 0.029449456832475688
# 0.18485941237350503
# 11.843719405613243
# 31.837015119680522

resultsRWSofar = resultsRWSo[(resultsRWSo["distance_to_shore"] > 50) & (resultsRWSo["distance_to_shore"] <= 300)]
farphosmean = resultsRWSofar['total_phosphate'].mean() 
farsilmean = resultsRWSofar['total_silicate'].mean() 
fartempmean = resultsRWSofar['temperature'].mean() 
farsalmean = resultsRWSofar['salinity'].mean() 
print(farphosmean)
print(farsilmean)
print(fartempmean)
print(farsalmean)

# 0.011734314416637286
# 0.0640179473496976
# 11.976591838533404
# 34.475227634618804

#%%

# Winter values (year 2000,2010,2020)
# fCO2 socat
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[350, 380, 400],
    par2=[7.75, 7.55, 7.9],
    par1_type=4,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    opt_pH_scale=4)

# TA = [730.492, 492.331, 1192.53]
# DIC = [710.916, 490.648, 1148.56]

#%%

# Winter values (year 2000,2010,2020)
# TA combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2290, 2320, 2360],
    par2=[7.75, 7.55, 7.9],
    par1_type=1,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    opt_pH_scale=4)

# DIC = [2278.99, 2369.77, 2304.36]
# fCO2 = [1117.43, 1827.88, 799.249]

#%%

# Winter values (year 2000,2010,2020)
# DIC combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2110, 2150, 2210],
    par2=[7.75, 7.55, 7.9],
    par1_type=2,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    opt_pH_scale=4)

print(results['alkalinity']) # no dot notation for dict
# TA = [2121.93, 2106.24, 2264.69]
# fCO2 = [1034.57, 1658.36, 766.522]

#%%

# Winter values (year 2000,2010,2020)
# TA combined
# DIC combined

# + include nutrients
results = pyco2.sys(
    par1=[2290, 2320, 2360],
    par2=[2110, 2150, 2210],
    par1_type=1,
    par2_type=2,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    )

# pH (total_scale) = [8.15273, 8.12556, 8.0721]
# fCO2 = [316.405, 344.334, 402.575]

#%%

# Winter values (year 2000,2010,2020)
# TA combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2290, 2320, 2360],
    par2=[350, 380, 400],
    par1_type=1,
    par2_type=4,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    )

# DIC = [2125.46, 2164.84, 2208.38]
# pH (total_scale) = [8.11574, 8.08923, 8.07617]

#%%

# Winter values (year 2000,2010,2020)
# DIC combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2110, 2150, 2210],
    par2=[350, 380, 400],
    par1_type=2,
    par2_type=4,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    )

# TA = [2272.51, 2303.31, 2361.81]
# pH (total_scale) = [8.11272, 8.08637, 8.07648]

#%%

# Summer values (year 2000,2010,2020)
# fCO2 socat
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[390, 375, 420],
    par2=[8, 7.85, 8.05],
    par1_type=4,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean, 
    opt_pH_scale=4)

# TA = [1453.45, 966.326, 1770.27]
# DIC = [1355.82, 914.463, 1645.74]

#%%

# Summer values (year 2000,2010,2020)
# TA combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2280, 2315, 2380],
    par2=[8, 7.85, 8.05],
    par1_type=1,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean,
    opt_pH_scale=4)

# DIC = [2153.56, 2239.67, 2230.36]
# fCO2 = [617.186, 915.056, 567.101]

#%%

# Summer values (year 2000,2010,2020)
# DIC combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2060, 2100, 2145],
    par2=[8, 7.85, 8.05],
    par1_type=2,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean, 
    opt_pH_scale=4)

# TA = [2183.06, 2172.86, 2290.97]
# fCO2 = [590.374, 857.991, 545.397]

#%%

# Summer values (year 2000,2010,2020)
# TA combined
# DIC combined

# + include nutrients
results = pyco2.sys(
    par1=[2280, 2315, 2380],
    par2=[2060, 2100, 2145],
    par1_type=1,
    par2_type=2,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

# pH (total_scale) = [8.10587, 8.09074, 8.12266]
# fCO2 = [345.435, 365.502, 345.09]

#%%

# Summer values (year 2000,2010,2020)
# TA combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2280, 2315, 2380],
    par2=[390, 375, 420],
    par1_type=1,
    par2_type=4,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

# DIC = [2080.57, 2103.9, 2179.94]
# pH (total_scale) = [8.062, 8.08255, 8.05077]

#%%

# Summer values (year 2000,2010,2020)
# DIC combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2060, 2100, 2145],
    par2=[390, 375, 420],
    par1_type=2,
    par2_type=4,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

# TA = [2256.19, 2310.47, 2339.73]
# pH (total_scale) = [8.05794, 8.0818, 8.04415]

#%%

# Close values (year 2000,2010,2020)
# fCO2 socat
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[345, 375, 428],
    par2=[8, 7.76, 8.1],
    par1_type=4,
    par2_type=3,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    opt_pH_scale=4)

# TA = [1284.87, 774.877, 2033.96]
# DIC = [1202.25, 744.744, 1894.21]

#%%

# Close values (year 2000,2010,2020)
# TA combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2375],
    par2=[8.1],
    par1_type=1,
    par2_type=3,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    opt_pH_scale=4)

# DIC = [2220.59]
# fCO2 = [499.86]

#%%

# Close values (year 2000,2010,2020)
# DIC combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2155],
    par2=[8.1],
    par1_type=2,
    par2_type=3,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    opt_pH_scale=4)

# TA = [2306.47]
# fCO2 = [485.095]

#%%

# Close values (year 2000,2010,2020)
# TA combined
# DIC combined

# + include nutrients
results = pyco2.sys(
    par1=[2375],
    par2=[2155],
    par1_type=1,
    par2_type=2,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    )

# pH (total_scale) = [8.13373]
# fCO2 = [338.894]

#%%

# Close values (year 2000,2010,2020)
# TA combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2375],
    par2=[428],
    par1_type=1,
    par2_type=4,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    )

# DIC = [2194.88]
# pH (total_scale) = [8.04722]

#%%

# Close values (year 2000,2010,2020)
# DIC combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2155],
    par2=[428],
    par1_type=2,
    par2_type=4,
    salinity=closesalmean,
    temperature=closetempmean,
    total_phosphate=closephosmean, 
    total_silicate=closesilmean, 
    )

# TA = [2329.55]
# pH (total_scale) = [8.03966]

#%%

# Far values (year 2000,2010,2020)
# fCO2 socat
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[350, 360, 400],
    par2=[7.9, 7.78, 8.1],
    par1_type=4,
    par2_type=3,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean, 
    opt_pH_scale=4)

# TA = [1045.82, 801.945, 1959.78]
# DIC = [982.353, 763.108, 1808.8]

#%%

# Far values (year 2000,2010,2020)
# TA combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2300, 2328, 2358],
    par2=[7.9, 7.78, 8.1],
    par1_type=1,
    par2_type=3,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean, 
    opt_pH_scale=4)

# DIC = [2208.46, 2275.24, 2188.26]
# fCO2 = [783.892, 1069.33, 482.098]

#%%

# Far values (year 2000,2010,2020)
# DIC combined
# pH RWSo

# + include nutrients
results = pyco2.sys(
    par1=[2095, 2100, 2185],
    par2=[7.9, 7.78, 8.1],
    par1_type=2,
    par2_type=3,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean, 
    opt_pH_scale=4)

# TA = [2183.95, 2151.15, 2354.58]
# fCO2 = [743.621, 986.967, 481.381]

#%%

# Far values (year 2000,2010,2020)
# TA combined
# DIC combined

# + include nutrients
results = pyco2.sys(
    par1=[2300, 2328, 2358],
    par2=[2095, 2100, 2185],
    par1_type=1,
    par2_type=2,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean, 
    )

# pH (total_scale) = [8.07594, 8.12007, 7.99779]
# fCO2 = [374.719, 337.017, 472.661]

#%%

# Far values (year 2000,2010,2020)
# TA combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2300, 2328, 2358],
    par2=[350, 360, 400],
    par1_type=1,
    par2_type=4,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean, 
    )

# DIC = [2082.26, 2111.31, 2155.89]
# pH (total_scale) = [8.1028, 8.09697, 8.06249]

#%%

# Far values (year 2000,2010,2020)
# DIC combined
# fCO2 socat

# + include nutrients
results = pyco2.sys(
    par1=[2095, 2100, 2185],
    par2=[350, 360, 400],
    par1_type=2,
    par2_type=4,
    salinity=farsalmean,
    temperature=fartempmean,
    total_phosphate=farphosmean, 
    total_silicate=farsilmean,  
    )

# TA = [2314.89, 2314.82, 2391.64]
# pH (total_scale) = [8.10528, 8.09479, 8.06798]