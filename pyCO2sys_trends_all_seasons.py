import PyCO2SYS as pyco2

#%%

resultssocatnswinter = resultssocatns[(resultssocatns["dayofyear"] >= 355) | (resultssocatns["dayofyear"] <= 79)]
resultscombinedwinter = resultscombined[(resultscombined["dayofyear"] >= 355) | (resultscombined["dayofyear"] <= 79)]
resultsRWSowinter = resultsRWSo[(resultsRWSo["dayofyear"] >= 355) | (resultsRWSo["dayofyear"] <= 79)]

winterphosmean = resultsRWSowinter['total_phosphate'].mean() 
wintersilmean = resultsRWSowinter['total_silicate'].mean() 
wintertempmean = resultsRWSowinter['temperature'].mean() 
wintersalmean = resultsRWSowinter['salinity'].mean() 
print(winterphosmean)
print(wintersilmean)
print(wintertempmean)
print(wintersalmean)
# 0.033935917667238406
# 0.3262493517570795
# 5.6794882586481386
# 32.623408542520465

resultssocatnsspring = resultssocatns[(resultssocatns["dayofyear"] > 79) & (resultssocatns["dayofyear"] <= 171)]
resultscombinedspring = resultscombined[(resultscombined["dayofyear"] > 79) & (resultscombined["dayofyear"] <= 171)]
resultsRWSospring = resultsRWSo[(resultsRWSo["dayofyear"] > 79) & (resultsRWSo["dayofyear"] <= 171)]

springphosmean = resultsRWSospring['total_phosphate'].mean() 
springsilmean = resultsRWSospring['total_silicate'].mean() 
springtempmean = resultsRWSospring['temperature'].mean() 
springsalmean = resultsRWSospring['salinity'].mean() 
print(springphosmean)
print(springsilmean)
print(springtempmean)
print(springsalmean)
# 0.012955822177317498
# 0.06778968966401638
# 10.168111304418987
# 32.65352243397448

resultssocatnssummer = resultssocatns[(resultssocatns["dayofyear"] > 171) & (resultssocatns["dayofyear"] <= 263)]
resultscombinedsummer = resultscombined[(resultscombined["dayofyear"] > 171) & (resultscombined["dayofyear"] <= 263)]
resultsRWSosummer = resultsRWSo[(resultsRWSo["dayofyear"] > 171) & (resultsRWSo["dayofyear"] <= 263)]

summerphosmean = resultsRWSosummer['total_phosphate'].mean() 
summersilmean = resultsRWSosummer['total_silicate'].mean() 
summertempmean = resultsRWSosummer['temperature'].mean() 
summersalmean = resultsRWSosummer['salinity'].mean() 
print(summerphosmean) 
print(summersilmean)
print(summertempmean)
print(summersalmean)
# 0.015812418755803147
# 0.04974023565095659
# 17.216356513951595
# 32.84486815656702

resultssocatnsautumn = resultssocatns[(resultssocatns["dayofyear"] > 263) & (resultssocatns["dayofyear"] <= 354)]
resultscombinedautumn = resultscombined[(resultscombined["dayofyear"] > 263) & (resultscombined["dayofyear"] <= 354)]
resultsRWSoautumn = resultsRWSo[(resultsRWSo["dayofyear"] > 263) & (resultsRWSo["dayofyear"] <= 354)]

autumnphosmean = resultsRWSoautumn['total_phosphate'].mean() 
autumnsilmean = resultsRWSoautumn['total_silicate'].mean() 
autumntempmean = resultsRWSoautumn['temperature'].mean() 
autumnsalmean = resultsRWSoautumn['salinity'].mean() 
print(autumnphosmean)
print(autumnsilmean)
print(autumntempmean)
print(autumnsalmean)
# 0.03267865307383378
# 0.16668046533416614
# 12.681317903955073
# 33.213807238967846

#%% # WINTER

L0 =  (resultsRWSowinter.year == 2000)#
L10 = (resultsRWSowinter.year == 2010)# 
L18 = (resultsRWSowinter.year == 2018)#

F2 = (resultssocatnswinter.year == 2002)  
F10 = (resultssocatnswinter.year == 2010) | (resultssocatnswinter.year == 2009) | (resultssocatnswinter.year == 2011)
F20 = (resultssocatnswinter.year == 2020) | (resultssocatnswinter.year == 2019) | (resultssocatnswinter.year == 2021)

