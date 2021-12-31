
#%% # RWSo Chl - Dayofyear

fig, ax1 = plt.subplots(dpi=300)

# ax=ax1
ax.scatter('dayofyear', 'chlorophyll',  c="xkcd:aqua", data=RWSo, label='RWSo')
ax1.set_ylabel('Chlorophyll')
ax.legend()

# ax2 = ax1.twinx()
# ax=ax2
# ax.scatter('dayofyear', 'dic',  c="xkcd:dark orange", data=RWSnmean, label='RWSn')
# ax.plot(x_plotting, y_plotting, c='xkcd:dark orange')
# ax2.set_ylabel('DIC (umol/kg)')

ax.grid(alpha=0.3)
ax1.set_xlabel("Day of Year")
ax.legend()
ax.set_title('Chl and DIC data - Day of Year North Sea')

plt.tight_layout()
#plt.savefig("figures/Chl&DIC_dayofyear_datasets.png")
plt.show()


#%% # Apparent oxygen utilisation koolstof

# Convert oxygen mg/l to umol/kg
convertfactor = 30.4948984
RWSomean['oxygen umol/kg'] = RWSomean['oxygen'] * convertfactor
resultsRWSo['oxygen umol/kg'] = resultsRWSo['oxygen'] * convertfactor
RWSo['oxygen umol/kg'] = RWSo['oxygen'] * convertfactor

# aou is the difference in between gas oxygen solubility and the measured oxygen
aou = ks.parameterisations.aou_GG92(oxygen=RWSomean['oxygen umol/kg'], temperature=RWSomean['temperature'], salinity=RWSomean['salinity'])
RWSomean['aou'] = aou[0]
RWSomean['%_aou_from_oxygen'] = aou[1]
RWSomean['oxygen_saturation'] = aou[2]

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
RWSo["oxygen_sat"] = calc_oxy_sat(RWSo["salinity"], RWSo["temperature"])
RWSo["aou"] = RWSo["oxygen_sat"] - RWSo["oxygen umol/kg"] 

#%% # ALL fCO2 - Time - Datasets (Data generated with pyCO2sys)

fig, ax = plt.subplots(dpi=300)

ax = ax
glodapnsmean.plot.scatter("datetime", "fCO2", c="b", ax=ax, s=20, alpha=0.4, label='GLODAP')
Cefasmean.plot.scatter('datetime', 'fCO2', c='xkcd:greenish', ax=ax, s=20, alpha=0.4, label='Cefas')
D366mean.plot.scatter('datetime', 'fCO2', c='xkcd:pink', ax=ax, s=20, alpha=0.4, label='D366')
RWSnmean.plot.scatter('datetime', 'fCO2', c='xkcd:dark orange', ax=ax, s=20, alpha=0.4, label='RWSn')
socatnsmean.plot.scatter('datetime', 'fCO2', c='xkcd:goldenrod', ax=ax, s=20, alpha=0.4, label='SOCAT sea')
socatnsairmean.plot.scatter('datetime', 'fCO2', c='black', ax=ax, s=20, alpha=0.4, label='SOCAT air')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("fCO$_2$ (uatm)")
ax.set_ylim([150, 550])
ax.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())
plt.xticks(rotation=0)
ax.set_title('All fCO$_2$ data - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/fCO2_all_mean_datasets.png")
plt.show()


