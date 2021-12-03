# Oxygen

#%% # Apparent oxygen utilisation koolstof

# Convert oxygen mg/l to umol/kg
convertfactor = 30.4948984
RWSomean['oxygen umol/kg'] = RWSomean['oxygen'] * convertfactor
resultsRWSo['oxygen umol/kg'] = resultsRWSo['oxygen'] * convertfactor
RWSo['oxygen umol/kg'] = RWSo['oxygen'] * convertfactor

# aou is the difference in between gas oxygen solubility and the measured oxygen
aou = ks.parameterisations.aou_GG92(oxygen=RWSomean['oxygen umol/kg'], temperature=RWSomean['temperature'], salinity=RWSomean['salinity'])

# First series: AOU
# Second series: % (0 in equilibrium AOU %)
# Third series: Saturation O2

#%% # Apparent oxygen utilisation Garcia & Gordon (1992)

# === CALCULATE OXYGEN SATURATION
def calc_oxy_sat(sss, sst):
    """Calculate the oxygen saturation from
    salinity and temperature. Combined fit constants 
    from Garcia & Gordon (1992)."""
    # Define salinity variable
    S = sss
    # Scale temperature
    Ts = np.log((298.15 - sst)*((273.15 + sst)**-1))
    # Define constants (Combined fit)
    A0 = 5.80818
    A1 = 3.20684
    A2 = 4.11890
    A3 = 4.93845
    A4 = 1.01567
    A5 = 1.41575
    B0 = -7.01211 * (10**-3)
    B1 = -7.25958 * (10**-3)
    B2 = -7.93334 * (10**-3)
    B3 = -5.54491 * (10**-3)
    C0 = -1.32412 * (10**-7) 
    # Calculate natural log of C0*
    lnC0 = (A0
             + (A1 * Ts)
             + (A2 * (Ts**2))
             + (A3 * (Ts**3))
             + (A4 * (Ts**4))
             + (A5 * (Ts**5))
             + (S * (B0
                    + (B1 * Ts)
                    + (B2 * (Ts**2))
                    + (B3 * (Ts**3))                    
                    )
                )
             + (C0 * (S**2))
             )
    # Calculate in equilibrium with the atmosphere at sst and sss
    C0 = np.exp(lnC0)
    return C0
print(calc_oxy_sat(35, 10)) # salinity check from Garcia & Gordon (1992) -> 274.64589470912495

# === CALCULATE AOU
# Calculate oxygen saturation and AOU
RWSomean["oxygen_sat"] = calc_oxy_sat(RWSomean["salinity"], RWSomean["temperature"])
RWSomean["aou"] = RWSomean["oxygen_sat"] - RWSomean["oxygen umol/kg"] 

#%% # Oxygen - Time - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datetime', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)
#ax.scatter('datetime', 'aou', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Oxygen (µmol/kg)")
ax.set_ylim(175, 425)
# ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
# ax.set_ylim(-150, 100)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/O2_mean_time_datasets.png")
plt.show()