meanpH0 = resultsRWSowinter['pH_total'][L0].mean()
meanpH10 = resultsRWSowinter['pH_total'][L10].mean()
meanpH18 = resultsRWSowinter['pH_total'][L18].mean()

meanfco22 = resultssocatnswinter['fCO2'][F2].mean()
meanfco210 = resultssocatnswinter['fCO2'][F10].mean()
meanfco220 = resultssocatnswinter['fCO2'][F20].mean()

print('pH values')
print(meanpH0)
print(meanpH10)
print(meanpH18)
# Value for 2020: 7.95
# 7.904346415224052
# 7.612731806285325
# 7.839403152474453
print('fCO2 values')
print(meanfco22)
print(meanfco210)
print(meanfco220)
# Value for 2000: 352
# 362.9583518280434
# 332.1811787959274
# 396.6024811224489

L2 =  (resultscombinedwinter.year == 2002)
L18 = (resultscombinedwinter.year == 2018) 
L20 = (resultscombinedwinter.year == 2020) 
L19 =  (resultscombinedwinter.year == 2019) 

meanTA2 = resultscombinedwinter['normalized_TA'][L2].mean()
meanTA18 = resultscombinedwinter['normalized_TA'][L18].mean()
meanTA19 = resultscombinedwinter['normalized_TA'][L19].mean()
meanTA20 = resultscombinedwinter['normalized_TA'][L20].mean()

meandic2 = resultscombinedwinter['dic'][L2].mean()
meandic18 = resultscombinedwinter['dic'][L18].mean()
meandic19 = resultscombinedwinter['dic'][L19].mean()
meandic20 = resultscombinedwinter['dic'][L20].mean()

print('TA values')
print(meanTA2)
print(meanTA18)
print(meanTA19)
print(meanTA20)
# Value for 2000: 2344
# Value for 2010: 2345
# 2344.8043269831537
# 2351.1157850876566
# 2339.8423107444683
print('DIC values')
print(meandic2)
print(meandic18)
print(meandic19)
print(meandic20)
# Value for 2000: 2125
# Value for 2010: 2160
# 2131.99054054054
# 2210.7386363636365
# 2196.4884615384613

#%%

# Winter values (year 2000, 2010, 2020)
# fCO2 socat
# pH RWSo

results = pyco2.sys(
    par1=[352, 332, 396],
    par2=[7.9, 7.6, 7.95],
    par1_type=5,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean
    )

print(results['alkalinity']) 
print(results['dic']) 
# TA = [1351.09898662  619.54999348 1713.2282603 ]
# DIC = [1284.10155814  604.8978884  1625.35074832]

#%%

# Winter values (year 2000, 2010, 2020)
# TA combined
# DIC combined

results = pyco2.sys(
    par1=[2344, 2345, 2345],
    par2=[2125, 2160, 2196],
    par1_type=1,
    par2_type=2,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean 
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.23196473 8.15759929 8.07096582]
# fCO2 = [262.60865615 320.09342569 401.11510201]

#%%

# Winter values (year 2000, 2010, 2020)
# TA combined
# pH RWSo

results = pyco2.sys(
    par1=[2344, 2345, 2345],
    par2=[7.9, 7.6, 7.95],
    par1_type=1,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean
    )

print(results['dic']) 
print(results['fCO2']) 
# DIC = [2256.53542476 2348.86852934 2240.62962575]
# fCO2 = [ 618.56514734 1289.18345839  545.90637295]

#%%

# Winter values (year 2000, 2010, 2020)
# DIC combined
# pH RWSo

results = pyco2.sys(
    par1=[2125, 2160, 2196],
    par2=[7.9, 7.6, 7.95],
    par1_type=2,
    par2_type=3,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean
    )

print(results['alkalinity']) 
print(results['fCO2']) 
# TA = [2209.69610436 2158.13721829 2299.17405451]
# fCO2 = [582.50844356 1185.52240593  535.03282347]

#%%

# Winter values (year 2000, 2010, 2020)
# TA combined
# fCO2 socat

