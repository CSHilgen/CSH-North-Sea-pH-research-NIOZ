# pH

#%% # RWSomean pH - Datasets

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
RWSomean.plot.scatter('datetime', 'pH_total', c='xkcd:aqua', ax=ax, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("pH (total scale)")
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('RWSo pH data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/pH_mean_datasets.png")
plt.show()

#%% # RWSomean pH - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
RWSomean.plot.scatter('datetime', 'pH_total', c='dayofyear', cmap=cm, vmin=1, vmax=365, ax=ax, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("pH (total scale)")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('RWSo pH data - Seasons North Sea')

plt.tight_layout()
plt.savefig("figures/pH_mean_seasons.png")
plt.show()

#%% # RWSomean pH data - Regions

x = RWSomean['datetime']
y = RWSomean['pH_total']

#Choose different method periods
L0 = (RWSomean['distance_to_shore'] > 0) & (RWSomean['distance_to_shore'] <=4)
L1 = (RWSomean['distance_to_shore'] > 4) & (RWSomean['distance_to_shore'] <=10)
L2 = (RWSomean['distance_to_shore'] > 10) & (RWSomean['distance_to_shore'] <=20)
L3 = (RWSomean['distance_to_shore'] > 20) & (RWSomean['distance_to_shore'] <=30)
L4 = (RWSomean['distance_to_shore'] > 30) & (RWSomean['distance_to_shore'] <=50)
L5 = (RWSomean['distance_to_shore'] > 50) & (RWSomean['distance_to_shore'] <=70)
L6 = (RWSomean['distance_to_shore'] > 70) & (RWSomean['distance_to_shore'] <=100)
L7 = (RWSomean['distance_to_shore'] > 100) & (RWSomean['distance_to_shore'] <=150)
L8 = (RWSomean['distance_to_shore'] > 150) & (RWSomean['distance_to_shore'] <=200)
L9 = (RWSomean['distance_to_shore'] > 200) & (RWSomean['distance_to_shore'] <=250)
L10 = (RWSomean['distance_to_shore'] > 250) & (RWSomean['distance_to_shore'] <=300)

fig, ax = plt.subplots(dpi=300)
ax.scatter(x[L0], y[L0], alpha=0.5, s=40, c='xkcd:butter', edgecolor='none', label='0-4')
ax.scatter(x[L1], y[L1], alpha=0.5, s=40, c='xkcd:blush pink', edgecolor='none', label='4-10')
ax.scatter(x[L2], y[L2], alpha=0.5, s=40, c='xkcd:orangered', edgecolor='none', label='10-20')
ax.scatter(x[L3], y[L3], alpha=0.5, s=40, c='xkcd:ruby', edgecolor='none', label='20-30')
ax.scatter(x[L4], y[L4], alpha=0.5, s=40, c='xkcd:lightish purple', edgecolor='none', label='30-50')
ax.scatter(x[L5], y[L5], alpha=0.5, s=40, c='xkcd:gross green', edgecolor='none', label='50-70')
ax.scatter(x[L6], y[L6], alpha=0.5, s=40, c='xkcd:greenish', edgecolor='none', label='70-100')
ax.scatter(x[L7], y[L7], alpha=0.5, s=40, c='xkcd:water blue', edgecolor='none', label='100-150')
ax.scatter(x[L8], y[L8], alpha=0.5, s=40, c='xkcd:royal', edgecolor='none', label='150-200')
ax.scatter(x[L9], y[L9], alpha=0.5, s=40, c='xkcd:rich purple', edgecolor='none', label='200-250')
ax.scatter(x[L10], y[L10], alpha=0.5, s=40, c='xkcd:eggplant', edgecolor='none', label='250-300')

ax.grid(alpha=0.3)
# ax.grid(axis='both', which='minor', linestyle=':', linewidth='0.5')
# ax.set_yticks
ax.set_xlabel('Time (yrs)')
ax.set_ylabel('pH (total scale)')
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
#ax.set_axisbelow(True)
ax.set_title('RWSo pH - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/pH_mean_regions.png")
plt.show()

#%% # RWSo pH per RWS station over time

x = RWSo.datetime
y = RWSo.pH

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
    ax.set_ylabel('pH (nbs scale)')
    ax.grid(alpha=0.3)
    ax.set_ylim(5,10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    # ax.set_xlim(1975, 2020)
    # ax.set_xlim(x.min()-150, x.max()+150)
    # ax.xaxis.set_major_locator(mdates.YearLocator(5))
    
    #ax.xaxis.set_minor_locator(mdates.MonthLocator())
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

#RWSomean.plot.scatter('dayofyear', 'pH',  c="xkcd:aqua", ax=ax, label='RWSo')

RWSomean.plot.scatter('dayofyear', 'pH',  c="year", cmap='rainbow', vmax=1970, vmin=2021, ax=ax)

#RWSomean.plot.scatter('dayofyear', 'pH',  c="xkcd:aqua", ax=ax, label='RWSo')

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
ax.set_ylabel("pH (nbs scale)")
#ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
#ax.get_legend().set_title("Dataset")
ax.set_title('RWSo pH data - Day of Year North Sea')

plt.tight_layout()
plt.savefig("figures/pH_mean_dayofyear_datasets.png")
#plt.savefig("figures/pH_allpoints_dayofyear_datasets.png")
plt.show()