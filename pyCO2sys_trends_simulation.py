# End of spring values (year 2002, 2014, 2018, 2021) - colour: deep purple
# TA normalized combined
# DIC combined

results = pyco2.sys(
    par1=[2352, 2357, 2371, 2355],
    par2=[2098, 2108, 2150, 2108],
    par1_type=1,
    par2_type=2,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['pH_total']) 
print(results['fCO2']) 
# Outcomes corresponding to the initial TA and DIC
# pH = [8.22172288 8.21143437 8.15384135 8.20785218]
# fCO2 = [264.18396032 272.31965857 320.22542921 274.75239301]

# TA = 2352, 2357, 2371, 2355
# DIC = 2098, 2108, 2150, 2108
# pH = 7.93, 8.1, 8.14, >8.14 
# fCO2 = 300, +/-290, 255, 275 

#%% # Changed values to get a better outcome of pH and fCO2

par1=[2352, 2357, 2328 D, 2355],
par2=[2122 I, 2120 I, 2100 D, 2108],

[8.17468313 8.18799283 8.1738818  8.20785218]
[300.23797676 290.25238541 297.71332237 274.75239301]

#%%

# Values used to see what is happening in general
# TA normalized combined
# DIC combined

results = pyco2.sys(
    par1=[2300, 2301, 2299, 2301],
    par2=[2100, 2101, 2101, 2099],
    par1_type=1,
    par2_type=2,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean)

print(results['pH_total']) 
print(results['fCO2']) 

#%%

[8.11844565 8.11831776 8.11417227 8.1226942 ]
[341.13780918 341.40699842 344.88396341 337.45039265]

#%%

x =  341.13780918 - 337.45039265
y = 8.1226942 - 8.11844565
print(x)
print(y)

#%% # All observed numbers of TA and DIC

# End of spring values (year 2000, 2001, 2002, 2005, 2010, 2011, 
#                           2014, 2015, 2018, 2019, 2020) - deep purple
# TA normalized combined
# DIC combined

results = pyco2.sys(
    par1=[2352, 2352, 2352, 2353.5, 2361, 2361, 2355, 2370, 2372, 2370, 2362],
    par2=[2097, 2097, 2097, 2103, 2103, 2103, 2108, 2110, 2015, 2108, 2120],
    par1_type=1,
    par2_type=2,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.22362713 8.22362713 8.22362713 8.21481257 8.22802706 8.22802706
# 8.20785218 8.23050542 8.3958691  8.2342493  8.19714906]
# fCO2 = [262.80965023 262.80965023 262.80965023 269.40325739 260.6897979 260.6897979 
# 274.75239301 259.94736592 163.27444586 257.28830243 283.74797095]

# Values derived from datasets. TA and DIC are used for these results
# TA = +/- 2352, +/- 2352, 2352, 2352-2355, 2352-2370, 2352-2370, 2355, 2370, 2372, 2370, +/- 2362 
# DIC = +/- 2097, +/- 2097, 2097, 2097-2108, 2097-2108, 2097-2108, 2108, 2110, 2015, 2108, 2120
# fCO2 = <300, <300, 300, <300, <310, <325, 290, 255, 175, 275
# pH = 8.1, 8.25, 7.93, 8.1, 7.78, 8, 8.1, +/- 8.1, 8.19, >8.19, >8.19

#%% # Adjust the numbers till the numbers of pH and fCO2 correspond to the observations

# End of spring values (year 2000, 2001, 2002, 2005, 2010, 2011, 
#                           2014, 2015, 2018, 2019, 2020) - deep purple
# TA normalized combined
# DIC combined

results = pyco2.sys(
    par1=[2342, 2352, 2352, 2353.5, 2361, 2361, 2355, 2370, 2372, 2370, 2362],
    par2=[2107, 2097, 2137, 2103, 2103, 2103, 2108, 2110, 2015, 2108, 2120],
    par1_type=1,
    par2_type=2,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.22362713 8.22362713 8.22362713 8.21481257 8.22802706 8.22802706
# 8.20785218 8.23050542 8.3958691  8.2342493  8.19714906]
# fCO2 = [262.80965023 262.80965023 262.80965023 269.40325739 260.6897979 260.6897979 
# 274.75239301 259.94736592 163.27444586 257.28830243 283.74797095]