results = pyco2.sys(
    par1=[2344, 2345, 2345],
    par2=[352, 332, 396],
    par1_type=1,
    par2_type=5,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    )

print(results['dic']) 
print(results['pH_total']) 
# DIC = [2174.64636223 2166.03380467 2194.03225956]
# pH = [8.12115941 8.14369462 8.07593923]

#%%

# Winter values (year 2000, 2010, 2020)
# DIC combined
# fCO2 socat

results = pyco2.sys(
    par1=[2125, 2160, 2196],
    par2=[352, 332, 396],
    par1_type=2,
    par2_type=5,
    salinity=wintersalmean,
    temperature=wintertempmean,
    total_phosphate=winterphosmean, 
    total_silicate=wintersilmean, 
    )

print(results['alkalinity']) 
print(results['pH_total']) 
# TA = [2287.80898563 2338.12937716 2347.20655592]
# pH = [8.11159356 8.14254351 8.07631257]


#%% # SPRING

L0 =  (resultsRWSospring.year == 2000)#
L10 = (resultsRWSospring.year == 2010)# 
L18 = (resultsRWSospring.year == 2018)#

F2 = (resultssocatnsspring.year == 2002)  
F10 = (resultssocatnsspring.year == 2010) | (resultssocatnsspring.year == 2009) | (resultssocatnsspring.year == 2011)
F20 = (resultssocatnsspring.year == 2020)# | (resultssocatnsspring.year == 2019) | (resultssocatnsspring.year == 2021)

meanpH0 = resultsRWSospring['pH_total'][L0].mean()
meanpH10 = resultsRWSospring['pH_total'][L10].mean()
meanpH18 = resultsRWSospring['pH_total'][L18].mean()

meanfco22 = resultssocatnsspring['fCO2'][F2].mean()
meanfco210 = resultssocatnsspring['fCO2'][F10].mean()
meanfco220 = resultssocatnsspring['fCO2'][F20].mean()

print('pH values')
print(meanpH0)
print(meanpH10)
print(meanpH18)
# 8.05122875686354
# 7.816800748733113
# 8.1379939873643
# Value for 2020: 8.2
print('fCO2 values')
print(meanfco22)
print(meanfco210)
print(meanfco220)
# Value for 2000: 252
# 298.8832866942304
# 265.2915695826952
# 278.0719197046608

L2 =  (resultscombinedspring.year == 2002)
L14 = (resultscombinedspring.year == 2014) 
L20 = (resultscombinedspring.year == 2020) 

meanTA2 = resultscombinedspring['normalized_TA'][L2].mean()
meanTA14 = resultscombinedspring['normalized_TA'][L14].mean()
meanTA20 = resultscombinedspring['normalized_TA'][L20].mean()

meandic2 = resultscombinedspring['dic'][L2].mean()
meandic14 = resultscombinedspring['dic'][L14].mean()
meandic20 = resultscombinedspring['dic'][L20].mean()

print('TA values')
print(meanTA2)
print(meanTA14)
print(meanTA20)
# Value for 2000: 2350
# Value for 2010: 2354
# 2351.281106161372
# 2356.564892337445
# 2388.685116124478
print('DIC values')
print(meandic2)
print(meandic14)
print(meandic20)
# Value for 2000: 2095
# Value for 2010: 2102
# 2097.0340425531917
# 2106.5494958161116
# 2126.05

#%%

# spring values (year 2000, 2010, 2020)
# fCO2 socat
# pH RWSo

results = pyco2.sys(
    par1=[252, 265.29, 278.07],
    par2=[8.05, 7.82, 8.2],
    par1_type=5,
    par2_type=3,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['alkalinity']) 
print(results['dic']) 
# TA = [1441.7430402   854.34101745 2333.76143686]
# DIC = [1313.36348354  799.04507288 2092.30617821]

#%%

# spring values (year 2000, 2010, 2020)
# TA combined
# DIC combined

results = pyco2.sys(
    par1=[2350, 2354, 2388],
    par2=[2095, 2102, 2126.05],
    par1_type=1,
    par2_type=2,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean 
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.22391223 8.21761848 8.23158797]
# fCO2 = [262.3727402  267.40359155 261.2189262 ]

#%%

# spring values (year 2000, 2010, 2020)
# TA combined
# pH RWSo

