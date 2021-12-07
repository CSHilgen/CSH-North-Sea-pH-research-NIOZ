pH_low = (RWSomean['year'] >= 2015) & (RWSomean['pH_total'] < 7.75)
pH_low = RWSomean[pH_low]

#%% # Plotting NS longitude latitude and bathymetry

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

# Scatter northsea from data
smin=7.25
smax=7.75

splot = ax.scatter("longitude", "latitude", data=pH_low
                   , c='pH_total', cmap='plasma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
scbar = plt.colorbar(splot)
scbar.set_label("pH")
scbar.set_ticks(np.arange(smin, smax + 1, 0.05))
scbar.set_ticklabels(scbar.get_ticks())
#ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Plot bathymetry from data
gmin = -150
gmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, gmin, gmax, 0)

gplot = (gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(add_colorbar=False, ax=ax, 
        cmap=cmap, transform=ccrs.PlateCarree(), 
        vmin=gmin, vmax=gmax, zorder=-5))

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth (m)")
gcbar.set_ticks(np.arange(gmin, gmax + 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((2, 7, 51, 56.5))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("Low values pH data North Sea")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.tight_layout()
plt.savefig("figures/pH_longterm/pH_low_values_from_2015.png")

#%%

S_low = (RWSomean['salinity'] <= 32) & (RWSomean['year'] >= 2000) &(RWSomean['year'] <=2003)
S_low = RWSomean[S_low]

#%% # Plotting NS longitude latitude and bathymetry

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

# Scatter northsea from data
smin=30
smax=32

splot = ax.scatter("longitude", "latitude", data=S_low
                   , c='salinity', cmap='plasma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
scbar = plt.colorbar(splot)
scbar.set_label("Salinity")
scbar.set_ticks(np.arange(smin, smax + 1, 0.5))
scbar.set_ticklabels(scbar.get_ticks())
#ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Plot bathymetry from data
gmin = -150
gmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, gmin, gmax, 0)

gplot = (gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(add_colorbar=False, ax=ax, 
        cmap=cmap, transform=ccrs.PlateCarree(), 
        vmin=gmin, vmax=gmax, zorder=-5))

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth (m)")
gcbar.set_ticks(np.arange(gmin, gmax + 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((2, 7, 51, 56.5))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("Low values S data North Sea")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.tight_layout()
plt.savefig("figures/S_longterm/S_low_values_below_32_2000-2003.png")