#%% # Oxygen - Time - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
sc = ax.scatter('datetime', 'oxygen umol/kg', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
#sc = ax.scatter('datetime', 'aou', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Oxygen (µmol/kg)")
ax.set_ylim(175, 425)
# ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
# ax.set_ylim(-150, 100)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/O2_mean_time_seasons.png")
plt.show()

#%% # Oxygen - Time - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
x = RWSomean['datetime']
#y = RWSomean['oxygen umol/kg']
y = RWSomean['aou']

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

ax.grid(alpha=0.3)
ax.set_xlabel('Time (yrs)')
# ax.set_ylabel('Oxygen (µmol/kg)')
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
# ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Oxygen data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_time_regions.png")
plt.show()

#%% # Oxygen - Dayofyear - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter('dayofyear', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)
ax.scatter('dayofyear', 'aou', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Day of Year")
# ax.set_ylabel("Oxygen (µmol/kg)")
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_dayofyear_datasets.png")
plt.show()

#%% # Oxygen - Dayofyear - Regions

fig, ax = plt.subplots(dpi=300)

ax=ax
x = RWSomean['dayofyear']
#y = RWSomean['oxygen umol/kg']
y = RWSomean['aou']

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

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
# ax.set_ylabel('Oxygen (µmol/kg)')
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Km to shore")
ax.set_title('Oxygen data - Regions North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_dayofyear_regions.png")
plt.show()

#%% Oxygen - Dayofyear - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
#sc = ax.scatter('dayofyear', 'oxygen umol/kg',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('dayofyear', 'aou',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Day of Year')
# ax.set_ylabel('Oxygen (µmol/kg)')
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Year North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_dayofyear_year.png")
plt.show()

#%% # Oxygen - Regions - Datasets

fig, ax = plt.subplots(dpi=300)

ax = ax
#ax.scatter('distance_to_shore', 'oxygen umol/kg', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)
ax.scatter('distance_to_shore', 'aou', c='xkcd:aqua', data=RWSomean, label='RWSo', s=20, alpha=0.4)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
# ax.set_ylabel("Oxygen (µmol/kg)")
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_regions_datasets.png")
plt.show()

#%% # Oxygen - Regions - Seasons

fig, ax = plt.subplots(dpi=300)
cm = plt.cm.get_cmap('twilight')

ax = ax
# sc = ax.scatter('distance_to_shore', 'oxygen umol/kg', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)
sc = ax.scatter('distance_to_shore', 'aou', c='dayofyear', cmap=cm, vmin=1, vmax=365, data=RWSomean, s=20)

ax.grid(alpha=0.3)
ax.set_xlabel("Distance to shore (km)")
# ax.set_ylabel("Oxygen (µmol/kg)")
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Seasons North Sea')

cbar=fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Seasons')
label=[80,172,264,355]
cbar.set_ticks(label)
cbar.set_ticklabels(['Spring', 'Summer', 'Autumn', 'Winter'])

plt.tight_layout()
plt.savefig("figures/AOU_mean_regions_seasons.png")
plt.show()

#%% Oxygen - Regions - Year

fig, ax = plt.subplots(dpi=300)

cm = plt.cm.get_cmap('rainbow')
vmin = 2000
vmax = 2021

ax=ax
#sc = ax.scatter('distance_to_shore', 'oxygen umol/kg',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)
sc = ax.scatter('distance_to_shore', 'aou',  c="year", data=RWSomean, cmap=cm, vmin=vmin, vmax=vmax+1, s=20)

ticks = np.linspace(vmin, vmax, 5)
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', ticks=ticks)
cbar.set_label('Time (yrs)')
cbar.set_ticklabels([2000, 2005, 2010, 2015, 2020])

ax.grid(alpha=0.3)
ax.set_xlabel('Distance to shore (km)')
# ax.set_ylabel('Oxygen (µmol/kg)')
# ax.set_ylim(175, 425)
ax.set_ylabel("Apparent Oxygen Utilisation (µmol/kg)")
ax.set_ylim(-150, 100)
ax.minorticks_on()
ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Oxygen data - Year North Sea')

plt.tight_layout()
plt.savefig("figures/AOU_mean_regions_year.png")
plt.show()

#%% # RWSo O2 per RWS station over time

x = resultsRWSo['datetime']
y = resultsRWSo['oxygen umol/kg']

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
    ax.set_ylabel('Oxygen (µmol/kg)')
    ax.grid(alpha=0.3)
    ax.set_ylim(175, 425)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    # ax.set_xlim(1975, 2020)
    # ax.set_xlim(x.min()-150, x.max()+150)
    # ax.xaxis.set_major_locator(mdates.YearLocator(5))
    
    #ax.xaxis.set_minor_locator(mdates.MonthLocator())
    # plt.xticks(rotation=90)
    
    ax.set_title(fvar)
    plt.tight_layout()
    plt.savefig("figures/RWSo_stations_O2_datetime/O2_" + fvar + ".png")
    plt.show()
            
print("I am done!")