results = pyco2.sys(
    par1=[2344, 2345, 2345],
    par2=[8.05, 7.82, 8.2],
    par1_type=1,
    par2_type=3,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['dic']) 
print(results['fCO2']) 
# DIC = [2171.7939263  2258.98909001 2102.74697947]
# fCO2 = [416.7102834  750.00426888 279.45759501]

#%%

# spring values (year 2000, 2010, 2020)
# DIC combined
# pH RWSo

results = pyco2.sys(
    par1=[2095, 2102, 2126.05],
    par2=[8.05, 7.82, 8.2],
    par1_type=2,
    par2_type=3,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean
    )

print(results['alkalinity']) 
print(results['fCO2']) 
# TA = [2263.28541787 2184.7081022  2370.08356027]
# fCO2 = [401.97554342 697.88250866 282.55459438]

#%%

# spring values (year 2000, 2010, 2020)
# TA combined
# fCO2 socat

results = pyco2.sys(
    par1=[2350, 2354, 2388],
    par2=[252, 265.29, 278.07],
    par1_type=1,
    par2_type=5,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean, 
    )

print(results['dic']) 
print(results['pH_total']) 
# DIC = [2087.21311467 2100.48234042 2138.15207648]
# pH = [8.2386015 8.2205189 8.2087384]

#%%

# spring values (year 2000, 2010, 2020)
# DIC combined
# fCO2 socat

results = pyco2.sys(
    par1=[2095, 2102, 2126.05],
    par2=[252, 265.29, 278.07],
    par1_type=2,
    par2_type=5,
    salinity=springsalmean,
    temperature=springtempmean,
    total_phosphate=springphosmean, 
    total_silicate=springsilmean, 
    )

print(results['alkalinity']) 
print(results['pH_total']) 
# TA = [2359.30852815 2355.8041543  2373.67223521]
# pH = [8.24009326 8.22080924 8.20645134]

#%% # SUMMER

L0 =  (resultsRWSosummer.year == 2000)#
L10 = (resultsRWSosummer.year == 2010)# 
L18 = (resultsRWSosummer.year == 2018)#

F3 = (resultssocatnssummer.year == 2003)  
F10 = (resultssocatnssummer.year == 2010) | (resultssocatnssummer.year == 2009) | (resultssocatnssummer.year == 2011)
F20 = (resultssocatnssummer.year == 2020)# | (resultssocatnssummer.year == 2019) | (resultssocatnssummer.year == 2021)

meanpH0 = resultsRWSosummer['pH_total'][L0].mean()
meanpH10 = resultsRWSosummer['pH_total'][L10].mean()
meanpH18 = resultsRWSosummer['pH_total'][L18].mean()

meanfco23 = resultssocatnssummer['fCO2'][F3].mean()
meanfco210 = resultssocatnssummer['fCO2'][F10].mean()
meanfco220 = resultssocatnssummer['fCO2'][F20].mean()

print('pH values')
print(meanpH0)
print(meanpH10)
print(meanpH18)
# 7.9363973443940825
# 7.826558591292111
# 7.844660882226289
# Value for 2020: 8.05
print('fCO2 values')
print(meanfco23)
print(meanfco210)
print(meanfco220)
# Value for 2000: 380
# 402.8085746363061
# 384.7179399511301
# 385.02457921259844

L1 =  (resultscombinedsummer.year == 2001)
L11 = (resultscombinedsummer.year == 2011) 
L20 = (resultscombinedsummer.year == 2020) 

meanTA1 = resultscombinedsummer['normalized_TA'][L1].mean()
meanTA11 = resultscombinedsummer['normalized_TA'][L11].mean()
meanTA20 = resultscombinedsummer['normalized_TA'][L20].mean()

meandic1 = resultscombinedsummer['dic'][L1].mean()
meandic11 = resultscombinedsummer['dic'][L11].mean()
meandic20 = resultscombinedsummer['dic'][L20].mean()

print('TA values')
print(meanTA1)
print(meanTA11)
print(meanTA20)
# Value for 2000: 2352
# Value for 2010: 2358
# 2354.1928396626577
# 2360.6804459695577
# 2384.339543588676

print('DIC values')
print(meandic1)
print(meandic11)
print(meandic20)
# Value for 2000: 2092
# Value for 2010: 2097
# 2094.0010309278346
# 2098.5813953488373
# 2137.7683333333334

