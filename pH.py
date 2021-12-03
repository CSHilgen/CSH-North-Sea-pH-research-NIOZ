# pH

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
    temperature_out=RWSn['temperature']
    )

print(results['pH_total_out']) 
results_out = pd.DataFrame.from_dict(results)
results_out['datetime'] = resultsRWSn['datetime']
results_out['longitude'] = resultsRWSn['longitude']
results_out['latitude'] = resultsRWSn['latitude']
results_out['station'] = resultsRWSn['station']
results_out['total_nitrate'] = resultsRWSn['total_nitrate']
results_out['datenum'] = resultsRWSn['datenum']
results_out['dayofyear'] = resultsRWSn['dayofyear']
results_out['month'] = resultsRWSn['month']
results_out['year'] = resultsRWSn['year']

# Make dataset based on the mean 
RWSnmean_out = results_out.set_index('datetime').resample('M').mean()
RWSnmean_out = RWSnmean_out.reset_index()
RWSnmean_out = RWSnmean_out.dropna(axis='rows', how='all', subset=['pH_total_out'])

#%% # pH - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datenum', 'pH_total', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)
ax.scatter('datenum', 'pH_total_out', c='xkcd:dark orange', data=RWSnmean_out, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_xlim(10950, 19000)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
# ax.set_title('pH RWSo data - Datasets North Sea') 
ax.set_title('pH RWS data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_time_datasets_RWSo_spectro_zoomin.png")
plt.show()

#%% # pH - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
#sc = ax.scatter('datetime', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
sc = ax.scatter('datetime', 'pH_total_out', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSnmean_out, s=20)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Seasons North Sea') 

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/pH_mean_time_seasons_RWSn.png")
plt.show()

#%% # pH - Time - Regions

L0 = (RWSnmean_out['distance_to_shore'] > 0) & (RWSnmean_out['distance_to_shore'] <=4)
L1 = (RWSnmean_out['distance_to_shore'] > 4) & (RWSnmean_out['distance_to_shore'] <=10)
L2 = (RWSnmean_out['distance_to_shore'] > 10) & (RWSnmean_out['distance_to_shore'] <=20)
L3 = (RWSnmean_out['distance_to_shore'] > 20) & (RWSnmean_out['distance_to_shore'] <=30)
L4 = (RWSnmean_out['distance_to_shore'] > 30) & (RWSnmean_out['distance_to_shore'] <=50)
L5 = (RWSnmean_out['distance_to_shore'] > 50) & (RWSnmean_out['distance_to_shore'] <=70)
L6 = (RWSnmean_out['distance_to_shore'] > 70) & (RWSnmean_out['distance_to_shore'] <=100)
L7 = (RWSnmean_out['distance_to_shore'] > 100) & (RWSnmean_out['distance_to_shore'] <=150)
L8 = (RWSnmean_out['distance_to_shore'] > 150) & (RWSnmean_out['distance_to_shore'] <=200)
L9 = (RWSnmean_out['distance_to_shore'] > 200) & (RWSnmean_out['distance_to_shore'] <=250)
L10 = (RWSnmean_out['distance_to_shore'] > 250) & (RWSnmean_out['distance_to_shore'] <=300)

fig, ax = plt.subplots(dpi=300)

ax = ax
x = RWSnmean_out['datetime']
# y = RWSomean['pH_total']
y = RWSnmean_out['pH_total_out']

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Regions North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_time_regions_RWSn.png")
plt.show()

#%% # pH - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter("dayofyear", "pH_total", c="xkcd:aqua", data=RWSomean, label='RWSo', s=20, alpha=0.4)
ax.scatter('dayofyear', 'pH_total_out', c='xkcd:dark orange', data=RWSnmean_out, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_dayofyear_datasets_RWSn.png")
plt.show()

#%% # pH - Dayofyear - Regions

L0 = (RWSnmean_out['distance_to_shore'] > 0) & (RWSnmean_out['distance_to_shore'] <=4)
L1 = (RWSnmean_out['distance_to_shore'] > 4) & (RWSnmean_out['distance_to_shore'] <=10)
L2 = (RWSnmean_out['distance_to_shore'] > 10) & (RWSnmean_out['distance_to_shore'] <=20)
L3 = (RWSnmean_out['distance_to_shore'] > 20) & (RWSnmean_out['distance_to_shore'] <=30)
L4 = (RWSnmean_out['distance_to_shore'] > 30) & (RWSnmean_out['distance_to_shore'] <=50)
L5 = (RWSnmean_out['distance_to_shore'] > 50) & (RWSnmean_out['distance_to_shore'] <=70)
L6 = (RWSnmean_out['distance_to_shore'] > 70) & (RWSnmean_out['distance_to_shore'] <=100)
L7 = (RWSnmean_out['distance_to_shore'] > 100) & (RWSnmean_out['distance_to_shore'] <=150)
L8 = (RWSnmean_out['distance_to_shore'] > 150) & (RWSnmean_out['distance_to_shore'] <=200)
L9 = (RWSnmean_out['distance_to_shore'] > 200) & (RWSnmean_out['distance_to_shore'] <=250)
L10 = (RWSnmean_out['distance_to_shore'] > 250) & (RWSnmean_out['distance_to_shore'] <=300)

fig, ax = plt.subplots(dpi=300)

ax = ax
x = RWSnmean_out['dayofyear']
y = RWSnmean_out['pH_total_out']

ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:beige', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pumpkin', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:deep red', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:snot green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:bottle green', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:barney purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Regions North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_dayofyear_regions_RWSn.png")
plt.show()

#%% # pH - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = ax
#sc = ax.scatter('dayofyear', 'pH_total', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'pH_total_out', c='year', data=RWSnmean_out, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Year North Sea') 

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/pH_mean_dayofyear_year_RWSn.png")
plt.show()

#%% # pH - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter("distance_to_shore", "pH_total", c="xkcd:aqua", data=RWSomean, label='RWSo', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'pH_total_out', c='xkcd:dark orange', data=RWSnmean_out, label='RWSn', s=20, alpha=0.4)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Datasets North Sea') 

plt.tight_layout()
plt.savefig("figures/pH_mean_regions_datasets_RWSn.png")
plt.show()

#%% # pH - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
#sc = ax.scatter('distance_to_shore', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
sc = ax.scatter('distance_to_shore', 'pH_total_out', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSnmean_out, s=20)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Seasons North Sea') 

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/pH_mean_regions_seasons_RWSn.png")
plt.show()

#%% # pH - Regions - Year

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax = ax
#sc = ax.scatter('distance_to_shore', 'pH_total', c='year', data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'pH_total_out', c='year', data=RWSnmean_out, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ax.set_ylabel("pH (total scale)")
ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('pH RWSn data - Year North Sea') 

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

plt.tight_layout()
plt.savefig("figures/pH_mean_regions_year_RWSn.png")
plt.show()

#%% # RWSo pH per RWS station over time

x = resultsRWSo.datetime
y = resultsRWSo.pH_total

fvar = 'CALLOG4'

for fvar in ['CALLOG4', "CALLOG10", "CALLOG30",'CALLOG50','CALLOG70',
'EGMAZE4', 'EGMAZE10','EGMAZE20','EGMAZE30','EGMAZE50','EGMAZE70',
'GOERE6','GOERE10','GOERE20','GOERE30','GOERE50','GOERE70',
'NOORDWK4','NOORDWK10','NOORDWK20','NOORDWK30','NOORDWK50','NOORDWK70',
'ROTTMPT20','ROTTMPT30','ROTTMPT50','ROTTMPT70','ROTTMPT100',
'SCHOUWN1','SCHOUWN4','SCHOUWN10','SCHOUWN20','SCHOUWN30','SCHOUWN50','SCHOUWN70',
'TERSLG10','TERSLG30','TERSLG50','TERSLG70','TERSLG100','TERSLG135','TERSLG175',
'WALCRN4','WALCRN10','WALCRN20','WALCRN30','WALCRN50','WALCRN70',
'TERHDE70']:
    
    L1 = (RWSo.station == fvar)
        
    fig, ax = plt.subplots(dpi=300, figsize=(8,3))
    ax.scatter(x[L1], y[L1],
               alpha=0.5, s=40, c='royalblue', edgecolor='none')
    
    ax.set_yticks
    ax.set_xlabel('Time (yrs)')
    ax.set_ylabel('pH')
    ax.grid(alpha=0.3)
    ax.set_ylim(5,10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    # ax.set_xlim(1975, 2020)
    # ax.set_xlim(x.min()-150, x.max()+150)
    # ax.xaxis.set_major_locator(mdates.YearLocator(5))
    
    # ax.xaxis.set_minor_locator(mdates.MonthLocator())
    # plt.xticks(rotation=90)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_pH_datetime/pH_" + fvar + ".png")
    plt.show()
            
print("I am done!")

#%% # RWSo pH all stations over time

x = RWSo.datetime
y = RWSo.pH

L2 = (RWSo.station == 'GOERE6')
L3 = (RWSo.station == 'NOORDWK10')
L4 = (RWSo.station == 'NOORDWK20')
L5 = (RWSo.station == 'NOORDWK70')
L6 = (RWSo.station == 'ROTTMPT50')
L7 = (RWSo.station == 'ROTTMPT70')
L8 = (RWSo.station == 'SCHOUWN10')
L9 = (RWSo.station == 'TERSLG10')
L10 = (RWSo.station == 'TERSLG50')
L11 = (RWSo.station == 'TERSLG100')
L12 = (RWSo.station == 'TERSLG135')
L13 = (RWSo.station == 'TERSLG175')
L14 = (RWSo.station == 'WALCRN20')
L15 = (RWSo.station == 'WALCRN70')

fig, ax = plt.subplots(dpi=300, figsize=(8,3))
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='royalblue', edgecolor='none', label='GOERE6')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:pink', edgecolor='none', label='NOORDWK10')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:teal', edgecolor='none', label='NOORDWK20')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:coral', edgecolor='none', label='NOORDWK70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:teal green', edgecolor='none', label='ROTTMPT50')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:pinkish purple', edgecolor='none', label='ROTTMPT70')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:banana', edgecolor='none', label='SCHOUWN10')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:dark orange', edgecolor='none', label='TERSLG10')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:light orange', edgecolor='none', label='TERSLG50')
ax.scatter(x[L11], y[L11], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='TERSLG100')
ax.scatter(x[L12], y[L12], alpha=0.5, s=40, c='xkcd:dark blue', edgecolor='none', label='TERSLG135')
ax.scatter(x[L13], y[L13], alpha=0.5, s=40, c='xkcd:dark green', edgecolor='none', label='TERSLG175')
ax.scatter(x[L14], y[L14], alpha=0.5, s=40, c='xkcd:violet', edgecolor='none', label='WALCRN20')
ax.scatter(x[L15], y[L15], alpha=0.5, s=40, c='xkcd:red', edgecolor='none', label='WALCRN70')

ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('pH (nbs scale)')
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("RWS station")
ax.set_axisbelow(True)
ax.grid(alpha=0.3)

ax.set_title('RWSo pH - Stations North Sea')
# plt.tight_layout()
plt.savefig("figures/RWSo_stations_pH_datetime/allstationsfrom_1975_2020.png")
#plt.savefig("figures/RWSo_stations_pH_datetime/allstationsfrom_1975_2020_transect_same_color.png")
plt.show()

#%% # pH - mean & allpoints - Dayofyear

fig, ax = plt.subplots(dpi=300)

RWSomean.plot.scatter('dayofyear', 'pH_total',  c="xkcd:aqua", ax=ax, label='RWSo')

#sc = ax.scatter('dayofyear', 'pH_total',  c="year", cmap='rainbow', vmax=1970, vmin=2021, data=RWSomean)

#resultsRWSo.plot.scatter('dayofyear', 'pH_total',  c="xkcd:aqua", ax=ax, label='RWSo')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("pH (total scale)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.set_title('RWSo pH data - Day of Year North Sea')

# cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
# cbar.set_label('Time (yrs)')

plt.tight_layout()
plt.savefig("figures/pH_mean_dayofyear_datasets.png")
#plt.savefig("figures/pH_mean_dayofyear_year.png")
#plt.savefig("figures/pH_allpoints_dayofyear_datasets.png")
plt.show()
