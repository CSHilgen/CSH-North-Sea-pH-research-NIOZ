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

resultsRWSosummer = resultsRWSo[(resultsRWSo["dayofyear"] > 78) | (resultsRWSo["dayofyear"] < 355)]
summerphosmean = resultsRWSosummer['total_phosphate'].mean() 
summersilmean = resultsRWSosummer['total_silicate'].mean() 
summertempmean = resultsRWSosummer['temperature'].mean() 
summersalmean = resultsRWSosummer['salinity'].mean() 
print(summerphosmean)
print(summersilmean)
print(summertempmean)
print(summersalmean)

# 0.022478396560094312
# 0.1374106963263025
# 11.893951666839158
# 32.82967455275024

resultsRWSofar = resultsRWSo[(resultsRWSo["distance_to_shore"] >= 0) | (resultsRWSo["distance_to_shore"] <= 50)]
farphosmean = resultsRWSofar['total_phosphate'].mean() 
farsilmean = resultsRWSofar['total_silicate'].mean() 
fartempmean = resultsRWSofar['temperature'].mean() 
farsalmean = resultsRWSofar['salinity'].mean() 
print(farphosmean) 
print(farsilmean)
print(fartempmean)
print(farsalmean)

# 0.022478396560094312
# 0.1374106963263025
# 11.893951666839158
# 32.82967455275024

resultsRWSoclose = resultsRWSo[(resultsRWSo["distance_to_shore"] > 50) | (resultsRWSo["distance_to_shore"] <= 300)]
closephosmean = resultsRWSoclose['total_phosphate'].mean() 
closesilmean = resultsRWSoclose['total_silicate'].mean() 
closetempmean = resultsRWSoclose['temperature'].mean() 
closesalmean = resultsRWSoclose['salinity'].mean() 
print(closephosmean)
print(closesilmean)
print(closetempmean)
print(closesalmean)

# 0.022478396560094312
# 0.1374106963263025
# 11.893951666839158
# 32.82967455275024

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    opt_pH_scale=4)

# TA = [730.47, 492.318, 1192.49]
# DIC = [710.902, 490.639, 1148.54]

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    opt_pH_scale=4)

# DIC = [2279.01, 2369.79, 2304.38]
# fCO2 = [1117.46, 1827.92, 799.273]

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    opt_pH_scale=4)

# TA = [2121.91, 2106.23, 2264.67]
# fCO2 = [1034.59, 1658.39, 766.538]

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    )

# pH (total_scale) = [8.1528, 8.12563, 8.07217]
# fCO2 = [316.36, 344.285, 402.518]

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    )

# DIC = [2125.48, 2164.86, 2208.4]
# pH (total_scale) = [8.11575, 8.08924, 8.07618]

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
    salinity=32.62,
    temperature=5.67,
    total_phosphate= 0.033965, # Winterphosmean 
    total_silicate= 0.32666, # Wintersilmean 
    )

# TA = [2272.48, 2303.28, 2361.79]
# pH (total_scale) = [8.11272, 8.08638, 8.07648]

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

# TA = [1462.08, 973.248, 1780.03]
# DIC = [1370.09, 924.991, 1662.44]

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

# DIC = [2161.89, 2246.74, 2239.57]
# fCO2 = [613.075, 907.429, 563.679]

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

# TA = [2174.75, 2166.03, 2281.69]
# fCO2 = [584.181, 848.161, 539.877]

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

# pH (total_scale) = [8.13257, 8.11742, 8.14946]
# fCO2 = [323.103, 341.891, 322.707]

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

# DIC = [2091.79, 2115.5, 2191.41]
# pH (total_scale) = [8.06355, 8.08424, 8.05223]

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

# TA = [2243.47, 2297.09, 2326.88]
# pH (total_scale) = [8.05727, 8.08124, 8.04342]