#%%

# summer values (year 2000, 2010, 2020)
# fCO2 socat
# pH RWSo

results = pyco2.sys(
    par1=[380, 383.72, 385.02],
    par2=[7.94, 7.83, 8.05],
    par1_type=5,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

print(results['alkalinity']) 
print(results['dic']) 
# TA = [1636.9809533  1251.70427441 2202.38047634]
# pH = [1497.75624019 1160.80560743 1985.89861921]

#%%

# summer values (year 2000, 2010, 2020)
# TA combined
# DIC combined

results = pyco2.sys(
    par1=[2352, 2358, 2384.34],
    par2=[2092, 2097, 2137.77],
    par1_type=1,
    par2_type=2,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean 
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.11473903 8.11572996 8.08488868]
# fCO2 = [345.3936799  345.36371418 380.17775015]

#%%

# summer values (year 2000, 2010, 2020)
# TA combined
# pH RWSo

results = pyco2.sys(
    par1=[2352, 2358, 2384.34],
    par2=[7.94, 7.83, 8.05],
    par1_type=1,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

print(results['dic']) 
print(results['fCO2']) 
# DIC = [2176.87442956 2227.79423848 2155.70348149]
# fCO2 = [552.30100936 736.42752905 417.94125159]

#%%

# summer values (year 2000, 2010, 2020)
# DIC combined
# pH RWSo

results = pyco2.sys(
    par1=[2092, 2097, 2137.77],
    par2=[7.94, 7.83, 8.05],
    par1_type=2,
    par2_type=3,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean
    )

print(results['alkalinity']) 
print(results['fCO2']) 
# TA = [2262.63877442 2222.38739575 2365.12283681]
# fCO2 = [530.76727619 693.19172379 414.4643626 ]

#%%

# summer values (year 2000, 2010, 2020)
# TA combined
# fCO2 socat

results = pyco2.sys(
    par1=[2352, 2358, 2384.34],
    par2=[380, 383.72, 385.02],
    par1_type=1,
    par2_type=5,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean, 
    )

print(results['dic']) 
print(results['pH_total']) 
# DIC = [2110.369611   2117.28675373 2140.19928304]
# pH = [8.07987868 8.07726982 8.08024628]

#%%

# summer values (year 2000, 2010, 2020)
# DIC combined
# fCO2 socat

results = pyco2.sys(
    par1=[2092, 2097, 2137.77],
    par2=[380, 383.72, 385.02],
    par1_type=2,
    par2_type=5,
    salinity=summersalmean,
    temperature=summertempmean,
    total_phosphate=summerphosmean, 
    total_silicate=summersilmean, 
    )

print(results['alkalinity']) 
print(results['pH_total']) 
# TA = [2330.26887197 2334.0215664  2381.46583309]
# pH = [8.07635293 8.07338517 8.07978841]

#%% # AUTUMN

L0 =  (resultsRWSoautumn.year == 2000)#
L10 = (resultsRWSoautumn.year == 2010)# 
L18 = (resultsRWSoautumn.year == 2018)#

F1 = (resultssocatnsautumn.year == 2001)  
F10 = (resultssocatnsautumn.year == 2010)# | (resultssocatnsautumn.year == 2009) | (resultssocatnsautumn.year == 2011)
F20 = (resultssocatnsautumn.year == 2020)# | (resultssocatnsautumn.year == 2019) | (resultssocatnsautumn.year == 2021)

meanpH0 = resultsRWSoautumn['pH_total'][L0].mean()
meanpH10 = resultsRWSoautumn['pH_total'][L10].mean()
meanpH18 = resultsRWSoautumn['pH_total'][L18].mean()

meanfco21 = resultssocatnsautumn['fCO2'][F1].mean()
meanfco210 = resultssocatnsautumn['fCO2'][F10].mean()
meanfco220 = resultssocatnsautumn['fCO2'][F20].mean()

print('pH values')
print(meanpH0)
print(meanpH10)
print(meanpH18)
# 7.814256666796082
# 7.74121198603161
# 8.368374743697549
# Value for 2020: 8
print('fCO2 values')
print(meanfco21)
print(meanfco210)
print(meanfco220)
# Value for 2000: 365
# 367.4696530884503
# 373.45724999999993
# 415.52869196581196

L1 =  (resultscombinedautumn.year == 2001)
L18 = (resultscombinedautumn.year == 2018)
L20 = (resultscombinedautumn.year == 2020) 

meanTA1 = resultscombinedautumn['normalized_TA'][L1].mean()
meanTA18 = resultscombinedautumn['normalized_TA'][L18].mean()
meanTA20 = resultscombinedautumn['normalized_TA'][L20].mean()

meandic1 = resultscombinedautumn['dic'][L1].mean()
meandic18 = resultscombinedautumn['dic'][L18].mean()
meandic20 = resultscombinedautumn['dic'][L20].mean()

print('TA values')
print(meanTA1)
print(meanTA18)
print(meanTA20)
# Value for 2000: 2342
# Value for 2010: 2349
# 2343.0904533717217
# 2395.1078316986564
# 2353.972769377348
print('DIC values')
print(meandic1)
print(meandic18)
print(meandic20)
# Value for 2000: 2093
# Value for 2010: 2122
# 2098.0363636363636
# 2195.504761904762
# 2154.707142857143

#%%

# autumn values (year 2000, 2010, 2020)
# fCO2 socat
# pH RWSo

results = pyco2.sys(
    par1=[365, 373.46, 415.53],
    par2=[7.81, 7.74, 8],
    par1_type=5,
    par2_type=3,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=autumnsilmean
    )

print(results['alkalinity']) 
print(results['dic']) 
# TA = [1139.02891795  980.75747882 2077.50585339]
# DIC = [1070.43512111  929.01844    1918.81336528]

#%%

# autumn values (year 2000, 2010, 2020)
# TA combined
# DIC combined

results = pyco2.sys(
    par1=[2342, 2349, 2353.97],
    par2=[2093, 2122, 2154.71],
    par1_type=1,
    par2_type=2,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=autumnsilmean 
    )

print(results['pH_total']) 
print(results['fCO2']) 
# pH = [8.16384369 8.11956629 8.06094677]
# fCO2 = [303.33644856 343.1616403  402.35832791]

#%%

# autumn values (year 2000, 2010, 2020)
# TA combined
# pH RWSo

results = pyco2.sys(
    par1=[2342, 2349, 2353.97],
    par2=[7.81, 7.74, 8],
    par1_type=1,
    par2_type=3,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=autumnsilmean
    )

print(results['dic']) 
print(results['fCO2']) 
# DIC = [2243.61955894 2274.15028273 2181.86330433]
# fCO2 = [765.03575309 914.19516344 472.49496759]

#%%

# autumn values (year 2000, 2010, 2020)
# DIC combined
# pH RWSo

results = pyco2.sys(
    par1=[2093, 2122, 2154.71],
    par2=[7.81, 7.74, 8],
    par1_type=2,
    par2_type=3,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=autumnsilmean
    )

print(results['alkalinity']) 
print(results['fCO2']) 
# TA = [2187.55627576 2194.23562685 2325.4320154 ]
# fCO2 = [713.67706919 853.03163627 466.61476436]

#%%

# autumn values (year 2000, 2010, 2020)
# TA combined
# fCO2 socat

results = pyco2.sys(
    par1=[2342, 2349, 2353.97],
    par2=[365, 373.46, 415.53],
    par1_type=1,
    par2_type=5,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=autumnsilmean, 
    )

print(results['dic']) 
print(results['pH_total']) 
# DIC = [2127.18875708 2137.29742523 2160.2803099 ]
# pH = [8.09548729 8.08808313 8.04880335]

#%%

# autumn values (year 2000, 2010, 2020)
# DIC combined
# fCO2 socat

results = pyco2.sys(
    par1=[2093, 2122, 2154.71],
    par2=[365, 373.46, 415.53],
    par1_type=2,
    par2_type=5,
    salinity=autumnsalmean,
    temperature=autumntempmean,
    total_phosphate=autumnphosmean, 
    total_silicate=springsilmean, 
    )

print(results['alkalinity']) 
print(results['pH_total']) 
# TA = [2302.20965655 2331.22455598 2347.56094052]
# pH = [8.08888615 8.08515403 8.04774413]

